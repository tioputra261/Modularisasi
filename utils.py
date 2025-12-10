"""
Modul Utility
Berisi fungsi-fungsi untuk formatting tampilan
"""
from datetime import datetime

def format_rupiah(nominal):
    """
    Mengubah angka menjadi format mata uang Rupiah
    """
    return f"Rp {nominal:,.0f}".replace(",", ".")

def ambil_tanggal_hari_ini():
    """
    Mengembalikan tanggal hari ini dalam format string
    """
    return datetime.now().strftime("%d-%m-%Y %H:%M")

def buat_garis(panjang=40, karakter="="):
    """
    Membuat garis pemisah visual
    """
    return karakter * panjang