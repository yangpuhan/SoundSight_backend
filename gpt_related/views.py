from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from gpt_related.models import AudioInfo, FullAudio, UserRequest, AudioSummary
from user_auth.models import User
from gpt_related import GPT_call
import json
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

# @login_required()
# @csrf_exempt
# @require_http_methods(["GET"])
# def realtime_summary(request):
#     body = json.loads(request.body.decode("utf-8"))  
#     text = body.get('sound_new')
#     instruction = body.get('instruction')
#     checkCode = body.get('checkCode')

#     role_content_pair = {
#         "role": "user",
#         "content": text
#     }
    
#     response = GPT_call.GPT_related.connect_openai_api_chat(GPT_call.MODEL, GPT_call.polish_prompt+[role_content_pair], 4000, GPT_call.logger, 30, ["debug", "[EXAMPLE]"])
#     polished = GPT_call.GPT_related.get_content_from_response(response)
#     print("POLISH DONE")

#     last_audio_info = AudioInfo.objects.filter(user=request.user, checkCode=checkCode).order_by('-created_time').first()
#     if last_audio_info:
#         last_output = json.loads(last_audio_info.json_text).get('last_output')
#     else:
#         last_output = ""
        
#     role_content_pair = {
#         "role": "user",
#         "content": json.dumps({
#             "last_output": last_output,
#             "sound_new": polished,
#             "instruction": instruction
#         },ensure_ascii=False)
#     }
#     print(role_content_pair)

#     response = GPT_call.GPT_related.connect_openai_api_chat(GPT_call.MODEL, GPT_call.realtime_prompt+[role_content_pair], 4000, GPT_call.logger, 30, ["debug", "[EXAMPLE]"])
#     content = GPT_call.GPT_related.get_content_from_response(response)
#     output = json.loads(content).get('topic')

#     save_audio_info = AudioInfo(
#         checkCode=checkCode,
#         json_text=json.dumps({
#             "last_output": output
#         },ensure_ascii=False),
#         user=request.user
#     )
#     save_audio_info.save()

#     current_audio = FullAudio.objects.filter(user=request.user, checkCode=checkCode).first()
#     if current_audio:
#         cur_summary = current_audio.summary + output
#         cur_text = current_audio.full_text + polished
#         current_audio.summary = cur_summary
#         current_audio.full_text = cur_text
#         current_audio.updated_time = datetime.datetime.now().timestamp()
#         current_audio.save()
#     else:
#         save_audio_summary = FullAudio(
#             checkCode=checkCode,
#             full_text=polished,
#             summary=output,
#             user=request.user
#         )
#         save_audio_summary.save()
#     print(current_audio)

#     return JsonResponse({'code': 0, 'info': 'Succeed response', "topics": output})
    

scheduler = BackgroundScheduler(timezone='Asia/Shanghai')

def polish():
    print("POLISH START")
    audios = AudioInfo.objects.filter(polish_text="")
    for audio in audios:
        print("POLISHING", audio.id)
        request = UserRequest.objects.filter(user=audio.user).first()
        role_content_pair = {
            "role": "user",
            "content": audio.text
        }
        response = GPT_call.GPT_related.connect_openai_api_chat(GPT_call.MODEL, GPT_call.polish_prompt+[audio.json_text], 4000, GPT_call.logger, 30, ["debug", "[EXAMPLE]"])
        polished = GPT_call.GPT_related.get_content_from_response(response)
        audio.polish_text = polished
        audio.save()
    print("POLISH DONE")
    
def summary():
    print("SUMMARY START")
    users = User.objects.all()
    for user in users:
        audios = AudioInfo.objects.filter(user=user, is_summary=False)
        if len(audios) > 5:
            print("SUMMARYING", user.id)
            request = UserRequest.objects.filter(user=user).first()
            summary_log = AudioSummary.objects.filter(user=user).first()
            if summary_log is None:
                summary_log = AudioSummary.objects.create(user=user)
            all_text = ''.join([audio.polish_text for audio in audios])
            role_content_pair = {
                "role": "user",
                "content": json.dumps({
                    "last_output": summary_log.summary if summary_log else "",
                    "sound_new": all_text,
                    "instruction": request.instructions if request else ""
                },ensure_ascii=False)
            }
            response = GPT_call.GPT_related.connect_openai_api_chat(GPT_call.MODEL, GPT_call.instruction_prompt+[role_content_pair], 4000, GPT_call.logger, 30, ["debug", "[EXAMPLE]"])
            summary = GPT_call.GPT_related.get_content_from_response(response)
            summary_log.summary = summary
            summary_log.save()
            for audio in audios:
                audio.is_summary = True
                audio.save()
    print("SUMMARY DONE")
    
scheduler.add_job(polish, 'interval', seconds = 10, replace_existing=True, coalesce=True)
scheduler.add_job(summary, 'interval', seconds = 30, replace_existing=True, coalesce=True)
scheduler.start()

@login_required()
@csrf_exempt
@require_http_methods(["POST"])
def realtime_summary(request):
    body = json.loads(request.body.decode("utf-8"))  
    instruction = body.get('instruction')
    conference_name = body.get('conference_name')
    is_end = body.get('is_end')
    
    user = request.user
    
    audios = AudioInfo.objects.filter(user=user, is_send=False)
    
    summary_log = AudioSummary.objects.filter(user=user).first()
    
    polishedText = ''.join([audio.polish_text for audio in audios])
    
    summary = summary_log.summary if summary_log else ""
    
    request = UserRequest.objects.filter(user=user).first()
    if request is None:
        request = UserRequest.objects.create(user=user, instructions=instruction)
    request.instruction = instruction
    request.meeting_name = conference_name
    request.save()

    if is_end:
        pass
    else:
        return JsonResponse({'code': 0, 'info': 'Succeed response', "polishedText": polishedText, "summary": summary})