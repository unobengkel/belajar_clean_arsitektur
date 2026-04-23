"""Unit test untuk DTO Satuan."""
from data.dto.dto_satuan import DTOSatuan

class TestDTOSatuan:
    def test_to_dict_dan_from_dict(self):
        dto = DTOSatuan(id=1, nama="Unit")
        data = dto.to_dict()
        assert data == {"id": 1, "nama": "Unit"}
        result = DTOSatuan.from_dict(data)
        assert result.id == 1
        assert result.nama == "Unit"

    def test_konversi_tidak_hilang_data(self):
        original = DTOSatuan(id=2, nama="Kg")
        result = DTOSatuan.from_dict(original.to_dict())
        assert result.id == original.id
        assert result.nama == original.nama
