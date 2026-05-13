from dotenv import load_dotenv
load_dotenv()

from rich import print
from concurrent.futures import ThreadPoolExecutor

from llm.openai_client import ask_chatgpt
from llm.gemini_client import ask_gemini
from llm.merger import merge_outputs

from utils.loader import load_system_context

def main():

    system_context = load_system_context()

    while True:

        user_prompt = input("\n> ")

        if user_prompt == "exit":
            break

        with ThreadPoolExecutor() as executor:

            gpt_future = executor.submit(
                ask_chatgpt,
                user_prompt,
                system_context
            )

            gemini_future = executor.submit(
                ask_gemini,
                user_prompt,
                system_context
            )

            try:
                gpt_response = gpt_future.result()
            except Exception as e:
                gpt_response = f"GPT ERROR: {e}"

            try:
                gemini_response = gemini_future.result()
            except Exception as e:
                gemini_response = f"GEMINI ERROR: {e}"

        merged = merge_outputs(
            gpt_response,
            gemini_response
        )

        print(merged)

if __name__ == "__main__":
    main()