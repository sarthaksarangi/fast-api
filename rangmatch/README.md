# Rangmatch

FastAPI service for theatre (natak) play reviews, built with SQLModel over SQLite.

## Features

- Submit, list, fetch, update, and delete reviews
- Filter reviews by play name, with pagination
- Per-play average rating endpoint
- Rating validated to 1-5

## Run it

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Docs available at `http://127.0.0.1:8000/docs`.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| GET | `/` | Status check |
| POST | `/review/` | Create a review |
| GET | `/review/` | List reviews (filter by `play_name`, paginate with `skip`/`limit`) |
| GET | `/review/avarage/{play_name}` | Average rating and review count for a play |
| GET | `/review/{review_id}` | Fetch a single review |
| PATCH | `/review/{review_id}` | Update a review's rating/comment |
| DELETE | `/review/{review_id}` | Delete a review |

## Structure

```
main.py            # app setup, lifespan (creates tables on startup)
database.py        # SQLite engine + session dependency
models.py          # Review, ReviewCreate, ReviewRead, ReviewUpdate
routes/reviews.py  # review CRUD + average rating
```

Data is persisted to `rangmatch.db` (SQLite), created automatically on startup.
