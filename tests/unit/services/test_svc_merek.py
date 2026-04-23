"""Unit test untuk SvcMerek dengan mocking."""
import pytest
from unittest.mock import Mock
from domain.repository_interfaces.if_merek_repository import IMerekRepository
from domain.entities.entity_merek import Merek
from service.svc_merek import SvcMerek


class TestSvcMerek:
    @pytest.fixture
    def svc(self):
        repo = Mock(spec=IMerekRepository)
        return SvcMerek(repo), repo

    def test_tambah_sukses(self, svc):
        svc, repo = svc
        repo.cari_by_nama.return_value = None
        repo.simpan.return_value = Merek(id=1, nama="Samsung")
        result = svc.tambah("Samsung")
        assert result.id == 1
        assert result.nama == "Samsung"

    def test_tambah_duplikat(self, svc):
        svc, repo = svc
        repo.cari_by_nama.return_value = Merek(id=1, nama="Samsung")
        with pytest.raises(ValueError, match="sudah ada"):
            svc.tambah("Samsung")

    def test_semua(self, svc):
        svc, repo = svc
        repo.cari_semua.return_value = [Merek(id=1, nama="Samsung")]
        results = svc.semua()
        assert len(results) == 1
