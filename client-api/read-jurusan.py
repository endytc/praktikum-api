import requests

# base url
base_url = "http://127.0.0.1:8000/"


jurusan_request = requests.get(base_url+"api/v1/jurusan/")

# # parsing json
jurusans = jurusan_request.json()

# # print(type(jurusans))

# print(jurusan_request.json())

for jurusan in jurusans["results"]:
  print(jurusan["nama_jurusan"])


jurusan_data = {
    "nama_jurusan": "Teknik Industri",
    "fakultas": "FTT"
}

# jurusan_request = requests.post(base_url+"api/v1/jurusan/",jurusan_data)

# print(jurusan_request.json())



