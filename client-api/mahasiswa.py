import requests
# base url
base_url = "http://127.0.0.1:8000/"

mahasiswa_request = requests.get(base_url+"api/v1/mahasiswa/")

# print(mahasiswa_request.content)
# # parsing json
mahasiswaList = mahasiswa_request.json()

# print(type(mahasiswas))

# print(mahasiswa_request.json())

for mahasiswa in mahasiswaList["results"]:
  print("[%s] %s %s" % (mahasiswa["nim"],mahasiswa["nama"],mahasiswa["jurusan"]))

nim = input("NIM  : ")

matakuliah_request = requests.get(base_url+"api/v1/matakuliah/")
matakuliahList = matakuliah_request.json()

for matakuliah in matakuliahList["results"]:
  nilai = input("Nilai matakuliah %s: " % matakuliah["matakuliah"])
  data = {
    "nim":nim,
    "matakuliah_id":matakuliah["id"],
    "nilai": float(nilai)
  }
  response = requests.post(base_url+"api/v1/mahasiswa/nilai",data)
  print(response.content)
