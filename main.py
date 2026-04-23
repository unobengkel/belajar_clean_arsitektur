import sys
import os

# Pastikan root project ada di sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import init_database
from data.repositories.repo_jenis import RepoJenis
from data.repositories.repo_merek import RepoMerek
from data.repositories.repo_satuan import RepoSatuan
from data.repositories.repo_barang import RepoBarang
from data.repositories.repo_stok import RepoStok
from service.svc_jenis import SvcJenis
from service.svc_merek import SvcMerek
from service.svc_satuan import SvcSatuan
from service.svc_barang import SvcBarang
from service.svc_stok import SvcStok
from api.menu_utama import tampilkan_menu_utama, pilih_menu
from api.api_jenis import ApiJenis
from api.api_merek import ApiMerek
from api.api_satuan import ApiSatuan
from api.api_barang import ApiBarang
from api.api_stok import ApiStok


def main():
    """Entry point aplikasi."""
    # Inisialisasi database
    init_database()
    print("Database berhasil diinisialisasi.")

    # Dependency Injection
    repo_jenis = RepoJenis()
    repo_merek = RepoMerek()
    repo_satuan = RepoSatuan()
    repo_barang = RepoBarang()
    repo_stok = RepoStok()

    svc_jenis = SvcJenis(repo_jenis)
    svc_merek = SvcMerek(repo_merek)
    svc_satuan = SvcSatuan(repo_satuan)
    svc_barang = SvcBarang(repo_barang, repo_jenis, repo_merek, repo_satuan)
    svc_stok = SvcStok(repo_stok, repo_barang)

    api_jenis = ApiJenis(svc_jenis)
    api_merek = ApiMerek(svc_merek)
    api_satuan = ApiSatuan(svc_satuan)
    api_barang = ApiBarang(svc_barang)
    api_stok = ApiStok(svc_stok)

    # Menu utama
    while True:
        tampilkan_menu_utama()
        pilihan = pilih_menu()

        if pilihan == 0:
            print("Terima kasih telah menggunakan aplikasi.")
            sys.exit(0)
        elif pilihan == 1:
            api_jenis.menu()
        elif pilihan == 2:
            api_merek.menu()
        elif pilihan == 3:
            api_satuan.menu()
        elif pilihan == 4:
            api_barang.menu()
        elif pilihan == 5:
            api_stok.menu()
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
