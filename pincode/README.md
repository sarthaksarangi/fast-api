# Pincode API

FastAPI service for looking up Indian postal (PIN) code details — city, state, and district — with custom exception handling.

## Features

- Single pincode lookup
- Bulk lookup (up to 20 pincodes per request)
- Custom exception handlers for invalid and not-found pincodes
- In-memory sample dataset covering 15 major cities

## Run it

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Docs available at `http://127.0.0.1:8000/docs`.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| GET | `/pincode` | Liveness check |
| GET | `/pincode/{code}` | Look up a single 6-digit pincode |
| POST | `/pincode/bulk` | Look up multiple pincodes at once (`{"pincodes": [...]}`) |

## Structure

```
main.py        # app + routes
models.py      # request/response schemas + validators
exceptions.py  # PincodeNotFoundError, InvalidPincodeError + handlers
data.py        # in-memory pincode_db sample dataset
```
