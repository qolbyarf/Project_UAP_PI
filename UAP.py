import json, requests, random

# Fungsi pemilihan page library
def pilihan(nBuku):
  code = 'https://gutendex.com/books/?page='+str(nBuku)
  return code

# Class untuk melihat Judul dan Author buku
class RakBuku:
  def __init__(self, id):
    self.id = id

  def judul(self):
    for data in bukuN['results']:
      if data['id'] == self.id:
        print("\nJudul:", data['title'])
  
  def author(self):
    for data in bukuN['results']:
      if data['id'] == self.id:
        print("Pengarang")
        for bio in data['authors']:
          print("\tNama:", bio['name'])
          print("\tLahir:", bio['birth_year'])
          print("\tWafat:", bio['death_year'])

  def subject(self):
    for data in bukuN['results']:
      if data['id'] == self.id:
        print("Kategori:", data['subjects'])
  
  def memory(self):
    print("Jika ingin mencari buku ini Anda bisa mencari di Rak Buku No."+str(nBuku), "bagian")
    for data in bukuN['results']:
      if data['id'] == self.id:
        print(data['bookshelves'])


user = str(input("Masukkan Username Anda: "))
while True:
  a = random.randint(100, 999)
  print("Captcha Anda adalah", a)
  captcha = int(input("Masukkan captcha untuk melanjutkan: "))
  if captcha == a:
    # Pilihan apa yang ingin dilakukan
    print("\nHalo", user.upper())
    print("Apa yang ingin anda lakukan di library ini?")
    print('''1. Melihat detail buku satu per satu \n2. Melihat banyak detail buku sekaligus''')

    pilih = int(input())

    # Melihat detail buku satu per satu
    if pilih == 1:
      # Memilih page API
      print("Page library dari 1 - 10!")
      nBuku = int(input("Page library: "))

      # Karena pagenya kebanyakan makanya dibatesin sampe 10 🙂
      if nBuku > 10:
        nBuku = 10
        print("Page diatur otomatis ke 10!")
      elif nBuku < 1:
        nBuku = 1
        print("Page diatur otomatis ke 1!")
      
      bukuN = requests.get(pilihan(nBuku))
      bukuN = bukuN.json()
      
      # Kumpulan ID buku pada page yang dipilih
      print("ID buku dalam page",nBuku)
      list1 = []
      for data in bukuN['results']:
        list1.append(data['id'])

      list1.sort()
      print(list1)

      # Memilih ID buku
      while True:
        id = int(input("Masukkan ID buku dari page diatas: "))
        if id in list1:
          info = RakBuku(id)
          info.judul()
          info.author()
          break
        else:
          print("Masukkan ID dengan benar sesuai List di atas!")
 
      break

    # Melihat banyak detail buku sekaligus
    elif pilih == 2:
      # Memilih page API
      print("\nPage buku dari 1 - 10!")
      nBuku = int(input("Page buku: "))

      # Karena pagenya kebanyakan makanya dibatesin sampe 10 🙂
      if nBuku > 10:
        nBuku = 10
        print("Page diatur otomatis ke 10!")
      elif nBuku < 1:
        nBuku = 1
        print("Page diatur otomatis ke 1!")
      
      bukuN = requests.get(pilihan(nBuku))
      bukuN = bukuN.json()
      
      # Kumpulan ID buku pada page yang dipilih
      print("ID buku dalam page",nBuku)
      list1 = []
      for data in bukuN['results']:
        list1.append(data['id'])

      list1.sort()
      print(list1)

      # Membuat list ID untuk dilihat sekaligus
      daftarBuku = []
      while True:
        id = int(input("\nMasukkan ID buku dari page diatas: "))
        if id in list1:
          if id not in daftarBuku:
            daftarBuku.append(id)
          else:
            print('ID sudah ada')
        else:
          print("ID tidak ada")

        print("Ada lagi? Y/N")
        lagi = input()
        if lagi == 'Y' or lagi == 'y':
          print("Pilih ID yang lain!")
        else:
          break

      print("\n", daftarBuku)

      # Memeriksa apakah list kosong atau tidak
      if len(daftarBuku) == 0:
        print("Daftar ID Kosong")
      else:
        for i in daftarBuku:
          info = RakBuku(i)
          info.judul()
          info.author()
          print()
      break 

  else:
    print("Captcha anda salah. Ingin coba lagi? Y/N")
    coba = input()
    if coba == 'Y' or coba == 'y':
      print("Okee")
    else:
      break
