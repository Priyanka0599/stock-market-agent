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

    # Step 3: Define top stock tickers to analyze
    stock_tickers = ["AAPL", "MSFT", "GOOGL", "NVDA", "AMZN"]
    stock_data_dict = {}

    for ticker in stock_tickers:
        data = get_stock_data(ticker)
        stock_data_dict[ticker] = data.tail().to_string()

    # Step 4: Construct user prompt with all stock data
    user_prompt = """
    Analyze the recent performance of the following stocks based on their historical trends and their interests and their growth initiatives:
    """
    for ticker, df_string in stock_data_dict.items():
        user_prompt += f"\nTicker: {ticker}\n{df_string}\n"

    user_prompt += """
    ✅ List the top 2 stocks worth investing in right now with a short reason.
    ❌ Also mention one stock to avoid with reasoning based on the company trend.
    Output in a clean, readable format.
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",  # Make sure this is a valid Groq model
        messages=[
            {"role": "system", "content": "You are a financial assistant AI."},
            {"role": "user", "content": user_prompt}
        ]
    )

    ai_reply = response.choices[0].message.content
    print("\n📊 AI Recommendation:")
    print(ai_reply)
