# 🐱 Tom And Jerry Classic 🎮

A fun, interactive, grid-based game where Jerry the Mouse tries to reach the cheese while avoiding Tom the Cat — powered by AI!

[![Game Demo](https://img.shields.io/badge/Play-Now-blueviolet?style=for-the-badge&logo=javascript)](#)  
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)](https://www.python.org/) 
[![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## 🕹️ Game Overview

> **Tom** is the AI-controlled cat 🐱  
> **Jerry** is you — the player mouse 🐭  
> **Goal**: Reach the 🧀 **cheese** before Tom catches you!

You control Jerry using your arrow keys. After every move, Tom makes a strategic move using AI logic based on the selected difficulty level.

---

## 🔥 Features

- 🎮 **Three difficulty levels**:
  - Easy: Tom can only move in 4 directions (no diagonals)
  - Intermediate: Tom moves diagonally too
  - Unbeatable: Tom uses the Minimax algorithm to outsmart you
- 🧠 AI logic with Minimax decision-making
- ⚡ Smooth frontend with beautiful UI animations
- 🧽 Clean, responsive design with character images and styled game board
- 🐍 Flask backend for AI move computation
- 😾 Emoji-powered board for fun visuals

---

## 🧠 How the AI Works

The game uses the **Minimax algorithm** for unbeatable difficulty:

```python
def minimax(cat, mouse, cheese, depth, is_cat_turn):
    # Cat tries to maximize its advantage
    # Mouse tries to minimize cat’s advantage
````

* The cat calculates all possible moves recursively
* It evaluates each outcome based on:

  * Distance to mouse
  * Mouse's distance to cheese
* AI adapts based on the selected difficulty level

---

## 📦 Technologies Used

| Frontend     | Backend        | AI Logic                  |
| ------------ | -------------- | ------------------------- |
| HTML5 + CSS3 | Flask (Python) | Minimax Algorithm         |
| JavaScript   | REST API       | Heuristics for evaluation |

---

## 🚀 Getting Started

### Prerequisites

* Python 3.10 or above
* pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/sujal-1245/Tom-And-Jerry-Classic.git
cd Tom-And-Jerry-Classic

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install flask
```

### Run the App

```bash
python app.py
```

Then open your browser and go to:
👉 [http://localhost:5000](http://localhost:5000)

---

## 🧩 Screenshots

| Gameplay                                  | Difficulty Dropdown                          |
| ----------------------------------------- | -------------------------------------------- |
| ![image](https://github.com/user-attachments/assets/f882ace3-0c3e-4ab5-91f0-11c063cbb945)

 | ![image](https://github.com/user-attachments/assets/ecb188b4-1cc4-4b7f-9acc-d322cda874a3)

 |

---

## 🤖 AI Modes Explained

| Mode         | Movement           | Intelligence           |
| ------------ | ------------------ | ---------------------- |
| Easy         | No diagonals       | Basic pathing          |
| Intermediate | Includes diagonals | Smarter pursuit        |
| Unbeatable   | Minimax AI         | Near-perfect hunter 😼 |

---

## 📁 Project Structure

```
Tom-And-Jerry-Classic/
│
├── app.py             # Flask backend
├── game_logic.py      # Minimax logic & AI moves
├── templates/
│   └── index.html     # Frontend game UI
├── static/            # (Optional) For assets
└── README.md          # Project description
```

---

## 📜 License

This project is licensed under the MIT License.
Feel free to fork, modify, and share!

---

## 🙌 Credits

Developed with ❤️ by **[Sujal](https://github.com/sujal-1245)**
Icons and emojis by [Twemoji](https://twemoji.twitter.com/) & Unicode

---

## 🌟 Star This Repo

If you like this project, please consider giving it a ⭐ on GitHub — it motivates and helps visibility!

```

---
