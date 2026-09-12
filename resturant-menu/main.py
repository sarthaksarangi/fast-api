from fastapi import FastAPI, HTTPException
from fastapi.params import Query
from data import menu_items
from models import MenuItem, MenuResponse

app = FastAPI(
    title="Coffee Point Menu Service",
    description=(
        "Read Only API for Coffee Point Menu Service. "
    ),
    version="1.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/status", tags=["Health Check"])
def status():
    """Health Check endpoint"""
    return {"status": "OK"}

@app.get('/menu',response_model=MenuResponse, tags=["Menu"])
def get_menu(category: str | None = Query(None, description="Filter menu items by category")):
    if category:
        filtered = [item for item in menu_items if item["category"] == category.lower()]

        if not filtered:
            raise HTTPException(status_code=404, detail=f"No item found in category {category}")
        return MenuResponse(count=len(filtered), items=filtered)

    return MenuResponse(count=len(menu_items), items=menu_items)

@app.get("/menu/{menu_item}", response_model=MenuResponse, tags=["Menu"])
def menu_item(menu_item: str):
    items = [item for item in menu_items if  menu_item.lower() in item["name"].lower()] 
    print(items)
    if not items:
        raise HTTPException(status_code=404, detail="Item not found in Menu")
    return MenuResponse(count= len(items), items=items)