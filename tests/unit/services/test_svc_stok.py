"""Unit test untuk SvcStok dengan mocking."""
import pytest
from unittest.mock import Mock
from domain.repository_interfaces.if_stok_repository import IStokRepository
from domain.repository_interfaces.if_barang_repository import IBarangRepository
from domain.entities.entity_stok import Stok
from domain.entities.entity_barang import Barang
from service.svc_stok import SvcStok


class TestSvcStok:
    @pytest.fixture
    def mocks(self):
        return {
            "repo": Mock(spec=IStokRepository),
            "repo_barang": Mock(spec=IBarangRepository),
        }

    @pytest.fixture
    def svc(self, mocks):
        return SvcStok(mocks["repo"], mocks["repo_barang"])

    def test_tambah_stok_baru(self, svc, mocks):
        mocks["repo_barang"].cari_by_id.return_value = Barang(1, 1, 1, 1, "TV")
        mocks["repo"].cari_by_idbarang.return_value = None
        mocks["repo"].simpan.return_value = Stok(1, 1, 50, "2025-01-01 10:00:00")

        result = svc.tambah_stok(1, 50)
        assert result.jumlah == 50
        assert result.nama_barang == "TV"

    def test_tambah_stok_existing(self, svc, mocks):
        mocks["repo_barang"].cari_by_id.return_value = Barang(1, 1, 1, 1, "TV")
        mocks["repo"].cari_by_idbarang.return_value = Stok(1, 1, 50, "2025-01-01")
        mocks["repo"].update.return_value = Stok(1, 1, 70, "2025-06-01")

        result = svc.tambah_stok(1, 20)
        assert result.jumlah == 70

    def test_tambah_stok_barang_not_found(self, svc, mocks):
        mocks["repo_barang"].cari_by_id.return_value = None
        with pytest.raises(ValueError, match="tidak ditemukan"):
            svc.tambah_stok(999, 10)

    def test_tambah_stok_jumlah_tidak_valid(self, svc, mocks):
        mocks["repo_barang"].cari_by_id.return_value = Barang(1, 1, 1, 1, "TV")
        with pytest.raises(ValueError, match="lebih dari 0"):
            svc.tambah_stok(1, 0)

    def test_kurangi_stok_sukses(self, svc, mocks):
        mocks["repo"].cari_by_idbarang.return_value = Stok(1, 1, 50, "2025-01-01")
        mocks["repo"].update.return_value = Stok(1, 1, 40, "2025-06-01")

        result = svc.kurangi_stok(1, 10)
        assert result.jumlah == 40

    def test_kurangi_stok_tidak_cukup(self, svc, mocks):
        mocks["repo"].cari_by_idbarang.return_value = Stok(1, 1, 5, "2025-01-01")
        with pytest.raises(ValueError, match="tidak mencukupi"):
            svc.kurangi_stok(1, 10)

    def test_kurangi_stok_belum_ada(self, svc, mocks):
        mocks["repo"].cari_by_idbarang.return_value = None
        with pytest.raises(ValueError, match="belum ada"):
            svc.kurangi_stok(1, 10)

    def test_lihat_stok(self, svc, mocks):
        mocks["repo_barang"].cari_by_id.return_value = Barang(1, 1, 1, 1, "TV")
        mocks["repo"].cari_by_idbarang.return_value = Stok(1, 1, 50, "2025-01-01")

        result = svc.lihat_stok(1)
        assert result is not None
        assert result.jumlah == 50

    def test_lihat_stok_tidak_ada(self, svc, mocks):
        mocks["repo"].cari_by_idbarang.return_value = None
        result = svc.lihat_stok(999)
        assert result is None
