**﻿Stock Market Agent**

A lightweight Agentic AI stock recommendation agent that fetches real-time stock data, 
autonomously analyzes investment trends using LLMs (Groq LLaMA3), and returns actionable buy/sell insights via CLI

**What It Does**

1. Fetches recent stock data (e.g., NVDA, AAPL, MSFT) using yfinance
2. Analyzes market trends using a language model (Groq's LLaMA3-70B)
3. Recommends top stocks to invest in and highlights ones to avoid

| Tool             | Purpose                                   |
| ---------------- | ----------------------------------------- |
| `yfinance`       | Fetch historical stock data               |
| `openai` (Groq)  | Query LLMs for market insights            |
| `dotenv`         | Manage secure API keys                    |
| `pandas`         | Data manipulation                         |
| `Git` + `GitHub` | Version control & collaboration           |


│Project Structure: stock-market-agent/
├── agents/
│   └── stock_agent.py        # AI logic to analyze stock trends
├── utils/
│   └── fetch_stock_data.py   # Function to fetch stock data via yfinance
├── main.py                   # CLI entrypoint to run the agent
├── app.py                    # Streamlit app (Optional)
├── .env                      # API key for Groq
├── requirements.txt          # All dependencies
└── README.md                 # You are here!


1. Clone the repo:

    git clone https://github.com/yourusername/stock-market-agent.git

    cd stock-market-agent

3. Install dependencies:

    pip install -r requirements.txt

5. Set up .env file:

    GROQ_API_KEY=your_groq_key_here

7. Run the app

    python main.py

**Skills Demonstrated**

✅ Data ingestion from external APIs (yfinance)

✅ Prompt engineering for LLMs (Groq + OpenAI client)

✅ Data analysis and investment logic

✅ Git-based version control & clean module structure

**Future Ideas**

* Add charts (via Plotly/Matplotlib)

* Rank 100+ tickers automatically and visualize

* Integrate AWS Lambda for backend automation

* Schedule daily reports via cron jobs




