import os
from dotenv import load_dotenv
from openai import OpenAI
from utils.fetch_stock_data import get_stock_data

# Step 1: Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Step 2: Set up OpenAI client for Groq
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def run_agent():
    print("Running stock agent...")

    # Step 3: Get stock data
    data = get_stock_data("AAPL")
    print(data.tail())

    # Step 4: Ask Groq for analysis
    user_prompt = "Based on AAPL's recent trends, should I consider buying the stock now with the stats on how much % profit/loss I can make?"

    response = client.chat.completions.create(
    model="llama3-70b-8192",  # Updated to supported Groq model
    messages=[
        {"role": "system", "content": "You are a financial assistant AI."},
        {"role": "user", "content": user_prompt}
    ]
)

    ai_reply = response.choices[0].message.content
    print("\n📊 AI Recommendation:")
    print(ai_reply)
