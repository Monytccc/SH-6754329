import requests
import time

url = "https://www.xshellz.com/ajax/shell/keep"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Channel": "4ozGFU9rWS0prTum3MiLyMeM6VoDBI0FYhlbdKwJ1717704414b1ac04e93b",
    "Content-Length": "17",
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": "_ga=GA1.2.1167815375.1717703977; u=herlambang; pw=bd84bf8e79741748a723b81fc76c2a4f9a4e3c2e27c0cc45a93bd3adc11b7ff3a57de832bc0e44167029855f18e00ab92579990dc66ece3b3bf560b7d315cf52e16ef6307929ceff9dd2ac2c202755dca69425f4dfb3762ccd3fb10050d3c4a728bf53b9; xshellz_session=4ozGFU9rWS0prTum3MiLyMeM6VoDBI0FYhlbdKwJ; _gid=GA1.2.1358500101.1717807525; _ga_0MP03KZ0MW=GS1.2.1717807525.2.0.1717807525.0.0.0; XSRF-TOKEN=eyJpdiI6IjVBY3NzcTc2eGx1RkpjYlJWb3FhZkE9PSIsInZhbHVlIjoiZFlWaHpYOUxVZUFJVGFPZUluQnlVOU5SN0w0aE9VWTdcL0Y2T3pwRGp1OGd2MlFzSlBnc0VnUDJlaHpwQTBETXciLCJtYWMiOiJmNGVmMzlmMWM0ZTJlY2RiNWQwZDQ2MzBhNDIwOTU5MDAwYTU4NWEyMzc5YmQ4YzIwY2VmZTMwNWQ2ZDc5ZDcxIn0%3D",
    "Origin": "https://www.xshellz.com",
    "Priority": "u=1, i",
    "Referer": "https://www.xshellz.com/xpanel/shell/143758",
    "Sec-Ch-Ua": '"Chromium";v="125", "Not.A/Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "X-Xsrf-Token": "eyJpdiI6InBEbXRYMzRPSk1lUEt2U0lmSWJFeVE9PSIsInZhbHVlIjoiZlFEQnJLSWl3RWdGTjAwVjdIK203THVvYndtXC95QnJVWDg3YmtnM3FyUStqR0tVQjVcLzhmRzBobDBEUm42K0t2IiwibWFjIjoiYTY1ZmY1NDEzNDYxMmYzODY0YTFlZmJkYmRlMmY1ODA5ODc0NGZjZGJhMGQ1ZWJhNWY2MzBiMTQzMzVhMzBlOSJ9"
}

data = {"opid": "143758"}  # Data yang akan dikirim

while True:
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Permintaan berhasil")
        print(response.text)  # Cetak respons dari server jika perlu
    else:
        print(f"Error: {response.status_code}")

    time.sleep(1000)  # Tunggu 1 detik sebelum mengulang permintaan
