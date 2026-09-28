import pandas as pd
import numpy as np
from datetime import datetime
from typing import Tuple

from src.repositories.purchase_repository import PurchaseRepository
from src.repositories.payment_repository import PaymentRepository
from src.repositories.delivery_repository import DeliveryRepository
from src.repositories.customer_repository import CustomerRepository
from src.repositories.bike_repository import BikeRepository

class SalesService:
    def __init__(self):
        self.purchase_repo = PurchaseRepository()
        self.payment_repo = PaymentRepository()
        self.delivery_repo = DeliveryRepository()
        self.cust_repo = CustomerRepository()
        self.bike_repo = BikeRepository()

    def get_all_purchases(self) -> pd.DataFrame:
        return self.purchase_repo.load_all()

    def get_all_payments(self) -> pd.DataFrame:
        return self.payment_repo.load_all()

    def generate_bill(self, cust_id: str, model: str, color: str, qty: int, accessories: float, insurance: float, registration: float, payment_method: str) -> Tuple[str, str]:
        cust_df = self.cust_repo.load_all()
        bike_df = self.bike_repo.load_all()
        
        # Validations
        if cust_id not in cust_df["CustomerID"].values:
            return "❌ Error: Customer not found.", ""
        bike_row = bike_df[bike_df["Model"] == model]
        if bike_row.empty:
            return "❌ Error: Bike not found.", ""
            
        bike_price = float(bike_row["Price"].values[0])
        available_qty = int(bike_row["Quantity"].values[0])
        qty = int(qty)
        
        if available_qty < qty:
            return f"❌ Error: Insufficient stock. Only {available_qty} available.", ""
            
        # Numpy Calculations
        subtotal = np.multiply(bike_price, qty)
        total_amount = np.sum([subtotal, float(accessories), float(insurance), float(registration)])
        
        purchases_df = self.purchase_repo.load_all()
        invoice_no = f"INV{len(purchases_df) + 1:03d}"
        date = datetime.now().strftime("%Y-%m-%d")
        
        # Log Purchase
        new_purchase = {
            "InvoiceNo": invoice_no, "CustomerID": cust_id, "Model": model, "Color": color,
            "Quantity": qty, "BikePrice": bike_price, "Accessories": float(accessories),
            "Insurance": float(insurance), "Registration": float(registration),
            "TotalAmount": total_amount, "PaymentMethod": payment_method, "PurchaseDate": date
        }
        self.purchase_repo.append_row(new_purchase)
        
        # Log Payment
        payments_df = self.payment_repo.load_all()
        pay_id = f"PAY{len(payments_df) + 1:03d}"
        new_payment = {
            "PaymentID": pay_id, "InvoiceNo": invoice_no, "CustomerID": cust_id, 
            "Amount": total_amount, "Method": payment_method, "Status": "Completed", "Date": date
        }
        self.payment_repo.append_row(new_payment)
        
        # Create Delivery Log
        deliveries_df = self.delivery_repo.load_all()
        del_id = f"DEL{len(deliveries_df) + 1:03d}"
        new_del = {
            "DeliveryID": del_id, "InvoiceNo": invoice_no, "Model": model, 
            "DeliveryDate": "TBD", "Status": "Pending"
        }
        self.delivery_repo.append_row(new_del)
        
        # Decrease Inventory Stock
        self.bike_repo.update_quantity(model, max(0, available_qty - qty))
        
        # Generate Bill String
        cust_name = cust_df[cust_df["CustomerID"] == cust_id]["Name"].values[0]
        bill_text = f"""
========================================
    ROYAL ENFIELD SHOWROOM - TAX INVOICE
========================================
Invoice No : {invoice_no}
Date       : {date}
Customer ID: {cust_id} ({cust_name})
----------------------------------------
Model      : {model} ({color})
Quantity   : {qty}
Base Price : ₹{bike_price:,.2f}

Subtotal   : ₹{subtotal:,.2f}
Accessories: ₹{float(accessories):,.2f}
Insurance  : ₹{float(insurance):,.2f}
RTO / Reg  : ₹{float(registration):,.2f}
----------------------------------------
TOTAL      : ₹{total_amount:,.2f}
Payment    : {payment_method}
========================================
Thank you for choosing Royal Enfield!
"""
        return "✅ Purchase successful!", bill_text
