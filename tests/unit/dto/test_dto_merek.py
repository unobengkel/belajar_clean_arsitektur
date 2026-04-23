"""Unit test untuk DTO Merek."""
from data.dto.dto_merek import DTOMerek

class TestDTOMerek:
    def test_to_dict_dan_from_dict(self):
        dto = DTOMerek(id=1, nama="Samsung")
        data = dto.to_dict()
        assert data == {"id": 1, "nama": "Samsung"}
        result = DTOMerek.from_dict(data)
        assert result.id == 1
        assert result.nama == "Samsung"

    def test_konversi_tidak_hilang_data(self):
        original = DTOMerek(id=5, nama="LG")
        result = DTOMerek.from_dict(original.to_dict())
        assert result.id == original.id
        assert result.nama == original.nama
