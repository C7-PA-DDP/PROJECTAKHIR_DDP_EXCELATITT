# Sistem Reservasi Gym & Fitness

Aplikasi **berbasis terminal (CLI)** yang ditulis dengan **Python** untuk mengelola reservasi kelas di pusat kebugaran: mulai dari registrasi dan login member, top up saldo, pemesanan kelas lengkap dengan invoice, hingga pengelolaan kelas dan pemantauan reservasi oleh admin. Seluruh data disimpan permanen dalam file **JSON**.

---

## Anggota Kelompok

| No | Nama | NIM | Peran dalam kelompok |
|:--:|------|:---:|---------------------|
| 1 | Marexcel Elibino | 2609116087 | Kode program dan Flowchart |
| 2 | Muhammad Ardhika Prasanjayu | 2609116108 | Codingan Python |
| 3 | Alfian Nugraha | 2609116084 | Laporan dan Flowchart |
| 4 | Novitasari Muhammad Noor | 2609116082 | Laporan dan Flowchart |

Program Studi Sistem Informasi, Fakultas Teknik, Universitas Mulawarman, Samarinda.

---


## Deskripsi Singkat

**Sistem Reservasi Gym & Fitness** memudahkan pengelolaan kelas kebugaran (Zumba, Body Pump, Body Combat, Spinning, Pilates, dan kelas lain yang ditambahkan admin) tanpa pencatatan manual. Program membedakan dua peran pengguna:

- **Member** mendaftar sendiri, mengisi saldo, memesan kelas yang masih memiliki kuota, melihat riwayat, dan membatalkan reservasi dengan pengembalian dana (refund) otomatis ke saldo.
- **Admin** mengelola data kelas (tambah, ubah, hapus) serta memantau seluruh reservasi dan daftar member.

Setiap perubahan data langsung ditulis ke file JSON sehingga data tetap ada ketika program ditutup dan dijalankan kembali.

---

## Fitur Program

### Fitur Umum

| Fitur | Keterangan |
|-------|------------|
| Registrasi member | Username otomatis diubah ke huruf kecil, tidak boleh mengandung spasi dan tidak boleh sama dengan username lain. Password minimal 4 karakter. |
| Login dengan batas percobaan | Maksimal **3 kali** percobaan. Password disembunyikan saat diketik (ditampilkan sebagai `*`). |
| Keamanan password | Password disimpan dalam bentuk hash **SHA-256**, bukan teks asli. |
| Pemisahan peran | Setelah login, pengguna diarahkan ke menu **Admin** atau menu **Member** sesuai `role`-nya. |
| Validasi input | Input teks tidak boleh kosong, input angka harus bilangan bulat dan memenuhi nilai minimum, pilihan menu yang salah ditolak. |
| Penyimpanan otomatis | File JSON dibuat otomatis jika belum ada. Jika file rusak, program memakai data bawaan. Data pengguna versi lama dilengkapi otomatis oleh `lengkapi_data_user()`. |
| Penanganan `Ctrl+C` | Program tidak langsung berhenti, melainkan kembali ke menu awal. |

### Fitur Member

| Menu | Keterangan |
|------|------------|
| 1. Lihat Kelas | Menampilkan tabel kelas: ID, nama, instruktur, jadwal, harga, dan sisa kuota. |
| 2. Reservasi Kelas | Memesan kelas berdasarkan ID. Program memeriksa kelas ada, kuota belum penuh, belum pernah memesan kelas yang sama (yang masih aktif), dan saldo cukup. Jika berhasil, saldo dipotong, kuota berkurang 1, dan **invoice** dicetak. |
| 3. Top Up Saldo | Pilih paket Rp50.000 / Rp100.000 / Rp200.000 / Rp500.000 atau nominal lain. Nominal harus antara **Rp10.000 dan Rp5.000.000**. |
| 4. Riwayat Reservasi | Menampilkan semua reservasi milik member (status *Aktif* maupun *Dibatalkan*). |
| 5. Batalkan Reservasi | Membatalkan reservasi aktif berdasarkan nomor invoice. Status menjadi *Dibatalkan*, saldo dikembalikan penuh, dan kuota kelas bertambah 1. |

### Fitur Admin

