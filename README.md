
# Indian Banks API

A Flask-based REST API that provides real-time information on Indian banks and their branches using IFSC codes and bank IDs. Built with PostgreSQL, SQLAlchemy, and Docker for local deployment and testing.

---

## 🚀 Features

- 🔍 Get branch details using IFSC code
- 🏦 List all Indian banks
- 🐘 PostgreSQL database integration using `.sql` dump
- 📦 Docker & Docker Compose support
- 🔐 Environment variable-based configuration
- 🌐 Clean RESTful API architecture

---

## 🗂 Project Structure

```

indian-banks-api/
│
├── app.py                  # Main Flask application
├── models.py               # SQLAlchemy models
├── requirements.txt        # Python dependencies
├── Dockerfile              # App container setup
├── docker-compose.yml      # Orchestration for Flask + Postgres
├── indian\_banks.sql        # SQL dump with bank data
├── .env                    # Environment variables (user creates this)
└── README.md               # You're reading it

````

---

## 🧪 API Endpoints

| Method | Endpoint                    | Description                            |
|--------|-----------------------------|----------------------------------------|
| GET    | `/`                         | Home route / welcome message           |
| GET    | `/get/banks`               | Get list of all banks                  |
| GET    | `/get/branch/<ifsc>`       | Get branch details by IFSC code        |

---

## 📦 Option 1: Run with Docker (Recommended)

### ✅ 1. Clone the Repository
```bash
git clone https://github.com/Parth1304/indian-banks-api.git
cd indian-banks-api
````

### ✅ 2. Create `.env` File

In the root directory, create a `.env` file:

```env
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
DB_NAME=indian_banks
```

### ✅ 3. Start the App

```bash
docker-compose up --build
```

App will run at:
📍 `http://localhost:5000`

---

## 🛠 Option 2: Run Without Docker

> For users who want to run the project manually using Flask and their local PostgreSQL setup.

### ✅ 1. Install PostgreSQL

Download & install from: [https://www.postgresql.org/download/](https://www.postgresql.org/download/)

Create a database named:

```sql
indian_banks
```

### ✅ 2. Import SQL Dump

Run the following command:

```bash
psql -U your_username -d indian_banks -f path/to/indian_banks.sql
```

Replace:

* `your_username` with your Postgres username (often `postgres`)
* `path/to/...` with the correct path to the SQL file

---

### ✅ 3. Set Up Python Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# or
source venv/bin/activate    # Mac/Linux
```

### ✅ 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### ✅ 5. Create `.env` File

```env
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=indian_banks
```

### ✅ 6. Run the App

```bash
flask run
```

Visit:
📍 `http://localhost:5000`

---

## 🧾 Sample Response

**Endpoint:**

```
GET /get/branch/SBIN0005943
```

**Response:**

```json
{
  "ifsc": "SBIN0005943",
  "branch": "GREATER NOIDA",
  "address": "ALPHA COMMERCIAL BELT, GREATER NOIDA, U.P.",
  "city": "GREATER NOIDA",
  "district": "GAUTAM BUDDHA NAGAR",
  "state": "UTTAR PRADESH",
  "bank_name": "STATE BANK OF INDIA"
}
```

---

## 🧱 Built With

* 🐍 Python (Flask)
* 🐘 PostgreSQL
* 🐳 Docker & Docker Compose
* ⚙️ SQLAlchemy
* 🔐 python-dotenv

---

## 📌 License

This project is for educational purposes only. Indian bank data used via `.sql` dump is assumed to be sample or publicly available data.

---

## 🙋‍♂️ Author

**Parth Khandelwal**
📧 [khandelwal.parth2000@gmail.com](mailto:khandelwal.parth2000@gmail.com)
🌐 [GitHub](https://github.com/Parth1304) | [LinkedIn](https://linkedin.com/in/parth-khandelwal-55a974192)

---

```

Let me know if you'd like me to include:
- Badges at the top (build passing, Python version, etc.)
- A live deployed link (e.g., on Render)
- A short demo video or screenshot section


```
