# **Google Sheets Clone** 📝

## **Table of Contents**
- [About the Project](#about-the-project)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Setup & Running the Project](#setup--running-the-project)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Additional Enhancements](#additional-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## **About the Project** 🎯
This is a **Google Sheets Clone** built using **Python (Flask) and JavaScript**. It allows users to enter, save, and retrieve spreadsheet data dynamically through a web-based interface.

---

## **Features** ✨
✅ Create and edit a simple spreadsheet  
✅ Save spreadsheet data into a database  
✅ Retrieve and display saved data  
✅ User-friendly web interface  
✅ Built using Flask (backend) and HTML/JavaScript (frontend)  

---

## **Technologies Used** 🛠  
- **Backend:** Flask, Flask-SQLAlchemy, Pandas  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite  
- **Version Control:** Git & GitHub  

---

## **Installation** ⚙️  

### **Step 1: Clone the Repository**  
```sh
git clone https://github.com/your-username/Google_Sheet_Clone.git
cd Google_Sheet_Clone
```

### **Step 2: Set Up a Virtual Environment** (Recommended)  
```sh
# For Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### **Step 3: Install Dependencies**  
```sh
pip install -r requirements.txt
```

---

## **Setup & Running the Project** 🚀  

### **Step 1: Initialize the Database**  
```sh
python init_db.py
```

### **Step 2: Run the Flask Server**  
```sh
python spreadsheet.py
```

By default, the application will be available at:  
👉 **http://127.0.0.1:5000/**  

---

## **API Endpoints** 🔗  
| Method | Endpoint | Description |
|--------|----------|-------------|
| **GET** | `/` | Loads the main spreadsheet UI |
| **POST** | `/save` | Saves spreadsheet data to the database |
| **GET** | `/load` | Loads saved spreadsheet data |

---

## **Project Structure** 📁  

```
Google_Sheet_Clone/
│── static/
│   ├── styles.css        # Frontend CSS styles
│   ├── script.js         # Frontend JavaScript
│── templates/
│   ├── index.html        # Main UI
│── spreadsheet.py        # Flask app (backend)
│── init_db.py            # Database initialization script
│── database.db           # SQLite database file
│── requirements.txt      # List of dependencies
│── README.md             # Project documentation
```

---

## **Additional Enhancements** ⭐  
✔ **Security Layer:** CSRF Protection added for API calls  
✔ **Performance Optimizations:** Cached responses for faster loading  
✔ **Future Improvements:** Multi-user support & Excel export functionality  

---

## **Contributing** 🤝  
Want to contribute? Follow these steps:  
1. **Fork** the repository  
2. **Clone** your fork:  
   ```sh
   git clone https://github.com/your-username/Google_Sheet_Clone.git
   ```
3. **Create a new branch**  
   ```sh
   git checkout -b feature-branch
   ```
4. **Make your changes & commit**  
   ```sh
   git add .
   git commit -m "Added new feature"
   ```
5. **Push changes & create a pull request**  

---

## **License** 📜  
This project is licensed under the **MIT License**.
