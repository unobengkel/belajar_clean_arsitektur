"""Integration test untuk RepoMerek dengan database in-memory."""
import pytest
from data.repositories.repo_merek import RepoMerek
from domain.entities.entity_merek import Merek


class TestRepoMerekIntegration:
    @pytest.fixture
    def repo(self):
        return RepoMerek()

    def test_crud_lengkap(self, repo):
        # Create
        m = repo.simpan(Merek(0, "Samsung"))
        assert m.id > 0
        # Read
        found = repo.cari_by_id(m.id)
        assert found.nama == "Samsung"
        # Update
        m.nama = "LG"
        repo.update(m)
        assert repo.cari_by_id(m.id).nama == "LG"
        # Delete
        repo.hapus(m.id)
        assert repo.cari_by_id(m.id) is None
