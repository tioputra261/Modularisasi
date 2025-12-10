"""
Modul Inventaris
Mengelola data buku dan stok
"""

# Database buku (Dictionary dalam List)
data_buku = [
    {"id": 101, "judul": "Belajar Python Dasar", "harga": 85000, "stok": 10},
    {"id": 102, "judul": "Algoritma & Struktur Data", "harga": 120000, "stok": 5},
    {"id": 103, "judul": "Kecerdasan Buatan", "harga": 150000, "stok": 3},
    {"id": 104, "judul": "Novel Laskar Pelangi", "harga": 95000, "stok": 8}
]

def lihat_semua_buku():
    """Mengembalikan list semua buku"""
    return data_buku

def cari_buku_by_id(kode_buku):
    """
    Mencari buku berdasarkan ID
    Returns: Dictionary buku atau None jika tidak ketemu
    """
    for buku in data_buku:
        if buku["id"] == kode_buku:
            return buku
    return None

def kurangi_stok(kode_buku, jumlah):
    """
    Mengurangi stok buku setelah pembelian
    Returns: True jika berhasil, False jika stok kurang
    """
    buku = cari_buku_by_id(kode_buku)
    if buku and buku["stok"] >= jumlah:
        buku["stok"] -= jumlah
        return True
    return False