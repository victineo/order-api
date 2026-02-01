# Order API
This project is a REST API developed in Python with Flask, following Clean Architecture principles. The system manages users and orders, including authentication via JWT.

## 🚀 Technologies Used
- **Python 3**
- **Flask**: Web Framework.
- **PyJWT**: Handling JSON Web Tokens for authentication.
- **BCrypt**: Password hashing.
- **SQLite**: Database (`storage.db` file).
- **Pytest**: Automated tests.
- **Clean Architecture**: Structure organized in Layers (Views, Controllers, Models/Repositories).

## 📂 Project Structure
The structure follows the separation of responsibilities:
- `src/main`: Route configuration, composers, and server initialization.
- `src/views`: Presentation layer, handles HTTP Requests and Responses.
- `src/controllers`: Business logic and orchestration.
- `src/models`: Repositories for database access.
- `src/drivers`: Low-level implementations (e.g., DB Connection).
- `src/errors`: Centralized error handling.

## 📦 Installation and Execution
### Prerequisites
- Python 3.x installed.

### Steps
1. **Clone the repository**.
2. **Create a virtual environment** (optional, but recommended):
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**:
   ```bash
   python run.py
   ```
   The API will be running at `http://0.0.0.0:3000`.

## 🔗 Endpoints (Routes)
### **Users**
- `POST /user/register`
  - Creates a new user.
  - Body: JSON with user data (e.g., username, password).

- `POST /user/login`
  - Performs login and returns JWT token.
  - Body: JSON with credentials.

### **Orders**
*Requires Authentication (Header Authorization)*

- `POST /orders`
  - Creates a new order.
- `GET /orders/<user_id>`
  - Returns orders for a specific user.
- `PATCH /orders/<order_id>`
  - Updates an existing order.

## 🧪 Tests
To run the tests:
```bash
pytest src/
```
