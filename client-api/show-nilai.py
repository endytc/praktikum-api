import requests

# base url
base_url = "http://127.0.0.1:8000/"


nilai_request = requests.get(base_url+"api/v1/mahasiswa/nilai/07650062")

# # parsing json
nilais = nilai_request.json()

# # print(type(nilais))

# print(nilai_request.json())
print("mahasiswa %s" % nilais.get("mahasiswa").get("nama"))
for nilai in nilais["nilai"]:
  print(("%s: %s") % (nilai["matakuliah"],nilai["nilai"]))


# nilai_request = requests.post(base_url+"api/v1/nilai/",nilai_data)

# print(nilai_request.json())