| Menu | Keterangan |
|------|------------|
| 1. Lihat Kelas | Menampilkan seluruh kelas beserta sisa kuota. |
| 2. Tambah Kelas | Menambah kelas baru. ID dibuat otomatis (ID terbesar + 1). Harga dan kuota minimal 1. |
| 3. Ubah Kelas | Mengubah nama, instruktur, jadwal, harga, dan kuota. Mengosongkan input (Enter) berarti data tidak diubah. Harga minimal 1, kuota minimal 0. |
| 4. Hapus Kelas | Menghapus kelas setelah konfirmasi `y/n`. Kelas yang **masih memiliki reservasi aktif tidak dapat dihapus**. |
| 5. Lihat Semua Reservasi | Menampilkan seluruh reservasi dari semua member. |
| 6. Lihat Daftar Member | Menampilkan username, role, saldo, dan waktu terdaftar semua akun. |

### Akun Bawaan

| Username | Password | Role |
|----------|----------|------|
| `admin` | `admin123` | admin |

Akun admin dibuat otomatis jika belum ada. Member baru dibuat lewat menu **Registrasi**.

### Data Kelas Bawaan

| ID | Kelas | Instruktur | Jadwal | Harga | Kuota |
|:--:|-------|------------|--------|------:|:-----:|
| 1 | Zumba | Fina | Senin 07:00 | Rp50.000 | 15 |
| 2 | Body Pump | Juhdi | Selasa 17:00 | Rp40.000 | 20 |
| 3 | Body Combat | Alfian | Rabu 18:30 | Rp60.000 | 12 |
| 4 | Spinning | Excel | Kamis 06:30 | Rp55.000 | 10 |
| 5 | Pilates | Vita | Jumat 16:00 | Rp65.000 | 8 |

---

## Teknologi dan Cara Menjalankan

