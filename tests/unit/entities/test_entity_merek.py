"""Unit test untuk entity Merek."""
from domain.entities.entity_merek import Merek

class TestEntityMerek:
    def test_buat_default(self):
        m = Merek()
        assert m.id == 0
        assert m.nama == ""

    def test_buat_dengan_nilai(self):
        m = Merek(id=1, nama="Samsung")
        assert m.id == 1
        assert m.nama == "Samsung"

    def test_ubah_nama(self):
        m = Merek(id=1, nama="Samsung")
        m.nama = "LG"
        assert m.nama == "LG"

    def test_repr(self):
        m = Merek(id=1, nama="Samsung")
        assert repr(m) == "Merek(id=1, nama='Samsung')"
