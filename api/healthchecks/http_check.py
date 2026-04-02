import requests
import time

def check_http(url):
    try:
        start = time.time()
        r = requests.get(url, timeout=5)

        return {
            "status": "healthy" if r.status_code == 200 else "fail",
            "response_time": (time.time() - start) * 1000
        }
    except:
        return {"status": "down"}