import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from src.repositories.purchase_repository import PurchaseRepository
from src.repositories.feedback_repository import FeedbackRepository
from src.repositories.bike_repository import BikeRepository
from src.repositories.payment_repository import PaymentRepository
from src.repositories.test_ride_repository import TestRideRepository
from src.repositories.delivery_repository import DeliveryRepository
import matplotlib
matplotlib.use('Agg')

# 1. Sales & Revenue
def generate_sales_chart():
    repo = PurchaseRepository()
    df = repo.load_all()
    if df.empty: return None
    fig, ax = plt.subplots(figsize=(8, 4))
    sales = df.groupby("Model")["Quantity"].sum().reset_index()
    sns.barplot(data=sales, x="Model", y="Quantity", ax=ax, palette="viridis")
    ax.set_title("Number of Bikes Sold by Model")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def generate_revenue_chart():
    repo = PurchaseRepository()
    df = repo.load_all()
    if df.empty: return None
    fig, ax = plt.subplots(figsize=(8, 4))
    revenue = df.groupby("Model")["TotalAmount"].sum().reset_index()
    # Adding a clean pie chart with exploding effect for the largest slice
    explode = [0.05] * len(revenue)
    ax.pie(revenue["TotalAmount"], labels=revenue["Model"], autopct='%1.1f%%', startangle=140, explode=explode, shadow=True, colors=sns.color_palette("Set2"))
    ax.set_title("Total Sales Revenue by Model")
    plt.tight_layout()
    return fig

# 2. Inventory Insights
def generate_inventory_chart():
    repo = BikeRepository()
    df = repo.load_all()
    if df.empty: return None
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=df, x="Model", y="Quantity", ax=ax, palette="mako")
    ax.set_title("Current Bike Inventory Levels")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

# 3. Payments
def generate_payment_method_chart():
    repo = PaymentRepository()
    df = repo.load_all()
    if df.empty: return None
    fig, ax = plt.subplots(figsize=(8, 4))
    payment_counts = df["Method"].value_counts()
    ax.pie(payment_counts.values, labels=payment_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
    ax.set_title("Preferred Payment Methods")
    plt.tight_layout()
    return fig

# 4. Test Rides
def generate_test_ride_chart():
    repo = TestRideRepository()
    df = repo.load_all()
    if df.empty: return None
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.countplot(data=df, x="Model", ax=ax, palette="rocket")
    ax.set_title("Test Rides Booked per Model")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

# 5. Deliveries
def generate_delivery_status_chart():
    repo = DeliveryRepository()
    df = repo.load_all()
    if df.empty: return None
    fig, ax = plt.subplots(figsize=(8, 4))
    status_counts = df["Status"].value_counts()
    ax.pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=["#ff9999","#66b3ff","#99ff99"])
    ax.set_title("Delivery Status Distribution")
    plt.tight_layout()
    return fig

# 6. Customer Feedback
def generate_satisfaction_chart():
    repo = FeedbackRepository()
    df = repo.load_all()
    if df.empty: return None
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df["OverallRating"], bins=5, kde=True, ax=ax, color="blue")
    ax.set_title("Overall Customer Satisfaction Distribution")
    ax.set_xlabel("Rating (1-5)")
    plt.tight_layout()
    return fig

def generate_average_ratings_chart():
    repo = FeedbackRepository()
    df = repo.load_all()
    if df.empty: return None
    fig, ax = plt.subplots(figsize=(8, 4))
    avg_ratings = df[["TestRideRating", "SalesRating", "DeliveryRating", "OverallRating"]].mean().reset_index()
    avg_ratings.columns = ["Category", "Average Rating"]
    sns.barplot(data=avg_ratings, x="Category", y="Average Rating", ax=ax, palette="magma")
    ax.set_title("Average Ratings by Category")
    ax.set_ylim(0, 5)
    plt.tight_layout()
    return fig
