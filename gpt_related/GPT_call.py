import os
import logging

from handyllm import PromptConverter, OpenAIAPI, EndpointManager
from dotenv import load_dotenv, find_dotenv
# load env parameters from .env file
load_dotenv(find_dotenv())

# import prompt
# import GPT_related
import prompt
import GPT_related
from GPT_related import MODEL

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("test")
logger.setLevel(logging.DEBUG)
converter = PromptConverter()

# Example_prompt = converter.rawfile2chat(os.path.join(os.path.dirname(__file__), '..','templates','Example_prompt.txt'))
instruction_prompt = converter.raw2chat(prompt.instruction_prompt)
integration_prompt = converter.raw2chat(prompt.integration_prompt)
polish_prompt = converter.raw2chat(prompt.polish_prompt)
realtime_prompt = converter.raw2chat(prompt.realtime_prompt)


if __name__ == '__main__':
    # Example
    user_input_str = "你好呀！\n你好你好"
    role_content_pair = {
        "role": "user",
        "content": user_input_str
    }
    response = GPT_related.connect_openai_api_chat(MODEL, [role_content_pair], 512, logger, 30, ["debug", "[EXAMPLE]"])
    content = GPT_related.get_content_from_response(response)
    print(content)