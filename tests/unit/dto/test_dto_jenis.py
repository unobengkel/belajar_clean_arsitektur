"""Unit test untuk DTO Jenis."""
from data.dto.dto_jenis import DTOJenis

class TestDTOJenis:
    def test_buat_default(self):
        dto = DTOJenis()
        assert dto.id == 0
        assert dto.nama == ""

    def test_buat_dengan_nilai(self):
        dto = DTOJenis(id=1, nama="Elektronik")
        assert dto.id == 1
        assert dto.nama == "Elektronik"

    def test_to_dict(self):
        dto = DTOJenis(id=1, nama="Elektronik")
        data = dto.to_dict()
        assert data == {"id": 1, "nama": "Elektronik"}

    def test_from_dict(self):
        dto = DTOJenis.from_dict({"id": 2, "nama": "Furniture"})
        assert dto.id == 2
        assert dto.nama == "Furniture"

    def test_from_dict_kosong(self):
        dto = DTOJenis.from_dict({})
        assert dto.id == 0
        assert dto.nama == ""

    def test_repr(self):
        dto = DTOJenis(id=1, nama="Elektronik")
        assert repr(dto) == "DTOJenis(id=1, nama='Elektronik')"
