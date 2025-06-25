# late-show-api-challenge


##  Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge
```

### 2. Create a virtual environment with pipenv
```bash
pipenv install
pipenv shell
```

### 3. Create your PostgreSQL database
```sql
CREATE DATABASE late_show_db;
```

### 4. Set up environment variables (optional `.env`)
```
DATABASE_URI=postgresql://<user>:<password>@localhost:5432/late_show_db
JWT_SECRET_KEY=your-secret-key
```

### 5. Run database setup
```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial"
flask db upgrade
```

### 6. Seed data
```bash
python server/seed.py
```

### 7. Run the server
```bash
flask run
```

---

##  Authentication
- `POST /register`: Create user (no token required)
- `POST /login`: Get JWT token
- Protected routes require:
```http
Authorization: Bearer <your-token>
```

---

##  Routes
| Route | Method | Auth | Description |
|-------|--------|------|-------------|
| /register | POST | ❌ | Register user |
| /login | POST | ❌ | Login user, return JWT |
| /episodes | GET | ❌ | List all episodes |
| /episodes/<id> | GET | ❌ | Get episode + appearances |
| /episodes/<id> | DELETE | ✅ | Delete episode + appearances |
| /guests | GET | ❌ | List guests |
| /appearances | POST | ✅ | Create appearance |

---

##  Postman Testing
1. Import `challenge-4-lateshow.postman_collection.json`
2. Register & login to get token
3. Add `Authorization` header: `Bearer <your-token>`
4. Test protected routes like POST /appearances and DELETE /episodes/<id>

