"""Unit test untuk entity Jenis."""
import pytest
from domain.entities.entity_jenis import Jenis


class TestEntityJenis:
    def test_buat_jenis_default(self):
        j = Jenis()
        assert j.id == 0
        assert j.nama == ""

    def test_buat_jenis_dengan_nilai(self):
        j = Jenis(id=1, nama="Elektronik")
        assert j.id == 1
        assert j.nama == "Elektronik"

    def test_ubah_nama(self):
        j = Jenis(id=1, nama="Elektronik")
        j.nama = "Furniture"
        assert j.nama == "Furniture"

    def test_ubah_id(self):
        j = Jenis(id=1, nama="Elektronik")
        j.id = 5
        assert j.id == 5

    def test_repr(self):
        j = Jenis(id=1, nama="Elektronik")
        assert repr(j) == "Jenis(id=1, nama='Elektronik')"
