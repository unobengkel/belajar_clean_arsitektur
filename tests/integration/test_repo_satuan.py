"""Integration test untuk RepoSatuan dengan database in-memory."""
import pytest
from data.repositories.repo_satuan import RepoSatuan
from domain.entities.entity_satuan import Satuan


class TestRepoSatuanIntegration:
    @pytest.fixture
    def repo(self):
        return RepoSatuan()

    def test_crud_lengkap(self, repo):
        s = repo.simpan(Satuan(0, "Unit"))
        assert s.id > 0
        found = repo.cari_by_id(s.id)
        assert found.nama == "Unit"
        s.nama = "Pcs"
        repo.update(s)
        assert repo.cari_by_id(s.id).nama == "Pcs"
