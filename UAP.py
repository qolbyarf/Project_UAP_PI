import json, requests

print("Page buku dari 1 - 10!")

nBuku = int(input("Page buku:"))

if nBuku > 10:
  nBuku = 10
  print("Page diatur otomatis ke 10!")
elif nBuku < 1:
  nBuku = 1
  print("Page diatur otomatis ke 1!")

bukuN = requests.get('https://gutendex.com/books/?page='+str(nBuku))

bukuN = bukuN.json()

bukuN
