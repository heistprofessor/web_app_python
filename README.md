# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install Flask
pip install Flask

pip install Flask-MySQL Flask-WTF

pip install email_validator

# MYSQL Queries
CREATE DATABASE bike_store;

USE bike_store;

CREATE TABLE inquiries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    phone_number VARCHAR(15) NOT NULL,
    email VARCHAR(50) NOT NULL,
    bike_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

pip install email_validator
