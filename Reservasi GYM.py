import json
import os
import hashlib
import time
import random
from prettytable import PrettyTable
import pwinput

FILE_USERS = "users.json"
FILE_KELAS = "kelas.json"
FILE_RESERVASI = "reservasi.json"

def hash_password(password):
    """Hash password menggunakan SHA-256. Return: string heksadesimal."""
    return hashlib.sha256(password.encode()).hexdigest()

def sudah_hash(text):
    """Cek apakah string sudah di-hash (64 karakter heksadesimal)."""
    return len(text) == 64 and all(c in "0123456789abcdef" for c in text.lower())

PAKET_TOPUP = (50000, 100000, 200000, 500000)
ROLE_VALID = ("admin", "user")
MIN_TOPUP = 10000
MAX_TOPUP = 5000000

DEFAULT_USERS = {
    "admin": {"password": hash_password("admin123"), "role": "admin", "saldo": 0, "terdaftar": "-"},
}
DEFAULT_KELAS = [
    {"id": 1, "nama": "Zumba", "instruktur": "Fina", "jadwal": "Senin 07:00", "harga": 50000, "kuota": 15},
    {"id": 2, "nama": "Body Pump", "instruktur": "Juhdi", "jadwal": "Selasa 17:00", "harga": 40000, "kuota": 20},
    {"id": 3, "nama": "Body Combat", "instruktur": "Alfian", "jadwal": "Rabu 18:30", "harga": 60000, "kuota": 12},
    {"id": 4, "nama": "Spinning", "instruktur": "Excel", "jadwal": "Kamis 06:30", "harga": 55000, "kuota": 10},
    {"id": 5, "nama": "Pilates", "instruktur": "Vita", "jadwal": "Jumat 16:00", "harga": 65000, "kuota": 8},
]


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def jeda():
    input("\nTekan Enter untuk melanjutkan...")

def rupiah(angka):
    return "Rp{:,}".format(angka).replace(",", ".")

def input_teks(pesan):
    """Input teks tidak boleh kosong. Return: string."""
    while True:
        nilai = input(pesan).strip()
        if nilai:
            return nilai
        print("Input tidak boleh kosong!")

def input_angka(pesan, minimum=0):
    """Input bilangan bulat >= minimum. Return: int."""
    while True:
        try:
            nilai = int(input(pesan))
            if nilai < minimum:
                print(f"Nilai minimal {minimum}!")
                continue
            return nilai
        except ValueError:
            print("Input harus berupa angka bulat!")

def input_password(pesan):
    """Input password tersembunyi (pwinput). Return: string."""
    while True:
        pw = pwinput.pwinput(pesan, mask="*").strip()
        if pw:
            return pw
        print("Password tidak boleh kosong!")


def simpan_data(nama_file, data):
    try:
        with open(nama_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except OSError:
        print(f"Gagal menyimpan ke {nama_file}!")

def muat_data(nama_file, default):
    """Muat JSON. Jika file belum ada/rusak, buat dari data default."""
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, type(default)):
                raise ValueError("Tipe data tidak sesuai.")
            return data
    except FileNotFoundError:
        print(f"File {nama_file} belum ada, membuat file baru...")
        simpan_data(nama_file, default)
        return json.loads(json.dumps(default))
    except json.JSONDecodeError:
        print(f"File {nama_file} rusak, memakai data default.")
        simpan_data(nama_file, default)
        return json.loads(json.dumps(default))

def lengkapi_data_user(users):
    """Menambah kolom saldo/terdaftar pada users.json versi lama. Return: users."""
    for nama in list(users):
        data = users[nama]
        if not isinstance(data, dict) or not isinstance(data.get("password"), str):
            del users[nama]
            continue
        if not sudah_hash(data["password"]):
            data["password"] = hash_password(data["password"])
        if data.get("role") not in ROLE_VALID:
            data["role"] = ROLE_VALID[1]
        if not isinstance(data.get("saldo"), int) or data["saldo"] <0:
            data["saldo"] = 0
        data.setdefault("terdaftar", "-")
    if "admin" not in users:
        users["admin"] = dict(DEFAULT_USERS["admin"])
    simpan_data(FILE_USERS, users)
    return users


def tampil_kelas(daftar_kelas):
    if not daftar_kelas:
        print("Belum ada data kelas.")
        return
    tabel = PrettyTable(["ID", "Nama Kelas", "Instruktur", "Jadwal", "Harga", "Sisa Kuota"])
    for k in daftar_kelas:
        tabel.add_row([k["id"], k["nama"], k["instruktur"], k["jadwal"], rupiah(k["harga"]), k["kuota"]])
    print(tabel)

