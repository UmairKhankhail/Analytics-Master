import google.generativeai as genai
#from pandasai.llm import GoogleGemini
from pandasai.llm import GooglePalm,BambooLLM

# Set your Google API key
# GOOGLE_API_KEY = "AIzaSyBjCrtVUiixLho8kdBKY1z8kpIMn7QRcmg"
# genai.configure(api_key=GOOGLE_API_KEY)
Bamboo_API_KEY='$2a$10$scg9r.xsaDEizMf4Ci.Vyuk0/cJ/7mCDAc/DIB/rDprnmzbjuO4ca'
# llm = GooglePalm(api_key=GOOGLE_API_KEY, temperature=0, seed=26)
llm = BambooLLM(api_key=Bamboo_API_KEY)