"""
🌙 Moon Dev's OHLCV Data Collector
Collects Open-High-Low-Close-Volume data for specified tokens
Built with love by Moon Dev 🚀
"""

from ...core.config import *
from ...core.utils.nice_funcs import get_data
import pandas as pd
from datetime import datetime
import os
from termcolor import colored, cprint
import time

class OHLCVCollector:
    def __init__(self):
        """Initialize the OHLCV data collector with Moon Dev's magic ✨"""
        self.data_dir = "data/ohlcv"
        self.ensure_data_directory()
        
    def ensure_data_directory(self):
        """Create data directory if it doesn't exist 📁"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            print(f"🌙 Moon Dev created data directory at {self.data_dir}")

    def collect_data(self, token_address, days_back=DAYSBACK_4_DATA, timeframe=DATA_TIMEFRAME):
        """
        Collect OHLCV data for a specific token
        Returns DataFrame and saves to CSV
        """
        try:
            print(f"🔍 Moon Dev is fetching data for {token_address[-4:]} over {days_back} days...")
            df = get_data(token_address, days_back, timeframe)
            
            if df is not None and not df.empty:
                # Save to CSV with timestamp
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{self.data_dir}/{token_address}_{timestamp}.csv"
                df.to_csv(filename)
                print(f"💾 Data saved to {filename}")
                
                # Also save as latest version
                latest_filename = f"{self.data_dir}/{token_address}_latest.csv"
                df.to_csv(latest_filename)
                print(f"✨ Latest data updated for {token_address[-4:]}")
                
                return df
            else:
                print(f"❌ No data received for {token_address[-4:]}")
                return None
                
        except Exception as e:
            print(f"❌ Error collecting data for {token_address[-4:]}: {str(e)}")
            return None

    def collect_all_tokens(self):
        """
        Collect data for all tokens in the config's tokens_to_trade list
        Returns dict of token_address: DataFrame
        """
        results = {}
        for token in tokens_to_trade:
            print(f"\n🌙 Moon Dev is working on {token[-4:]}...")
            df = self.collect_data(token)
            if df is not None:
                results[token] = df
            time.sleep(1)  # Be nice to the API
        return results

def main():
    """Main function to run the collector"""
    print("🌙 Moon Dev OHLCV Data Collector Starting Up! 🚀")
    collector = OHLCVCollector()
    
    try:
        results = collector.collect_all_tokens()
        print("\n✅ Moon Dev has finished collecting all token data!")
        return results
    except KeyboardInterrupt:
        print("\n👋 Moon Dev OHLCV Collector shutting down gracefully...")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("🔧 Moon Dev suggests checking the logs and trying again!")

if __name__ == "__main__":
    main() 