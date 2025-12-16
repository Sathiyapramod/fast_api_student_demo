from fastapi import APIRouter, status

products_router = APIRouter(prefix="/products", tags=["Products"])


@products_router.get("/", status_code=status.HTTP_200_OK)
def get_all_products():
    pass


@products_router.get("/{id}", status_code=status.HTTP_200_OK)
def get_product_by_id(id: int):
    pass


@products_router.post("/", status_code=status.HTTP_200_OK)
def create_product(new_product):
    pass
