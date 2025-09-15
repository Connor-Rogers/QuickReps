# QuickReps 🏋️‍♂️🎙️

**QuickReps** is a **voice-first workout logger** designed to make logging your training sessions effortless.  
Instead of fumbling with apps mid-set, simply say:  

> “Log 8 reps of lat pulldowns at 140 pounds”  

QuickReps handles the rest. It uses **Automatic Speech Recognition (ASR)** and **LLM reasoning** to structure logs and store them via a **FastAPI web app**.

---

## ✨ Features
- 🎤 **Voice-First Input**: Log exercises hands-free with natural speech.
- 🤖 **LLM-powered Parsing**: Uses [Ollama](https://ollama.ai/) models to interpret your spoken inputs into structured logs.
- ⚡ **FastAPI Backend**: Lightweight, high-performance API for logging and retrieving workouts.
- 📊 **Future Dashboard**: View trends, progressive overload, and training history.
- 🔗 **Extensible**: Designed to integrate with B2C fitness logging and B2B (coach/clinical dashboards).

---

## 🛠️ Tech Stack
- **ASR** → Speech-to-text (planned integration with Whisper or other ASR models).  
- **Ollama** → Local LLM parsing for exercise intent & log structuring.  
- **FastAPI** → REST API backend.  
- **Frontend** → Simple web interface (planned).  
- **Database** → TBD (SQLite/PostgreSQL planned for persistence).  

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.ai/) installed locally
- (Optional) Virtual environment

### Installation
```bash
# Clone repo
git clone https://github.com/<your-username>/quickreps.git
cd quickreps

# Install dependencies
pip install -r requirements.txt