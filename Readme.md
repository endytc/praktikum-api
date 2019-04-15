*  **Installasi**
*  install library requirements `pip install -r requirements.txt`, perintah ini akan melakukan instalasi module-module yang dibutuhkan di dalam requirements.txt
*  buat basisdata dengan mysql, anda tidak perlu menambahkan tabel, tabel akan digenerate oleh django
*  sesuaikan konfigurasi pada file `quickstart/settings.py`, isi `NAME` dengan database name anda. sesuaikan user dan passwordnya
```
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db2.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'praktikum_api',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
```
*  eksekusi `./manage.py makemigrations`, django akan menyiapkan query untuk membuat tabel-tabel berdasarkan class `model` yang anda buat
*  eksekusi `./manage.py migrate`, django akan membuat table-table yang sudah didefinisikan di class model
*  create superuser, username dan password akan digunakan untuk login
     ./manage.py createsuperuser
*  eksekusi `./manage.py runserver`
*  Django admin berhasil diinstall, buka `http://127.0.0.1:8000/admin/` lakukan manipulasi data `jurusan` dan `mahasiswa`
*  Django API dapat diakses melalui `http://127.0.0.1:8000/api/v1/`

