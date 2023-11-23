from handyllm import PromptConverter, OpenAIAPI, EndpointManager
from tenacity import retry, stop_after_attempt, wait_fixed

# 调用openai api，返回response类型为chat stream
@retry(stop=stop_after_attempt(3))
def connect_openai_api_chat(model, messages, max_tokens, logger, timeout, log_marks):
    try:
        response = OpenAIAPI.chat(
            model=model,
            messages=messages,
            temperature=0.2,
            max_tokens=max_tokens,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            logger=logger,
            timeout=timeout,
            stream=True,
            log_marks=log_marks
        )
        return response
    except Exception as e:
        print("ERROR connet openai api chat: ", e)
        raise e
  
# 将response类型为chat stream转换为string  
def get_content_from_response(response):
    content = ""
    for text in OpenAIAPI.stream_chat(response):
        # print(text, end='')
        content += text
    return content