| Komponen | Keterangan |
|----------|------------|
| Bahasa | Python 3.6 atau lebih baru |
| Library bawaan Python | `json`, `os`, `hashlib`, `time`, `random` |
| Library tambahan | [`prettytable`](https://pypi.org/project/prettytable/) (tampilan tabel) dan [`pwinput`](https://pypi.org/project/pwinput/) (input password bertanda `*`) |
| Penyimpanan | File JSON (`users.json`, `kelas.json`, `reservasi.json`) |

**Instalasi library tambahan**

```bash
pip install prettytable pwinput
```

**Menjalankan program**

```bash
python konsul2.py
```

Pada saat pertama kali dijalankan, ketiga file JSON dibuat otomatis di folder yang sama dengan `konsul2.py`.

---

## Struktur Program dan Penyimpanan Data

### Struktur Folder

```text
.
├── konsul2.py                    # kode program utama
├── reservasi_gym_fitnes.drawio   # flowchart (3 halaman: Main, Menu Admin, Menu User)
├── README.md
├── images/
│   ├── flowchart/                # gambar flowchart
│   └── output/                   # screenshot output program
├── users.json                    # dibuat otomatis
├── kelas.json                    # dibuat otomatis
└── reservasi.json                # dibuat otomatis
```

### Struktur Kode

Kode dibagi menjadi fungsi-fungsi kecil yang dikelompokkan berdasarkan tugasnya.

| Kelompok | Fungsi / Konstanta | Tugas |
|----------|--------------------|-------|
| Konfigurasi | `FILE_USERS`, `FILE_KELAS`, `FILE_RESERVASI`, `PAKET_TOPUP`, `ROLE_VALID`, `MIN_TOPUP`, `MAX_TOPUP`, `DEFAULT_USERS`, `DEFAULT_KELAS` | Nama file data, paket dan batas top up, daftar role, serta data awal (akun admin dan 5 kelas). |
| Keamanan | `hash_password()`, `sudah_hash()` | Membuat hash SHA-256 dan memeriksa apakah suatu teks sudah berupa hash (64 karakter heksadesimal). |
| Utilitas tampilan dan input | `bersihkan_layar()`, `jeda()`, `rupiah()`, `input_teks()`, `input_angka()`, `input_password()` | Membersihkan layar, menunggu Enter, format `Rp50.000`, serta input yang tervalidasi (tidak kosong, angka bulat, password tersembunyi). |
| Penyimpanan data | `simpan_data()`, `muat_data()`, `lengkapi_data_user()` | Menulis dan membaca JSON, membuat file dari data default bila belum ada atau rusak, serta melengkapi data pengguna versi lama. |
| Tampilan tabel | `tampil_kelas()`, `tampil_reservasi()`, `tampil_users()`, `cetak_invoice()` | Mencetak tabel (PrettyTable) dan invoice reservasi. |
| Fungsi bantu logika | `cari_kelas()`, `buat_id_baru()`, `buat_no_invoice()`, `jumlah_reservasi_aktif()`, `sudah_reservasi()`, `bayar_saldo()` | Mencari kelas, membuat ID kelas dan nomor invoice unik, menghitung reservasi aktif, memeriksa duplikasi reservasi, dan memotong saldo. |
| Autentikasi | `registrasi()`, `login()` | Pendaftaran member dan verifikasi login (maksimal 3 percobaan). |
| Fitur admin | `tambah_kelas()`, `ubah_kelas()`, `hapus_kelas()`, `menu_admin()` | Pengelolaan kelas dan menu admin. |
| Fitur member | `top_up()`, `reservasi_kelas()`, `riwayat_user()`, `batal_reservasi()`, `menu_user()` | Top up, pemesanan, riwayat, pembatalan, dan menu member. |
| Program utama | `main()` dan blok `if __name__ == "__main__"` | Memuat data, menampilkan menu utama, mengarahkan ke menu sesuai role, dan menangkap `Ctrl+C`. |

### Struktur Data di Memori

Saat program dimulai, tiga file JSON dibaca satu kali ke dalam tiga variabel di `main()`, lalu dikirim sebagai parameter ke fungsi-fungsi yang membutuhkan.

| Variabel | Tipe | Isi |
|----------|------|-----|
| `users` | `dict` (kunci: username) | Data akun: password (hash), role, saldo, waktu terdaftar |
| `daftar_kelas` | `list` berisi `dict` | Data kelas |
| `reservasi` | `list` berisi `dict` | Data transaksi reservasi |

Setiap kali data berubah (registrasi, top up, reservasi, pembatalan, tambah/ubah/hapus kelas), fungsi `simpan_data()` langsung menulis ulang file JSON yang bersangkutan.

### Penyimpanan Data (File JSON)

Data disimpan dalam tiga file berformat JSON (UTF-8, indentasi 4 spasi).

**1. `users.json` — data akun** (objek dengan username sebagai kunci)

| Field | Tipe | Keterangan |
|-------|------|------------|
| `password` | string | Hash SHA-256 dari password |
| `role` | string | `admin` atau `user` |
| `saldo` | integer | Saldo dalam rupiah |
| `terdaftar` | string | Waktu registrasi (`dd-mm-yyyy HH:MM`), `-` untuk admin bawaan |

```json
{
    "admin": {
        "password": "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9",
        "role": "admin",
        "saldo": 0,
        "terdaftar": "-"
    },
    "user": {
        "password": "e8979d2eb704c94fa2fa5044edba1c29232526eec3965ffc64308b6783f2de12",
        "role": "user",
        "saldo": 60000,
        "terdaftar": "03-11-2026 12:43"
    }
}
```

**2. `kelas.json` — data kelas** (array)

| Field | Tipe | Keterangan |
|-------|------|------------|
| `id` | integer | ID unik kelas |
| `nama` | string | Nama kelas |
| `instruktur` | string | Nama instruktur |
| `jadwal` | string | Hari dan jam kelas |
| `harga` | integer | Harga per sesi (rupiah) |
| `kuota` | integer | Sisa kuota |

```json
[
    {
        "id": 1,
        "nama": "Zumba",
        "instruktur": "Fina",
        "jadwal": "Senin 07:00",
        "harga": 50000,
        "kuota": 15
    }
]
```

**3. `reservasi.json` — data reservasi** (array)

| Field | Tipe | Keterangan |
|-------|------|------------|
| `invoice` | string | Nomor invoice unik, format `INV-yymmdd-xxxx` |
| `username` | string | Pemesan |
| `id_kelas` | integer | ID kelas yang dipesan |
| `nama_kelas` | string | Nama kelas saat dipesan |
| `jadwal` | string | Jadwal saat dipesan |
| `harga` | integer | Harga yang dibayar |
| `waktu` | string | Waktu pemesanan |
| `status` | string | `Aktif` atau `Dibatalkan` |

```json
[
    {
        "invoice": "INV-261103-6234",
        "username": "juhdi",
        "id_kelas": 2,
        "nama_kelas": "Body Pump",
        "jadwal": "Selasa 17:00",
        "harga": 40000,
        "waktu": "03-11-2026 12:43",
        "status": "Aktif"
    }
]
```

> Reservasi yang dibatalkan **tidak dihapus**, melainkan hanya diubah statusnya menjadi `Dibatalkan` agar riwayat tetap tercatat.

---

## Flowchart dan Penjelasan Alur

Flowchart dibuat dengan **draw.io** (file sumber: [`reservasi_gym_fitnes.drawio`](reservasi_gym_fitnes.drawio)) dan terdiri dari **3 halaman**: *Main*, *Menu Admin*, dan *Menu User*. Setiap halaman ditampilkan utuh sebagai gambaran umum, lalu dipotong per fitur agar mudah dibaca. Klik gambar untuk memperbesar.

**Simbol yang digunakan**

| Simbol | Arti |
|--------|------|
| Oval hijau | Mulai / Selesai |
| Jajar genjang oranye | Input atau output (tampilan) |
| Persegi biru / ungu | Proses / pemanggilan fungsi |
| Belah ketupat kuning | Keputusan (Ya / Tidak) |
| Silinder oranye tua | Proses yang membaca atau menulis data (JSON) atau menampilkan tabel data |
| Lingkaran bernomor **1** | Penghubung kembali ke awal perulangan menu pada halaman yang sama |
| Pentagon **A**, **B**, **C** | Penghubung antarhalaman: **A** = Menu Admin, **B** = Menu Member, **C** = kembali ke Menu Utama setelah logout |
### Halaman 1: Alur Utama (Main)

<p align="center">
<img width="3817" height="2426" alt="reservasi_gym_fitnes-Flowchart Reservasi Gym   Fitness (Main) drawio" src="https://github.com/user-attachments/assets/f19f10f4-51a9-4c86-b5e7-a9dc412ab43f" />

  <em>Gambar 1. Flowchart utama (gambaran umum)</em>
</p>

Alur utama mencakup inisialisasi program, menu utama, login, registrasi, dan keluar. Rinciannya dijelaskan per bagian berikut.

#### a. Inisialisasi dan memuat data

<p align="center">
<img width="646" height="404" alt="Screenshot 2026-11-03 214030" src="https://github.com/user-attachments/assets/d13a36c8-603f-4444-bbc5-56591d9a47b2" />    
    
  <em>Gambar 2. Flowchart utama: inisialisasi, memuat data, dan menu utama</em>
</p>

1. Program **dimulai**, lalu mengimpor library (`os`, `time`, `json`, `hashlib`, `random`, `prettytable`, `pwinput`) dan mendeklarasikan konstanta serta data default.
2. Program **membaca** `users.json`, `kelas.json`, dan `reservasi.json`.
3. Jika terjadi **FileNotFoundError**, program menampilkan *"File belum ada, membuat file baru..."*. Jika terjadi **ValueError** (JSON rusak atau tipe data salah), program menampilkan *"File rusak, memakai data default."*. Pada kedua kasus, data default disimpan ke file lewat `simpan_data()` lalu dipakai.
4. `lengkapi_data_user(users)` dijalankan: password lama yang belum di-hash diubah menjadi hash, akun yang rusak dibuang, akun `admin` dipastikan ada, lalu `users.json` disimpan.
5. Layar dibersihkan dan **menu utama** ditampilkan (1. Login, 2. Registrasi, 0. Keluar). Pilihan pengguna diperiksa berurutan: `'1'` → Login, `'2'` → Registrasi, `'0'` → Keluar, selain itu → *"Menu tidak valid!"*.

#### b. Login

<p align="center">
<img width="479" height="406" alt="image" src="https://github.com/user-attachments/assets/16de12e6-b27c-4e2a-8622-df3ca2f86ba5" />    
    
  <em>Gambar 3. Flowchart utama: proses login</em>
</p>

1. Menampilkan judul `=== LOGIN ===` dan menyiapkan penghitung `percobaan = 0`.
2. Selama `percobaan < 3`: pengguna memasukkan **username** (diubah ke huruf kecil) dan **password** (disamarkan).
3. Program memeriksa apakah **username ada di `users` dan hash password cocok**.
   - **Tidak cocok**: tampil *"Username/password salah! (sisa percobaan: ...)"*, `percobaan` bertambah 1, lalu kembali ke pemeriksaan jumlah percobaan.
   - **Cocok**: tampil *"Login berhasil! Selamat datang, username."*, kemudian program memeriksa `role`. Jika `admin` menuju konektor **A** (Menu Admin), selain itu menuju konektor **B** (Menu Member).
4. Jika `percobaan` sudah mencapai 3, tampil *"Login gagal 3 kali."*, program menjalankan `jeda()` lalu kembali ke menu utama.

#### c. Registrasi

<p align="center">
<img width="326" height="417" alt="image" src="https://github.com/user-attachments/assets/af2f0e8e-fff2-41be-836a-3047258333f0" />    
    
  <em>Gambar 4. Flowchart utama: proses registrasi</em>
</p>

1. Menampilkan `=== REGISTRASI MEMBER ===` dan meminta **username** (diubah ke huruf kecil).
2. Validasi berurutan:
   - Username mengandung **spasi** → *"Username tidak boleh mengandung spasi!"*.
   - Username **sudah ada** di `users` → *"Username sudah dipakai!"*.
3. Jika lolos, pengguna memasukkan **password** (disamarkan). Jika panjangnya **kurang dari 4 karakter** → *"Password minimal 4 karakter!"*.
4. Jika semua valid, akun dibuat dengan isi: password (hash), `role = 'user'`, `saldo = 0`, dan `terdaftar` = waktu sekarang. Data disimpan ke `users.json` dan tampil *"Registrasi berhasil! Silakan login."*.
5. Setiap jalur (berhasil maupun gagal) berakhir di `jeda()` lalu kembali ke menu utama.

#### d. Keluar dan pilihan tidak valid

<p align="center">
<img width="210" height="237" alt="image" src="https://github.com/user-attachments/assets/c3bfe99b-8b7f-48ae-8acc-78353be81e87" />    
    
  <em>Gambar 5. Flowchart utama: keluar program dan pilihan tidak valid</em>
</p>

- Pilihan `'0'`: tampil *"Terima kasih telah menggunakan sistem ini!"*, perulangan dihentikan dengan `break`, dan program **selesai**.
- Pilihan lain: tampil *"Menu tidak valid!"*, `jeda()`, lalu kembali ke menu utama.

---

### Halaman 2: Menu Admin

<p align="center">
<img width="5672" height="2600" alt="reservasi_gym_fitnes-Menu Admin drawio" src="https://github.com/user-attachments/assets/7c3d212a-ab92-493a-afb3-cde90b686940" />    
    
  <em>Gambar 6. Flowchart Menu Admin (gambaran umum)</em>
</p>

Menu admin berjalan dalam perulangan `while True` sampai admin memilih **0. Logout**. Setiap fitur (kecuali logout) diakhiri `jeda()` lalu kembali ke awal menu.

#### a. Menu dan Lihat Kelas (pilihan 1)

<p align="center">
<img width="306" height="323" alt="Screenshot 2026-11-03 215235" src="https://github.com/user-attachments/assets/8f6fc20e-e8fc-4ecf-a4d8-d33bde355ec3" />    
    
  <em>Gambar 7. Flowchart Menu Admin: tampilan menu dan Lihat Kelas</em>
</p>

Dari konektor **A**, layar dibersihkan dan menu admin ditampilkan (enam pilihan + logout), lalu pilihan dibaca. Pilihan `'1'` memanggil `tampil_kelas(daftar_kelas)` untuk menampilkan tabel semua kelas.

#### b. Tambah Kelas (pilihan 2)

<p align="center">
<img width="167" height="417" alt="image" src="https://github.com/user-attachments/assets/d534210a-4ee7-40fe-987e-0912e7eedf87" />    
    
  <em>Gambar 8. Flowchart Menu Admin: Tambah Kelas</em>
</p>

1. ID baru dibuat oleh `buat_id_baru()` (ID terbesar + 1, atau 1 jika belum ada kelas).
2. Admin mengisi nama kelas, instruktur, jadwal (tidak boleh kosong), serta harga dan kuota (bilangan bulat minimal 1).
3. Data kelas baru ditambahkan dan disimpan ke `kelas.json`, lalu tampil *"Kelas berhasil ditambahkan!"*.

#### c. Ubah Kelas (pilihan 3)

<p align="center">
<img width="263" height="422" alt="image" src="https://github.com/user-attachments/assets/cb91789e-7d39-42cf-b433-17cdacc2cb40" />    
    
  <em>Gambar 9. Flowchart Menu Admin: Ubah Kelas</em>
</p>

1. Tabel kelas ditampilkan, lalu admin memasukkan **ID kelas**. `cari_kelas()` mencari kelas tersebut. Jika tidak ditemukan → *"Kelas tidak ditemukan!"*.
2. Jika ditemukan, admin diminta mengisi nama, instruktur, dan jadwal baru. **Mengosongkan input berarti data tidak diubah.**
3. Untuk harga dan kuota, setiap input yang diisi divalidasi: harus **angka bulat** (jika bukan → *"... harus angka, tidak diubah."*) dan memenuhi **nilai minimum** (harga minimal 1, kuota minimal 0; jika tidak → *"... tidak diubah (minimal ...)."*). Nilai yang tidak valid dilewati tanpa membatalkan perubahan lainnya.
4. Perubahan disimpan ke `kelas.json` dan tampil *"Kelas berhasil diperbarui!"*.

#### d. Hapus Kelas (pilihan 4)

<p align="center">
<img width="247" height="365" alt="image" src="https://github.com/user-attachments/assets/ebe077c5-c521-4985-9eb0-4c3cd7dba502" />    
    
  <em>Gambar 10. Flowchart Menu Admin: Hapus Kelas</em>
</p>

1. Tabel kelas ditampilkan dan admin memasukkan **ID kelas**. Jika tidak ditemukan → *"Kelas tidak ditemukan!"*.
2. Program memeriksa `jumlah_reservasi_aktif(reservasi, id) > 0`. Jika kelas **masih memiliki reservasi aktif** → *"Kelas masih memiliki reservasi aktif, tidak bisa dihapus!"* dan proses dihentikan.
3. Jika tidak ada reservasi aktif, admin diminta konfirmasi *"Yakin hapus ...? (y/n)"*. Jawaban selain `y` → *"Penghapusan dibatalkan."*. Jawaban `y` → kelas dihapus, `kelas.json` disimpan, dan tampil *"Kelas berhasil dihapus!"*.

#### e. Lihat Semua Reservasi dan Lihat Daftar Member (pilihan 5 dan 6)

<p align="center">
<img width="378" height="217" alt="image" src="https://github.com/user-attachments/assets/1c620dfe-f7d6-4c57-b58c-e39e8e39038f" />    
    
  <em>Gambar 11. Flowchart Menu Admin: Lihat Semua Reservasi dan Lihat Daftar Member</em>
</p>

- Pilihan `'5'` memanggil `tampil_reservasi(reservasi)` untuk menampilkan semua reservasi dari seluruh member.
- Pilihan `'6'` memanggil `tampil_users(users)` untuk menampilkan username, role, saldo, dan waktu terdaftar.

#### f. Logout dan pilihan tidak valid

<p align="center">
<img width="427" height="294" alt="image" src="https://github.com/user-attachments/assets/90868a63-7aec-48fd-9359-96fbcf0e3ee2" />    
    
  <em>Gambar 12. Flowchart Menu Admin: logout dan pilihan tidak valid</em>
</p>

- Pilihan `'0'`: tampil *"Logout berhasil."*, perulangan dihentikan (`break`), dan alur kembali ke menu utama melalui konektor **C**.
- Pilihan lain: tampil *"Menu tidak valid!"*, `jeda()`, lalu kembali ke menu admin.

---

### Halaman 3: Menu User (Member)

<p align="center">
<img width="5192" height="2782" alt="reservasi_gym_fitnes-Menu User drawio" src="https://github.com/user-attachments/assets/000f33ba-876d-44e6-96cd-6a0a272537fb" />    
    
  <em>Gambar 13. Flowchart Menu User (gambaran umum)</em>
</p>

Menu member juga berjalan dalam perulangan `while True` sampai member memilih **0. Logout**. Selain daftar menu, **saldo member** ditampilkan di bagian atas setiap kali menu muncul.

#### a. Menu dan Lihat Kelas (pilihan 1)

<p align="center">
<img width="319" height="347" alt="image" src="https://github.com/user-attachments/assets/203e1bb2-115e-4c0b-a229-f58501d9e5a2" />

  <em>Gambar 14. Flowchart Menu User: tampilan menu dan Lihat Kelas</em>
</p>

Dari konektor **B**, layar dibersihkan, menu member ditampilkan beserta saldo, lalu pilihan dibaca. Pilihan `'1'` memanggil `tampil_kelas(daftar_kelas)`.

#### b. Reservasi Kelas (pilihan 2)

<p align="center">
<img width="188" height="395" alt="image" src="https://github.com/user-attachments/assets/f1bc3673-8a90-4cb8-bdc3-25c4fe45a049" />

  <em>Gambar 15. Flowchart Menu User: Reservasi Kelas</em>
</p>

Setelah tabel kelas ditampilkan dan member memasukkan ID kelas, program melakukan **empat pemeriksaan berurutan**. Jika salah satu gagal, proses berhenti dengan pesan yang sesuai lalu menuju `jeda()`:

| Urutan | Pemeriksaan | Pesan jika gagal |
|:------:|-------------|------------------|
| 1 | Kelas dengan ID tersebut ada (`k is None`?) | *Kelas tidak ditemukan!* |
| 2 | Kuota masih tersedia (`kuota <= 0`?) | *Maaf, kuota kelas sudah penuh!* |
| 3 | Belum pernah memesan kelas yang sama dan masih aktif (`sudah_reservasi`) | *Anda sudah mereservasi kelas ini!* |
| 4 | Saldo mencukupi (`bayar_saldo` gagal jika `saldo < harga`) | *Saldo tidak cukup! Harga ..., saldo ...* |

Jika semua pemeriksaan lolos: saldo dikurangi harga kelas, kuota kelas dikurangi 1, dan data reservasi dibuat (nomor invoice dari `buat_no_invoice()`, status `Aktif`) lalu ditambahkan ke daftar reservasi. Ketiga file (`users.json`, `kelas.json`, `reservasi.json`) disimpan, tampil *"Reservasi berhasil!"*, dan `cetak_invoice()` mencetak invoice.

#### c. Top Up Saldo (pilihan 3)

<p align="center">
<img width="401" height="408" alt="image" src="https://github.com/user-attachments/assets/f607ed82-a1c1-4b98-8f93-a8c41dc9548c" />

  <em>Gambar 16. Flowchart Menu User: Top Up Saldo</em>
</p>

1. Menampilkan saldo saat ini dan lima pilihan: Rp50.000, Rp100.000, Rp200.000, Rp500.000, serta *Nominal lain*.
2. Jika pilihan **1 sampai 4**, nominal diambil dari `PAKET_TOPUP`. Jika pilihan **5**, member memasukkan nominal sendiri. Pilihan lain → *"Pilihan tidak valid!"*.
3. Nominal diperiksa: jika **kurang dari `MIN_TOPUP` (Rp10.000) atau lebih dari `MAX_TOPUP` (Rp5.000.000)** → *"Nominal top up harus Rp10.000 - Rp5.000.000!"*.
4. Jika valid, saldo ditambah, `users.json` disimpan, dan tampil *"Top up berhasil! Saldo sekarang: ..."*.

#### d. Riwayat Reservasi (pilihan 4)

<p align="center">
<img width="197" height="244" alt="image" src="https://github.com/user-attachments/assets/cea6a4b8-74e4-44c3-be90-c155def06dc4" />

  <em>Gambar 17. Flowchart Menu User: Riwayat Reservasi</em>
</p>

Program menyaring reservasi yang `username`-nya sama dengan member yang login (`milik`), lalu menampilkannya dengan `tampil_reservasi(milik)`. Semua status (Aktif dan Dibatalkan) ikut ditampilkan.

#### e. Batalkan Reservasi (pilihan 5)

<p align="center">
<img width="215" height="415" alt="image" src="https://github.com/user-attachments/assets/60eeb526-22d3-4251-a13e-02ed6dc7526e" />

  <em>Gambar 18. Flowchart Menu User: Batalkan Reservasi</em>
</p>

1. Program menyaring reservasi milik member yang berstatus `Aktif` (`aktif`). Jika kosong → *"Tidak ada reservasi aktif."*.
2. Jika ada, tabel reservasi aktif ditampilkan dan member memasukkan **nomor invoice** (diubah ke huruf besar). Jika tidak cocok dengan reservasi aktif mana pun → *"Invoice tidak ditemukan!"*.
3. Jika cocok:
   - status reservasi diubah menjadi `Dibatalkan`,
   - saldo member ditambah sebesar harga reservasi (**refund**),
   - kelas dicari lewat `cari_kelas()`; **jika kelas masih ada**, kuotanya ditambah 1,
   - `users.json`, `kelas.json`, dan `reservasi.json` disimpan, lalu tampil *"Reservasi dibatalkan. Refund ... dikembalikan ke saldo."*.

#### f. Logout dan pilihan tidak valid

<p align="center">
<img width="393" height="234" alt="image" src="https://github.com/user-attachments/assets/fbc8fa83-88d4-4cbc-a960-92b98543e5a2" />

  <em>Gambar 19. Flowchart Menu User: logout dan pilihan tidak valid</em>
</p>

- Pilihan `'0'`: tampil *"Logout berhasil."*, perulangan dihentikan (`break`), dan alur kembali ke menu utama melalui konektor **C**.
- Pilihan lain: tampil *"Menu tidak valid!"*, `jeda()`, lalu kembali ke menu member.

---
# 3,1 Menu Awal dan Login

1. Tampilan menu utama
<img width="376" height="161" alt="image" src="https://github.com/user-attachments/assets/240768eb-c8bf-451e-abbe-2406a1fb05a3" />

Menu utama menampilkan judul SISTEM RESERVASI GYM & FITNESS dengan tiga pilihan: Login, Registrasi, dan Keluar

2. Tampilan menu login
<img width="542" height="195" alt="image" src="https://github.com/user-attachments/assets/d2446505-3d9c-4a96-aa4f-98aadd87133a" />

Tampilan menu login salah memasukan user 3 kali

3. Setelah 3 kali salah, pengguna akan di arahkan ke menu utama
<img width="562" height="303" alt="image" src="https://github.com/user-attachments/assets/eb2b91fc-cdf8-4293-9f44-201339010104" />

# 3.2 Menu Admin 
1. Tampilan Menu admin 
<img width="486" height="217" alt="image" src="https://github.com/user-attachments/assets/5b1929f5-fbb3-421d-b278-943b2d20b43b" />

2. Submenu untuk mengelola reservasi GYM/Fitness
<img width="756" height="457" alt="image" src="https://github.com/user-attachments/assets/e17ee8ce-9c88-49ee-88be-8388e67a4109" />

3. Menu tambah kelas
Admin mengisi nama kelas, instruktur, jadwal, harga, dan sisa kuota 
<img width="591" height="421" alt="Screenshot 2026-11-03 223232" src="https://github.com/user-attachments/assets/06d3c68e-d6b1-4399-a35b-012667507e35" />

4. Menu ubah kelas 
Admin memilih ID kelas lalu mengisi data yang baru
<img width="721" height="708" alt="Screenshot 2026-11-03 223459" src="https://github.com/user-attachments/assets/141063b8-8e67-48aa-a2c7-14c16211e509" />

5. Menu hapus kelas 
Sebelum dihapus, program akan meminta konfirmasi (y/n)
<img width="936" height="601" alt="Screenshot 2026-11-03 230610" src="https://github.com/user-attachments/assets/54bb3ab0-6042-4a51-b0ce-de19beeed98e" />

6. Daftar akun
<img width="497" height="187" alt="image" src="https://github.com/user-attachments/assets/06350974-a904-46a9-bb4c-eb6fe5742150" />

# 3.3 Menu User
1. Tampilan menu user
<img width="355" height="202" alt="image" src="https://github.com/user-attachments/assets/e3edbff0-a88e-40ad-b3f3-bdbce2285c84" />

2. Reservasi kelas
<img width="791" height="352" alt="image" src="https://github.com/user-attachments/assets/1f6007bd-8dfc-43f3-807a-78e8ced98291" />

3. Tampilan apabila dari user tersebut tidak memiliki saldo yang cukup 
<img width="741" height="592" alt="Screenshot 2026-11-03 223112" src="https://github.com/user-attachments/assets/6fc5e049-ee8b-49b5-bc02-bf46133de08c" />

4. Tampilan Top up saldo 
<img width="487" height="277" alt="image" src="https://github.com/user-attachments/assets/604d769f-8499-4ddd-9361-777f8f5607e9" />

5. Tampilan setelah berhasil reservasi kelas 
Invoice dicetak beserta kode transaksi serta sisa saldo
<img width="792" height="801" alt="image" src="https://github.com/user-attachments/assets/4e823982-75aa-4237-8392-2319520c0505" />

6. Tampilan Riwayat reservasi kelas 
<img width="1012" height="416" alt="image" src="https://github.com/user-attachments/assets/8ad4e066-a6a5-46f7-a7ec-eb86c9c76613" />


# 3.4 Keluar
Program akan keluar
<img width="667" height="273" alt="Screenshot 2026-11-03 231059" src="https://github.com/user-attachments/assets/d715b73b-d9db-4afb-bfce-043911569bb3" />
