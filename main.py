import schedule
import time
import requests
import json

from fastapi import FastAPI

app = FastAPI()

def fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

@app.get("/berth")
async def fetch_berth():
    url1 = "https://api.tradlinx.com/berthplan?1687485467783"
    headers1 = {
       "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6",
        "Cookie": "_gcl_au=1.1.1679281944.1687485453; _fbp=fb.1.1687485453430.18690922; _clck=8ia1tc|2|fcp|0|1269; _ga_FEGZQJQLV4=GS1.1.1687485453.1.0.1687485453.60.0.0; _ga=GA1.2.65732494.1687485453; _gid=GA1.2.314520510.1687485454; _dc_gtm_UA-69830188-1=1; ch-veil-id=f20d8bce-731f-4886-bf0c-8f7ecd45490b; ch-session-125719=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiIxMjU3MTktNjQ5NGZjMTBlMTE5N2RkNjZmM2EiLCJpYXQiOjE2ODc0ODU0NTYsImV4cCI6MTY5MDA3NzQ1Nn0.btN6ynSTKaoUOv6deb6imk4GH3fBToM_akaKqs5p9JI; _clsk=jqkwpf|1687485467789|2|1|o.clarity.ms/collect",
        "Referer": "https://www.tradlinx.com/",
        "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Tx-Clientid": "tradlinx",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
         data = fetch_data(url1, headers1)
        return data

@app.get("/terminal")
async def fetch_terminal():
    url2 = "https://api-terminal.tradlinx.com/terminalWork?1687485467214"
    headers2 = {
       "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6",
        "Cookie": "_gcl_au=1.1.1679281944.1687485453; _fbp=fb.1.1687485453430.18690922; _clck=8ia1tc|2|fcp|0|1269; _ga_FEGZQJQLV4=GS1.1.1687485453.1.0.1687485453.60.0.0; _ga=GA1.2.65732494.1687485453; _gid=GA1.2.314520510.1687485454; _dc_gtm_UA-69830188-1=1; ch-veil-id=f20d8bce-731f-4886-bf0c-8f7ecd45490b; ch-session-125719=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiIxMjU3MTktNjQ5NGZjMTBlMTE5N2RkNjZmM2EiLCJpYXQiOjE2ODc0ODU0NTYsImV4cCI6MTY5MDA3NzQ1Nn0.btN6ynSTKaoUOv6deb6imk4GH3fBToM_akaKqs5p9JI; _clsk=jqkwpf|1687485467789|2|1|o.clarity.ms/collect",
        "Referer": "https://www.tradlinx.com/",
        "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Tx-Clientid": "tradlinx",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
        data = fetch_data(url2, headers2)
        return data

def job():
    schedule.run_pending()
    time.sleep(1)

schedule.every().day.at("07:00").do(job)
schedule.every().day.at("12:00").do(job)  
schedule.every().day.at("16:00").do(job)
schedule.every().day.at("17:00").do(job)
schedule.every().day.at("18:00").do(job)
schedule.every().day.at("19:00").do(job) 
schedule.every().day.at("20:00").do(job)
schedule.every().day.at("21:00").do(job)
schedule.every().day.at("22:00").do(job)
schedule.every().day.at("23:00").do(job)
schedule.every().day.at("03:00").do(job)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(main, host="0.0.0.0", port=8000)
