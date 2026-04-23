import os

BASE = r"C:\Users\prime\Documents\belajar_clean_arsitektur\tests"

def write(path, content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)
    print(f"Created: {path}")


# ========== SERVICE TESTS (with mocking) ==========

write("unit/services/test_svc_jenis.py", '''"""Unit test untuk SvcJenis dengan mocking."""
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
''')

write("unit/services/test_svc_merek.py", '''"""Unit test untuk SvcMerek dengan mocking."""
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
''')

write("unit/services/test_svc_satuan.py", '''"""Unit test untuk SvcSatuan dengan mocking."""
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
''')

write("unit/services/test_svc_barang.py", '''"""Unit test untuk SvcBarang dengan mocking."""
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
''')

write("unit/services/test_svc_stok.py", '''"""Unit test untuk SvcStok dengan mocking."""
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
''')

print("Service test files created successfully!")
