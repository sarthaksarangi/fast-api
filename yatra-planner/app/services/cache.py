import time
from typing import Any

_cache: dict[str, dict[str, Any]] = {}


def get_cache(key: str) -> Any | None:
    if key not in _cache:
        return None

    entry = _cache[key]
    if time.time() - entry["timestamp"] > entry["ttl"]:
        del _cache[key]
        return None
    return entry["data"]

def set_cache(key: str, data: Any, ttl: int) -> None:
    _cache[key] = {
    "data": data,
    "timestamp": time.time(),
    "ttl": ttl
    }

def clear_cache() -> None:
    _cache.clear()


def get_cache_stats() -> dict[str, int]:
    current_time = time.time()
    expired_keys = [
        key
        for key, entry in _cache.items()
        if current_time - entry["timestamp"] > entry["ttl"]
    ]
    for key in expired_keys:
        del _cache[key]

    return {"entries": len(_cache)}