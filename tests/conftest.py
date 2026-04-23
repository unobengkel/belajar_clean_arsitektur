import sys
import os
import tempfile
import shutil
import pytest

# Tambahkan root project ke sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

import database
from database import get_conn


@pytest.fixture(scope="session")
def test_db_path():
    """Buat temporary database file untuk testing (session scope)."""
    tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    tmp.close()
    db_path = tmp.name

    # Override DB_PATH agar semua koneksi menggunakan file sementara
    database.DB_PATH = db_path

    # Inisialisasi tabel
    from database import init_database
    init_database()

    yield db_path

    # Cleanup setelah semua test selesai
    try:
        os.unlink(db_path)
    except PermissionError:
        pass


@pytest.fixture(autouse=True)
def setup_test_db(test_db_path):
    """Setiap test menggunakan database file sementara yang sama, 
    tapi dibersihkan antar test."""
    with get_conn() as conn:
        conn.execute("PRAGMA foreign_keys = OFF")
        conn.execute("DELETE FROM stok")
        conn.execute("DELETE FROM barang")
        conn.execute("DELETE FROM jenis")
        conn.execute("DELETE FROM merek")
        conn.execute("DELETE FROM satuan")
        conn.execute("PRAGMA foreign_keys = ON")

    yield
