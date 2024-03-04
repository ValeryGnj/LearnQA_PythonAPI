import requests

url = "https://portcall.marinet.ru/seaport.php?Section=ships&Mode=wa&Action=formwaterarea&ID=105821&login=aps-kd&password=508389"

payload = {}
headers = {
  'Cookie': 'PHPSESSID=74f739e79a40ec8ee000639ca1cd008c'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
