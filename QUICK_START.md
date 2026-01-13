# 🚀 Quick Start Guide

**Get Samarthya running in 5 minutes!**

---

## ⚡ Fast Setup

### Prerequisites Check
```bash
# Verify you have these installed:
python --version    # Should be 3.8+
node --version      # Should be 14.0+
npm --version       # Any recent version
```

---

## 📋 Step-by-Step

### 1️⃣ Backend Setup (2 minutes)

```bash
# Navigate to backend
cd my-app-backend

# Create & activate virtual environment
python -m venv venv
venv\Scripts\activate                # Windows
# source venv/bin/activate           # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Start server
uvicorn main:app --reload

# ✅ Backend running at http://localhost:8000
```

### 2️⃣ Frontend Setup (2 minutes)

```bash
# Open NEW terminal
cd Frontend

# Install dependencies
npm install

# Start development server
npm start

# ✅ Frontend running at http://localhost:3000
```

### 3️⃣ Database Setup (1 minute)

**Option A: Using MySQL Client**
```bash
mysql -h gateway01.ap-southeast-1.prod.aws.tidbcloud.com \
  -P 4000 \
  -u 2p6u58mMBxe8vS4.root \
  -p \
  --ssl-ca=my-app-backend/isrgrootx1.pem \
  samarthya_db < MOCK_DATA.sql
```

**Option B: Using MySQL Workbench**
1. Create connection with TiDB Cloud details
2. File → Run SQL Script → Select `MOCK_DATA.sql`
3. Execute

---

## 🔐 Test Login

### Student Login
- **Email**: `siddhantakhade1@gmail.com`
- **Password**: `student123`

### Company Login
- **Email**: `tcs@example.com`
- **Password**: `company123`

### Admin Login
- **Email**: `admin@samarthya.com`
- **Password**: `admin123`

---

## 🎯 First Steps

1. **Login as Student** → Upload Resume → Submit Preferences
2. **Login as Company** → Post Job → View Allocated Students
3. **Login as Admin** → Run Allocation → View Results

---

## ❓ Troubleshooting

| Issue | Solution |
|-------|----------|
| Backend won't start | Activate virtual environment |
| Frontend won't start | Delete `node_modules`, run `npm install` |
| Database error | Check internet connection, verify SSL cert |
| CORS error | Backend should allow all origins (check `main.py`) |
| Port in use | Kill process: `taskkill /PID <id> /F` (Windows) |

---

## 📚 Full Documentation

See [README_FINAL.md](README_FINAL.md) for complete documentation including:
- System requirements
- Detailed installation
- Running on different devices
- API documentation
- Advanced troubleshooting

---

**Happy Coding! 🎉**
