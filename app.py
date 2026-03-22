import requests
import random
import time

TARGET_URL = "https://omg10.com/4/10761774"

def start_engine():
    print("🚀 GitHub Machine Started...")
    # GitHub Action max 6 ghante chalti hai, hum 5 ghante ka loop rakhenge
    end_time = time.time() + (5 * 3600) 
    
    while time.time() < end_time:
        try:
            # Proxy scrape (Har baar fresh list)
            r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000", timeout=5)
            proxies = r.text.splitlines()
            
            if proxies:
                proxy = random.choice(proxies)
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
                # Direct hit
                requests.get(TARGET_URL, headers=headers, proxies={"http": f"http://{proxy}"}, timeout=10)
                print(f"✅ Hit Success | Proxy: {proxy}")
        except:
            pass
        time.sleep(2)

if __name__ == "__main__":
    start_engine()
