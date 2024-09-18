# [The Deployment Link: Words of Affir-MACHINE](http://haliza-nafiah-wordsofaffirmachine.pbp.cs.ui.ac.id/)

# Answers
## Implementasi checklist step-by-step
1. **Membuat proyek Django baru**: Pada awalnya, saya membuat direktori dengan nama proyek baru secara lokal. Selanjutnya, saya membuat file _requirements.txt_ yang berisi hal-hal yang akan diinstal. Melalui Command Prompt, saya masuk ke virtual environment pada direktori tadi kemudian menginstal requirements. Setelah sudah terinstal, saya menjalankan command untuk membuat project Django. Pengecekan apabila project Django sudah dibuat dilakukan pada localhost:8000.

2. **Membuat aplikasi dengan nama main pada proyek tersebut**: Setelah project Django dibuat, akan ada file manage.py. Saya jalankan command "_python manage.py startapp main_" sehingga dibuatlah direktori aplikasi bernama _main_. Kemudian, pada file _settings.py_ yang ada di direktori utama, saya menambahkan "main" ke dalam list INSTALLED_APPS.

3. **Melakukan routing pada proyek agar dapat menjalankan aplikasi main**: Saya membuat file _urls.py_ berisi nama aplikasi "main" beserta list urlpatterns dalam direktori aplikasi. Kemudian, pada file _urls.py_ yang ada pada direktori proyek, saya menambahkan file _urls.py_ dari direktori aplikasi ke list urlpatterns yang ada di dalamnya.

4. **Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib name, price, description**: Pada file _models.py_ yang ada di direktori aplikasi, saya membuat class model Product dan menambahkan atribut CharField name, IntegerField price, serta TextField description. Atribut wajib ini akan dimunculkan pada aplikasi saya, dan nantinya bila saya akan menambahkan atribut lain, maka saya akan menambahkannya pada _models.py_ kembali. 

5. **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu**: Pada file _views.py_ yang ada di direktori aplikasi, saya membuat fungsi _show_main_ yang memiliki dictionary _content_ dengan key dan value dari nama aplikasi, nama, serta kelas saya.

6. **Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py**: Pada file _urls.py_ dalam direktori main, saya menambahkan "path('', include('main.urls'))," ke list urlpatterns sehingga akan diarahkan ke main ketika membuka URL

7. **Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet**: Pada PWS, saya membuat project baru dengan nama wordsofaffirmachine sehingga terbentuk URL "haliza-nafiah-wordsofaffirmachine.pbp.cs.ui.ac.id" yang selanjutnya saya tambahkan ke list _ALLOWED_HOSTS_ pada file _settings.py_ yang ada di direktori proyek. Selanjutnya, saya  mengimplementasi MVT dengan memodifikasi file-file sesuai tutorial. Setelah itu, saya melakukan add, commit, dan push ke Github baru kemudian melakukan push ke PWS sehingga proyek saya tidak hanya bisa dibuka pada localhost, tetapi juga pada internet.

## Bagan request client
![Screenshot_20240911_102744](https://github.com/user-attachments/assets/2e9c3432-4d0b-4f1c-ae57-b247aa6cad18)
Pertama, Client mengirim request melalui Browser. Kemudian, request tersebut diproses _urls.py_, yang menentukan view mana yang akan digunakan. Setelah itu, kode dalam _views.py_ dijalankan. Jika terdapat data yang diperlukan maka view akan mengambil data dari _models.py_. Setelah data terkumpul, _main.html_ akan dirender dengan template dan data tersebut. Kemudian, hasil berupa website akan dikembalikan ke Browser dari Client.

## Fungsi git dalam pengembangan perangkat lunak
Fungsi git adalah sebagai tempat penyimpanan perubahan yang terjadi serta versi-versi dari suatu proyek. Dengan adanya "archive" versi ini, apabila di tengah terjadi masalah, dapat diambil dan digunakan lagi versi sebelum terjadinya perubahan. Selain itu, git memungkinkan kolaborasi antar orang-orang yang mengerjakan suatu proyek, dengan sistem branching yang memungkinkan kode menjadi terorganisasi.

## Mengapa framework Django?
Karena Django mengikuti pola Models-Views-Template (MVT) sehingga memungkinkan pemula memahami cara kerja pengembangan perangkat lunak. Django juga memiliki fitur-fitur yang dapat dengan mudah digunakan dan dikembangkan untuk membangun aplikasi. Selain itu, Django menggunakan bahasa pemrograman Python yang memiliki readability tinggi dan straight-forward. Dengan begitu, pemula dapat dengan mudah memahami struktur kode-kode pada pembuatan aplikasi dengan Django.

## Mengapa model pada Django disebut sebagai ORM?
ORM artinya Object Relational Mapping, yakni teknik menghubungkan antara tabel pada database dengan objek. Pada Django, model merupakan objek-objeknya. Setiap kali dilakukan perubahan pada model, dilakukan pula migrasi untuk memperbarui database mengikuti perubahan yang terjadi. Hal inilah yang disebut dengan ORM, yakni berupa jembatan antara tabel database dengan model pada Django. 
