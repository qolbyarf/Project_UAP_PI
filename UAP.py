import json, requests, random

def pilihan(nBuku):
  code = 'https://gutendex.com/books/?page='+str(nBuku)
  return code

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

print("***SELAMAT DATANG DI PROGRAM ID BOOK LIBRARY***")
print("----Di sini Anda bisa melihat kumpulan buku----")
print("-----yang ada di Rak Besar di hadapan Anda-----")
print()
print("Untuk melanjutkan silahkan masukan Nama anda yang akan digunakan jika anda meminjam buku di sini\n")

z = 0
user = str(input("Masukkan Nama Anda: "))
while z < 3:
  a = random.randint(100, 999)
  print("Captcha Anda adalah", a)

  captcha = 0
  i = 0
  while i < 3:
    try:
      captcha = int(input("\nMasukkan captcha untuk melanjutkan: "))
      break
    except:
      if i < 2: print("Captcha berupa angka di atas")
    i += 1
    if i == 2: print("Kesempatan Anda tinggal 1 kali lagi")
    if i == 3: print("Kesempatan Anda habis! Program telah dihentikan!\n")

  if captcha == 0:
    break

  if captcha == a:
    # Pilihan apa yang ingin dilakukan
    print("\nHalo", user.upper())
    while True:
      print("Apa yang ingin anda lakukan di library ini?")
      print('''1. Melihat satu detail buku \n2. Melihat banyak detail buku sekaligus\n''')

      while True:
        try:
          pilih = int(input("Masukkan Pilihan: "))
          break
        except:
          print("Pilihan dalam bentuk angka\n")

      # Melihat detail buku satu per satu
      if pilih == 1:
        # Memilih page API
        print("Page library dari 1 - 10!")

        while True:
          try:
            nBuku = int(input("Page library: "))
            break
          except:
            print("Page dalam library tidak valid\n")

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
        print("\nID dan Judul buku dalam page",nBuku)
        list1 = []
        list2 = []
        for data in bukuN['results']:
          list1.append(data['id'])
          list2.append(data['title'])
          
        dict0 = {}
        for key in list1:
          for value in list2:
            dict0[key] = value
            list2.remove(value)
            break

        dict1 = {}
        for i in sorted(dict0):
            dict1[i]=dict0[i]

        for key, value in dict1.items():
            print(key, ' : ', value)

        # Memilih ID buku
        while True:

          while True:
            try:
              id = int(input("Masukkan ID buku dari page diatas: "))
              break
            except:
              print("Tidak ada id yang menggunakan huruf atau simbol\n")

          if id in list1:
            info = RakBuku(id)
            info.judul()
            info.author()
            info.subject()
            info.memory()
            break
          else:
            print("Masukkan ID dengan benar sesuai List di atas!")
        break
        
      # Melihat banyak detail buku sekaligus
      elif pilih == 2:
        # Memilih page API
        print("\nPage buku dari 1 - 10!")

        while True:
          try:
            nBuku = int(input("Page library: "))
            break
          except:
            print("Page dalam library tidak valid\n")

        # Karena pagenya kebanyakan makanya dibatesin sampe 10 🙂
        if nBuku > 10:
          nBuku = 10
          print("Page diatur otomatis ke 10!")
        elif nBuku < 1:
          nBuku = 1
          print("Page diatur otomatis ke 1!")
        
        bukuN = requests.get(pilihan(nBuku))
        bukuN = bukuN.json()
        
        # Kumpulan ID dan Judul buku pada page yang dipilih
        print("\nID dan Judul buku dalam page",nBuku)
        list1 = []
        list2 = []
        for data in bukuN['results']:
          list1.append(data['id'])
          list2.append(data['title'])

        dict0 = {}
        for key in list1:
          for value in list2:
            dict0[key] = value
            list2.remove(value)
            break
        
        dict1 = {}
        for i in sorted(dict0):
            dict1[i]=dict0[i]

        for key, value in dict1.items():
            print(key, ' : ', value)

        # Membuat list ID untuk dilihat sekaligus
        daftarBuku = []
        while True:

          while True:
            try:
              id = int(input("Masukkan ID buku dari page diatas: "))
              break
            except:
              print("Tidak ada id yang menggunakan huruf atau simbol\n")

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

        if len(daftarBuku) == 0:
          print("Daftar ID Kosong")
        else:
          for i in daftarBuku:
            info = RakBuku(i)
            info.judul()
            info.author()
            info.subject()
            info.memory()
            print()
        break 
        
      else:
        print("\nPilihan Tidak Ada")

    break

  else:
    if z < 2: print("Captcha anda salah. Coba lagi")
    z += 1
    if z == 2: print("Kesempatan Anda tinggal 1 kali lagi")
    if i == 3: print("Kesempatan Anda habis! Program telah dihentikan!\n")
    break

saranKK = str(input("\nApakah Anda ingin menambahkan kritik atau saran pada program ini? Y/N: "))

if saranKK == 'Y' or saranKK == 'y':
  saran = open('KritikSaranPengguna.txt', 'a')
  tulis = str(input("Apa kritik atau saran Anda?\n"))
  saran.write(tulis+'\n')
  print("\n***Kritik dan saran berhasil ditambahkan***\n")
  saran = open('KritikSaranPengguna.txt','r')
  print(saran.read())
  saran.close()

else:
  print("Kami akan terus mencoba yang terbaik")
