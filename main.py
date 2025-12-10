"""
Program Utama Toko Buku
Mengintegrasikan modul inventaris, kasir, dan utils
"""
import inventaris
import kasir
import utils

def tampilkan_katalog():
    print(utils.buat_garis(50))
    print("KATALOG BUKU GRAMEDIA KW")
    print(utils.buat_garis(50))
    print(f"{'ID':<5} {'Judul Buku':<25} {'Harga':<12} {'Stok'}")
    print("-" * 50)
    
    for buku in inventaris.lihat_semua_buku():
        harga_fmt = utils.format_rupiah(buku['harga'])
        print(f"{buku['id']:<5} {buku['judul']:<25} {harga_fmt:<12} {buku['stok']}")

def proses_transaksi():
    tampilkan_katalog()
    print("\n" + utils.buat_garis(30, "-"))
    
    try:
        kode = int(input("Masukkan ID Buku: "))
        qty = int(input("Jumlah beli   : "))
        
        # 1. Cek ketersediaan barang (Pakai modul inventaris)
        buku = inventaris.cari_buku_by_id(kode)
        
        if not buku:
            print("Error: Buku tidak ditemukan!")
            return

        if not inventaris.kurangi_stok(kode, qty):
            print(f"Error: Stok tidak cukup! Sisa stok: {buku['stok']}")
            return

        # 2. Lakukan perhitungan (Pakai modul kasir)
        subtotal = kasir.hitung_subtotal(buku['harga'], qty)
        potongan = kasir.hitung_diskon(subtotal)
        total_bayar = kasir.hitung_total_akhir(subtotal, potongan)
        
        # 3. Cetak Struk (Pakai modul utils untuk format)
        print("\n" + utils.buat_garis(40))
        print(f"STRUK BELANJA - {utils.ambil_tanggal_hari_ini()}")
        print(utils.buat_garis(40))
        print(f"Item      : {buku['judul']}")
        print(f"Harga     : {utils.format_rupiah(buku['harga'])}")
        print(f"Jumlah    : {qty}")
        print("-" * 40)
        print(f"Subtotal  : {utils.format_rupiah(subtotal)}")
        print(f"Diskon    : {utils.format_rupiah(potongan)}")
        print(f"TOTAL     : {utils.format_rupiah(total_bayar)}")
        print(utils.buat_garis(40))
        print("Terima kasih telah berbelanja!")
        
    except ValueError:
        print("Input error: Harap masukkan angka.")

if __name__ == "__main__":
    while True:
        print("\nMENU UTAMA")
        print("1. Lihat Katalog")
        print("2. Beli Buku")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == "1":
            tampilkan_katalog()
        elif pilihan == "2":
            proses_transaksi()
        elif pilihan == "3":
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")