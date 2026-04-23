import os

BASE = r"C:\Users\prime\Documents\belajar_clean_arsitektur\tests"

def write(path, content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)
    print(f"Created: {path}")


# ========== INTEGRATION TESTS (Repository + Database) ==========

write("integration/test_repo_jenis.py", '''"""Integration test untuk RepoJenis dengan database in-memory."""
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
''')

write("integration/test_repo_merek.py", '''"""Integration test untuk RepoMerek dengan database in-memory."""
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
''')

write("integration/test_repo_satuan.py", '''"""Integration test untuk RepoSatuan dengan database in-memory."""
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
''')

write("integration/test_repo_barang.py", '''"""Integration test untuk RepoBarang dengan database in-memory."""
import pytest
from data.repositories.repo_barang import RepoBarang
from data.repositories.repo_jenis import RepoJenis
from data.repositories.repo_merek import RepoMerek
from data.repositories.repo_satuan import RepoSatuan
from domain.entities.entity_barang import Barang
from domain.entities.entity_jenis import Jenis
from domain.entities.entity_merek import Merek
from domain.entities.entity_satuan import Satuan


class TestRepoBarangIntegration:
    @pytest.fixture
    def repos(self):
        return {
            "jenis": RepoJenis(),
            "merek": RepoMerek(),
            "satuan": RepoSatuan(),
            "barang": RepoBarang(),
        }

    @pytest.fixture
    def master_ids(self, repos):
        j = repos["jenis"].simpan(Jenis(0, "Elektronik"))
        m = repos["merek"].simpan(Merek(0, "Samsung"))
        s = repos["satuan"].simpan(Satuan(0, "Unit"))
        return {"idjenis": j.id, "idmerek": m.id, "idsatuan": s.id}

    def test_simpan_dan_cari(self, repos, master_ids):
        b = repos["barang"].simpan(Barang(
            0, master_ids["idjenis"], master_ids["idmerek"],
            master_ids["idsatuan"], "TV LED 32 Inch"
        ))
        assert b.id > 0
        found = repos["barang"].cari_by_id(b.id)
        assert found is not None
        assert found.nama == "TV LED 32 Inch"

    def test_cari_by_nama(self, repos, master_ids):
        b = repos["barang"].simpan(Barang(0, master_ids["idjenis"],
            master_ids["idmerek"], master_ids["idsatuan"], "TV LED 32 Inch"))
        results = repos["barang"].cari_by_nama("TV")
        assert len(results) >= 1
        assert results[0].nama == "TV LED 32 Inch"
''')

write("integration/test_repo_stok.py", '''"""Integration test untuk RepoStok dengan database in-memory."""
import pytest
from data.repositories.repo_stok import RepoStok
from data.repositories.repo_barang import RepoBarang
from data.repositories.repo_jenis import RepoJenis
from data.repositories.repo_merek import RepoMerek
from data.repositories.repo_satuan import RepoSatuan
from domain.entities.entity_stok import Stok
from domain.entities.entity_barang import Barang
from domain.entities.entity_jenis import Jenis
from domain.entities.entity_merek import Merek
from domain.entities.entity_satuan import Satuan


class TestRepoStokIntegration:
    @pytest.fixture
    def stok_repo(self):
        return RepoStok()

    @pytest.fixture
    def idbarang(self):
        j = RepoJenis().simpan(Jenis(0, "Elektronik"))
        m = RepoMerek().simpan(Merek(0, "Samsung"))
        s = RepoSatuan().simpan(Satuan(0, "Unit"))
        b = RepoBarang().simpan(Barang(0, j.id, m.id, s.id, "TV"))
        return b.id

    def test_simpan_dan_cari(self, stok_repo, idbarang):
        st = stok_repo.simpan(Stok(0, idbarang, 50, "2025-01-01 10:00:00"))
        assert st.id > 0
        found = stok_repo.cari_by_id(st.id)
        assert found is not None
        assert found.jumlah == 50

    def test_cari_by_idbarang(self, stok_repo, idbarang):
        stok_repo.simpan(Stok(0, idbarang, 50, "2025-01-01"))
        found = stok_repo.cari_by_idbarang(idbarang)
        assert found is not None
        assert found.jumlah == 50

    def test_update(self, stok_repo, idbarang):
        st = stok_repo.simpan(Stok(0, idbarang, 50, "2025-01-01"))
        st.jumlah = 75
        updated = stok_repo.update(st)
        assert updated.jumlah == 75
''')

write("integration/test_svc_with_repo.py", '''"""Integration test: Service + Repository (tanpa mock)."""
import pytest
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


class TestServiceWithRepo:
    @pytest.fixture
    def svcs(self):
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

    def test_alur_lengkap(self, svcs):
        # Tambah master data
        j = svcs["jenis"].tambah("Elektronik")
        m = svcs["merek"].tambah("Samsung")
        s = svcs["satuan"].tambah("Unit")
        assert j.id > 0 and m.id > 0 and s.id > 0

        # Tambah barang
        b = svcs["barang"].tambah(j.id, m.id, s.id, "TV LED 32 Inch")
        assert b.id > 0
        assert b.nama_jenis == "Elektronik"

        # Stok
        st = svcs["stok"].tambah_stok(b.id, 50)
        assert st.jumlah == 50

        # Kurangi stok
        st2 = svcs["stok"].kurangi_stok(b.id, 10)
        assert st2.jumlah == 40

        # Cari barang
        found = svcs["barang"].cari_by_nama("TV")
        assert len(found) >= 1

        # Cek stok
        stok = svcs["stok"].lihat_stok(b.id)
        assert stok.jumlah == 40
''')


# ========== E2E TESTS ==========

write("e2e/test_full_flow.py", '''"""End-to-End test: API layer sampai Database."""
import pytest
from database import get_connection
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
        conn = get_connection(":memory:")
        cur = conn.execute(sql, params)
        result = cur.fetchall()
        conn.close()
        return result

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
''')


# ========== REQUIREMENTS TEST ==========

write("requirements-test.txt", '''pytest>=9.0.0
pytest-mock>=3.15.0
''')

print("Integration, E2E test files, and requirements-test.txt created successfully!")
