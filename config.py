import google.generativeai as genai
#from pandasai.llm import GoogleGemini
from pandasai.llm import GooglePalm

# Set your Google API key
GOOGLE_API_KEY = "AIzaSyBjCrtVUiixLho8kdBKY1z8kpIMn7QRcmg"
genai.configure(api_key=GOOGLE_API_KEY)

llm = GooglePalm(api_key=GOOGLE_API_KEY, temperature=0, seed=26)
