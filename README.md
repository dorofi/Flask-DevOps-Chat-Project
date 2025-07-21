
# Flask DevOps Chat Project

Welcome to the Flask DevOps Chat! This project is a modern, mobile-friendly web chat application built with Flask, designed for hands-on DevOps practice. It demonstrates best practices in Python project structure, containerization, and CI/CD automation.

## 🌟 Features
- **Live Group Chat:** Users can send and receive messages in real time. The chat auto-updates for all connected users without page reloads.
- **Mobile-First Design:** Responsive interface adapts beautifully to smartphones and desktops.
- **Simple & Clean UI:** Minimalist design for easy communication.
- **In-Memory Storage:** Messages are stored in server memory (for demo purposes).
- **Docker Support:** Ready-to-use Dockerfile for easy containerization and deployment.
- **CI/CD Pipeline:** Automated testing and linting via GitHub Actions.

## 🚀 Quick Start
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run locally:**
   ```bash
   python app.py
   ```
   Open your browser at `http://localhost:5000` (or your server IP).
3. **Build Docker image:**
   ```bash
   docker build -t flask-devops .
   ```
4. **Run Docker container:**
   ```bash
   docker run -p 5000:5000 flask-devops
   ```

## 🛠 DevOps Highlights
- **Containerization:** The app runs seamlessly in Docker, making it easy to deploy anywhere.
- **CI/CD:** Every push triggers automated checks (linting, test run) via GitHub Actions. See `.github/workflows/ci.yml`.
- **Best Practices:** Clean code, clear structure, and easy extensibility for further DevOps experiments.

## 📱 Mobile Experience
The chat UI is optimized for mobile devices. Just open the site on your phone and enjoy a smooth messaging experience!

## 📂 Project Structure
- `app.py` — Main Flask application with chat logic
- `requirements.txt` — Python dependencies
- `Dockerfile` — Container build instructions
- `.github/workflows/ci.yml` — CI/CD pipeline config
- `README.md` — Project documentation

## 🤝 Contributing
Feel free to fork, experiment, and extend this project for your DevOps learning journey!

---
Made for DevOps practice and learning.
