from service.svc_stok import SvcStok
from api.menu_utama import input_int


class ApiStok:
    """Antarmuka CLI untuk mengelola Stok Barang."""

    def __init__(self, svc: SvcStok):
        self._svc = svc

    def menu(self):
        while True:
            print("\n--- KELOLA STOK BARANG ---")
            print("1. Tambah Stok (Barang Masuk)")
            print("2. Kurangi Stok (Barang Keluar)")
            print("3. Lihat Stok per Barang")
            print("4. Lihat Semua Stok")
            print("0. Kembali")
            pilihan = input_int("Pilih [0-4]: ")

            if pilihan == 0:
                break
            elif pilihan == 1:
                self._tambah_stok()
            elif pilihan == 2:
                self._kurangi_stok()
            elif pilihan == 3:
                self._lihat_stok()
            elif pilihan == 4:
                self._semua_stok()
            else:
                print("Pilihan tidak valid!")

    def _tambah_stok(self):
        try:
            idbarang = input_int("ID Barang: ")
            jumlah = input_int("Jumlah tambah: ")
            hasil = self._svc.tambah_stok(idbarang, jumlah)
            print(f"Stok berhasil ditambahkan: {hasil.nama_barang} -> {hasil.jumlah}")
            print(f"Terakhir update: {hasil.last_timeupdate}")
        except ValueError as e:
            print(f"Error: {e}")

    def _kurangi_stok(self):
        try:
            idbarang = input_int("ID Barang: ")
            jumlah = input_int("Jumlah kurangi: ")
            hasil = self._svc.kurangi_stok(idbarang, jumlah)
            print(f"Stok berhasil dikurangi: {hasil.nama_barang} -> {hasil.jumlah}")
            print(f"Terakhir update: {hasil.last_timeupdate}")
        except ValueError as e:
            print(f"Error: {e}")

    def _lihat_stok(self):
        try:
            idbarang = input_int("ID Barang: ")
            hasil = self._svc.lihat_stok(idbarang)
            if hasil:
                print(f"\nInformasi Stok:")
                print(f"Barang : {hasil.nama_barang}")
                print(f"Jumlah : {hasil.jumlah}")
                print(f"Update : {hasil.last_timeupdate}")
            else:
                print(f"Stok untuk barang id {idbarang} belum ada.")
        except ValueError as e:
            print(f"Error: {e}")

    def _semua_stok(self):
        daftar = self._svc.semua_stok()
        if not daftar:
            print("Belum ada data stok.")
            return
        print(f"\nDaftar Semua Stok ({len(daftar)} data):")
        print("-" * 60)
        for s in daftar:
            print(f"{s.idbarang}. {s.nama_barang} - Stok: {s.jumlah} (update: {s.last_timeupdate})")
