# fast-api

FastAPI practice projects, each a self-contained service with its own virtual environment and dependencies.

## Projects

| Project | Description |
| --- | --- |
| [`dabewalla/`](dabewalla/README.md) | Dabbewala delivery order tracking API (SQLModel + SQLite) |
| [`pincode/`](pincode/README.md) | Indian PIN code lookup API with custom exception handling |
| [`rangmatch/`](rangmatch/README.md) | Theatre play reviews API (SQLModel + SQLite) |
| [`resturant-menu/`](resturant-menu/README.md) | Read-only chai/snacks menu API |
| `rag/` | Empty — reserved for a future RAG project |

## Running a project

Each project is independent. From the project's directory:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open `http://127.0.0.1:8000/docs` for interactive API docs.
