"""
🌙 Moon Dev's AI Trading Agent
Built with love by Moon Dev 🚀
"""

import anthropic
from src.core.config import *
from src.data.ohlcv_collector import collect_all_tokens
import os
from termcolor import colored, cprint
from dotenv import load_dotenv

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
                        "content": f"Analyze this market data and provide trading insights: {market_data}"
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
            print(f"\n🔍 Analyzing {token[-4:]}...")
            analysis = agent.analyze_market_data(data.to_dict())
            print(f"\n📈 Analysis for {token[-4:]}:")
            print(analysis)
            
    except KeyboardInterrupt:
        print("\n👋 Moon Dev AI Agent shutting down gracefully...")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("🔧 Moon Dev suggests checking the logs and trying again!")

if __name__ == "__main__":
    main() 