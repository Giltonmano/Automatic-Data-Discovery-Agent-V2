import requests

url = "https://www.coleparmer.com/p/elmi-swing-out-benchtop-centrifuges/88174"
headers = {"User-Agent": "Mozilla/5.0 (student research project)"}
response = requests.get(url, headers=headers)
print(response.status_code)

with open("page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Saved page length:", len(response.text))