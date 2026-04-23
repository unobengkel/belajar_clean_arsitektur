"""Unit test untuk DTO Stok."""
from data.dto.dto_stok import DTOStok

class TestDTOStok:
    def test_buat_dengan_nilai(self):
        dto = DTOStok(id=1, idbarang=1, jumlah=50, last_timeupdate="2025-01-01 10:00:00")
        assert dto.id == 1
        assert dto.idbarang == 1
        assert dto.jumlah == 50

    def test_to_dict_dan_from_dict(self):
        dto = DTOStok(id=1, idbarang=1, jumlah=50, last_timeupdate="2025-01-01")
        data = dto.to_dict()
        result = DTOStok.from_dict(data)
        assert result.id == dto.id
        assert result.jumlah == dto.jumlah

    def test_repr(self):
        dto = DTOStok(id=1, idbarang=1, jumlah=50, last_timeupdate="2025-01-01")
        assert repr(dto) == "DTOStok(id=1, idbarang=1, jumlah=50)"
