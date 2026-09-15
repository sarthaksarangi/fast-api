# Coffee Point Menu Service

Read-only FastAPI service exposing a chai/snacks menu.

## Features

- List the full menu or filter by category (`chai`, `snacks`, `combos`)
- Search menu items by (partial) name
- Health check endpoint

## Run it

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Docs available at `http://127.0.0.1:8000/docs`, ReDoc at `/redoc`.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| GET | `/status` | Health check |
| GET | `/menu` | List menu items (optionally filter by `category`) |
| GET | `/menu/{menu_item}` | Search menu items by name |

## Structure

```
main.py    # app + routes
models.py  # MenuItem, MenuResponse schemas
data.py    # in-memory menu_items dataset
```