def tampil_reservasi(daftar):
    if not daftar:
        print("Belum ada data reservasi.")
        return
    tabel = PrettyTable(["Invoice", "Member", "Kelas", "Jadwal", "Harga", "Waktu Pesan", "Status"])
    for r in daftar:
        tabel.add_row([r["invoice"], r["username"], r["nama_kelas"], r["jadwal"],
            rupiah(r["harga"]), r["waktu"], r["status"]])
    print(tabel)

def tampil_users(users):
    tabel = PrettyTable(["Username", "Role", "Saldo", "Terdaftar"])
    for nama, data in users.items():
        tabel.add_row([nama, data["role"], rupiah(data["saldo"]), data["terdaftar"]])
    print(tabel)

def cetak_invoice(r, sisa_saldo):
    print("\n" + "=" * 40)
    print("        INVOICE RESERVASI GYM")
    print("=" * 40)
    print(f"No. Invoice : {r['invoice']}")
    print(f"Tanggal     : {r['waktu']}")
    print(f"Member      : {r['username']}")
    print(f"Kelas       : {r['nama_kelas']}")
    print(f"Jadwal      : {r['jadwal']}")
    print(f"Total Bayar : {rupiah(r['harga'])}")
    print(f"Sisa Saldo  : {rupiah(sisa_saldo)}")
    print("=" * 40)
    print("   Terima kasih, selamat berlatih!")
    print("=" * 40)


def cari_kelas(daftar_kelas, id_kelas):
    """Return: dict kelas atau None."""
    for k in daftar_kelas:
        if k["id"] == id_kelas:
            return k
    return None

def buat_id_baru(daftar_kelas):
    if not daftar_kelas:
        return 1
    return max(k["id"] for k in daftar_kelas) + 1

def buat_no_invoice(reservasi):
    sudah_ada = {r["invoice"] for r in reservasi}
    while True:
        nomor = "INV-" + time.strftime("%y%m%d") + "-" + str(random.randint(1000, 9999))
        if nomor not in sudah_ada:
            return nomor

def jumlah_reservasi_aktif(reservasi, id_kelas):
    total = 0
    for r in reservasi:
        if r["id_kelas"] == id_kelas and r["status"] == "Aktif":
            total += 1
    return total

def sudah_reservasi(reservasi, username, id_kelas):
    for r in reservasi:
        if r["username"] == username and r["id_kelas"] == id_kelas and r["status"] == "Aktif":
            return True
    return False

def bayar_saldo(users, username, jumlah):
    """Kurangi saldo. Return True jika berhasil, False jika saldo kurang."""
    if users[username]["saldo"] < jumlah:
        return False
    users[username]["saldo"] -= jumlah
    return True


def registrasi(users):
    print("\n=== REGISTRASI MEMBER ===")
    username = input_teks("Username baru : ").lower()
    if " " in username:
        print("Username tidak boleh mengandung spasi!")
        return
    if username in users:
        print("Username sudah dipakai!")
        return
    password = input_password("Password      : ")
    if len(password) < 4:
        print("Password minimal 4 karakter!")
        return
    users[username] = {
        "password": hash_password(password),
        "role": ROLE_VALID[1],
        "saldo": 0,
        "terdaftar": time.strftime("%d-%m-%Y %H:%M"),
    }
    simpan_data(FILE_USERS, users)
    print("Registrasi berhasil! Silakan login.")

def login(users):
    """Return: username jika berhasil, None jika gagal 3x."""
    print("\n=== LOGIN ===")
    for percobaan in range(3):
        username = input_teks("Username : ").lower()
        password = input_password("Password : ")
        if username in users and users[username]["password"] == hash_password(password):
            print(f"Login berhasil! Selamat datang, {username}.")
            return username
        print(f"Username/password salah! (sisa percobaan: {2 - percobaan})")
    print("Login gagal 3 kali.")
    return None


def tambah_kelas(daftar_kelas):
    print("\n--- Tambah Kelas ---")
    kelas_baru = {
        "id": buat_id_baru(daftar_kelas),
        "nama": input_teks("Nama kelas  : "),
        "instruktur": input_teks("Instruktur  : "),
        "jadwal": input_teks("Jadwal      : "),
        "harga": input_angka("Harga       : ", 1),
        "kuota": input_angka("Kuota       : ", 1),
    }
    daftar_kelas.append(kelas_baru)
    simpan_data(FILE_KELAS, daftar_kelas)
    print("Kelas berhasil ditambahkan!")

