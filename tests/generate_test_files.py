import os

BASE = r"C:\Users\prime\Documents\belajar_clean_arsitektur\tests"

def write(path, content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)
    print(f"Created: {path}")

# ========== ENTITY TESTS ==========

write("unit/entities/test_entity_merek.py", '''"""Unit test untuk entity Merek."""
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
''')

write("unit/entities/test_entity_satuan.py", '''"""Unit test untuk entity Satuan."""
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
''')

write("unit/entities/test_entity_barang.py", '''"""Unit test untuk entity Barang."""
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
''')

write("unit/entities/test_entity_stok.py", '''"""Unit test untuk entity Stok."""
from domain.entities.entity_stok import Stok

class TestEntityStok:
    def test_buat_dengan_nilai(self):
        st = Stok(id=1, idbarang=1, jumlah=50, last_timeupdate="2025-01-01 10:00:00")
        assert st.id == 1
        assert st.idbarang == 1
        assert st.jumlah == 50
        assert st.last_timeupdate == "2025-01-01 10:00:00"

    def test_ubah_jumlah(self):
        st = Stok(id=1, idbarang=1, jumlah=50, last_timeupdate="2025-01-01 10:00:00")
        st.jumlah = 25
        assert st.jumlah == 25

    def test_ubah_timestamp(self):
        st = Stok(id=1, idbarang=1, jumlah=50, last_timeupdate="2025-01-01 10:00:00")
        st.last_timeupdate = "2025-06-01 12:00:00"
        assert st.last_timeupdate == "2025-06-01 12:00:00"

    def test_repr(self):
        st = Stok(id=1, idbarang=1, jumlah=50, last_timeupdate="2025-01-01 10:00:00")
        assert repr(st) == "Stok(id=1, idbarang=1, jumlah=50, last_timeupdate='2025-01-01 10:00:00')"
''')

# ========== DTO TESTS ==========

write("unit/dto/test_dto_jenis.py", '''"""Unit test untuk DTO Jenis."""
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
''')

write("unit/dto/test_dto_merek.py", '''"""Unit test untuk DTO Merek."""
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
''')

write("unit/dto/test_dto_satuan.py", '''"""Unit test untuk DTO Satuan."""
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
''')

write("unit/dto/test_dto_barang.py", '''"""Unit test untuk DTO Barang."""
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
''')

write("unit/dto/test_dto_stok.py", '''"""Unit test untuk DTO Stok."""
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
''')

print("All entity and DTO test files created successfully!")
