"""Unit test untuk SvcSatuan dengan mocking."""
import pytest
from unittest.mock import Mock
from domain.repository_interfaces.if_satuan_repository import ISatuanRepository
from domain.entities.entity_satuan import Satuan
from service.svc_satuan import SvcSatuan


class TestSvcSatuan:
    @pytest.fixture
    def svc(self):
        repo = Mock(spec=ISatuanRepository)
        return SvcSatuan(repo), repo

    def test_tambah_sukses(self, svc):
        svc, repo = svc
        repo.cari_by_nama.return_value = None
        repo.simpan.return_value = Satuan(id=1, nama="Unit")
        result = svc.tambah("Unit")
        assert result.id == 1
        assert result.nama == "Unit"

    def test_tambah_duplikat(self, svc):
        svc, repo = svc
        repo.cari_by_nama.return_value = Satuan(id=1, nama="Unit")
        with pytest.raises(ValueError, match="sudah ada"):
            svc.tambah("Unit")
