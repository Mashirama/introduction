GNU nano 6.3                  sadap
import requests, os

def logo():                                                         print("""
    |SadapByNov41|
    |Author :Mr.Nova1|
    |judul:sadap|
                                                                  """)

def menu():
  os.system('clear')
  logo()
  print("\nMasukan Nomer Di Awali (62xxx)")                         nomor = input("Nomer Target :62")
  jum = int(input("Jumlah : "))
  for i in range(jum):
      req = requests.get("https://ainxbot-sms.herokuapp.com/api/s>


    if 'terkirim' in req:
           print("\nSpam Terkirim")
      else:
           print("\nSpam Gagal")
           os.system('clear')

menu()
