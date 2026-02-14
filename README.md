# 🧠 Kortex | كوريتكس 

> **The Ultimate AI-Powered Academic & Career OS.** > Built for students and developers to bridge the gap between university lectures and professional execution.

---

## 📸 Overview
**Kortex** is more than just a dashboard; it's a "Cognitive Shell" that manages your **IAU University** materials, tracks your **GitHub Projects**, and optimizes your **Career Roadmap** (Co-op & LinkedIn) using the latest **Gemini 3 Flash** AI engine.

---

## ⚡ Key Features (v0.1 - Backend Ready)

### 🤖 AI Study Brain (Context-Aware)
- **Deep PDF Analysis:** Upload your university lectures (PDF/PPTX) and chat directly with the content.
- **Gemini 3 Integration:** Powered by Google's latest `gemini-3-flash-preview` for lighting-fast summaries.
- **Academic Context:** Answers questions based *only* on your uploaded materials to prevent AI hallucinations.

### 📚 Academic Hub (IAU Edition)
- **Course Management:** Structured database for your semester subjects (e.g., Machine Learning, Computer Vision).
- **Automated Tasking:** (In Progress) Link tasks directly to courses for a seamless study flow.

### 📁 Smart File Handling
- **Secure Uploads:** Dedicated system to store and link study materials to their respective courses.
- **Instant Extraction:** High-speed text extraction from academic documents via PyMuPDF.

---

## 🛠️ Tech Stack (Current)

- **Engine:** Python 3.10+
- **API Framework:** FastAPI (Asynchronous, High Performance)
- **AI Model:** Google Gemini 3 Flash Preview (`google-genai`)
- **Database:** SQLAlchemy ORM with SQLite
- **File Processing:** PyMuPDF (fitz)

---

## 🚀 Development Roadmap

### ✅ Phase 1: The Brain (Completed)
- [x] FastAPI Server Setup.
- [x] Gemini 3 AI Engine Integration.
- [x] Database Schema for Users, Courses, and Tasks.
- [x] PDF Content Extraction & Contextual Chat.

### ⏳ Phase 2: The Visuals (Next Up)
- [ ] **Next.js & Tailwind CSS:** Cinematic Professional UI.
- [ ] **3D Components:** Interactive project showcases.

### 🔮 Phase 3: The Nervous System
- [ ] **n8n Automation:** Sync IAU university emails & deadlines.
- [ ] **GitHub API:** Real-time tracking of personal dev projects.

---

## 🛠️ Installation (Local Dev)

1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/KhalidExe/Kortex.git](https://github.com/KhalidExe/Kortex.git)
   cd Kortex/backend
   ```

2. **Environment Setup:**
Create a .env file in the backend/ directory:
    ```bash
    GEMINI_API_KEY=your_key_here
    ```

3. **Run the API:**

    ```bash
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```

---

*Developed by **KhalidExe** © 2026*