def ubah_kelas(daftar_kelas):
    print("\n--- Ubah Kelas ---")
    tampil_kelas(daftar_kelas)
    k = cari_kelas(daftar_kelas, input_angka("ID kelas yang diubah: ", 1))
    if k is None:
        print("Kelas tidak ditemukan!")
        return
    print("(Kosongkan jika tidak ingin mengubah)")
    for kolom, label in (("nama", "Nama"), ("instruktur", "Instruktur"), ("jadwal", "Jadwal")):
        baru = input(f"{label} [{k[kolom]}]: ").strip()
        if baru:
            k[kolom] = baru
    for kolom, label, minimum in (("harga", "Harga", 1), ("kuota", "Kuota", 0)):
        baru = input(f"{label} [{k[kolom]}]: ").strip()
        if baru:
            try:
                nilai = int(baru)
                if nilai < minimum:
                    print(f"{label} tidak diubah (minimal {minimum}).")
                else:
                    k[kolom] = nilai
            except ValueError:
                print(f"{label} harus angka, tidak diubah.")
    simpan_data(FILE_KELAS, daftar_kelas)
    print("Kelas berhasil diperbarui!")

def hapus_kelas(daftar_kelas, reservasi):
    print("\n--- Hapus Kelas ---")
    tampil_kelas(daftar_kelas)
    k = cari_kelas(daftar_kelas, input_angka("ID kelas yang dihapus: ", 1))
    if k is None:
        print("Kelas tidak ditemukan!")
        return
    if jumlah_reservasi_aktif(reservasi, k["id"]) > 0:
        print("Kelas masih memiliki reservasi aktif, tidak bisa dihapus!")
        return
    if input(f"Yakin hapus '{k['nama']}'? (y/n): ").lower() == "y":
        daftar_kelas.remove(k)
        simpan_data(FILE_KELAS, daftar_kelas)
        print("Kelas berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")

def menu_admin(username, users, daftar_kelas, reservasi):
    while True:
        bersihkan_layar()
        print(f"=== MENU ADMIN ({username}) ===")
        print("1. Lihat Kelas")
        print("2. Tambah Kelas")
        print("3. Ubah Kelas")
        print("4. Hapus Kelas")
        print("5. Lihat Semua Reservasi")
        print("6. Lihat Daftar Member")
        print("0. Logout")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampil_kelas(daftar_kelas)
        elif pilihan == "2":
            tambah_kelas(daftar_kelas)
        elif pilihan == "3":
            ubah_kelas(daftar_kelas)
        elif pilihan == "4":
            hapus_kelas(daftar_kelas, reservasi)
        elif pilihan == "5":
            tampil_reservasi(reservasi)
        elif pilihan == "6":
            tampil_users(users)
        elif pilihan == "0":
            print("Logout berhasil.")
            break
        else:
            print("Menu tidak valid!")
        jeda()


def top_up(username, users):
    print("\n--- Top Up Saldo ---")
    print(f"Saldo saat ini: {rupiah(users[username]['saldo'])}")
    for i, nominal in enumerate(PAKET_TOPUP, start=1):
        print(f"{i}. {rupiah(nominal)}")
    print(f"{len(PAKET_TOPUP) + 1}. Nominal lain")
    pilih = input_angka("Pilih: ", 1)

    if 1 <= pilih <= len(PAKET_TOPUP):
        jumlah = PAKET_TOPUP[pilih - 1]
    elif pilih == len(PAKET_TOPUP) + 1:
        jumlah = input_angka("Masukkan nominal: ", 1)
    else:
        print("Pilihan tidak valid!")
        return
    if jumlah < MIN_TOPUP or jumlah > MAX_TOPUP:
        print(f"Nominal top up harus {rupiah(MIN_TOPUP)} - {rupiah(MAX_TOPUP)}!")
        return
    users[username]["saldo"] += jumlah
    simpan_data(FILE_USERS, users)
    print(f"Top up berhasil! Saldo sekarang: {rupiah(users[username]['saldo'])}")

