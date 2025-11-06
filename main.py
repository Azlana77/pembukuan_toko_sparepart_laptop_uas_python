from modules import login, barang, transaksi, laporan

def menu_admin():
    while True:
        print("""
=== MENU ADMIN ===
1. Lihat Barang
2. Tambah Barang
3. Ubah Barang
4. Hapus Barang
5. Transaksi Penjualan
6. Laporan Penjualan
7. Keluar
""")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            barang.tampilkan_barang()
        elif pilih == "2":
            barang.tambah_barang()
        elif pilih == "3":
            barang.ubah_barang()
        elif pilih == "4":
            barang.hapus_barang()
        elif pilih == "5":
            transaksi.transaksi_penjualan()
        elif pilih == "6":
            laporan.laporan_penjualan()
        elif pilih == "7":
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid!")

def main():
    role = login.login()
    if role:
        menu_admin()
    else:
        print("Akses ditolak!")

if __name__ == "__main__":
    main()
