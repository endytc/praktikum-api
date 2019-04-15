*  **Installasi**
*  install library requirements `pip install -r requirements.txt`, perintah ini akan melakukan instalasi module-module yang dibutuhkan di dalam requirements.txt
*  buat basisdata dengan mysql
*  sesuaikan konfigurasi pada file `quickstart/settings.py`
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
*  eksekusi `./manage.py makemigrations`
*  eksekusi `./manage.py migrate`
*  create superuser, inputkan username dan password
     ./manage.py createsuperuser
*  eksekusi `./manage.py runserver`
*  buka `http://127.0.0.1:8000/api/v1/` lakukan manipulasi data

