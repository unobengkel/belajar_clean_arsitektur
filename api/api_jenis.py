from service.svc_jenis import SvcJenis
from api.menu_utama import input_required, input_int, konfirmasi_hapus


class ApiJenis:
    """Antarmuka CLI untuk mengelola Jenis Barang."""

    def __init__(self, svc: SvcJenis):
        self._svc = svc

    def menu(self):
        while True:
            print("\n--- KELOLA JENIS BARANG ---")
            print("1. Tambah Jenis")
            print("2. Lihat Semua Jenis")
            print("3. Cari Jenis by ID")
            print("4. Ubah Jenis")
            print("5. Hapus Jenis")
            print("0. Kembali")
            pilihan = input_int("Pilih [0-5]: ")

            if pilihan == 0:
                break
            elif pilihan == 1:
                self._tambah()
            elif pilihan == 2:
                self._semua()
            elif pilihan == 3:
                self._cari_by_id()
            elif pilihan == 4:
                self._ubah()
            elif pilihan == 5:
                self._hapus()
            else:
                print("Pilihan tidak valid!")

    def _tambah(self):
        try:
            nama = input_required("Nama Jenis: ")
            hasil = self._svc.tambah(nama)
            print(f"Berhasil ditambahkan: {hasil}")
        except ValueError as e:
            print(f"Error: {e}")

    def _semua(self):
        daftar = self._svc.semua()
        if not daftar:
            print("Belum ada data jenis.")
            return
        print(f"\nDaftar Jenis ({len(daftar)} data):")
        print("-" * 30)
        for j in daftar:
            print(f"{j.id}. {j.nama}")

    def _cari_by_id(self):
        try:
            id = input_int("ID Jenis: ")
            hasil = self._svc.cari_by_id(id)
            if hasil:
                print(f"Ditemukan: {hasil}")
            else:
                print(f"Jenis dengan id {id} tidak ditemukan.")
        except ValueError as e:
            print(f"Error: {e}")

    def _ubah(self):
        try:
            id = input_int("ID Jenis yang akan diubah: ")
            nama_baru = input_required("Nama baru: ")
            hasil = self._svc.ubah(id, nama_baru)
            print(f"Berhasil diubah: {hasil}")
        except ValueError as e:
            print(f"Error: {e}")

    def _hapus(self):
        try:
            id = input_int("ID Jenis yang akan dihapus: ")
            if konfirmasi_hapus(f"jenis id={id}"):
                self._svc.hapus(id)
                print("Berhasil dihapus.")
            else:
                print("Dibatalkan.")
        except ValueError as e:
            print(f"Error: {e}")
