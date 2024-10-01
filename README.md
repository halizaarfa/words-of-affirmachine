 [The Deployment Link: Words of Affir-MACHINE](http://haliza-nafiah-wordsofaffirmachine.pbp.cs.ui.ac.id/)

---

# Tugas 2: Implementasi Model-View-Template (MVT) pada Django
## Implementasi checklist step-by-step
1. **Membuat proyek Django baru**: Pada awalnya, saya membuat direktori dengan nama proyek baru secara lokal. Selanjutnya, saya membuat file ```requirements.txt``` yang berisi hal-hal yang akan diinstal. Melalui Command Prompt, saya masuk ke virtual environment pada direktori tadi kemudian menginstal requirements. Setelah sudah terinstal, saya menjalankan command untuk membuat project Django. Pengecekan apabila project Django sudah dibuat dilakukan pada localhost:8000.

2. **Membuat aplikasi dengan nama ```main``` pada proyek tersebut**: Setelah project Django dibuat, akan ada file manage.py. Saya jalankan command ```python manage.py startapp main``` sehingga dibuatlah direktori aplikasi bernama ```main```. Kemudian, pada file ```settings.py``` yang ada di direktori utama, saya menambahkan ```main``` ke dalam list ```INSTALLED_APPS```.

3. **Melakukan routing pada proyek agar dapat menjalankan aplikasi ```main```**: Saya membuat file ```urls.py``` berisi nama aplikasi ```main``` beserta list ```urlpatterns``` dalam direktori aplikasi. Kemudian, pada file ```urls.py``` yang ada pada direktori proyek, saya menambahkan file ```urls.py``` dari direktori aplikasi ke list ```urlpatterns``` yang ada di dalamnya.

4. **Membuat model pada aplikasi ```main``` dengan nama ```Product``` dan memiliki atribut wajib name, price, description**: Pada file ```models.py``` yang ada di direktori aplikasi, saya membuat class model ```Product``` dan menambahkan atribut CharField ```name```, IntegerField ```price```, serta TextField ```description```. Atribut wajib ini akan dimunculkan pada aplikasi saya, dan nantinya bila saya akan menambahkan atribut lain, maka saya akan menambahkannya pada ```models.py``` kembali. 

5. **Membuat sebuah fungsi pada ```views.py``` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu**: Pada file ```views.py``` yang ada di direktori aplikasi, saya membuat fungsi ```show_main()``` yang memiliki dictionary ```content``` dengan key dan value dari nama aplikasi, nama, serta kelas saya.

6. **Membuat sebuah routing pada ```urls.py``` aplikasi main untuk memetakan fungsi yang telah dibuat pada ```views.py```**: Pada file ```urls.py``` dalam direktori main, saya menambahkan ```path('', include('main.urls')),``` ke list ```urlpatterns``` sehingga akan diarahkan ke ```main``` ketika membuka URL

7. **Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet**: Pada PWS, saya membuat project baru dengan nama wordsofaffirmachine sehingga terbentuk URL "haliza-nafiah-wordsofaffirmachine.pbp.cs.ui.ac.id" yang selanjutnya saya tambahkan ke list ```ALLOWED_HOSTS``` pada file ```settings.py``` yang ada di direktori proyek. Selanjutnya, saya  mengimplementasi MVT dengan memodifikasi file-file sesuai tutorial. Setelah itu, saya melakukan add, commit, dan push ke Github baru kemudian melakukan push ke PWS sehingga proyek saya tidak hanya bisa dibuka pada localhost, tetapi juga pada internet.

## Bagan request client
![Screenshot_20240911_102744](https://github.com/user-attachments/assets/2e9c3432-4d0b-4f1c-ae57-b247aa6cad18)
Pertama, Client mengirim request melalui Browser. Kemudian, request tersebut diproses ```urls.py```, yang menentukan view mana yang akan digunakan. Setelah itu, kode dalam ```views.py``` dijalankan. Jika terdapat data yang diperlukan maka view akan mengambil data dari ```models.py```. Setelah data terkumpul, ```main.html``` akan dirender dengan template dan data tersebut. Kemudian, hasil berupa website akan dikembalikan ke Browser dari Client.

## Fungsi git dalam pengembangan perangkat lunak
Fungsi git adalah sebagai tempat penyimpanan perubahan yang terjadi serta versi-versi dari suatu proyek. Dengan adanya "archive" versi ini, apabila di tengah terjadi masalah, dapat diambil dan digunakan lagi versi sebelum terjadinya perubahan. Selain itu, git memungkinkan kolaborasi antar orang-orang yang mengerjakan suatu proyek, dengan sistem branching yang memungkinkan kode menjadi terorganisasi.

## Mengapa framework Django?
Karena Django mengikuti pola Models-Views-Template (MVT) sehingga memungkinkan pemula memahami cara kerja pengembangan perangkat lunak. Django juga memiliki fitur-fitur yang dapat dengan mudah digunakan dan dikembangkan untuk membangun aplikasi. Selain itu, Django menggunakan bahasa pemrograman Python yang memiliki readability tinggi dan straight-forward. Dengan begitu, pemula dapat dengan mudah memahami struktur kode-kode pada pembuatan aplikasi dengan Django.

## Mengapa model pada Django disebut sebagai ORM?
ORM artinya Object Relational Mapping, yakni teknik menghubungkan antara tabel pada database dengan objek. Pada Django, model merupakan objek-objeknya. Setiap kali dilakukan perubahan pada model, dilakukan pula migrasi untuk memperbarui database mengikuti perubahan yang terjadi. Hal inilah yang disebut dengan ORM, yakni berupa jembatan antara tabel database dengan model pada Django. 

---

# Tugas 3: Implementasi Form dan Data Delivery pada Django
## Mengapa diperlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan karena terjadinya perpindahan informasi atau data antar bagian dalam sistem, misalnya dari server ke client ataupun sebaliknya. Implementasi data delivery memastikan bahwa terjadi integrasi antar bagian-bagian sistem sehingga data berpindah sesuai yang seharusnya.
 
## Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih baik. Hal ini terbukti dari kepopuleran JSON yang melebihi XML, alasan utamanya adalah karena JSON lebih sederhana dan memiliki _readability_ tinggi. Karena sifatnya yang _compact_, ia lebih fleksibel dan cenderung mudah untuk dilakukan _parsing_.

## Fungsi dari method ```is_valid()``` pada form Django dan mengapa dibutuhkannya method tersebut
Method ```is_valid()``` memastikan bahwa semua field pada form Django telah terisi dengan data yang sesuai sebelum berlanjut ke proses berikutnya. Tanpa method ini, program akan terus berjalan meski field pada form kosong, sehingga dapat menyebabkan kesalahan pemrosesan.

## Mengapa dibutuhkan ```csrf_token``` saat membuat form di Django? Apa yang dapat terjadi ```csrf_token``` pada form Django tidak ditambahkan? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
```csrf_token``` dibutuhkan sebagai langkah keamanan untuk memastikan bahwa tidak sembarang orang dapat mengakses form karena token bersifat unik. Tanpa ```csrf_token```, siapapun dapat membuat form palsu dan tidak ada cara untuk memverifikasi bahwa request tersebut berasal dari seseorang yang benar. Hal ini dapat dimanfaatkan penyerang untuk melakukan hal-hal dengan mengatasnamakan orang lain, terutama jika web terkait melibatkan informasi penting seperti transaksi pada bank.

## Implementasi checklist step-by-step
1. **Membuat input form untuk menambahkan objek model pada app sebelumnya.**: Pada proses ini, saya membuat file ```forms.py``` pada direktori main yang isinya class untuk menerima form data Product baru. Selanjutnya, saya meng-import class tersebut ke ```views.py``` dan membuat fungsi yang menerima parameter request di situ. Fungsi inilah yang digunakan untuk memvalidasi dan menerima form data baru. 

2. **Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.**: Pada ```views.py```, saya menambahkan 4 fungsi baru yakni ```show_xml``` dan ```show_json``` yang menerima parameter _request_, serta ```show_xml_by_id``` dan ```show_json_by_id``` yang menerima parameter _request, id_. Kedua fungsi ini akan menampilkan data dari entri Product dalam bentuk XML/JSON masing-masing. Parameter ID ditambahkan sehingga memungkinkan untuk menampilkan hanya entri tertentu saja berdasarkan ID yang telah di-generate.

3. **Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.**: Pada ```urls.py```, saya melakukan import fungsi-fungsi yang telah dibuat pada poin 2. Selanjutnya, saya menambahkan path URL ke list ```urlpatterns``` yang ada pada file tersebut. Path url yang ditambahkan terdiri dari 4, yang masing-masing berkorespondensi dengan tiap fungsi sebelumnya. Misalnya, path ```'xml/'``` akan mengarah ke fungsi ```show_xml```, dan path ```'json/<str:id>/'``` akan mengarah ke fungsi ```show_json_by_id```.

## Screenshot hasil masing-masing URL pada Postman
1. http://localhost:8000/xml/
![xml](https://github.com/user-attachments/assets/e879337f-4779-4dc0-bb2c-a0e764620aed)

2. http://localhost:8000/json/
![json](https://github.com/user-attachments/assets/cfa5ff69-8c6e-4157-969c-a1e7b8ea6321)

3. http://localhost:8000/xml/1651819f-8dc7-4011-9160-9d49c4225117
![json-id](https://github.com/user-attachments/assets/93cdc49d-a397-402c-984d-e09318641434)

4. http://localhost:8000/json/686d6f5b-7c92-4ead-ae65-a9bfbb0f2fa6
![xml-id](https://github.com/user-attachments/assets/ebaea87f-a9c7-4da0-9030-aebcc3a0b820)

---

# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django
## Perbedaan antara ```HttpResponseRedirect()``` dan ```redirect()```
Perbedaan utamanya adalah pada parameter atau argumen. ```HttpResponseRedirect()``` hanya bisa menerima argumen pertama berupa url, sementara pada ```redirect()``` dapat berupa model, view, ataupun url. Fungsi ```redirect()``` sendiri pada dasarnya mengenkapsulasi ```HttpResponseRedirect()```, sehingga dapat dikatakan ```redirect()``` adalah bentuk shortcut yang lebih fleksibel.

## Cara kerja penghubungan model Product dengan User
Pada ```models.py``` ditambahkan atribut user, yang dihubungkan dengan class User melalui method ```models.ForeignKey(User, on_delete=models.CASCADE)```. Dengan ForeignKey, didefinisikan hubungan one-to-many antara User dengan Product, di mana satu user bisa memiliki beberapa produk tetapi tidak sebaliknya. Model User sendiri sudah dimiliki Django sehingga tidak perlu dibuat class User pada ```models.py```. ```on_delete=models.CASCADE``` artinya apabila suatu user dihapus, seluruh produk yang dibuat user tersebut juga terhapus. Pada ```views.py```, variabel ```products``` yang tadinya menampilkan seluruh object diubah menjadi ```products = Product.objects.filter(user=request.user)``` sehingga hanya ditampilkan produk yang dibuat masing-masing user.

## Perbedaan antara authentication dan authorization, mana yang dilakukan saat pengguna login, dan bagaimana Django mengimplementasikan kedua konsep tersebut.
- Authentication: proses memverifikasi identitas pengguna yang login, yakni memastikan bahwa yang login adalah benar sesuai apa yang diisikan pengguna
- Authorization: proses menentukan akses dan izin apa saja yang dimiliki seorang pengguna yang telah login, dan selanjutnya memberikan pengguna akses-akses tersebut

Django mengimplementasikan keduanya. Untuk autentikasi, Django melakukannya melalui fungsi ```authenticate()``` dari ```django.contrib.auth```. Untuk autorisasi, misalnya pada halaman main, ditambahkan dekorator ```@login_required``` sehingga akses hanya terbatas pada halaman itu saja selama pengguna belum login.

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login menggunakan session. Ketika seorang pengguna login, dibuat suatu session ID yang disimpan pada browser pengguna sebagai cookie. Selanjutnya, Django mencocokkan session ID pada cookie dengan informasi pada server untuk setiap request yang dilakukan berikutnya. Session bersifat sementara, serta akan berakhir saat pengguna logout dan dibuat session baru ketika login kembali.

Beberapa kegunaan-kegunaan lain dari cookies di antaranya: mengingat preferensi pengguna serta mempermudah navigasi antarlaman. Contoh preferensi, misalnya, switch antara dark mode dengan light mode. Ketika berpindah laman, mode akan tetap sama, karena masih dalam satu session yang sama. Untuk mengakses laman berbeda pun tidak diperlukan login ulang terus menerus.

Tidak semua cookies aman digunakan. Cookies sebetulnya tidak bisa bertindak sebagai virus bagi device. Data pada cookies pun umumnya tidak berbahaya, karena hanya menyimpan sesi sementara. Namun, sekelibat data yang ada pada cookie tersebut bisa saja dimanfaatkan secara jahat untuk mencuri data pribadi seseorang. Inilah pentingnya tidak langsung mengklik "Accept All Cookies" pada setiap browser, khususnya pada browser yang tidak terlalu umum.

## Implementasi checklist step-by-step
1. **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar**: Untuk fungsi registrasi, digunakan bawaan dari Django, yakni ```UserCreationForm```. Untuk login digunakan ```authenticate```, ```login```, dan ```AuthenticationForm```, dan untuk logout digunakan ```logout```. Seluruh fungsi ini diimplementasikan dengan dilakukannya perubahan pada ```views.py```, ditambahkan path-nya pada ```urls.py```, serta ditambahkan tombol dan tampilannya dalam bentuk html.

2. **Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal**: Pada localhost, saya melakukan registrasi dengan mengisi username dan password. Setelah registrasi akan langsung diarahkan ke laman login, dan saya melakukan login sesuai dengan identitas yang telah dibuat. Setelah login, akan ditampilkan laman utama dengan jumlah produk yang masih kosong. Hal ini karena akun tersebut baru dibuat dan belum menambahkan produk apapun. Barulah saya buat tiga produk dengan tombol add product yang ada pada laman tersebut. Proses ini saya ulangi untuk user kedua. 

3. **Menghubungkan model Product dengan User**: Pada class Product yang ada di ```models.py```, ditambahkan atribut ```user = models.ForeignKey(User, on_delete=models.CASCADE)```. Selanjutnya, variabel ```products``` pada ```views.py``` diubah dari menampilkan all objects menjadi terfilter berdasarkan user yang sedang login, ```products = Product.objects.filter(user=request.user)```.

4. **Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi**: Pada ```views.py```, ```name``` pada dictionary ```context``` diubah value-nya menjadi ```request.user.username```. Dengan ini, informasi nama tidak lagi dalam bentuk statis, melainkan bergantung pada user yang sedang login. Selanjutnya, dilakukan import datetime, HttpResponseRedirect, serta reverse untuk membuat cookie ```last_login```. Kode pada blok ```if form.is_valid()``` diisi dengan kode pembuatan cookie, pada dictionary ```context``` juga ditambahkan key ```last_login``` dengan value ```request.COOKIES['last_login']```. Terakhir, tambahkan ```last_login``` pada berkas ```main.html``` untuk menampilkannya pada laman.