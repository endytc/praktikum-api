import requests
# base url
base_url = "http://127.0.0.1:8000/"

mahasiswa_request = requests.get(base_url+"api/v1/mahasiswa/")

# print(mahasiswa_request.content)
# # parsing json
mahasiswas = mahasiswa_request.json()

# print(type(mahasiswas))

# print(mahasiswa_request.json())

for mahasiswa in mahasiswas["results"]:
  print("%s %s %s" % (mahasiswa["nim"],mahasiswa["nama"],mahasiswa["jurusan_text"]))