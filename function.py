def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("")
        print("Daftar kontak: ")
        print(f"Nama: {kontak['nama']}")
        print(f"No Telepon: {kontak['telepon']}")
        print("")

def new_kontak():
    nama = input("Nama: ")
    telepon = input("Telepon: ")
    print("Kontak berhasil ditambahkan")
    print("")
    kontak = {
        "nama" : nama,
        "telepon" : telepon
    }
    return kontak