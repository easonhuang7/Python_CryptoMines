import json
import urllib.request as req

# CryptoMines Spaceships
# url = "https://api.cryptomines.app/api/spaceships"
# CryptoMines Workers
url = "https://api.cryptomines.app/api/workers"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

data = json.loads(data)
# print(data[0])

list = []

# 星數
star = 2

# CryptoMines Workers
for i, value in enumerate(data):
    if(value['nftData']['level'] == star):
        price = int(value['price']) / 1000000000000000000
        minePower = value['nftData']['minePower']
        value['Value'] = price/minePower

        list.append(value)

list.sort(key=lambda x: (
    int(x['price']) / 1000000000000000000) / (x['nftData']['minePower']))

for index, data in enumerate(list):
    if(index < 100):
        seller = data['sellerAddress']
        price = int(data['price']) / 1000000000000000000
        minePower = data['nftData']['minePower']
        value = data['Value']
        print('算力:{0},價格:{1},賣家:{2},1MP價格{3}'.format(
            minePower, price, seller, value))

# CryptoMines Spaceships
# for i, value in enumerate(data):
#     if(value['nftData']['level'] == star):
#         price = int(value['price']) / 1000000000000000000
#         # minePower = value['nftData']['minePower']
#         # value['Value'] = price/minePower

#         list.append(value)

# list.sort(key=lambda x: (
#     int(x['price']) / 1000000000000000000))

# for data in list:
#     seller = data['sellerAddress']
#     price = int(data['price']) / 1000000000000000000
#     workers = data['nftData']['workers']
#     # value = data['Value']
#     print('等級:{0},價格:{1},賣家:{2}'.format(
#         workers, price, seller))
