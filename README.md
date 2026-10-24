# fast-api

FastAPI practice projects, each a self-contained service with its own virtual environment and dependencies.

## Projects

| Project | Description |
| --- | --- |
| `book-keeper/` | Book inventory API with user ownership and API-key protected writes |
| [`dabewalla/`](dabewalla/README.md) | Dabbewala delivery order tracking API (SQLModel + SQLite) |
| `netra-vision/` | No project files yet |
| [`pincode/`](pincode/README.md) | Indian PIN code lookup API with custom exception handling |
| [`rangmatch/`](rangmatch/README.md) | Theatre play reviews API (SQLModel + SQLite) |
| [`resturant-menu/`](resturant-menu/README.md) | Read-only chai/snacks menu API |
| [`yatra-planner/`](yatra-planner/README.md) | Travel planning API combining weather, currency, and destination data |

## Running a project

Each project is independent. From the project's directory:

```bash
pip install -r requirements.txt
```

Start most projects with `uvicorn main:app --reload`. For `yatra-planner`, set
`WEATHER_API_KEY` and run `uvicorn app.main:app --reload` instead.

Then open `http://127.0.0.1:8000/docs` for interactive API docs.
