"""Integration test untuk RepoBarang dengan database in-memory."""
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
