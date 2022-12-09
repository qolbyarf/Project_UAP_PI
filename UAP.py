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

list1 = []
for data in bukuN['results']:
  list1.append(data['id'])

list1.sort()
print(list1)

class RakBuku:
  def __init__(self, id):
    self.id = id

  def id_buku(self):
    return self.id
  n = int(input("Masukkan id buku yang ingin diambil dari rak: "))

buku = RakBuku(n)

ambil = buku.id_buku()

for data in bukuN['results']:
  if data['id'] == ambil:
    print(data['title'])
