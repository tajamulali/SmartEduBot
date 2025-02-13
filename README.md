# SmartEduBot 🤖 | AI-Powered Educational Chatbot

SmartEduBot is an AI-driven chatbot designed to assist students with academic queries, provide educational resources, and automate responses in an educational environment. Built using **Flask (Python)** for the backend and **MySQL** for data storage, it integrates **ChatterBot** for AI-driven conversations. The frontend is powered by **HTML, Tailwind CSS, and JavaScript**, ensuring a modern and interactive user experience.

## 🌟 Features

✅ **AI-Powered Responses** – Uses ChatterBot to generate intelligent, automated responses.  
✅ **User Authentication & Sessions** – Secure login/signup with session management.  
✅ **Predefined & Trained Responses** – Handles common student queries with structured answers.  
✅ **Flask-ReCaptcha Security** – Protects against spam interactions.  
✅ **Modern UI with Tailwind CSS** – Clean chat interface, dark mode, and animated message bubbles.  
✅ **Database Integration** – Stores user queries and chatbot interactions in **MySQL** for analysis and improvements.  

---

## 🛠️ Tech Stack

### **Backend:**  
- Python (Flask)  
- MySQL  
- ChatterBot (AI-powered chatbot)  
- Flask-Session (Session Management)  
- Flask-ReCaptcha (Security)  

### **Frontend:**  
- HTML  
- Tailwind CSS  
- JavaScript  

---

## 🚀 Installation Guide

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/tajamulali/SmartEduBot.git
cd SmartEduBot
```

### **2️⃣ Create a Virtual Environment & Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### **3️⃣ Set Up MySQL Database**
- Create a database named `smartedubot`.
- Run the SQL script provided in `database.sql` to create necessary tables.
- Update database credentials in `config.py`.

### **4️⃣ Run the Application**
```bash
python app.py
```

SmartEduBot will be accessible at `http://127.0.0.1:5000/`

---

## 🔨 Upcoming Features

🚧 **Enhanced AI Training** – Improve chatbot responses with better dataset training.  
🚧 **Custom Knowledge Base** – Allow admins to dynamically add new responses.  
🚧 **Integration with Educational APIs** – Fetch academic materials dynamically.  
🚧 **User Query Analytics** – Track chatbot usage and optimize responses.  

---

## 💡 Why SmartEduBot?
SmartEduBot is designed to enhance student learning through AI-powered conversations. It automates common academic queries, making learning more accessible and engaging. 

🔗 **GitHub Repository:** [Your GitHub Link Here]  
📧 **LinkenIn:** [Your Linkedin Here]  

Contributions are welcome! Feel free to fork, improve, and submit pull requests. 🚀
