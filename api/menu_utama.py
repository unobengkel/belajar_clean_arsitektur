def tampilkan_menu_utama():
    """Menampilkan menu utama aplikasi."""
    print("\n" + "=" * 50)
    print("          APLIKASI MANAJEMEN BARANG & STOK")
    print("=" * 50)
    print("1. Kelola Jenis Barang")
    print("2. Kelola Merek Barang")
    print("3. Kelola Satuan Barang")
    print("4. Kelola Barang")
    print("5. Kelola Stok Barang")
    print("0. Keluar")
    print("=" * 50)


def pilih_menu() -> int:
    """Meminta user memilih menu."""
    try:
        pilihan = int(input("Pilih menu [0-5]: "))
        return pilihan
    except ValueError:
        return -1


def konfirmasi_hapus(label: str) -> bool:
    """Konfirmasi sebelum menghapus data."""
    jawab = input(f"Yakin hapus {label}? [y/N]: ").strip().lower()
    return jawab == "y"


def input_required(pesan: str) -> str:
    """Meminta input yang tidak boleh kosong."""
    while True:
        nilai = input(pesan).strip()
        if nilai:
            return nilai
        print("Input tidak boleh kosong!")


def input_int(pesan: str) -> int:
    """Meminta input angka integer."""
    while True:
        try:
            return int(input(pesan).strip())
        except ValueError:
            print("Harus berupa angka!")
