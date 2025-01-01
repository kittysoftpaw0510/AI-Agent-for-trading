"""
🌙 Moon Dev AI Trading System
Main entry point for the trading system
Built with love by Moon Dev 🚀
"""

from core.bot import bot
import time

def main():
    print("🌙 Moon Dev AI Trading System Starting Up! 🚀")
    print("💫 Remember: Moon Dev says trade safe and smart! 💫")
    
    try:
        bot()
    except KeyboardInterrupt:
        print("\n🌙 Moon Dev AI Trading System shutting down gracefully... 👋")
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        print("🔧 Moon Dev suggests checking the logs and trying again!")

if __name__ == "__main__":
    main()
