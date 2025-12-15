from fastapi import APIRouter

products_router = APIRouter(prefix="/products", tags=["Products"])


@products_router.get("/")
def get_all_products():
    pass


@products_router.get("/{id}")
def get_product_by_id(id: int):
    pass


@products_router.post("/")
def create_product(new_product):
    pass
