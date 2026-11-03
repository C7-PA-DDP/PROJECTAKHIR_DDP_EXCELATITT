# Sistem Reservasi Gym & Fitness

Aplikasi **berbasis terminal (CLI)** yang ditulis dengan **Python** untuk mengelola reservasi kelas di pusat kebugaran: mulai dari registrasi dan login member, top up saldo, pemesanan kelas lengkap dengan invoice, hingga pengelolaan kelas dan pemantauan reservasi oleh admin. Seluruh data disimpan permanen dalam file **JSON**.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue) ![Interface](https://img.shields.io/badge/Interface-CLI-lightgrey) ![Storage](https://img.shields.io/badge/Storage-JSON-orange)

---

## Daftar Isi

1. [Anggota Kelompok](#anggota-kelompok)
2. [Deskripsi Singkat](#deskripsi-singkat)
3. [Fitur Program](#fitur-program)
4. [Teknologi dan Cara Menjalankan](#teknologi-dan-cara-menjalankan)
5. [Struktur Program dan Penyimpanan Data](#struktur-program-dan-penyimpanan-data)
6. [Flowchart dan Penjelasan Alur](#flowchart-dan-penjelasan-alur)
7. [Output Program dan Penjelasan](#output-program-dan-penjelasan)

---

## Anggota Kelompok

| No | Nama | NIM |
|:--:|------|:---:|
| 1 | Alfian Nugraha | 2609116084 |
| 2 | Novitasari Muhammad Nor | 2609116082 |
| 3 | Marexcel Elibino | 2609116087 |
| 4 | Muhammad Ardhika Prasanjayu | 2609116108 |


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
  <a href="images/flowchart/01_main_full.png"><img src="images/flowchart/01_main_full.png" width="860" alt="Flowchart utama (gambaran umum)"></a><br>
  <em>Gambar 1. Flowchart utama (gambaran umum)</em>
</p>

Alur utama mencakup inisialisasi program, menu utama, login, registrasi, dan keluar. Rinciannya dijelaskan per bagian berikut.

#### a. Inisialisasi dan memuat data

<p align="center">
  <a href="images/flowchart/01a_main_inisialisasi_menu.png"><img src="images/flowchart/01a_main_inisialisasi_menu.png" width="820" alt="Flowchart utama: inisialisasi, memuat data, dan menu utama"></a><br>
  <em>Gambar 2. Flowchart utama: inisialisasi, memuat data, dan menu utama</em>
</p>

1. Program **dimulai**, lalu mengimpor library (`os`, `time`, `json`, `hashlib`, `random`, `prettytable`, `pwinput`) dan mendeklarasikan konstanta serta data default.
2. Program **membaca** `users.json`, `kelas.json`, dan `reservasi.json`.
3. Jika terjadi **FileNotFoundError**, program menampilkan *"File belum ada, membuat file baru..."*. Jika terjadi **ValueError** (JSON rusak atau tipe data salah), program menampilkan *"File rusak, memakai data default."*. Pada kedua kasus, data default disimpan ke file lewat `simpan_data()` lalu dipakai.
4. `lengkapi_data_user(users)` dijalankan: password lama yang belum di-hash diubah menjadi hash, akun yang rusak dibuang, akun `admin` dipastikan ada, lalu `users.json` disimpan.
5. Layar dibersihkan dan **menu utama** ditampilkan (1. Login, 2. Registrasi, 0. Keluar). Pilihan pengguna diperiksa berurutan: `'1'` → Login, `'2'` → Registrasi, `'0'` → Keluar, selain itu → *"Menu tidak valid!"*.

#### b. Login

<p align="center">
  <a href="images/flowchart/01b_main_login.png"><img src="images/flowchart/01b_main_login.png" width="820" alt="Flowchart utama: proses login"></a><br>
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
  <a href="images/flowchart/01c_main_registrasi.png"><img src="images/flowchart/01c_main_registrasi.png" width="640" alt="Flowchart utama: proses registrasi"></a><br>
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
  <a href="images/flowchart/01d_main_keluar_invalid.png"><img src="images/flowchart/01d_main_keluar_invalid.png" width="860" alt="Flowchart utama: keluar program dan pilihan tidak valid"></a><br>
  <em>Gambar 5. Flowchart utama: keluar program dan pilihan tidak valid</em>
</p>

- Pilihan `'0'`: tampil *"Terima kasih telah menggunakan sistem ini!"*, perulangan dihentikan dengan `break`, dan program **selesai**.
- Pilihan lain: tampil *"Menu tidak valid!"*, `jeda()`, lalu kembali ke menu utama.

---

### Halaman 2: Menu Admin

<p align="center">
  <a href="images/flowchart/02_admin_full.png"><img src="images/flowchart/02_admin_full.png" width="860" alt="Flowchart Menu Admin (gambaran umum)"></a><br>
  <em>Gambar 6. Flowchart Menu Admin (gambaran umum)</em>
</p>

Menu admin berjalan dalam perulangan `while True` sampai admin memilih **0. Logout**. Setiap fitur (kecuali logout) diakhiri `jeda()` lalu kembali ke awal menu.

#### a. Menu dan Lihat Kelas (pilihan 1)

<p align="center">
  <a href="images/flowchart/02a_admin_menu_lihat_kelas.png"><img src="images/flowchart/02a_admin_menu_lihat_kelas.png" width="560" alt="Flowchart Menu Admin: tampilan menu dan Lihat Kelas"></a><br>
  <em>Gambar 7. Flowchart Menu Admin: tampilan menu dan Lihat Kelas</em>
</p>

Dari konektor **A**, layar dibersihkan dan menu admin ditampilkan (enam pilihan + logout), lalu pilihan dibaca. Pilihan `'1'` memanggil `tampil_kelas(daftar_kelas)` untuk menampilkan tabel semua kelas.

#### b. Tambah Kelas (pilihan 2)

<p align="center">
  <a href="images/flowchart/02b_admin_tambah_kelas.png"><img src="images/flowchart/02b_admin_tambah_kelas.png" width="430" alt="Flowchart Menu Admin: Tambah Kelas"></a><br>
  <em>Gambar 8. Flowchart Menu Admin: Tambah Kelas</em>
</p>

1. ID baru dibuat oleh `buat_id_baru()` (ID terbesar + 1, atau 1 jika belum ada kelas).
2. Admin mengisi nama kelas, instruktur, jadwal (tidak boleh kosong), serta harga dan kuota (bilangan bulat minimal 1).
3. Data kelas baru ditambahkan dan disimpan ke `kelas.json`, lalu tampil *"Kelas berhasil ditambahkan!"*.

#### c. Ubah Kelas (pilihan 3)

<p align="center">
  <a href="images/flowchart/02c_admin_ubah_kelas.png"><img src="images/flowchart/02c_admin_ubah_kelas.png" width="640" alt="Flowchart Menu Admin: Ubah Kelas"></a><br>
  <em>Gambar 9. Flowchart Menu Admin: Ubah Kelas</em>
</p>

1. Tabel kelas ditampilkan, lalu admin memasukkan **ID kelas**. `cari_kelas()` mencari kelas tersebut. Jika tidak ditemukan → *"Kelas tidak ditemukan!"*.
2. Jika ditemukan, admin diminta mengisi nama, instruktur, dan jadwal baru. **Mengosongkan input berarti data tidak diubah.**
3. Untuk harga dan kuota, setiap input yang diisi divalidasi: harus **angka bulat** (jika bukan → *"... harus angka, tidak diubah."*) dan memenuhi **nilai minimum** (harga minimal 1, kuota minimal 0; jika tidak → *"... tidak diubah (minimal ...)."*). Nilai yang tidak valid dilewati tanpa membatalkan perubahan lainnya.
4. Perubahan disimpan ke `kelas.json` dan tampil *"Kelas berhasil diperbarui!"*.

#### d. Hapus Kelas (pilihan 4)

<p align="center">
  <a href="images/flowchart/02d_admin_hapus_kelas.png"><img src="images/flowchart/02d_admin_hapus_kelas.png" width="640" alt="Flowchart Menu Admin: Hapus Kelas"></a><br>
  <em>Gambar 10. Flowchart Menu Admin: Hapus Kelas</em>
</p>

1. Tabel kelas ditampilkan dan admin memasukkan **ID kelas**. Jika tidak ditemukan → *"Kelas tidak ditemukan!"*.
2. Program memeriksa `jumlah_reservasi_aktif(reservasi, id) > 0`. Jika kelas **masih memiliki reservasi aktif** → *"Kelas masih memiliki reservasi aktif, tidak bisa dihapus!"* dan proses dihentikan.
3. Jika tidak ada reservasi aktif, admin diminta konfirmasi *"Yakin hapus ...? (y/n)"*. Jawaban selain `y` → *"Penghapusan dibatalkan."*. Jawaban `y` → kelas dihapus, `kelas.json` disimpan, dan tampil *"Kelas berhasil dihapus!"*.

#### e. Lihat Semua Reservasi dan Lihat Daftar Member (pilihan 5 dan 6)

<p align="center">
  <a href="images/flowchart/02e_admin_lihat_reservasi_member.png"><img src="images/flowchart/02e_admin_lihat_reservasi_member.png" width="860" alt="Flowchart Menu Admin: Lihat Semua Reservasi dan Lihat Daftar Member"></a><br>
  <em>Gambar 11. Flowchart Menu Admin: Lihat Semua Reservasi dan Lihat Daftar Member</em>
</p>

- Pilihan `'5'` memanggil `tampil_reservasi(reservasi)` untuk menampilkan semua reservasi dari seluruh member.
- Pilihan `'6'` memanggil `tampil_users(users)` untuk menampilkan username, role, saldo, dan waktu terdaftar.

#### f. Logout dan pilihan tidak valid

<p align="center">
  <a href="images/flowchart/02f_admin_logout_invalid.png"><img src="images/flowchart/02f_admin_logout_invalid.png" width="860" alt="Flowchart Menu Admin: logout dan pilihan tidak valid"></a><br>
  <em>Gambar 12. Flowchart Menu Admin: logout dan pilihan tidak valid</em>
</p>

- Pilihan `'0'`: tampil *"Logout berhasil."*, perulangan dihentikan (`break`), dan alur kembali ke menu utama melalui konektor **C**.
- Pilihan lain: tampil *"Menu tidak valid!"*, `jeda()`, lalu kembali ke menu admin.

---

### Halaman 3: Menu User (Member)

<p align="center">
  <a href="images/flowchart/03_user_full.png"><img src="images/flowchart/03_user_full.png" width="860" alt="Flowchart Menu User (gambaran umum)"></a><br>
  <em>Gambar 13. Flowchart Menu User (gambaran umum)</em>
</p>

Menu member juga berjalan dalam perulangan `while True` sampai member memilih **0. Logout**. Selain daftar menu, **saldo member** ditampilkan di bagian atas setiap kali menu muncul.

#### a. Menu dan Lihat Kelas (pilihan 1)

<p align="center">
  <a href="images/flowchart/03a_user_menu_lihat_kelas.png"><img src="images/flowchart/03a_user_menu_lihat_kelas.png" width="480" alt="Flowchart Menu User: tampilan menu dan Lihat Kelas"></a><br>
  <em>Gambar 14. Flowchart Menu User: tampilan menu dan Lihat Kelas</em>
</p>

Dari konektor **B**, layar dibersihkan, menu member ditampilkan beserta saldo, lalu pilihan dibaca. Pilihan `'1'` memanggil `tampil_kelas(daftar_kelas)`.

#### b. Reservasi Kelas (pilihan 2)

<p align="center">
  <a href="images/flowchart/03b_user_reservasi_kelas.png"><img src="images/flowchart/03b_user_reservasi_kelas.png" width="640" alt="Flowchart Menu User: Reservasi Kelas"></a><br>
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
  <a href="images/flowchart/03c_user_top_up.png"><img src="images/flowchart/03c_user_top_up.png" width="860" alt="Flowchart Menu User: Top Up Saldo"></a><br>
  <em>Gambar 16. Flowchart Menu User: Top Up Saldo</em>
</p>

1. Menampilkan saldo saat ini dan lima pilihan: Rp50.000, Rp100.000, Rp200.000, Rp500.000, serta *Nominal lain*.
2. Jika pilihan **1 sampai 4**, nominal diambil dari `PAKET_TOPUP`. Jika pilihan **5**, member memasukkan nominal sendiri. Pilihan lain → *"Pilihan tidak valid!"*.
3. Nominal diperiksa: jika **kurang dari `MIN_TOPUP` (Rp10.000) atau lebih dari `MAX_TOPUP` (Rp5.000.000)** → *"Nominal top up harus Rp10.000 - Rp5.000.000!"*.
4. Jika valid, saldo ditambah, `users.json` disimpan, dan tampil *"Top up berhasil! Saldo sekarang: ..."*.

#### d. Riwayat Reservasi (pilihan 4)

<p align="center">
  <a href="images/flowchart/03d_user_riwayat.png"><img src="images/flowchart/03d_user_riwayat.png" width="400" alt="Flowchart Menu User: Riwayat Reservasi"></a><br>
  <em>Gambar 17. Flowchart Menu User: Riwayat Reservasi</em>
</p>

Program menyaring reservasi yang `username`-nya sama dengan member yang login (`milik`), lalu menampilkannya dengan `tampil_reservasi(milik)`. Semua status (Aktif dan Dibatalkan) ikut ditampilkan.

#### e. Batalkan Reservasi (pilihan 5)

<p align="center">
  <a href="images/flowchart/03e_user_batalkan_reservasi.png"><img src="images/flowchart/03e_user_batalkan_reservasi.png" width="640" alt="Flowchart Menu User: Batalkan Reservasi"></a><br>
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
  <a href="images/flowchart/03f_user_logout_invalid.png"><img src="images/flowchart/03f_user_logout_invalid.png" width="640" alt="Flowchart Menu User: logout dan pilihan tidak valid"></a><br>
  <em>Gambar 19. Flowchart Menu User: logout dan pilihan tidak valid</em>
</p>

- Pilihan `'0'`: tampil *"Logout berhasil."*, perulangan dihentikan (`break`), dan alur kembali ke menu utama melalui konektor **C**.
- Pilihan lain: tampil *"Menu tidak valid!"*, `jeda()`, lalu kembali ke menu member.

---

## Output Program dan Penjelasan

Screenshot berikut diambil dari satu rangkaian pengujian berurutan: registrasi member `budi` → login → top up → reservasi → pembatalan → login sebagai admin untuk mengelola kelas dan memantau data. Karena itu angka saldo, kuota, dan status pada tiap gambar saling berkesinambungan.

### Menu Utama, Registrasi, dan Login

<p align="center">
  <a href="images/output/01_menu_utama.png"><img src="images/output/01_menu_utama.png" width="596" alt="Tampilan menu utama"></a><br>
  <em>Gambar 20. Tampilan menu utama</em>
</p>

Menu utama menampilkan judul **SISTEM RESERVASI GYM & FITNESS** dengan tiga pilihan: Login, Registrasi, dan Keluar.

<p align="center">
  <a href="images/output/02_registrasi_berhasil.png"><img src="images/output/02_registrasi_berhasil.png" width="596" alt="Registrasi member berhasil"></a><br>
  <em>Gambar 21. Registrasi member berhasil</em>
</p>

Member baru memilih menu **2**, mengisi username `budi` dan password (tampil sebagai `*`). Akun disimpan di `users.json` dengan `role = user`, `saldo = 0`, dan password dalam bentuk hash.

<p align="center">
  <a href="images/output/03_registrasi_username_spasi.png"><img src="images/output/03_registrasi_username_spasi.png" width="596" alt="Registrasi ditolak: username mengandung spasi"></a><br>
  <em>Gambar 22. Registrasi ditolak: username mengandung spasi</em>
</p>

<p align="center">
  <a href="images/output/04_registrasi_username_dipakai.png"><img src="images/output/04_registrasi_username_dipakai.png" width="596" alt="Registrasi ditolak: username sudah dipakai"></a><br>
  <em>Gambar 23. Registrasi ditolak: username sudah dipakai</em>
</p>

<p align="center">
  <a href="images/output/05_registrasi_password_pendek.png"><img src="images/output/05_registrasi_password_pendek.png" width="596" alt="Registrasi ditolak: password kurang dari 4 karakter"></a><br>
  <em>Gambar 24. Registrasi ditolak: password kurang dari 4 karakter</em>
</p>

Tiga validasi registrasi: username dengan spasi (`budi santoso`) ditolak, username yang sudah ada (`admin`) ditolak, dan password yang kurang dari 4 karakter ditolak. Pada ketiga kasus tidak ada akun yang dibuat.

<p align="center">
  <a href="images/output/06_login_gagal_3x.png"><img src="images/output/06_login_gagal_3x.png" width="596" alt="Login gagal tiga kali berturut-turut"></a><br>
  <em>Gambar 25. Login gagal tiga kali berturut-turut</em>
</p>

Setiap kesalahan username/password menampilkan sisa percobaan (2, 1, lalu 0). Setelah 3 kali gagal, tampil *"Login gagal 3 kali."* dan program kembali ke menu utama.

<p align="center">
  <a href="images/output/07_login_berhasil.png"><img src="images/output/07_login_berhasil.png" width="596" alt="Login berhasil"></a><br>
  <em>Gambar 26. Login berhasil</em>
</p>

Login yang benar menampilkan pesan sambutan. Program kemudian membersihkan layar dan langsung membuka menu sesuai `role` (Member atau Admin).

### Menu Member

<p align="center">
  <a href="images/output/08_menu_member.png"><img src="images/output/08_menu_member.png" width="596" alt="Tampilan menu member"></a><br>
  <em>Gambar 27. Tampilan menu member</em>
</p>

Menu member menampilkan **saldo saat ini** di bagian atas, diikuti lima fitur dan opsi logout.

<p align="center">
  <a href="images/output/09_member_lihat_kelas.png"><img src="images/output/09_member_lihat_kelas.png" width="727" alt="Member: Lihat Kelas"></a><br>
  <em>Gambar 28. Member: Lihat Kelas</em>
</p>

Daftar kelas ditampilkan dalam tabel lengkap dengan harga (format rupiah) dan sisa kuota.

<p align="center">
  <a href="images/output/10_member_topup_berhasil.png"><img src="images/output/10_member_topup_berhasil.png" width="596" alt="Member: top up berhasil"></a><br>
  <em>Gambar 29. Member: top up berhasil</em>
</p>

Member memilih paket **2 (Rp100.000)**. Saldo bertambah dari Rp0 menjadi Rp100.000 dan tersimpan di `users.json`.

<p align="center">
  <a href="images/output/11_member_topup_ditolak.png"><img src="images/output/11_member_topup_ditolak.png" width="596" alt="Member: top up ditolak (di bawah batas minimal)"></a><br>
  <em>Gambar 30. Member: top up ditolak (di bawah batas minimal)</em>
</p>

Pada pilihan **Nominal lain**, nominal Rp5.000 ditolak karena batas top up adalah Rp10.000 sampai Rp5.000.000. Saldo tidak berubah.

<p align="center">
  <a href="images/output/12_member_saldo_tidak_cukup.png"><img src="images/output/12_member_saldo_tidak_cukup.png" width="727" alt="Member: reservasi gagal karena saldo tidak cukup"></a><br>
  <em>Gambar 31. Member: reservasi gagal karena saldo tidak cukup</em>
</p>

Sebelum top up, member mencoba memesan Zumba (Rp50.000) dengan saldo Rp0, sehingga muncul *"Saldo tidak cukup! Harga Rp50.000, saldo Rp0."*.

<p align="center">
  <a href="images/output/13_member_reservasi_invoice.png"><img src="images/output/13_member_reservasi_invoice.png" width="727" alt="Member: reservasi berhasil dan invoice dicetak"></a><br>
  <em>Gambar 32. Member: reservasi berhasil dan invoice dicetak</em>
</p>

Setelah saldo mencukupi, reservasi **Zumba** berhasil. Saldo berkurang dari Rp100.000 menjadi Rp50.000, kuota Zumba berkurang dari 15 menjadi 14, dan **invoice** dicetak berisi nomor invoice, tanggal, member, kelas, jadwal, total bayar, dan sisa saldo.

<p align="center">
  <a href="images/output/14_member_sudah_reservasi.png"><img src="images/output/14_member_sudah_reservasi.png" width="727" alt="Member: reservasi ditolak karena sudah memesan kelas yang sama"></a><br>
  <em>Gambar 33. Member: reservasi ditolak karena sudah memesan kelas yang sama</em>
</p>

Mencoba memesan Zumba untuk kedua kalinya ditolak dengan pesan *"Anda sudah mereservasi kelas ini!"*. Tampak pula sisa kuota Zumba sudah menjadi 14.

<p align="center">
  <a href="images/output/15_member_kuota_penuh.png"><img src="images/output/15_member_kuota_penuh.png" width="727" alt="Member: reservasi ditolak karena kuota penuh"></a><br>
  <em>Gambar 34. Member: reservasi ditolak karena kuota penuh</em>
</p>

Kelas **Pilates** yang kuotanya telah diubah admin menjadi 0 (lihat Gambar 42) tidak dapat dipesan dan menampilkan *"Maaf, kuota kelas sudah penuh!"*.

<p align="center">
  <a href="images/output/16_member_riwayat.png"><img src="images/output/16_member_riwayat.png" width="860" alt="Member: Riwayat Reservasi"></a><br>
  <em>Gambar 35. Member: Riwayat Reservasi</em>
</p>

Riwayat menampilkan semua reservasi milik member, yaitu Zumba dan Body Pump, keduanya berstatus **Aktif** pada saat itu.

<p align="center">
  <a href="images/output/17_member_batal_reservasi.png"><img src="images/output/17_member_batal_reservasi.png" width="860" alt="Member: pembatalan reservasi dan refund"></a><br>
  <em>Gambar 36. Member: pembatalan reservasi dan refund</em>
</p>

Member memasukkan nomor invoice reservasi Zumba. Status berubah menjadi *Dibatalkan*, harga Rp50.000 dikembalikan ke saldo (dari Rp10.000 menjadi Rp60.000), dan kuota Zumba bertambah kembali menjadi 15.

<p align="center">
  <a href="images/output/18_member_invoice_tidak_ditemukan.png"><img src="images/output/18_member_invoice_tidak_ditemukan.png" width="860" alt="Member: nomor invoice tidak ditemukan"></a><br>
  <em>Gambar 37. Member: nomor invoice tidak ditemukan</em>
</p>

Nomor invoice yang tidak terdaftar pada reservasi aktif ditolak dengan pesan *"Invoice tidak ditemukan!"*.

<p align="center">
  <a href="images/output/19_member_logout.png"><img src="images/output/19_member_logout.png" width="596" alt="Member: logout"></a><br>
  <em>Gambar 38. Member: logout</em>
</p>

Pilihan **0** menampilkan *"Logout berhasil."* dan membawa pengguna kembali ke menu utama.

### Menu Admin

<p align="center">
  <a href="images/output/20_menu_admin.png"><img src="images/output/20_menu_admin.png" width="596" alt="Tampilan menu admin"></a><br>
  <em>Gambar 39. Tampilan menu admin</em>
</p>

Admin masuk dengan akun bawaan `admin` / `admin123`. Menu admin berisi enam fitur pengelolaan dan opsi logout.

<p align="center">
  <a href="images/output/21_admin_lihat_kelas.png"><img src="images/output/21_admin_lihat_kelas.png" width="727" alt="Admin: Lihat Kelas"></a><br>
  <em>Gambar 40. Admin: Lihat Kelas</em>
</p>

Tabel kelas mencerminkan transaksi member sebelumnya: kuota Body Pump menjadi 19 (ada 1 reservasi aktif), sedangkan Zumba kembali 15 karena reservasinya dibatalkan.

<p align="center">
  <a href="images/output/22_admin_tambah_kelas.png"><img src="images/output/22_admin_tambah_kelas.png" width="596" alt="Admin: Tambah Kelas"></a><br>
  <em>Gambar 41. Admin: Tambah Kelas</em>
</p>

Admin menambahkan kelas **Yoga** (instruktur Vita, Sabtu 08:00, Rp45.000, kuota 10). ID dibuat otomatis (menjadi 6) dan data disimpan di `kelas.json`.

<p align="center">
  <a href="images/output/23_admin_ubah_kelas.png"><img src="images/output/23_admin_ubah_kelas.png" width="727" alt="Admin: Ubah Kelas"></a><br>
  <em>Gambar 42. Admin: Ubah Kelas</em>
</p>

Admin mengubah kelas **Pilates (ID 5)**. Nama dan instruktur dikosongkan (tidak diubah), jadwal diubah menjadi *Jumat 15:30*, harga `abc` ditolak karena bukan angka (*"Harga harus angka, tidak diubah."*), dan kuota diubah menjadi 0 (diterima karena minimal kuota adalah 0). Perubahan lain tetap tersimpan.

<p align="center">
  <a href="images/output/24_admin_hapus_ditolak.png"><img src="images/output/24_admin_hapus_ditolak.png" width="727" alt="Admin: hapus kelas ditolak karena masih ada reservasi aktif"></a><br>
  <em>Gambar 43. Admin: hapus kelas ditolak karena masih ada reservasi aktif</em>
</p>

Kelas **Body Pump (ID 2)** tidak dapat dihapus karena masih memiliki reservasi aktif.

<p align="center">
  <a href="images/output/25_admin_hapus_berhasil.png"><img src="images/output/25_admin_hapus_berhasil.png" width="727" alt="Admin: hapus kelas berhasil"></a><br>
  <em>Gambar 44. Admin: hapus kelas berhasil</em>
</p>

Kelas **Yoga (ID 6)** tidak memiliki reservasi, sehingga setelah konfirmasi `y` kelas berhasil dihapus.

<p align="center">
  <a href="images/output/26_admin_lihat_reservasi.png"><img src="images/output/26_admin_lihat_reservasi.png" width="860" alt="Admin: Lihat Semua Reservasi"></a><br>
  <em>Gambar 45. Admin: Lihat Semua Reservasi</em>
</p>

Admin melihat seluruh reservasi. Reservasi Zumba berstatus **Dibatalkan** dan Body Pump berstatus **Aktif**, sesuai aktivitas member sebelumnya.

<p align="center">
  <a href="images/output/27_admin_lihat_member.png"><img src="images/output/27_admin_lihat_member.png" width="596" alt="Admin: Lihat Daftar Member"></a><br>
  <em>Gambar 46. Admin: Lihat Daftar Member</em>
</p>

Daftar akun menampilkan username, role, saldo, dan waktu terdaftar. Saldo `budi` (Rp60.000) sama dengan saldo terakhir setelah refund.

### Keluar dari Program

<p align="center">
  <a href="images/output/28_keluar_program.png"><img src="images/output/28_keluar_program.png" width="596" alt="Keluar dari program"></a><br>
  <em>Gambar 47. Keluar dari program</em>
</p>

Pilihan **0** pada menu utama menampilkan pesan penutup dan menghentikan program.

---

> Dokumen ini dibuat sebagai bagian dari tugas kelompok **Sistem Reservasi Gym & Fitness**.
