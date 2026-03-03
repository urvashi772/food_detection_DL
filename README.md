# 🍽 AI Food Detector & Analyzer

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Food Classes & Calories](#food-classes--calories)
- [Burn Time Calculation](#burn-time-calculation)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Project Overview

This project is a **web-based AI Food Detector & Analyzer** built with **Streamlit**, **YOLOv8**, and **OpenCV**.  
It allows users to upload a food image and:

- Detect the food item(s) using YOLOv8
- Display bounding boxes and labels
- Show estimated calories
- Categorize food as **Healthy** or **Unhealthy**
- Provide diet suggestions
- Calculate approximate time to burn calories via walking or running based on user weight

It’s a lightweight and interactive tool for health-conscious individuals or AI enthusiasts.

---

## Features

- 🍕 Detect multiple food items in an uploaded image
- 📊 Display calories and health category
- 🥗 Personalized diet suggestions
- 🔥 Calculate burn time for walking and running
- 💻 Web-based interface via **Streamlit**
- ⚡ Fast inference using **YOLOv8 pre-trained model**

---

## Tech Stack

- **Python 3.9+**
- **[Streamlit](https://streamlit.io/)** – for UI
- **[Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)** – object detection
- **OpenCV** – image processing
- **PIL (Pillow)** – image handling
- **NumPy** – numerical operations

---

## Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/ai-food-detector.git
cd ai-food-detector

**2️⃣ Create a Virtual Environment (Recommended)**
python -m venv food_env

# Windows
food_env\Scripts\activate

**3️⃣ Install Dependencies**
pip install -r requirements.txt

For GPU support (faster inference):

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
Usage
**1️⃣ Run the App**
streamlit run app.py
**2️⃣ Upload Image**

Upload a food image (jpg, jpeg, png)

The app detects food items, shows annotated image, calories, and suggestions

**3️⃣ Input Weight**

Enter your weight in kg to calculate burn time

Food Classes & Calories
Food Item	Calories (kcal)	Category
Pizza	285	Unhealthy
Burger	354	Unhealthy
Sushi	200	Healthy
Apple Pie	296	Unhealthy
Chocolate Cake	350	Unhealthy
Samosa	262	Unhealthy
Fried Rice	330	Unhealthy
Ice Cream	207	Healthy
Steak	271	Unhealthy
Omelette	154	Healthy
Burn Time Calculation

Burn time is estimated using MET values:

Walking MET = 3.5

Running MET = 8

Formula:

Time (hours) = Calories / (MET × Weight)

The app displays minutes of walking and running needed to burn detected food calories.

**Folder Structure**
ai-food-detector/
│
├─ app.py             # Main Streamlit application
├─ requirements.txt   # Dependencies
├─ images/            # Optional: sample input images
├─ outputs/           # Optional: annotated output images
└─ README.md          # Documentation
