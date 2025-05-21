from pydantic import BaseModel, validator
from datetime import datetime
from langchain_core.utils.function_calling import convert_to_openai_tool

class Expense(BaseModel):
    description: str
    net_amount: float
    gross_amount: float
    tax_rate: float
    date: datetime

class Report(BaseModel):
    report: str
    

test_add_expense_tool = convert_to_openai_tool(Expense)
test_report_tool = convert_to_openai_tool(Report)