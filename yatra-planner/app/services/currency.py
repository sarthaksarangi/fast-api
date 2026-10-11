import httpx

from app.services.cache import get_cache, set_cache


async def fetch_currency_data(base_currency: str) -> dict[str, float]:
    cache_key = f"currency_{base_currency}"
    cached_data = get_cache(cache_key)
    if cached_data:
        return cached_data
    
    """Fetch currency exchange rate from base_currency to target_currency"""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.exchangerate.host/latest"
        )
        response.raise_for_status()
        data = response.json()

        rates = data.get("conversion_rates", {})
        set_cache(cache_key, rates, ttl = 3600)
        return rates