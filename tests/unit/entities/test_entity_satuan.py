"""Unit test untuk entity Satuan."""
from domain.entities.entity_satuan import Satuan

class TestEntitySatuan:
    def test_buat_default(self):
        s = Satuan()
        assert s.id == 0
        assert s.nama == ""

    def test_buat_dengan_nilai(self):
        s = Satuan(id=1, nama="Unit")
        assert s.id == 1
        assert s.nama == "Unit"

    def test_ubah_nama(self):
        s = Satuan(id=1, nama="Unit")
        s.nama = "Pcs"
        assert s.nama == "Pcs"

    def test_repr(self):
        s = Satuan(id=1, nama="Unit")
        assert repr(s) == "Satuan(id=1, nama='Unit')"
