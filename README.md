# Grocery Store Inventory Manager with Streamlit 🍏🍖🥦🍞

Welcome to the Grocery Store Inventory Manager project! This application is built using Python and Streamlit, providing a seamless and interactive way to manage grocery store inventory across multiple categories.

## 🚀 Features

- 🌟 **Create, Update, and Delete Inventory:**

  - Users can easily add, update, and delete inventory items.
  - Supports multiple categories including Grocery, Meat, Produce, and Bakery.

- 📈 **Dynamic Stock Management:**
  - Adjust stock quantities directly in the SQL database using an intuitive slider.
- 🗃️ **Comprehensive Category Management:**

  - Manage items across various categories: Grocery, Meat, Produce, and Bakery.

- 🎉 **Instant Feedback:**
  - Receive real-time success and error messages for a seamless user experience.

## 🛠️ Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/grocery-inventory-manager.git
   cd grocery-inventory-manager
   ```

Create a Virtual Environment and Install Dependencies:

```sh
Copy code
python3 -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
Set Up the Database:

Ensure you have PostgreSQL installed and running.
Create the necessary tables by executing the SQL scripts provided in the database directory.
Environment Variables:
```

Create a .env file in the root directory with the following content:
env
Copy code
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
DB_DATABASE=your_db_name
🎮 Usage
Run the Application:

```sh
Copy code
streamlit run main.py
Navigate through the App:

Use the sidebar to switch between different functionalities.
Add, update, and delete inventory items within each category.
Adjust stock quantities using sliders.
📋 Database Schema
The application uses a PostgreSQL database with the following tables:
```

```SQL
Grocery
sql
Copy code
CREATE TABLE grocery (
id SERIAL PRIMARY KEY,
item_name VARCHAR(100) NOT NULL,
stock INT NOT NULL,
expiration_date DATE NOT NULL
);
Meat
sql
Copy code
CREATE TABLE meat (
id SERIAL PRIMARY KEY,
item_name VARCHAR(100) NOT NULL,
stock INT NOT NULL,
cut_type VARCHAR(100) NOT NULL
);
Produce
sql
Copy code
CREATE TABLE produce (
id SERIAL PRIMARY KEY,
item_name VARCHAR(100) NOT NULL,
stock INT NOT NULL,
in_season VARCHAR(100) NOT NULL
);
Bakery
sql
Copy code
CREATE TABLE bakery (
id SERIAL PRIMARY KEY,
item_name VARCHAR(100) NOT NULL,
stock INT NOT NULL,
pastry_type VARCHAR(100) NOT NULL
);
```

🧑‍💻 Contribution
Contributions are welcome! Feel free to fork the repository and submit pull requests.

📄 License
This project is licensed under the MIT License.
