# Indian Banks API

This repository contains a Flask-based API that interacts with a PostgreSQL database to provide details of Indian banks and their branches. The API allows you to retrieve information such as the list of banks and specific branch details using the IFSC code.

## Problem Solved

The goal of this project was to create an API that can provide data related to Indian banks. The main tasks involved:

1. **Setting up a PostgreSQL database**: I used a provided `.sql` backup file (`indianbanks.sql`) to populate the database with information about banks, branches, and their details.
2. **Creating a Flask API**: The API was developed to allow users to retrieve data from the PostgreSQL database via specific endpoints.
3. **Containerization with Docker**: To make the application easier to set up and run locally, I created a `Dockerfile` and `docker-compose.yml` for containerization.

### The API offers the following features:
- **Retrieve a list of all banks**: Get the names and IDs of all banks stored in the database.
- **Get branch details using the IFSC code**: Fetch branch-specific details (address, district, state, etc.) by providing the IFSC code.

You can also test the live version of the app at: [Live API Link](https://indian-banks-api.onrender.com)

## Project Structure

The project consists of the following key files:

- `app.py`: The main Flask application file, where the routes and logic for querying the database are defined.
- `models.py`: Defines the SQLAlchemy database models (Bank, Branch) for interacting with the PostgreSQL database.
- `requirements.txt`: Lists all the Python dependencies needed to run the application.
- `docker-compose.yml`: Defines the Docker services for the app and PostgreSQL database, enabling easy local setup.
- `Dockerfile`: The Docker configuration file for building the app's container.
- `.env`: Contains environment variables for database configuration (user, password, host, etc.).
- `indian_banks.sql`: The SQL backup file containing the data for banks and branches.

## Key Routes

- **`GET /`**: Basic home route that provides an overview of available API endpoints.
- **`GET /get/banks`**: Retrieves a list of all banks, including their `id` and `name`.
- **`GET /get/branch/<ifsc>`**: Retrieves branch details (e.g., address, city, state) for a given IFSC code.

## Steps to Run the Application Locally

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   ```

2. **Set Up PostgreSQL Database**:
   - Install PostgreSQL on your machine.
   - Create a new database (`indian_banks`) in PostgreSQL.
   - Restore the `indian_banks.sql` file to populate the database:
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

The total time taken to complete this assignment was approximately **2 days**. Here's a breakdown of the time spent on various tasks:

1. **Database Setup**: 
   - Set up PostgreSQL and restored the `.sql` file to populate the database with bank and branch data.

2. **Flask API Development**: 
   - Defined routes to handle API requests.
   - Implemented the logic to fetch data from the PostgreSQL database using SQLAlchemy.

3. **Dockerization**: 
   - Created `Dockerfile` and `docker-compose.yml` to containerize the app and PostgreSQL database, enabling easy local setup.
   - Faced some challenges with PostgreSQL connection settings in the Docker container but resolved them by ensuring correct environment variables were passed.

4. **Testing and Debugging**: 
   - Tested the application and fixed issues related to database queries and Flask routes.
   - Ensured proper error handling for missing or incorrect IFSC codes.

5. **Deployment**: 
   - Deployed the app on Render for live access, ensuring all components worked together.

### Challenges Faced
- **PostgreSQL Setup**: There were challenges in setting up the PostgreSQL database and ensuring it worked seamlessly with Flask and Docker.
- **Docker Configuration**: Learning how to containerize both Flask and PostgreSQL was a challenge. The key was understanding how to properly link the app and the database in Docker and passing the correct environment variables.

---

Feel free to open an issue or submit a pull request if you have any questions or improvements to suggest.

---
