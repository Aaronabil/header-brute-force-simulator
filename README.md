# 🔐 Brute Force Custom HTTP Header (Simulasi Edukasi)

Simulasi brute force terhadap custom HTTP header — berguna untuk edukasi keamanan API dan pengujian keamanan berbasis token. Cocok untuk memahami risiko apabila developer menyimpan otentikasi dalam header tanpa validasi ketat.

> ⚠️ **Disclaimer:** Tools ini hanya untuk **pembelajaran & simulasi lokal**. Jangan digunakan terhadap sistem nyata tanpa izin.

---

## Deskripsi

Simulasi ini menargetkan header custom seperti: X-Device-ID: device-xxxxxx

Tujuan dari script ini adalah menebak kombinasi `xxxxxx` menggunakan metode brute force.
Untuk contoh disini saya menggunakan kombinasi `a1b2c3`

---

## Tujuan Edukasi

- Mengenali risiko penggunaan header sebagai satu-satunya autentikasi.
- Memahami pentingnya entropi dan panjang token.
- Belajar dasar brute force & eksplorasi kombinasi token.

---

## Parameter yang bisa disesuaikan

- `TARGET_HEADER`
Nilai header yang ingin ditebak
- `charset`
Karakter yang digunakan, untuk a-z menggunakan string.ascii_lowercase dan untuk 0-9 menggunakan string.digits
- `length`
Panjang token target (default 6)
- `sleep()`
Bisa ditambahkan untuk simulasi delay tetapi disini saya tidak memakainya

## Contoh Penggunaan
- Buka file di visual studio code atau code editor lain
- Buka terminal
- Jalankan
```
python week2_sesi3.py
```

### Contoh kombinasi a1b2c3:
![Hasil](https://github.com/Aaronabil/header-brute-force-simulator/blob/main/hasil.jpg?raw=true)
- Disini saya melakukan 45.432.678 percobaan dan memakan waktu 2578 detik atau setara dengan 42 menit

---

## Potensi Pengembangan
- CLI interaktif (input target, charset, panjang token)
- Multi-threaded brute force (lebih cepat)
- Simulasi server lokal untuk pengujian end-to-end

---

## Penutup
- Header brute force adalah salah satu contoh bagaimana kesalahan kecil dalam desain autentikasi bisa berdampak besar. Pelajari, uji, dan gunakan pengetahuan ini secara etis.




