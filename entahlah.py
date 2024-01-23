import requests

#string yang ingin di cari
search_string = "lu nyari apa tulis disini"

#Melakukan pencarian pada halaman
for page_number in range(dari page berapa, 
sampe page berapa):

  #url halaman web yang ingin di cari
    url = f"https://tulisurldisini.com/{page_number}"

  #mengirim get ke url
    response = requests.get(url)

    #mengecek apakah request berhasil
    if response.status_code == 200:

      #Mengecek apakah string ditemukan pada halaman web (jika di temukan maka akan berhenti)
        if search_string in response.text:
            print(f"DI TEMUKAN {page_number}!")
            break
        else:
            print(f"Ga ketemu di halaman {page_number}.")
    else:
        print(f"Gagal melakukan request ke halaman {page_number}.")
