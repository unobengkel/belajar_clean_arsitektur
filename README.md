# 🏗️ Belajar Clean Architecture Python

Proyek contoh implementasi **Clean Architecture** menggunakan Python dengan studi kasus manajemen data barang (Inventory Management System).

## 📋 Struktur Database

```
jenis [ id, nama ]
merek [ id, nama ]
satuan [ id, nama ]
barang [ id, idjenis, idmerek, idsatuan, nama ]
stok  [ id, idbarang, jumlah, last_timeupdate ]
```

## 🏛️ Arsitektur

Proyek ini mengikuti prinsip **Clean Architecture** dimana setiap layer memiliki tanggung jawab yang terpisah dan file dipisahkan berdasarkan tujuannya masing-masing.

```
belajar_clean_arsitektur/
│
├── domain/                          # LAPISAN INTI (Enterprise Business Rules)
│   ├── entities/                    #   Entity - Object bisnis murni
│   │   ├── entity_jenis.py
│   │   ├── entity_merek.py
│   │   ├── entity_satuan.py
│   │   ├── entity_barang.py
│   │   └── entity_stok.py
│   └── repository_interfaces/       #   Interface Repository (abstraksi)
│       ├── if_jenis_repository.py
│       ├── if_merek_repository.py
│       ├── if_satuan_repository.py
│       ├── if_barang_repository.py
│       └── if_stok_repository.py
│
├── data/                            # LAPISAN DATA (Interface Adapters)
│   ├── dto/                         #   Data Transfer Object
│   │   ├── dto_jenis.py
│   │   ├── dto_merek.py
│   │   ├── dto_satuan.py
│   │   ├── dto_barang.py
│   │   └── dto_stok.py
│   ├── models/                      #   Model - Akses database langsung
│   │   ├── model_jenis.py
│   │   ├── model_merek.py
│   │   ├── model_satuan.py
│   │   ├── model_barang.py
│   │   └── model_stok.py
│   └── repositories/               #   Implementasi Repository
│       ├── repo_jenis.py
│       ├── repo_merek.py
│       ├── repo_satuan.py
│       ├── repo_barang.py
│       └── repo_stok.py
│
├── service/                         # LAPISAN APLIKASI (Use Cases)
│   ├── svc_jenis.py
│   ├── svc_merek.py
│   ├── svc_satuan.py
│   ├── svc_barang.py
│   └── svc_stok.py
│
├── api/                             # LAPISAN PRESENTASI / ANTARMUKA
│   ├── menu_utama.py
│   ├── api_jenis.py
│   ├── api_merek.py
│   ├── api_satuan.py
│   ├── api_barang.py
│   └── api_stok.py
│
├── tests/                           # PENGUJIAN (87 test cases)
│   ├── unit/                        #   Unit Test (mock)
│   │   ├── entities/
│   │   ├── dto/
│   │   └── services/
│   ├── integration/                 #   Integration Test (real SQLite)
│   │   ├── test_repo_jenis.py
│   │   ├── test_repo_merek.py
│   │   ├── test_repo_satuan.py
│   │   ├── test_repo_barang.py
│   │   ├── test_repo_stok.py
│   │   └── test_svc_with_repo.py
│   └── e2e/                         #   End-to-End Test
│       └── test_full_flow.py
│
├── database.py                      # Konfigurasi dan inisialisasi SQLite
├── main.py                          # Entry point aplikasi
├── requirements.txt                 # Dependencies
└── README.md                        # Dokumentasi ini
```

## 🔄 Alur Data (Dependency Rule)

**Arah dependency: dari luar ke dalam (inward)**

```
API → Service → Repository Interface ← Repository ← Model → SQLite
 │         │            │
 │         └── Entity ──┘
 └── DTO ───────────────┘
```

- **Layer luar** (API, DTO, Model) bisa bergantung ke **layer dalam** (Entity, Interface)
- **Layer dalam** TIDAK boleh bergantung ke **layer luar**
- Service hanya bergantung ke **Interface Repository**, bukan implementasi konkret

## ✨ Fitur

- ✅ **CRUD Jenis** - Kelola kategori barang
- ✅ **CRUD Merek** - Kelola merek barang
- ✅ **CRUD Satuan** - Kelola satuan barang
- ✅ **CRUD Barang** - Kelola data barang (terkait jenis, merek, satuan)
- ✅ **Manajemen Stok** - Tambah & kurangi stok dengan validasi
- ✅ **Validasi Duplikat** - Nama unik untuk jenis, merek, satuan
- ✅ **Foreign Key Constraints** - Integritas referensial terjaga
- ✅ **CLI Menu Interaktif** - Antarmuka terminal yang mudah digunakan
- ✅ **87 Test Cases** - Unit, Integration, dan End-to-End test

## 🚀 Cara Menjalankan

```bash
# 1. Clone repositori
git clone https://github.com/username/belajar_clean_arsitektur.git
cd belajar_clean_arsitektur

# 2. Jalankan aplikasi
python main.py
```

**Menu utama:**
```
=== APLIKASI MANAJEMEN BARANG ===
1. Kelola Jenis
2. Kelola Merek
3. Kelola Satuan
4. Kelola Barang
5. Kelola Stok
6. Keluar
Pilihan Anda:
```

## 🧪 Menjalankan Test

```bash
# Install pytest jika belum ada
pip install pytest

# Jalankan semua test (87 test cases)
python -m pytest tests -v

# Jalankan test spesifik
python -m pytest tests/unit -v
python -m pytest tests/integration -v
python -m pytest tests/e2e -v
```

### Hasil Test Terkini: ✅ **87/87 PASSED**

```
tests/unit/entities/     → 20 passed  (Entity business rules)
tests/unit/dto/          → 12 passed  (Data transfer objects)
tests/unit/services/     → 18 passed  (Service layer with mocked repos)
tests/integration/       → 34 passed  (Real SQLite database)
tests/e2e/               →  3 passed  (Full flow end-to-end)
------------------------------------------------
Total                    → 87 passed  ✅
```

## 📦 Teknologi

- **Python 3.13+**
- **SQLite3** - Database embedded (tanpa setup server)
- **pytest** - Framework pengujian
- **unittest.mock** - Mocking untuk unit test

## 🎯 Tujuan Pembelajaran

Proyek ini dibuat untuk demonstrasi **Clean Architecture** di Python dengan:

1. **Separation of Concerns** - Setiap file memiliki satu tujuan jelas
2. **Dependency Inversion** - Layer dalam tidak tahu tentang layer luar
3. **Testability** - Setiap layer bisa diuji secara terpisah
4. **Maintainability** - Perubahan di satu layer tidak merusak layer lain
5. **Domain-Centric** - Fokus pada entity & aturan bisnis di inti

---

**Dibuat untuk belajar** - Clean Architecture dengan Python 🐍
