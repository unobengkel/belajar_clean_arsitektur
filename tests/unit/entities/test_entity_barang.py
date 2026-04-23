"""Unit test untuk entity Barang."""
import pytest
from domain.entities.entity_barang import Barang

class TestEntityBarang:
    @pytest.fixture
    def barang(self):
        return Barang(id=1, idjenis=1, idmerek=1, idsatuan=1, nama="TV LED 32 Inch")

    def test_buat_dengan_nilai(self, barang):
        assert barang.id == 1
        assert barang.idjenis == 1
        assert barang.idmerek == 1
        assert barang.idsatuan == 1
        assert barang.nama == "TV LED 32 Inch"

    def test_ubah_nama(self, barang):
        barang.nama = "Kulkas 2 Pintu"
        assert barang.nama == "Kulkas 2 Pintu"

    def test_ubah_idjenis(self, barang):
        barang.idjenis = 2
        assert barang.idjenis == 2

    def test_ubah_idmerek(self, barang):
        barang.idmerek = 3
        assert barang.idmerek == 3

    def test_ubah_idsatuan(self, barang):
        barang.idsatuan = 2
        assert barang.idsatuan == 2

    def test_repr(self, barang):
        expected = "Barang(id=1, nama='TV LED 32 Inch', idjenis=1, idmerek=1, idsatuan=1)"
        assert repr(barang) == expected
