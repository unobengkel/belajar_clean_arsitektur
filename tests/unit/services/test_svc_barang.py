"""Unit test untuk SvcBarang dengan mocking."""
import pytest
from unittest.mock import Mock
from domain.repository_interfaces.if_barang_repository import IBarangRepository
from domain.repository_interfaces.if_jenis_repository import IJenisRepository
from domain.repository_interfaces.if_merek_repository import IMerekRepository
from domain.repository_interfaces.if_satuan_repository import ISatuanRepository
from domain.entities.entity_barang import Barang
from domain.entities.entity_jenis import Jenis
from domain.entities.entity_merek import Merek
from domain.entities.entity_satuan import Satuan
from service.svc_barang import SvcBarang
from data.dto.dto_barang import DTOBarang


class TestSvcBarang:
    @pytest.fixture
    def mocks(self):
        return {
            "repo": Mock(spec=IBarangRepository),
            "repo_jenis": Mock(spec=IJenisRepository),
            "repo_merek": Mock(spec=IMerekRepository),
            "repo_satuan": Mock(spec=ISatuanRepository),
        }

    @pytest.fixture
    def svc(self, mocks):
        return SvcBarang(
            mocks["repo"], mocks["repo_jenis"],
            mocks["repo_merek"], mocks["repo_satuan"]
        )

    def test_tambah_sukses(self, svc, mocks):
        mocks["repo_jenis"].cari_by_id.return_value = Jenis(1, "Elektronik")
        mocks["repo_merek"].cari_by_id.return_value = Merek(1, "Samsung")
        mocks["repo_satuan"].cari_by_id.return_value = Satuan(1, "Unit")
        mocks["repo"].simpan.return_value = Barang(1, 1, 1, 1, "TV LED 32 Inch")

        result = svc.tambah(1, 1, 1, "TV LED 32 Inch")
        assert isinstance(result, DTOBarang)
        assert result.nama == "TV LED 32 Inch"
        assert result.nama_jenis == "Elektronik"

    def test_tambah_jenis_tidak_ada(self, svc, mocks):
        mocks["repo_jenis"].cari_by_id.return_value = None
        with pytest.raises(ValueError, match="Jenis dengan id"):
            svc.tambah(999, 1, 1, "Test")
        mocks["repo"].simpan.assert_not_called()

    def test_tambah_merek_tidak_ada(self, svc, mocks):
        mocks["repo_jenis"].cari_by_id.return_value = Jenis(1, "Elektronik")
        mocks["repo_merek"].cari_by_id.return_value = None
        with pytest.raises(ValueError, match="Merek dengan id"):
            svc.tambah(1, 999, 1, "Test")

    def test_ubah_not_found(self, svc, mocks):
        mocks["repo"].cari_by_id.return_value = None
        with pytest.raises(ValueError, match="tidak ditemukan"):
            svc.ubah(999, 1, 1, 1, "Test")

    def test_hapus_not_found(self, svc, mocks):
        mocks["repo"].cari_by_id.return_value = None
        with pytest.raises(ValueError, match="tidak ditemukan"):
            svc.hapus(999)

    def test_cari_by_id(self, svc, mocks):
        mocks["repo"].cari_by_id.return_value = Barang(1, 1, 1, 1, "TV")
        mocks["repo_jenis"].cari_by_id.return_value = Jenis(1, "Elektronik")
        mocks["repo_merek"].cari_by_id.return_value = Merek(1, "Samsung")
        mocks["repo_satuan"].cari_by_id.return_value = Satuan(1, "Unit")

        result = svc.cari_by_id(1)
        assert result is not None
        assert result.nama == "TV"

    def test_semua(self, svc, mocks):
        mocks["repo"].cari_semua.return_value = [
            Barang(1, 1, 1, 1, "TV"), Barang(2, 1, 1, 1, "Kulkas")
        ]
        mocks["repo_jenis"].cari_by_id.return_value = Jenis(1, "Elektronik")
        mocks["repo_merek"].cari_by_id.return_value = Merek(1, "Samsung")
        mocks["repo_satuan"].cari_by_id.return_value = Satuan(1, "Unit")

        results = svc.semua()
        assert len(results) == 2
