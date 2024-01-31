from llama_index.prompts import PromptTemplate
from llama_index.llms import Gemini
import google.generativeai as genai
import os
GOOGLE_API_KEY = "<YOUR_GOOGLE_MAKERSUITE_API>"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

genai.configure()

llm = Gemini(model='models/gemini-pro')
prompt = """
Email information is below.
---------------------
{email_str}
---------------------
You are a professional personal assistant.\
Given the email information and not prior knowledge, \
your goal is to extract important information from email and summarize with markdown bullet points.
Always use traditional Chinese or use the words same as the email.
"""
prompt_tmpl = PromptTemplate(prompt)


def summarize_email(email: str):
    fmt_prompt = prompt_tmpl.format(
        email_str=email
    )
    response = llm.complete(fmt_prompt)
    return str(response)
