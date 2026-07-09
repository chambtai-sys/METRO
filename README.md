# 📊 METRO

**Managing Every Task Requires Organization.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Database](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

METRO is a professional, high-end Kanban board and task management engine built for your localhost. It focuses on clean organization, tactical resource management, and a minimalist design language to keep your operations running smoothly.

## 📡 Core Features

- **📂 Multi-Phase Kanban**: Track tasks across Backlog, To Do, In Progress, and Completed columns.
- **🎯 Precision Tagging**: Assign priority levels (High, Medium, Low) with visual indicators.
- **💾 SQL Persistence**: Powered by a local SQLite database—your tasks survive reboots.
- **🌃 High-End HUD**: A sleek, dark interface with glassmorphism effects and Lucide icon integration.
- **⚡ Reactive Workflow**: Instant task creation and column switching.
- **🔗 Localhost Native**: Zero build steps. Just run the core and start organizing.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/chambtai-sys/METRO.git
   cd METRO
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Engine**:
   ```bash
   python app.py
   ```

4. **Open the HUD**:
   Navigate to `http://localhost:5000` in your browser.

## 📁 Project Structure

```text
METRO/
├── app.py           # Flask Backend & SQL Logic
├── metro.db         # Local Database (auto-generated)
├── templates/       
│   └── index.html   # Main Kanban HUD
├── README.md        # Master Documentation
└── requirements.txt # Dependencies
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
