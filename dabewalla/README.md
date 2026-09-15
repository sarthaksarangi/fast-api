# Dabbewala Delivery API

FastAPI service for tracking dabbewala (tiffin/lunchbox) delivery orders, built with SQLModel over SQLite.

## Features

- Create and list delivery orders, filterable by status and creation date
- Order status lifecycle: `preparing` → `picked_up` → `in_transit` → `delivered`
- Daily stats endpoint summarizing order counts by status
- Health check endpoint

## Run it

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Docs available at `http://127.0.0.1:8000/docs`.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| POST | `/orders/` | Create a new order |
| GET | `/orders/` | List orders (filter by `status`, `created_date`; paginate with `skip`/`limit`) |
| GET | `/stats/daily` | Order counts by status for a given date (defaults to today) |
| GET | `/health` | Health check |

## Structure

```
main.py          # app setup, lifespan (creates tables on startup)
database.py      # SQLite engine + session dependency
models.py        # Order, OrderStatus, OrderCreate, OrderUpdate, StatusLog
routes/orders.py # order CRUD/listing
routes/stats.py  # daily summary
```

Data is persisted to `dabewalla.db` (SQLite), created automatically on startup.
