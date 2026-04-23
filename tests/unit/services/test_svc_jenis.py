"""Unit test untuk SvcJenis dengan mocking."""
import pytest
from unittest.mock import Mock, patch
from domain.repository_interfaces.if_jenis_repository import IJenisRepository
from domain.entities.entity_jenis import Jenis
from service.svc_jenis import SvcJenis
from data.dto.dto_jenis import DTOJenis


class TestSvcJenis:
    @pytest.fixture
    def mock_repo(self):
        repo = Mock(spec=IJenisRepository)
        return repo

    @pytest.fixture
    def svc(self, mock_repo):
        return SvcJenis(mock_repo)

    def test_tambah_sukses(self, svc, mock_repo):
        mock_repo.cari_by_nama.return_value = None
        mock_repo.simpan.return_value = Jenis(id=1, nama="Elektronik")
        result = svc.tambah("Elektronik")
        assert isinstance(result, DTOJenis)
        assert result.id == 1
        assert result.nama == "Elektronik"
        mock_repo.simpan.assert_called_once()

    def test_tambah_duplikat(self, svc, mock_repo):
        mock_repo.cari_by_nama.return_value = Jenis(id=1, nama="Elektronik")
        with pytest.raises(ValueError, match="sudah ada"):
            svc.tambah("Elektronik")
        mock_repo.simpan.assert_not_called()

    def test_ubah_sukses(self, svc, mock_repo):
        mock_repo.cari_by_id.return_value = Jenis(id=1, nama="Elektronik")
        mock_repo.update.return_value = Jenis(id=1, nama="Furniture")
        result = svc.ubah(1, "Furniture")
        assert result.nama == "Furniture"

    def test_ubah_not_found(self, svc, mock_repo):
        mock_repo.cari_by_id.return_value = None
        with pytest.raises(ValueError, match="tidak ditemukan"):
            svc.ubah(999, "Test")

    def test_hapus_sukses(self, svc, mock_repo):
        mock_repo.cari_by_id.return_value = Jenis(id=1, nama="Elektronik")
        svc.hapus(1)
        mock_repo.hapus.assert_called_once_with(1)

    def test_hapus_not_found(self, svc, mock_repo):
        mock_repo.cari_by_id.return_value = None
        with pytest.raises(ValueError, match="tidak ditemukan"):
            svc.hapus(999)

    def test_cari_by_id(self, svc, mock_repo):
        mock_repo.cari_by_id.return_value = Jenis(id=1, nama="Elektronik")
        result = svc.cari_by_id(1)
        assert result is not None
        assert result.nama == "Elektronik"

    def test_cari_by_id_tidak_ada(self, svc, mock_repo):
        mock_repo.cari_by_id.return_value = None
        result = svc.cari_by_id(999)
        assert result is None

    def test_semua(self, svc, mock_repo):
        mock_repo.cari_semua.return_value = [
            Jenis(id=1, nama="A"), Jenis(id=2, nama="B")
        ]
        results = svc.semua()
        assert len(results) == 2
        assert all(isinstance(r, DTOJenis) for r in results)
