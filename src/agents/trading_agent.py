"""
🌙 Moon Dev's AI Trading Agent
Built with love by Moon Dev 🚀
"""

# 🎯 Trading Strategy Prompt - The Secret Sauce! 
# This is where Moon Dev's trading edge lives! 
# Customize this prompt to create different trading strategies
PROMPT = """
You are Moon Dev's AI Trading Assistant 🌙

Analyze the provided market data and make a trading decision based on these criteria:
1. Price action relative to MA20 and MA40
2. RSI levels and trend
3. Volume patterns
4. Recent price movements

Respond in this exact format:
1. First line must be one of: BUY, SELL, or NOTHING (in caps)
2. Then explain your reasoning, including:
   - Technical analysis
   - Risk factors
   - Market conditions
   - Confidence level

"""

import anthropic
import os
from termcolor import colored, cprint
from dotenv import load_dotenv
from ..core.config import *
from ..data.ohlcv_collector import collect_all_tokens

# Load environment variables
load_dotenv()

class TradingAgent:
    def __init__(self):
        """Initialize the AI Trading Agent with Moon Dev's magic ✨"""
        api_key = os.getenv("ANTHROPIC_KEY")
        if not api_key:
            raise ValueError("🚨 ANTHROPIC_KEY not found in environment variables!")
            
        self.client = anthropic.Anthropic(api_key=api_key)
        print("🤖 Moon Dev's AI Trading Agent initialized!")
        
    def analyze_market_data(self, market_data):
        """Analyze market data using Claude"""
        try:
            message = self.client.messages.create(
                model=AI_MODEL,
                max_tokens=AI_MAX_TOKENS,
                temperature=AI_TEMPERATURE,
                messages=[
                    {
                        "role": "user", 
                        "content": f"{PROMPT}\n\nMarket Data to Analyze:\n{market_data}"
                    }
                ]
            )
            print("🎯 Moon Dev's AI Analysis Complete!")
            return message.content
            
        except Exception as e:
            print(f"❌ Error in AI analysis: {str(e)}")
            return None

def main():
    """Main function to run the trading agent"""
    print("🌙 Moon Dev AI Trading System Starting Up! 🚀")
    
    try:
        # Collect OHLCV data for all tokens
        print("📊 Collecting market data...")
        market_data = collect_all_tokens()
        
        # Initialize AI agent
        agent = TradingAgent()
        
        # Analyze each token's data
        for token, data in market_data.items():
            print(f"\n🔍 Analyzing token: {token}")  # Full contract address
            analysis = agent.analyze_market_data(data.to_dict())
            print(f"\n📈 Analysis for contract: {token}")  # Full contract address
            print(analysis)
            print("\n" + "="*50 + "\n")  # Separator for better readability
            
    except KeyboardInterrupt:
        print("\n👋 Moon Dev AI Agent shutting down gracefully...")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("🔧 Moon Dev suggests checking the logs and trying again!")

if __name__ == "__main__":
    main() 