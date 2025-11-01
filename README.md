# SaccoPlus

**SaccoPlus** is a digital SACCO (Savings and Credit Cooperative Organization) management system. It includes:

- ✅ A secure Django REST backend with JWT authentication
- 📱 A Flutter mobile app for SACCO members
- 🖥️ A React-based or Django template-based admin dashboard for SACCO staff

---

## 🔐 Features

### Backend (Django + DRF + JWT)
- Member registration and login (`/api/auth/`)
- Auto-linked Member profile upon signup
- Savings tracking
- Loan applications and repayments
- Monthly unit trust earnings
- Year-end interest sharing with deductibles
- Protected API endpoints with JWT

---

## 📁 Project Structure

SaccoPlus/
├── backend/ # Django REST backend (API)
├── mobile-app/ # Flutter mobile app for members
├── dashboard-frontend/ # React or Django dashboard for admins
├── docs/ # Wireframes, schema diagrams, notes
├── README.md # Project summary and setup


---

## 🚀 API Endpoints

| Endpoint                 | Method | Description                        |
|--------------------------|--------|------------------------------------|
| `/api/auth/register/`    | POST   | Register new member + profile      |
| `/api/auth/login/`       | POST   | Get JWT access and refresh tokens  |
| `/api/savings/`          | GET    | List or add member savings         |
| `/api/loans/`            | GET/POST | View or apply for a loan         |

Add the `Authorization: Bearer <access_token>` header to access protected endpoints.

---

## 🧪 Testing

Use **Postman** or **cURL** to:
1. Register a user
2. Login and get a token
3. Use the token to access secured resources

---

## 🛠 Tech Stack

- Backend: Django, Django REST Framework, Simple JWT
- Auth: JSON Web Tokens
- Mobile App: Flutter (in progress)
- Admin UI: React (optional), or Django templates

---

## 👨‍💻 Developer Setup (Backend)

```bash
cd backend
python -m venv env
env\Scripts\activate  # or source env/bin/activate
pip install -r requirements.txt  # after generating one
python manage.py runserver
