"""
🌙 Moon Dev AI Trading System
Main entry point for the trading system
Built with love by Moon Dev 🚀
"""

from src.agents.trading_agent import main as run_agent

if __name__ == "__main__":
    print("🚀 Starting Moon Dev's AI Trading System...")
    print("💫 Remember: Moon Dev says trade safe and smart!")
    
    try:
        run_agent()
    except KeyboardInterrupt:
        print("\n👋 Moon Dev AI Trading System shutting down gracefully...")
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        print("🔧 Moon Dev suggests checking the logs and trying again!")
