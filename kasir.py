"""
Modul Kasir
Berisi logika perhitungan transaksi dan diskon
"""

def hitung_subtotal(harga, jumlah):
    """Menghitung harga sebelum diskon"""
    return harga * jumlah

def cek_kelayakan_diskon(total_belanja):
    """
    Cek apakah pembeli berhak dapat diskon.
    Aturan: Belanja di atas Rp 200.000 dapat diskon
    """
    return total_belanja > 200000

def hitung_diskon(total_belanja):
    """
    Menghitung nominal diskon (10% jika layak)
    """
    if cek_kelayakan_diskon(total_belanja):
        return total_belanja * 0.1  # Diskon 10%
    return 0

def hitung_total_akhir(subtotal, diskon):
    """Menghitung total yang harus dibayar"""
    return subtotal - diskon