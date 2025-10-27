backend/
├── app/
│   ├── __init__.py          # Inisialisasi app dan konfigurasi global
│   ├── config.py            # Konfigurasi environment (dev, prod, testing)
│   ├── routes/              # Folder untuk blueprint (endpoint API)
│   │   ├── __init__.py
│   │   └── yaml_routes.py
│   ├── services/            # Logic utama / business logic
│   │   ├── __init__.py
│   │   └── yaml_service.py
│   ├── models/              # (Opsional) kalau nanti pakai DB / ORM
│   │   ├── __init__.py
│   │   └── yaml_model.py
│   ├── utils/               # Helper function, parser, validator, dsb
│   │   ├── __init__.py
│   │   └── yaml_parser.py
│   ├── middlewares/         # (Opsional) Auth, logging, dsb
│   │   ├── __init__.py
│   │   └── auth_middleware.py
│   ├── extensions/          # (Opsional) registrasi ekstensi (db, cache, cors, dsb)
│   │   ├── __init__.py
│   │   └── cors.py
│   └── main.py              # Entry point kalau mau jalankan `python -m app`
│
├── tests/                   # Unit test dan integration test
│   └── test_yaml_routes.py
│
├── requirements.txt
├── Dockerfile
└── run.py                   # Entry point utama aplikasi
