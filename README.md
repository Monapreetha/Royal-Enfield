# Royal Enfield Dealership Management System

This project is a complete, beginner-friendly dealership management application. It is built using Python, Gradio for the interactive UI, and popular data science libraries (Pandas, NumPy, Matplotlib, Seaborn) for data handling and analytics. 

## 1. Installation Commands

Ensure you have Python installed on your system. Navigate to the `royal_enfield_dealership` folder in your terminal and install the required libraries:

```bash
pip install -r requirements.txt
```

*(This will install gradio, pandas, numpy, matplotlib, and seaborn)*

## 2. How to Run the Application

Once the dependencies are installed, you can start the web application by running:

```bash
python app.py
```

After running the command, wait a few seconds, and you will see a local URL printed in the terminal (usually `http://127.0.0.1:7860/`). Open this URL in your web browser to use the application. The system will automatically create a `data/` folder and populate it with sample CSV data on the first run.

## 3. Explanation of Each Module

1. **Dashboard**: Provides a quick, high-level summary of total registered customers, total bikes in stock, and total revenue.
2. **Customer Management**: Allows registering new customers and searching/viewing existing customer records.
3. **Bike Management**: Manages the showroom's inventory. You can add new bikes and view available stock and features.
4. **Test Ride Booking**: Allows users to book test rides. Validates customer ID and bike availability to prevent double-booking.
5. **Bike Purchase & Billing**: Calculates billing based on bike price, quantity, accessories, insurance, and registration charges. It generates a unique invoice and updates inventory.
6. **Payment Management**: A unified view of all completed financial transactions and payment methods used.
7. **Delivery Management**: Allows showroom staff to track invoices and update the status of bike deliveries (e.g., Pending, Delivered).
8. **Customer Feedback**: Allows customers to submit satisfaction ratings.
9. **Data Analysis Dashboard**: Dynamically reads the CSV data to generate visualizations of sales trends and customer satisfaction.

## 4. Explanation of the Logical Flow

The application follows an **Object-Oriented Programming (OOP)** architecture via the `DealershipManager` class:
* **Initialization**: When `app.py` runs, it creates an instance of `DealershipManager`. This instance checks for the `data/` directory and creates sample CSV files if they don't exist.
* **Data Flow**: Every time a user clicks a button in the Gradio UI, it calls a specific method in the `DealershipManager` class (e.g., `book_test_ride`).
* **Processing**: The method loads the relevant CSV file using Pandas into a DataFrame, performs validation (e.g., checks if a bike is in stock), manipulates the data (e.g., reduces stock), and saves the DataFrame back to the CSV.
* **UI Update**: Gradio receives the return value from the method and updates the Textboxes, Dataframes, or Plots on the screen.

## 5. Sample Test Cases

*   **Test Case 1 (Booking Test Ride with Invalid Customer)**: Go to Tab 4. Enter Customer ID `C999` and try to book. The system will return: `Error: Customer ID does not exist.`
*   **Test Case 2 (Purchasing Out-of-Stock Bike)**: Go to Tab 5. Select `Continental GT 650` and enter a quantity of `10`. The system will return: `Error: Insufficient stock. Only 2 available.`
*   **Test Case 3 (Successful Purchase)**: Go to Tab 5. Enter Customer ID `C001`, select `Classic 350`, Quantity `1`, Accessories `2000`, and click Confirm. An invoice will be generated, and checking Tab 3 (Inventory) will show `Classic 350` stock decreased by 1.

## 6. Use of Libraries

*   **Pandas**: Used as the primary data storage and manipulation engine. It handles reading from and writing to CSV files, searching for specific rows (e.g., `df[df["CustomerID"] == cust_id]`), and concatenating new records.
*   **NumPy**: Used for robust numerical calculations, especially in the billing module (`np.multiply`, `np.sum`) to prevent type errors when calculating subtotals and total amounts.
*   **Matplotlib**: Used as the foundational plotting library to create figures and axes for the Data Analysis dashboard.
*   **Seaborn**: Used on top of Matplotlib to create attractive, statistical graphics easily (e.g., the bar chart for sales by model and the histogram for customer satisfaction).

## 7. Suggestions for Future Improvements

*   **Database Integration**: Migrate from CSV files to a robust relational database like SQLite or PostgreSQL for better concurrency handling.
*   **Authentication**: Add employee and admin login portals using Gradio's `auth` parameter.
*   **EMI Calculator**: Add a standalone module to calculate monthly loan installments for customers.
*   **Export to PDF**: Add functionality to export the generated text invoice into a downloadable PDF format.
