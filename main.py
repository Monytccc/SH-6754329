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
    "Cookie": "_ga=GA1.2.812910501.1717768630; u=herlambang; pw=d04e77595fbaf00a96faf836e7610fd84e702ada374db7653f0625a513ef119227d2ffd7ad25d36a81d99137c2b76d3214047d2f871e2c2178f535b9ed6ff23690d2ebe98763b9782634a11b4c6bfcfc427a96162fd44a9fa21ab9af7d11c33b3a3f8966; _gid=GA1.2.1650443215.1718457184; xshellz_session=jRdD6n3mfY4ft4VLdZO7SVlz5uyCDG210IUQbemy; _gat=1; _ga_0MP03KZ0MW=GS1.2.1718524439.7.1.1718524468.0.0.0; XSRF-TOKEN=eyJpdiI6Imo1S0h3NWtIVCtCa2FPSWZ4YUowOHc9PSIsInZhbHVlIjoiZFByMmRENFh4ZXdYVjhGVndrcjdXWHlrSG4zTHdPUmpwV3JuQk9obUlKanhNejRGWEJcL0hOV2RDNm9GQ050cnkiLCJtYWMiOiJkNmI4ZmM5NmZiZDA4MWU2OTQ0YWVjY2IwNDY5NjJkOWRlMGY2YTRmZDM2MjQ0MmI1NDJiMjU1OWIzNGJhZGZjIn0%3D",
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