def reservasi_kelas(username, users, daftar_kelas, reservasi):
    print("\n--- Reservasi Kelas ---")
    tampil_kelas(daftar_kelas)
    k = cari_kelas(daftar_kelas, input_angka("ID kelas yang dipesan: ", 1))
    if k is None:
        print("Kelas tidak ditemukan!")
        return
    if k["kuota"] <= 0:
        print("Maaf, kuota kelas sudah penuh!")
        return
    if sudah_reservasi(reservasi, username, k["id"]):
        print("Anda sudah mereservasi kelas ini!")
        return
    if not bayar_saldo(users, username, k["harga"]):
        print(f"Saldo tidak cukup! Harga {rupiah(k['harga'])}, saldo {rupiah(users[username]['saldo'])}.")
        return

    k["kuota"] -= 1
    data = {
        "invoice": buat_no_invoice(reservasi),
        "username": username,
        "id_kelas": k["id"],
        "nama_kelas": k["nama"],
        "jadwal": k["jadwal"],
        "harga": k["harga"],
        "waktu": time.strftime("%d-%m-%Y %H:%M"),
        "status": "Aktif",
    }
    reservasi.append(data)
    simpan_data(FILE_USERS, users)
    simpan_data(FILE_KELAS, daftar_kelas)
    simpan_data(FILE_RESERVASI, reservasi)
    print("Reservasi berhasil!")
    cetak_invoice(data, users[username]["saldo"])

def riwayat_user(username, reservasi):
    """Return: list reservasi milik user."""
    milik = [r for r in reservasi if r["username"] == username]
    tampil_reservasi(milik)
    return milik

def batal_reservasi(username, users, daftar_kelas, reservasi):
    print("\n--- Batalkan Reservasi ---")
    aktif = [r for r in reservasi if r["username"] == username and r["status"] == "Aktif"]
    if not aktif:
        print("Tidak ada reservasi aktif.")
        return
    tampil_reservasi(aktif)
    no = input_teks("Masukkan no. invoice: ").upper()
    for r in aktif:
        if r["invoice"] == no:
            r["status"] = "Dibatalkan"
            users[username]["saldo"] += r["harga"]
            k = cari_kelas(daftar_kelas, r["id_kelas"])
            if k is not None:
                k["kuota"] += 1
            simpan_data(FILE_USERS, users)
            simpan_data(FILE_KELAS, daftar_kelas)
            simpan_data(FILE_RESERVASI, reservasi)
            print(f"Reservasi dibatalkan. Refund {rupiah(r['harga'])} dikembalikan ke saldo.")
            return
    print("Invoice tidak ditemukan!")

def menu_user(username, users, daftar_kelas, reservasi):
    while True:
        bersihkan_layar()
        print(f"=== MENU MEMBER ({username}) ===")
        print(f"Saldo: {rupiah(users[username]['saldo'])}")
        print("1. Lihat Kelas")
        print("2. Reservasi Kelas")
        print("3. Top Up Saldo")
        print("4. Riwayat Reservasi")
        print("5. Batalkan Reservasi")
        print("0. Logout")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampil_kelas(daftar_kelas)
        elif pilihan == "2":
            reservasi_kelas(username, users, daftar_kelas, reservasi)
        elif pilihan == "3":
            top_up(username, users)
        elif pilihan == "4":
            riwayat_user(username, reservasi)
        elif pilihan == "5":
            batal_reservasi(username, users, daftar_kelas, reservasi)
        elif pilihan == "0":
            print("Logout berhasil.")
            break
        else:
            print("Menu tidak valid!")
        jeda()


def main():
    users = lengkapi_data_user(muat_data(FILE_USERS, DEFAULT_USERS))
    daftar_kelas = muat_data(FILE_KELAS, DEFAULT_KELAS)
    reservasi = muat_data(FILE_RESERVASI, [])

    while True:
        bersihkan_layar()
        print("=" * 36)
        print("   SISTEM RESERVASI GYM & FITNESS")
        print("=" * 36)
        print("1. Login")
        print("2. Registrasi")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            username = login(users)
            if username is not None:
                if users[username]["role"] == "admin":
                    menu_admin(username, users, daftar_kelas, reservasi)
                else:
                    menu_user(username, users, daftar_kelas, reservasi)
            else:
                jeda()
        elif pilihan == "2":
            registrasi(users)
            jeda()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan sistem ini!")
            break
        else:
            print("Menu tidak valid!")
            jeda()


if __name__ == "__main__":
    while True:
        try:
            main()
            break
        except KeyboardInterrupt:
            print("\nCtrl+C ditekan, kembali ke menu awal...")
            time.sleep(1)