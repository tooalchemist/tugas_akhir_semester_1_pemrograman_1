"""Buatlah program untuk sistem peminjaman buku disebuah perpustakaan. 
Program harus dapat mencatat anggota, daftar buku, memproses peminjaman, pengembalian, 
dan memeriksa status buku"""

list_anggota = [
    {
    "id_anggota": 8000,
    "Nama": "Jogi",
    "Kelas": "D4 DS B",
    "NRP": "60"
    },

    {
    "id_anggota": 8001,
    "Nama": "Robi",
    "Kelas": "D4 DS B",
    "NRP": "41"
    },
    
    {
    "id_anggota": 8002,
    "Nama": "Endika",
    "Kelas": "D4 DS B",
    "NRP": "53"
    },
]


list_buku = [
    { "id_buku": 0, "is_booked": False, "title": "Deathbook", "desc": "Semua akan kembali ke asalnya", "kode_buku": "X455", "id_peminjam": "",},
    {"id_buku": 1, "is_booked": True, "title": "Sang pemimpi", "desc": "Tak ada mimpi yang terlalu tinggi", "kode_buku": "X456", "id_peminjam": 8002,},
    {"id_buku": 2, "is_booked": False, "title": "Pulang", "desc": "Tentang tempat kembali", "kode_buku": "X457","id_peminjam": "",},
]

# Sabrina
def registerMember(nama: str, kelas: str, NRP: str):
    for i in list_anggota:
        if i["NRP"] == NRP:
            print("NRP Sudah Terpakai!")
            return False

    len_now = len(list_anggota)
    new = {"id_anggota": len_now + 8000, "Nama": nama, "Kelas": kelas, "NRP": NRP}
    list_anggota.append(new)

    print("Selamat, anda telah terdaftar sebagai anggota")
    return True

# Aulia
def listingAnggota():
    print("\nAnggota Terdaftar : \n")

    for i in list_anggota:
        for key, val in i.items():
            if key != "id_anggota":
                print(f"{key} : {val}")
        print("")

# Dinda
def listingBuku():
    print("All Book")

    for x, i in enumerate(list_buku):
        print(
            f"""
                No. {x+1} Kode Buku. {i["kode_buku"]}
                Judul Buku \t = {i["title"]}
                Deskripsi  \t = {i["desc"]}
            """,
            end="",
        )
        if i["is_booked"] == True:
            print("\tStatus     \t = Booked")
        else:
            print("\tStatus     \t = Available")

# Robi
def tersediaBuku():
    print("Available Book")

    for x, i in enumerate(list_buku):
        if not i["is_booked"]:
            print(
                f"""
                No. {x+1} Kode Buku. {i["kode_buku"]}
                Judul Buku \t = {i["title"]}
                Deskripsi  \t = {i["desc"]}
            """)

# Endika
def prosesPeminjaman(idBuku: int, idAnggota: int):
    flag = 0
    now = 99
    for i in list_anggota:
        if i["NRP"] == idAnggota:
            now = i["id_anggota"]
            flag = 1

    if flag:
        for i in list_buku:
            if i["is_booked"] == False and i["kode_buku"] == idBuku:
                i["id_peminjam"] = now
                i["is_booked"] = True
                print("Peminjaman Berhasil!")
                return True

    print("Peminjaman Gagal!")
    return False

# Joo
def prosesPengembalian(idBuku: int, idAnggota: int):
    flag = 0
    now = -1
    for i in list_anggota:
        if i["NRP"] == idAnggota:
            now = i["id_anggota"]
            flag = 1

    if flag:
        for i in list_buku:
            if (i["is_booked"] == True and i["kode_buku"] == idBuku and i["id_peminjam"] == now):
                i["id_peminjam"] == ""
                i["is_booked"] = False
                print("Pengembalian Berhasil!")
                return True

    else:
        print("Pengembalian Gagal!")
        return False

def menu():
    print("*" * 75)
    print(f"Welcome DI Perpustakaan D3 \n Choose Menu : \n1. List Buku\n2. List Member\n3. Daftar Member Baru\n4. Pinjam Buku\n5. Kembalikan Buku\n0. Exit")
    print("*" * 75)
    x = int(input("Pilih (angka) :"))
    flag = 1

    while flag:
        match x:
            case 0:
                flag = 0
            case 1:
                listingBuku()
                x = 99
            case 2:
                listingAnggota()
                x = 99
            case 3:
                n = str(input("Masukkan Nama : "))
                k = str(input("Masukkan Kelas : "))
                NRP = str(input("Masukkan NRP (WAJIB) : "))
                registerMember(n, k, NRP)
                x = 99
            case 4:
                is_booked = 0
                for i in list_buku:
                    if i["is_booked"] == True:
                        is_booked += 1
                if is_booked != len(list_buku):
                    tersediaBuku()
                    NRP = str(input("Masukkan NRP Peminjam : "))
                    kode = str(input("Masukkan Kode Buku : "))
                    prosesPeminjaman(kode, NRP)
                else:
                    print("Tidak Ada Buku yang Bisa Dipinjam!")
                x = 99
            case 5:
                NRP = str(input("Masukkan NRP Peminjam : "))
                kode = str(input("Masukkan Kode Buku : "))
                prosesPengembalian(kode, NRP)
                x = 99
            case _:
                print("*" * 75)
                print(f"Welcome DI Perpustakaan D3 \n Choose Menu : \n1. List Buku\n2. List Member\n3. Daftar Member Baru\n4. Pinjam Buku\n5. Kembalikan Buku\n0. Exit")
                print("*" * 75)
                x = int(input("Pilih (angka) :"))

def main():
    menu()

main()
