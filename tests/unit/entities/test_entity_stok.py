"""Unit test untuk entity Stok."""
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
