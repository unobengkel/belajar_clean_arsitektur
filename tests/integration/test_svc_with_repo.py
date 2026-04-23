"""Integration test: Service + Repository (tanpa mock)."""
import pytest
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


class TestServiceWithRepo:
    @pytest.fixture
    def svcs(self):
        repo_jenis = RepoJenis()
        repo_merek = RepoMerek()
        repo_satuan = RepoSatuan()
        repo_barang = RepoBarang()
        repo_stok = RepoStok()
        return {
            "jenis": SvcJenis(repo_jenis),
            "merek": SvcMerek(repo_merek),
            "satuan": SvcSatuan(repo_satuan),
            "barang": SvcBarang(repo_barang, repo_jenis, repo_merek, repo_satuan),
            "stok": SvcStok(repo_stok, repo_barang),
        }

    def test_alur_lengkap(self, svcs):
        # Tambah master data
        j = svcs["jenis"].tambah("Elektronik")
        m = svcs["merek"].tambah("Samsung")
        s = svcs["satuan"].tambah("Unit")
        assert j.id > 0 and m.id > 0 and s.id > 0

        # Tambah barang
        b = svcs["barang"].tambah(j.id, m.id, s.id, "TV LED 32 Inch")
        assert b.id > 0
        assert b.nama_jenis == "Elektronik"

        # Stok
        st = svcs["stok"].tambah_stok(b.id, 50)
        assert st.jumlah == 50

        # Kurangi stok
        st2 = svcs["stok"].kurangi_stok(b.id, 10)
        assert st2.jumlah == 40

        # Cari barang
        found = svcs["barang"].cari_by_nama("TV")
        assert len(found) >= 1

        # Cek stok
        stok = svcs["stok"].lihat_stok(b.id)
        assert stok.jumlah == 40
