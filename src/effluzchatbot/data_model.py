from pydantic import BaseModel, validator
from datetime import datetime
from langchain_core.utils.function_calling import convert_to_openai_tool

class Client(BaseModel):
    id: int
    name: str
    email: str
    phone: str

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

class SaleOrder(BaseModel):
    id: int
    client_id: int
    product_id: int
    quantity: int
    total_price: float
    date: datetime
    status: str

class Report(BaseModel):
    report: str
    

add_client_tool = convert_to_openai_tool(Client)
add_product_tool = convert_to_openai_tool(Product)
add_sale_order_tool = convert_to_openai_tool(SaleOrder)
report_tool = convert_to_openai_tool(Report)