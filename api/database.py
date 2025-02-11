from pymongo import MongoClient # type: ignore

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["book_db"]  # Use your database name

# Test the connection
print("Connected to MongoDB:", db)