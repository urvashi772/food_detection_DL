import streamlit as st
import numpy as np
import cv2
from PIL import Image
from ultralytics import YOLO

# -----------------------------
# Load YOLOv8 Model (Food detection)
# -----------------------------
# You can replace this with your own trained food detection model
model = YOLO("yolov8n.pt")  # YOLOv8 nano (general)

# Example mapping for food classes (update to match your model)
# If you trained a custom model, adjust class_names accordingly
class_names = [
    "pizza","burger","sushi","apple_pie","chocolate_cake",
    "samosa","fried_rice","ice_cream","steak","omelette"
]

# Calories dictionary (per detected food)
calories_dict = {
    "pizza": 285, "burger": 354, "sushi": 200,
    "apple_pie": 296, "chocolate_cake": 350,
    "samosa": 262, "fried_rice": 330,
    "ice_cream": 207, "steak": 271, "omelette": 154
}

# Burn time calculator
def calculate_burn_time(calories, weight):
    walking_met = 3.5
    running_met = 8
    walking_hours = calories / (walking_met * weight)
    running_hours = calories / (running_met * weight)
    return round(walking_hours*60,1), round(running_hours*60,1)

st.title("🍽 AI Food Detector & Analyzer")

uploaded_file = st.file_uploader("Upload Food Image", type=["jpg","jpeg","png"])

if uploaded_file is not None:
    # Load image
    img = Image.open(uploaded_file).convert("RGB")
    img_np = np.array(img)

    # Detect food items
    results = model(img_np)

    # Annotate image with boxes & labels
    annotated = results[0].plot()

    # Show annotated output
    st.image(annotated, use_column_width=True, caption="Detected Food Items")

    # Grab detection result
    detections = results[0].boxes
    if len(detections) == 0:
        st.write("No food items detected.")
    else:
        # Select highest confidence detection
        best = max(detections, key=lambda b: b.conf[0])

        label_id = int(best.cls[0])
        confidence = float(best.conf[0]) * 100

        # Safe class name
        if label_id < len(class_names):
            detected_food = class_names[label_id]
        else:
            detected_food = "pizza"

        calories = calories_dict.get(detected_food, 200)
        category = "Unhealthy" if calories > 250 else "Healthy"

        st.subheader("🔍 Top Detection")
        st.write(f"Food: **{detected_food}**")
        st.write(f"Confidence: {round(confidence,2)}%")
        st.write(f"Calories: {calories} kcal")
        st.write(f"Category: {category}")

        st.subheader("🥗 Diet Suggestion")
        if category == "Unhealthy":
            st.write("""
            • Next meal me salad + protein lo  
            • Sugar avoid karo  
            • Zyada pani piyo  
            • Light dinner karo  
            """)
        else:
            st.write("""
            • Balanced meal maintain karo  
            • Overeating avoid karo  
            • Protein include karo  
            """)

        # Ask for weight
        weight = st.number_input("Enter your weight (kg) to calculate burn time", min_value=30, max_value=120, value=55)
        walking_min, running_min = calculate_burn_time(calories, weight)

        st.subheader("🔥 To Burn Calories")
        st.write(f"🚶 Walking: {walking_min} minutes")
        st.write(f"🏃 Running: {running_min} minutes")