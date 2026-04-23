from service.svc_merek import SvcMerek
from api.menu_utama import input_required, input_int, konfirmasi_hapus


class ApiMerek:
    """Antarmuka CLI untuk mengelola Merek Barang."""

    def __init__(self, svc: SvcMerek):
        self._svc = svc

    def menu(self):
        while True:
            print("\n--- KELOLA MEREK BARANG ---")
            print("1. Tambah Merek")
            print("2. Lihat Semua Merek")
            print("3. Cari Merek by ID")
            print("4. Ubah Merek")
            print("5. Hapus Merek")
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
            nama = input_required("Nama Merek: ")
            hasil = self._svc.tambah(nama)
            print(f"Berhasil ditambahkan: {hasil}")
        except ValueError as e:
            print(f"Error: {e}")

    def _semua(self):
        daftar = self._svc.semua()
        if not daftar:
            print("Belum ada data merek.")
            return
        print(f"\nDaftar Merek ({len(daftar)} data):")
        print("-" * 30)
        for m in daftar:
            print(f"{m.id}. {m.nama}")

    def _cari_by_id(self):
        try:
            id = input_int("ID Merek: ")
            hasil = self._svc.cari_by_id(id)
            if hasil:
                print(f"Ditemukan: {hasil}")
            else:
                print(f"Merek dengan id {id} tidak ditemukan.")
        except ValueError as e:
            print(f"Error: {e}")

    def _ubah(self):
        try:
            id = input_int("ID Merek yang akan diubah: ")
            nama_baru = input_required("Nama baru: ")
            hasil = self._svc.ubah(id, nama_baru)
            print(f"Berhasil diubah: {hasil}")
        except ValueError as e:
            print(f"Error: {e}")

    def _hapus(self):
        try:
            id = input_int("ID Merek yang akan dihapus: ")
            if konfirmasi_hapus(f"merek id={id}"):
                self._svc.hapus(id)
                print("Berhasil dihapus.")
            else:
                print("Dibatalkan.")
        except ValueError as e:
            print(f"Error: {e}")
