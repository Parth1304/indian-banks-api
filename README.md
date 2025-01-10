# Indian Banks API

This repository contains a Flask-based API that interacts with a PostgreSQL database to provide details of Indian banks and their branches. The API allows you to retrieve information such as the list of banks and specific branch details using the IFSC code.

## Problem Solved

The goal of this project was to create an API that can provide data related to Indian banks. The main tasks involved:

1. **Setting up a PostgreSQL database**: I used a provided `.sql` backup file (`indianbanks.sql`) to populate the database with information about banks, branches, and their details.
2. **Creating a Flask API**: The API was developed to allow users to retrieve data from the PostgreSQL database via specific endpoints.
3. **Containerization with Docker**: To make the application easier to set up and run locally, I created a `Dockerfile` and `docker-compose.yml` for containerization.

The API offers the following features:
- Retrieve a list of all banks.
- Get branch details using the IFSC code.

You can also test the live version of the app at: [Live API Link](https://indian-banks-api.onrender.com)

## Steps to Run the Application Locally

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   ```

2. **Set Up PostgreSQL Database**:
   - Install PostgreSQL on your machine.
   - Create a new database (`indian_banks`) in PostgreSQL.
   - Restore the `indianbanks.sql` file to populate the database:
     ```bash
     psql -U postgres -d indian_banks -f path_to_indian_banks.sql
     ```

3. **Create a `.env` File**:
   In the root directory of the project, create a `.env` file and add the following variables:
   ```env
   DB_USER=postgres
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=indian_banks
   ```

4. **Install Dependencies**:
   Create a virtual environment and install the necessary dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

5. **Run the Application**:

   **Option 1: Using Docker (Recommended)**:
   - Run the app and PostgreSQL in containers:
     ```bash
     docker-compose up --build
     ```
   - The app will be accessible at `http://localhost:5000`.

   **Option 2: Without Docker**:
   - Run the Flask app directly:
     ```bash
     flask run
     ```
   - Ensure the `.env` file is configured correctly.

6. **Test the API**:
   - **Get all banks**: `GET /get/banks`
   - **Get branch details by IFSC**: `GET /get/branch/<ifsc>`

## Time Taken to Complete the Assignment

The total time taken to complete this assignment was approximately **2 days**, including:

- Setting up the PostgreSQL database and tables.
- Writing the Flask API to interact with the database.
- Testing the API endpoints.
- Creating Docker support for easier local setup.
- Debugging and refining the application.
- (The most challenging thing was to deploy the app, as I had to learn how to containerize through docker, and deploy the app and the postgres database)

---

Feel free to open an issue or submit a pull request if you have any questions or improvements to suggest.
```

Now, the `README.md` includes the live server link where the application is hosted.
