from service.svc_barang import SvcBarang
from api.menu_utama import input_required, input_int, konfirmasi_hapus


class ApiBarang:
    """Antarmuka CLI untuk mengelola Barang."""

    def __init__(self, svc: SvcBarang):
        self._svc = svc

    def menu(self):
        while True:
            print("\n--- KELOLA BARANG ---")
            print("1. Tambah Barang")
            print("2. Lihat Semua Barang")
            print("3. Cari Barang by ID")
            print("4. Cari Barang by Nama")
            print("5. Ubah Barang")
            print("6. Hapus Barang")
            print("0. Kembali")
            pilihan = input_int("Pilih [0-6]: ")

            if pilihan == 0:
                break
            elif pilihan == 1:
                self._tambah()
            elif pilihan == 2:
                self._semua()
            elif pilihan == 3:
                self._cari_by_id()
            elif pilihan == 4:
                self._cari_by_nama()
            elif pilihan == 5:
                self._ubah()
            elif pilihan == 6:
                self._hapus()
            else:
                print("Pilihan tidak valid!")

    def _tambah(self):
        try:
            nama = input_required("Nama Barang: ")
            idjenis = input_int("ID Jenis: ")
            idmerek = input_int("ID Merek: ")
            idsatuan = input_int("ID Satuan: ")
            hasil = self._svc.tambah(idjenis, idmerek, idsatuan, nama)
            print(f"Berhasil ditambahkan: {hasil}")
        except ValueError as e:
            print(f"Error: {e}")

    def _semua(self):
        daftar = self._svc.semua()
        if not daftar:
            print("Belum ada data barang.")
            return
        print(f"\nDaftar Barang ({len(daftar)} data):")
        print("-" * 80)
        for b in daftar:
            print(f"{b.id}. {b.nama}")
            print(f"   Jenis: {b.nama_jenis} | Merek: {b.nama_merek} | Satuan: {b.nama_satuan}")

    def _cari_by_id(self):
        try:
            id = input_int("ID Barang: ")
            hasil = self._svc.cari_by_id(id)
            if hasil:
                print(f"Ditemukan: {hasil}")
                print(f"   Jenis: {hasil.nama_jenis} | Merek: {hasil.nama_merek} | Satuan: {hasil.nama_satuan}")
            else:
                print(f"Barang dengan id {id} tidak ditemukan.")
        except ValueError as e:
            print(f"Error: {e}")

    def _cari_by_nama(self):
        nama = input_required("Cari Nama Barang: ")
        daftar = self._svc.cari_by_nama(nama)
        if not daftar:
            print(f"Tidak ada barang dengan nama '{nama}'.")
            return
        print(f"\nHasil pencarian '{nama}' ({len(daftar)} data):")
        print("-" * 80)
        for b in daftar:
            print(f"{b.id}. {b.nama}")
            print(f"   Jenis: {b.nama_jenis} | Merek: {b.nama_merek} | Satuan: {b.nama_satuan}")

    def _ubah(self):
        try:
            id = input_int("ID Barang yang akan diubah: ")
            nama = input_required("Nama Barang: ")
            idjenis = input_int("ID Jenis: ")
            idmerek = input_int("ID Merek: ")
            idsatuan = input_int("ID Satuan: ")
            hasil = self._svc.ubah(id, idjenis, idmerek, idsatuan, nama)
            print(f"Berhasil diubah: {hasil}")
        except ValueError as e:
            print(f"Error: {e}")

    def _hapus(self):
        try:
            id = input_int("ID Barang yang akan dihapus: ")
            if konfirmasi_hapus(f"barang id={id}"):
                self._svc.hapus(id)
                print("Berhasil dihapus.")
            else:
                print("Dibatalkan.")
        except ValueError as e:
            print(f"Error: {e}")
