"""
🌙 Moon Dev's OHLCV Data Collector
Collects Open-High-Low-Close-Volume data for specified tokens
Built with love by Moon Dev 🚀
"""

from ..core.config import *
from ..core.utils import nice_funcs as n
import pandas as pd
from datetime import datetime
import os
from termcolor import colored, cprint
import time

def collect_token_data(token_address, days_back=DAYSBACK_4_DATA, timeframe=DATA_TIMEFRAME):
    """Collect OHLCV data for a specific token"""
    try:
        print(f"🔍 Moon Dev is fetching data for {token_address[-4:]} over {days_back} days...")
        df = n.get_data(token_address, days_back, timeframe)
        
        if df is not None and not df.empty:
            # Save to CSV with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"src/data/ohlcv/{token_address}_{timestamp}.csv"
            df.to_csv(filename)
            print(f"💾 Data saved to {filename}")
            
            # Also save as latest version
            latest_filename = f"src/data/ohlcv/{token_address}_latest.csv"
            df.to_csv(latest_filename)
            print(f"✨ Latest data updated for {token_address[-4:]}")
            
            return df
        else:
            print(f"❌ No data received for {token_address[-4:]}")
            return None
            
    except Exception as e:
        print(f"❌ Error collecting data for {token_address[-4:]}: {str(e)}")
        return None

def collect_all_tokens():
    """Collect data for all tokens in the config"""
    print("🌙 Moon Dev OHLCV Data Collector Starting Up! 🚀")
    
    # Ensure the OHLCV directory exists
    os.makedirs("src/data/ohlcv", exist_ok=True)
    
    results = {}
    for token in tokens_to_trade:
        print(f"\n🌙 Moon Dev is working on {token[-4:]}...")
        df = collect_token_data(token)
        if df is not None:
            results[token] = df
        time.sleep(1)  # Be nice to the API
    
    print("\n✅ Moon Dev has finished collecting all token data!")
    return results

if __name__ == "__main__":
    try:
        collect_all_tokens()
    except KeyboardInterrupt:
        print("\n👋 Moon Dev OHLCV Collector shutting down gracefully...")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("🔧 Moon Dev suggests checking the logs and trying again!") 