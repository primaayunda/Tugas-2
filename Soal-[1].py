import function

daftar_kontak = []
daftar_kontak.append({
    "nama" : "Prima",
    "telepon" : "1111111111"
})

# Menu program
while True:
    print("Selamat datang!")
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

    menu = input("Pilih menu: ")

    if menu == "3":
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)
    else:
        print("Menu tidak tersedia")

print("Program selesai, sampai jumpa!")