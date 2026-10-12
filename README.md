# Pertemuan 07 Fungsi Python 
 
Nama: Riki Agil Saputra


NIM: 2225250026


Kelas: 3A
 
## Tujuan 
Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular. 
 
## Cara Menjalankan 
python3 praktik/utilitas_matematika.py 
 
## Struktur Fungsi 

1. def luas_persegi_panjang
    dipakai untuk menentukan luas persegi panjang dengan tanpa membuat fungsi baru di setiap blok lain karena menggunakan fungsi def. Fungsi ini mneggunakan parameter p = panjang dan l = lebar dengan return nilai = p * l = panjang * lebar = luas persegi panjang.


2. def_luas_segitiga
    dipakai untuk menentukan luas segitiga dengan tanpa harus membuat fungsi baru dis etiap blok lain karena menggunakan fungsi def. Fungsi ini menggunakan parameter a = panjang alas dan t = tinggi dengan return nilai = a * t + alas * tinggi = luas segitiga.


3. jumlah_n
    Fungsi yang dipakai untuk menghitung jumlah dari angka-angka yang diinginkan sesuai dengan range yang diinput. Parameter yang dipakai adalah n = angka ke-n pada deret aritmatika dengan return berupa total = total penjumlahan dari angka pertama hingga angka ke-n


4. def faktorial
    Fungsi ini dipakai untuk menghitung nilai faktorial dengan parameter yang dipakai merupakai n = nilai ke-n faktorial dengna return berupa hasil = nilai yang diperoleh dari hasil operasi faktorial.


5. tampilkan_menu
    Fungsi ini dipakai untuk menampilkan menu pilihan yang dapat dipilih oleh pengguna program. Fungsi ini tidak memiliki parameter, sehingga tidak memerlukan argumen. Fungsi ini juga tidak mengembalikan nilai (return) karena fungsi ini hanya menampilkan teks saja.

 
## Hasil Pengujian 

| Operasi | Input | Hasil yang diharapkan | Keluaran aktual | Status |
| :--- | :--- | :---: | :---: | :---: |
| Luas persegi Panjang | p = 8, l = 5 | 40 | 40 | Sesuai |
| Luas segitiga | a = 10, t = 6 | 30.0 | 30.0 | Sesuai |
| Jumlah 1..n | n = 10 | 55 | 55 | Sesuai |
| Faktorial | n = 5 | 120 | 120 | Sesuai |
| Faktorial | n = 0 | 1 | 1 | Sesuai |

## Refleksi 
Jelaskan satu bagian program yang menjadi lebih sederhana setelah dipisah menjadi fungsi.
Bagian program faktorial. Sebelum dipisah menjadi fungsi, setelah memvalidasi input, kita harus membuat kode program lagi di bawah validasi input, sehingga membuat kode menjadi lebih panjang. Namun,setelah dipisah menjadi fungsi, maka setelah validasi input kita hanya perlu memanggil fungsi yang telah didefinisikan sebelumnya.