# My Expenses Project

A minimal Django REST API for tracking expenses and incomes by category.

## Features
- Token-based user registration & login
- CRUD for categories, incomes, and expenses
- OpenAPI schema for documentation

## Quick Start
1. **Install Requirements**
   ```bash
   git clone https://github.com/KaungHtetSoe/myexpenses.git
   cd myexpenses
   pip install -r requirements.txt

2. **Run Migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

3. **Start Server**
    ```bash
    python manage.py runserver


## Endpoints
- User: POST /api/users/ (register), POST /api/login/ (login)
- Category: GET/POST/PUT/DELETE /api/categories/
- Income: GET/POST/PUT/DELETE /api/incomes/
- Expense: GET/POST/PUT/DELETE /api/expenses/
- OpenAPI Schema: GET /openapi/

## License
MIT