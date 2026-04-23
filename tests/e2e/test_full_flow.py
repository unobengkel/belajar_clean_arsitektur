"""End-to-End test: Service layer sampai Database."""
import pytest
import database
from database import get_conn
from data.repositories.repo_jenis import RepoJenis
from data.repositories.repo_merek import RepoMerek
from data.repositories.repo_satuan import RepoSatuan
from data.repositories.repo_barang import RepoBarang
from data.repositories.repo_stok import RepoStok
from service.svc_jenis import SvcJenis
from service.svc_merek import SvcMerek
from service.svc_satuan import SvcSatuan
from service.svc_barang import SvcBarang
from service.svc_stok import SvcStok


class TestE2EFullFlow:
    """Test alur lengkap dari Service ke Database dan verifikasi langsung ke DB."""

    @pytest.fixture
    def services(self):
        repo_jenis = RepoJenis()
        repo_merek = RepoMerek()
        repo_satuan = RepoSatuan()
        repo_barang = RepoBarang()
        repo_stok = RepoStok()
        return {
            "jenis": SvcJenis(repo_jenis),
            "merek": SvcMerek(repo_merek),
            "satuan": SvcSatuan(repo_satuan),
            "barang": SvcBarang(repo_barang, repo_jenis, repo_merek, repo_satuan),
            "stok": SvcStok(repo_stok, repo_barang),
        }

    def _query(self, sql, params=()):
        """Query langsung ke database test."""
        with get_conn() as conn:
            cur = conn.execute(sql, params)
            return cur.fetchall()

    def test_full_scenario(self, services):
        """Simulasi skenario lengkap bisnis."""
        # 1. Tambah Jenis
        jenis = services["jenis"].tambah("Elektronik")
        rows = self._query("SELECT * FROM jenis WHERE id=?", (jenis.id,))
        assert len(rows) == 1
        assert rows[0]["nama"] == "Elektronik"

        # 2. Tambah Merek
        merek = services["merek"].tambah("Samsung")
        rows = self._query("SELECT * FROM merek WHERE id=?", (merek.id,))
        assert len(rows) == 1

        # 3. Tambah Satuan
        satuan = services["satuan"].tambah("Unit")
        rows = self._query("SELECT * FROM satuan WHERE id=?", (satuan.id,))
        assert len(rows) == 1

        # 4. Tambah Barang
        barang = services["barang"].tambah(jenis.id, merek.id, satuan.id, "TV LED 32 Inch")
        rows = self._query("SELECT * FROM barang WHERE id=?", (barang.id,))
        assert len(rows) == 1
        assert rows[0]["nama"] == "TV LED 32 Inch"
        assert rows[0]["idjenis"] == jenis.id

        # 5. Tambah Stok
        stok = services["stok"].tambah_stok(barang.id, 50)
        rows = self._query("SELECT * FROM stok WHERE idbarang=?", (barang.id,))
        assert len(rows) >= 1
        assert rows[0]["jumlah"] == 50

        # 6. Kurangi Stok
        stok2 = services["stok"].kurangi_stok(barang.id, 10)
        rows = self._query("SELECT * FROM stok WHERE idbarang=?", (barang.id,))
        assert rows[0]["jumlah"] == 40

        # 7. Verifikasi Semua Data
        assert len(self._query("SELECT * FROM jenis")) >= 1
        assert len(self._query("SELECT * FROM merek")) >= 1
        assert len(self._query("SELECT * FROM satuan")) >= 1
        assert len(self._query("SELECT * FROM barang")) >= 1
        assert len(self._query("SELECT * FROM stok")) >= 1

    def test_foreign_key_integrity(self, services):
        """Test foreign key constraint: tambah barang dengan id yang tidak ada."""
        with pytest.raises(Exception):
            services["barang"].tambah(999, 1, 1, "Test Barang")

    def test_unique_constraint(self, services):
        """Test unique constraint: duplikat nama jenis."""
        services["jenis"].tambah("Unik")
        with pytest.raises(ValueError, match="sudah ada"):
            services["jenis"].tambah("Unik")
