from llama_index.prompts import PromptTemplate
from llama_index.llms import Gemini
import google.generativeai as genai
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

genai.configure()

llm = Gemini(model='models/gemini-pro')
prompt = """
Email:
---------------------
{email_str}
---------------------

Summarize this academic email for me, highlighting deadlines if there exist 
and extract important information as clear and short as possible.
Only use headers(#) and bullet points(-) in your summary with markdown format.
Only Use Traditional Chinese.
"""
prompt_tmpl = PromptTemplate(prompt_)


def summarize_email(email: str):
    fmt_prompt = prompt_tmpl.format(
        email_str=email
    )
    response = llm.complete(fmt_prompt)
    return str(response)
