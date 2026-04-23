"""Integration test untuk RepoStok dengan database in-memory."""
import pytest
from data.repositories.repo_stok import RepoStok
from data.repositories.repo_barang import RepoBarang
from data.repositories.repo_jenis import RepoJenis
from data.repositories.repo_merek import RepoMerek
from data.repositories.repo_satuan import RepoSatuan
from domain.entities.entity_stok import Stok
from domain.entities.entity_barang import Barang
from domain.entities.entity_jenis import Jenis
from domain.entities.entity_merek import Merek
from domain.entities.entity_satuan import Satuan


class TestRepoStokIntegration:
    @pytest.fixture
    def stok_repo(self):
        return RepoStok()

    @pytest.fixture
    def idbarang(self):
        j = RepoJenis().simpan(Jenis(0, "Elektronik"))
        m = RepoMerek().simpan(Merek(0, "Samsung"))
        s = RepoSatuan().simpan(Satuan(0, "Unit"))
        b = RepoBarang().simpan(Barang(0, j.id, m.id, s.id, "TV"))
        return b.id

    def test_simpan_dan_cari(self, stok_repo, idbarang):
        st = stok_repo.simpan(Stok(0, idbarang, 50, "2025-01-01 10:00:00"))
        assert st.id > 0
        found = stok_repo.cari_by_id(st.id)
        assert found is not None
        assert found.jumlah == 50

    def test_cari_by_idbarang(self, stok_repo, idbarang):
        stok_repo.simpan(Stok(0, idbarang, 50, "2025-01-01"))
        found = stok_repo.cari_by_idbarang(idbarang)
        assert found is not None
        assert found.jumlah == 50

    def test_update(self, stok_repo, idbarang):
        st = stok_repo.simpan(Stok(0, idbarang, 50, "2025-01-01"))
        st.jumlah = 75
        updated = stok_repo.update(st)
        assert updated.jumlah == 75
