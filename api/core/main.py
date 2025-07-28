from fastapi import FastAPI
from api.controller import (
    auth_controller,
    user_controller,
    whatsapp_controller,
    scheduling_controller,

    invoice_controller,
    plan_controller,
    subscription_controller,
    tenant_controller,
)
from api.core.middleware import LogMiddleware

app = FastAPI()


app.add_middleware(LogMiddleware)

app.include_router(auth_controller.router)
app.include_router(user_controller.router)
app.include_router(scheduling_controller.router)
app.include_router(whatsapp_controller.router)

# app.include_router(invoice_controller.router)
app.include_router(plan_controller.router)
app.include_router(subscription_controller.router)
app.include_router(tenant_controller.router)
