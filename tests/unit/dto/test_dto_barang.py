"""Unit test untuk DTO Barang."""
from data.dto.dto_barang import DTOBarang

class TestDTOBarang:
    def test_buat_dengan_nilai(self):
        dto = DTOBarang(id=1, idjenis=1, idmerek=1, idsatuan=1, nama="TV",
                        nama_jenis="Elektronik", nama_merek="Samsung", nama_satuan="Unit")
        assert dto.id == 1
        assert dto.nama_jenis == "Elektronik"
        assert dto.nama_merek == "Samsung"
        assert dto.nama_satuan == "Unit"

    def test_to_dict_dan_from_dict(self):
        dto = DTOBarang(id=1, idjenis=1, idmerek=1, idsatuan=1, nama="TV",
                        nama_jenis="Elektronik", nama_merek="Samsung", nama_satuan="Unit")
        data = dto.to_dict()
        result = DTOBarang.from_dict(data)
        assert result.id == dto.id
        assert result.nama_jenis == dto.nama_jenis
        assert result.nama_merek == dto.nama_merek
        assert result.nama_satuan == dto.nama_satuan

    def test_buat_default(self):
        dto = DTOBarang()
        assert dto.id == 0
        assert dto.nama == ""
