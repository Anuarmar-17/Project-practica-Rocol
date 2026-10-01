from fastapi import FastAPI

from modules.users.routers import router_user
from modules.products.routers import router_product

app = FastAPI()

app.include_router(router_user.router)
app.include_router(router_product.router)
