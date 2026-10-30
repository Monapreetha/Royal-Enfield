import pandas as pd
import os

class PublicBookingService:
    def __init__(self):
        # We assume the main data directory is located one level up from digital_showroom
        self.data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "test_rides.csv")

    def book_test_ride(self, name: str, contact: str, model: str, date_obj, time: str) -> tuple[bool, str]:
        if not name or not contact:
            return False, "Please fill in your Name and Contact Number."

        try:
            if os.path.exists(self.data_path):
                df = pd.read_csv(self.data_path)
            else:
                df = pd.DataFrame(columns=["BookingID", "CustomerID", "Model", "Date", "Time", "Contact"])
            
            # Create a pseudo CustomerID for the online lead
            cust_id = f"LEAD_{name.split()[0].upper()}"
            booking_id = f"TR{len(df) + 1:03d}"
            date_str = date_obj.strftime("%Y-%m-%d")
            
            new_row = {
                "BookingID": booking_id,
                "CustomerID": cust_id,
                "Model": model,
                "Date": date_str,
                "Time": time,
                "Contact": contact
            }
            
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            
            # Create data dir if it doesn't exist
            os.makedirs(os.path.dirname(self.data_path), exist_ok=True)
            df.to_csv(self.data_path, index=False)
            
            success_msg = f"Thank you, {name}! Your test ride for the {model} is confirmed. Booking Reference: {booking_id}"
            return True, success_msg
            
        except Exception as e:
            return False, f"An error occurred while booking: {str(e)}"

    def submit_inquiry(self, name: str, email: str, phone: str, topic: str, message: str) -> tuple[bool, str]:
        if not name or not (email or phone):
            return False, "Please provide your Name and at least an Email address or Phone number."

        try:
            inquiry_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "customer_inquiries.csv")
            if os.path.exists(inquiry_path):
                df = pd.read_csv(inquiry_path)
            else:
                df = pd.DataFrame(columns=["InquiryID", "Name", "Email", "Phone", "Topic", "Message"])
            
            inq_id = f"INQ{len(df) + 1:03d}"
            new_row = {
                "InquiryID": inq_id,
                "Name": name,
                "Email": email or "N/A",
                "Phone": phone or "N/A",
                "Topic": topic,
                "Message": message or "N/A"
            }
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            os.makedirs(os.path.dirname(inquiry_path), exist_ok=True)
            df.to_csv(inquiry_path, index=False)
            
            return True, f"Thank you, {name}! Your inquiry regarding '{topic}' has been registered. Reference Ticket: {inq_id}. Our team will contact you within 24 hours."
        except Exception as e:
            return False, f"An error occurred while submitting inquiry: {str(e)}"

