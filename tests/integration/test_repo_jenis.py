"""Integration test untuk RepoJenis dengan database in-memory."""
import pytest
from data.repositories.repo_jenis import RepoJenis
from domain.entities.entity_jenis import Jenis


class TestRepoJenisIntegration:
    @pytest.fixture
    def repo(self):
        return RepoJenis()

    def test_simpan_dan_cari_by_id(self, repo):
        entity = repo.simpan(Jenis(0, "Elektronik"))
        assert entity.id > 0
        found = repo.cari_by_id(entity.id)
        assert found is not None
        assert found.nama == "Elektronik"

    def test_simpan_duplikat_nama(self, repo):
        repo.simpan(Jenis(0, "Elektronik"))
        with pytest.raises(Exception):
            repo.simpan(Jenis(0, "Elektronik"))

    def test_cari_semua(self, repo):
        repo.simpan(Jenis(0, "A"))
        repo.simpan(Jenis(0, "B"))
        all_items = repo.cari_semua()
        assert len(all_items) == 2

    def test_update(self, repo):
        entity = repo.simpan(Jenis(0, "Elektronik"))
        entity.nama = "Furniture"
        updated = repo.update(entity)
        assert updated.nama == "Furniture"
        found = repo.cari_by_id(entity.id)
        assert found.nama == "Furniture"

    def test_hapus(self, repo):
        entity = repo.simpan(Jenis(0, "Elektronik"))
        repo.hapus(entity.id)
        assert repo.cari_by_id(entity.id) is None

    def test_cari_by_nama(self, repo):
        repo.simpan(Jenis(0, "Elektronik"))
        found = repo.cari_by_nama("Elektronik")
        assert found is not None
        assert found.nama == "Elektronik"

    def test_cari_by_nama_not_found(self, repo):
        found = repo.cari_by_nama("Tidak Ada")
        assert found is None
