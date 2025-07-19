import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import base64
import math
import numpy as np
import ast
import pandas as pd
import os
import datetime
import uuid
from scipy.optimize import fsolve
from pathlib import Path
import json
import shutil
from io import BytesIO
import smtplib
from email.message import EmailMessage

# ✅ Set page configuration FIRST
st.set_page_config(page_title="Aerospace Web Page", 
                   page_icon="Screenshot (50).png", 
                   layout="wide")

# ✅ Function to encode image to base64 for background
def get_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# ✅ Function to set background image
def set_background(image_path):
    try:
        base64_str = get_base64(image_path)
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{base64_str}");
                background-size: 100% 95%; ;
                background-position: center;
                background-attachment: fixed;    
            }}
            </style>
            """,unsafe_allow_html=True)
            
    except FileNotFoundError:
        st.error("Background image not found. Please check the file path.")

# ✅ Apply background image (Make sure the path is correct)
set_background("Demo.png")

# ---------- STYLING ----------
def set_custom_styles():
    st.markdown("""
    <style>
        .form-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 150px;
        }

        div[data-baseweb="input"] {
            width: 200px !important;
        }

        input {
            height: 40px !important;
            font-size: 16px !important;
            padding: 5px 10px !important;
            border-radius: 8px !important;
            border: 1px solid #ccc !important;
            background-color: #1e1e1e !important;
            color: white !important;
        }

        .stButton button {
            width: 200px;
            margin-top: 10px;
            padding: 10px;
            font-size: 16px;
            border-radius: 8px;
            background-color: #7b2cbf;
            color: white;
        }

        .stButton button:hover {
            background-color: #5a189a;
        }
    </style>
    """, unsafe_allow_html=True)

# ---------- LOGIN PAGE ----------
def login_page():
    set_custom_styles()
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    st.markdown("### Welcome")

    username = st.text_input("", placeholder="e.g. Aerospace", label_visibility="collapsed")

    if st.button("Explore Now"):
        if username.strip():
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.warning("Please enter your name.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- WELCOME PAGE ----------
def welcome_page():
        # Encode local image to base64 string
        def get_base64_image(image_path):
            with Image.open(image_path) as img:
                buffered = BytesIO()
                img.save(buffered, format="PNG")
                return base64.b64encode(buffered.getvalue()).decode()

        # Full absolute path to the image
        image_path = "923965.jpg"

        # Check if image exists first
        if os.path.exists(image_path):
            img_base64 = get_base64_image(image_path)

            # Apply background to sidebar using a more reliable CSS selector
            st.markdown(
                f"""
                <style>
                [data-testid="stSidebar"] {{
                    background-image: url("data:image/png;base64,{img_base64}");
                    background-size: cover;
                    background-position: center;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
        else:
            st.sidebar.error("Image file not found!")

        # ✅ Function to encode image to base64 for background
        def get_base64(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
    
        def Home():
                    # ✅ Function to set background image
                    def set_background(image_path):
                        try:
                            base64_str = get_base64(image_path)
                            st.markdown(
                                f"""
                                <style>
                                .stApp {{
                                    background-image: url("data:image/png;base64,{base64_str}");
                                    background-size: cover;
                                    background-position: center;
                                    background-attachment: fixed;    
                                }}
                                </style>
                                """,unsafe_allow_html=True)
                                
                        except FileNotFoundError:
                            st.error("Background image not found. Please check the file path.")

                    # ✅ Apply background image (Make sure the path is correct)
                    set_background("Sukhoi Su-30 Fighter Jet Desktop Wallpaper.jpg")
                    # ✅ Load the logo
                    logo = Image.open("Screenshot (50).png")
                    # ✅ Header Section
                    st.image(logo, width=150)
                    st.title("🛸 Welcome to the Aerospace Demo Web Page")
                    # ✅ Display Current Date, Time, and Day
                    now = datetime.datetime.now()
                    date_today = now.strftime("%Y-%m-%d")
                    time_now = now.strftime("%H:%M:%S")
                    day_today = now.strftime("%A")
                    st.write(f"📅 **Date:** {date_today}",f"⏰ **Time:** {time_now}",f"🗓️ **Day:** {day_today}")
                    st.subheader("Where Dreams Take Flight and Futures are Engineered.")
                    
                    # ✅ About Section
                    st.header("Discover the World of Aerospace")
                    st.markdown("""
                    <div style="
                        background-color: rgba(240, 242, 246, 0.3);
                        padding: 30px;
                        border-radius: 15px;
                        border: 1px solid rgba(255, 255, 255, 0.3);
                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                        font-size: 24px;
                        line-height: 1.8;
                        color: white;
                        backdrop-filter: blur(8px);
                        -webkit-backdrop-filter: blur(8px);
                        margin-bottom: 28px;
                    ">
                        <div style="font-size: 28px;">
                            From the depths of the atmosphere to the far reaches of space — aerospace engineering shapes how we move, explore, and connect.
                            This platform is your gateway to understanding and innovating in one of the most advanced and impactful fields of science and technology.
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    st.header("Why Aerospace?")
                    st.markdown("""
                    <div style="
                        background-color: rgba(240, 242, 246, 0.3); 
                        padding: 30px;
                        border-radius: 15px;
                        border: 1px solid rgba(255, 255, 255, 0.3);
                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                        line-height: 1.8;
                        color: white;
                        backdrop-filter: blur(8px);
                        -webkit-backdrop-filter: blur(8px);
                        margin-bottom: 28px;
                    ">
                        <div style="font-size: 28px;">
                            Aerospace engineering pushes the frontiers of science, technology, and human potential.
                            It powers global communication, defense, transportation, and space exploration — making it one of the most exciting and essential domains of the 21st century.
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    # ✅ Features Section
                    st.header("🚀 What You’ll Find Here")
                    col1, col2, col3,col4 = st.columns(4)
                    
                    col1, col2, col3, col4 = st.columns(4)  

                    with col1:
                        st.markdown("""
                            <div style="background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        line-height: 1.8;
                                        color: white;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;">
                                <h5 style="color:#003366;">✈️ Learn</h5>
                                <p style="font-size:28px;">
                                    Dive into aeronautics, astronautics, propulsion, aerodynamics, structures,
                                    control systems, and much more — simplified and made practical for learners and professionals.
                                </p>
                            </div>
                        """, unsafe_allow_html=True)  

                    with col2:
                        st.markdown("""
                            <div style="background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        line-height: 1.8;
                                        color: white;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;">
                                <h5 style="color:#003366;">🛠 Explore Projects</h5>
                                <p style="font-size:28px;">   
                                    Real-world aerospace projects from students, researchers, and innovators. Reusable launch vehicles, UAV systems, hybrid rockets, and orbital mechanics — all in one place.
                                </p>
                            </div>
                        """, unsafe_allow_html=True) 

                    with col3:
                       st.markdown("""
                            <div style="background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        line-height: 1.8;
                                        color: white;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;">
                                <h5 style="color:#003366;">📚 Free Tools & Resources</h5>
                                <p style="font-size:28px;">
                                         <li>Aerospace Engineering Calculators
                                         <li>Interactive Simulations & Animations
                                         <li>Lecture Notes, Diagrams, and Infographics
                                         <li>Conceptual Design Aids
                                         <li>Python-based Engineering Apps   
                                </p>
                            </div>
                        """, unsafe_allow_html=True)
                        
        def about():
                    # Function to set background
                    def about(image_path):
                        try:
                            base64_str = get_base64(image_path)
                            st.markdown(
                                f"""
                                <style>
                                .stApp {{
                                    background-image: url("data:image/png;base64,{base64_str}");
                                    background-size: cover;
                                    background-position: center;
                                    background-attachment: fixed;
                                }}
                                </style>
                                """,
                                unsafe_allow_html=True
                            )
                        except FileNotFoundError:
                            st.error("Background image not found. Please check the file path.")
                    # ✅ Set background image (Make sure the path is correct)
                    about("2488575.jpg")
                    # Title of the page
                    st.title("✈️ About Aerospace")
                    st.markdown("""
                    <div style="
                        background-color: rgba(240, 242, 246, 0.3);
                        padding: 30px;
                        border-radius: 15px;
                        border: 1px solid rgba(255, 255, 255, 0.3);
                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                        font-size: 24px;
                        line-height: 1.8;
                        color: white;
                        backdrop-filter: blur(8px);
                        -webkit-backdrop-filter: blur(8px);
                        margin-bottom: 28px;
                    ">
                        <div style="font-size: 28px;">
                          Aerospace is the field of engineering and science devoted to the development of aircraft and spacecraft.
                          It combines aeronautics (flight within Earth’s atmosphere) and astronautics (flight beyond the atmosphere),
                          enabling everything from commercial airliners to deep-space exploration missions.
                          At its core, aerospace engineering integrates principles of physics, mathematics, and material science to push the boundaries of speed, efficiency, and innovation.
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    # Section: The Team
                    st.header("Program and Design By")
                    # Create columns to display team members side by side
                    col1, = st.columns(1)
                    with col1:
                        team_member1 = Image.open("aman.jpeg").resize((150, 150))
                        st.image(team_member1)
                        st.markdown("Mr. Amandeep Singh")
                        st.markdown("""
                        <div style="
                            background-color: rgba(240, 242, 246, 0.3);
                            padding: 30px;
                            border-radius: 15px;
                            border: 1px solid rgba(255, 255, 255, 0.3);
                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                            font-size: 24px;
                            line-height: 1.8;
                            color: white;
                            backdrop-filter: blur(8px);
                            -webkit-backdrop-filter: blur(8px);
                            margin-bottom: 28px;
                        ">
                            <div style="font-size: 28px;">
                                With over 3 years of experience in aerospace engineering and education,
                                Mr.Amandeep Singh has always been dedicated to transforming the way aerospace concepts are taught.
                                After earning a degree in B.tech and M.tech in
                                Aerospace Engineering with specializtion in Guided Missile , they worked in different education companies,
                                where they led innovative projects that pushed the boundaries of aerospace technology. 
                                Mr.Amandeep Singh founded Amantah Education to create an environment where students could learn by doing and discover their potential in the field of aerospace.
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
        def design_area():
                design_area = st.sidebar.radio("Design Options", ["Dimension Section", "Airfoil Section", "Aerodynamic Section"])
                if design_area == "Dimension Section":
                        def Dimension_Section(image_path):
                                    try:
                                        base64_str = get_base64(image_path)
                                        st.markdown(
                                            f"""
                                            <style>
                                            .stApp {{
                                                background-image: url("data:image/png;base64,{base64_str}");
                                                background-size: cover;
                                                background-position: fit;
                                                background-attachment: fixed;
                                            }}
                                            </style>
                                            """,
                                            unsafe_allow_html=True
                                        )
                                    except FileNotFoundError:
                                        st.error("Background image not found. Please check the file path.")
                        # ✅ Set background image (Make sure the path is correct)
                        Dimension_Section("Pressure-nbqxhy.jpg")
                        def convert_units(value, from_unit, to_unit, conversion_dict):
                            if from_unit in conversion_dict and to_unit in conversion_dict:
                                return value * conversion_dict[to_unit] / conversion_dict[from_unit]
                            return None

                        def main():
                            st.title("Unit Conversion Web App")
                            category = st.selectbox("Select a category", ["Length", "Weight", "Temperature", "Speed"])
                            unit_dicts = {
                                "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084},
                                "Weight": {"Kilogram": 1, "Gram": 1000, "Milligram": 1000000, "Pound": 2.20462, "Ounce": 35.274},
                                "Speed": {"Meter per second": 1, "Kilometer per hour": 3.6, "Miles per hour": 2.23694, "Foot per second": 3.28084},}
                            
                            if category in ["Length", "Weight", "Speed"]:
                                from_unit = st.selectbox("From Unit", list(unit_dicts[category].keys()))
                                to_unit = st.selectbox("To Unit", list(unit_dicts[category].keys()))
                                value = st.number_input("Enter value", min_value=0.0, format="%.6f")
                                if st.button("Convert"):
                                    result = convert_units(value, from_unit, to_unit, unit_dicts[category])
                                    st.success(f"{value} {from_unit} is equal to {result:.6f} {to_unit}")
                            
                            elif category == "Temperature":
                                from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
                                to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
                                value = st.number_input("Enter temperature", format="%.2f")
                                if st.button("Convert"):
                                    result = None
                                    if from_unit == to_unit:
                                        result = value
                                    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
                                        result = (value * 9/5) + 32
                                    elif from_unit == "Celsius" and to_unit == "Kelvin":
                                        result = value + 273.15
                                    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                                        result = (value - 32) * 5/9
                                    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                                        result = (value - 32) * 5/9 + 273.15
                                    elif from_unit == "Kelvin" and to_unit == "Celsius":
                                        result = value - 273.15
                                    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                                        result = (value - 273.15) * 9/5 + 32
                                    
                                    st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")  
                        if __name__ == "__main__":
                            main()
                            
                elif design_area == "Graph Plotter":
                     def Dimension_Section(image_path):
                                try:
                                    base64_str = get_base64(image_path)
                                    st.markdown(
                                        f"""
                                        <style>
                                        .stApp {{
                                            background-image: url("data:image/png;base64,{base64_str}");
                                            background-size: cover;
                                            background-position: fit;
                                            background-attachment: fixed;
                                        }}
                                        </style>
                                        """,
                                        unsafe_allow_html=True
                                    )
                                except FileNotFoundError:
                                    st.error("Background image not found. Please check the file path.")
                     # ✅ Set background image (Make sure the path is correct)
                     Dimension_Section("pexels-weekendplayer-187041.jpg")
                     Graph_Plotter = st.sidebar.radio("Select Options", ["Cl vs Aoa","Cd vs Aoa","Cl vs Cd","Aerodynamic efficiency vs Aoa"])
                     if Graph_Plotter=="Cl vs Aoa":
                            st.title("Cl vs AOA Plotter")
                            # Inputs
                            initial_ao = st.number_input("Enter the Initial ao value with respect to NACA series:", value=6.28)
                            Aoa_alpha_stall_max = st.number_input("Enter the Stall Angle (degrees):", value=15.0)
                            Zero_lift_Aoa = st.number_input("Enter the zero lift angle of attack (degrees):", value=-2.0)
                            AR = st.number_input("Enter the Aspect Ratio of the wing:", value=6.0)
                            e = 0.95
                            pi=22/7
                            # Compute values
                            aoa_range = np.linspace(Zero_lift_Aoa - 5, Aoa_alpha_stall_max + 10, 300)
                            a = initial_ao / (1 + (initial_ao / (pi * e * AR)))
                            Cl_max = a * (Aoa_alpha_stall_max - Zero_lift_Aoa)
                            Cl_values = []
                            for aoa in aoa_range:
                                if aoa <= Aoa_alpha_stall_max:
                                    Cl = a * (aoa - Zero_lift_Aoa)
                                else:
                                    Cl = Cl_max - 0.1 * (aoa - Aoa_alpha_stall_max)
                                    Cl = max(Cl, 0)
                                Cl_values.append(Cl)
                            # Plot
                            fig, ax = plt.subplots(figsize=(8, 5))
                            ax.plot(aoa_range, Cl_values, label='Cl vs AOA', color='blue')
                            ax.axvline(x=Aoa_alpha_stall_max, color='red', linestyle='--', label='Stall Angle')
                            ax.set_title("Lift Coefficient (Cl) vs Angle of Attack (AOA)")
                            ax.set_xlabel("Angle of Attack (degrees)")
                            ax.set_ylabel("Lift Coefficient (Cl)")
                            ax.grid(True)
                            ax.legend()
                            st.pyplot(fig)
                            
                     elif Graph_Plotter=="Cd vs Aoa":
                            st.title("Cd vs Angle of Attack Plotter")
                            # User inputs
                            initial_ao = st.number_input("Initial ao (per rad):", value=6.28)
                            Aoa_alpha_stall_max = st.number_input("Stall Angle (degrees):", value=15.0)
                            Zero_lift_Aoa = st.number_input("Zero-lift AOA (degrees):", value=-2.0)
                            AR = st.number_input("Aspect Ratio:", value=6.0)
                            Cd0 = st.number_input("Zero-lift Drag (Cd0):", value=0.02)
                            e = 0.95
                            pi=22/7
                            # Compute range and values
                            aoa_range = np.linspace(Zero_lift_Aoa - 5, Aoa_alpha_stall_max + 10, 300)
                            a = initial_ao / (1 + (initial_ao / (pi * e * AR)))
                            Cl_max = a * (Aoa_alpha_stall_max - Zero_lift_Aoa)
                            Cl_values = []
                            for aoa in aoa_range:
                                if aoa <= Aoa_alpha_stall_max:
                                    Cl = a * (aoa - Zero_lift_Aoa)
                                else:
                                    Cl = Cl_max - 0.1 * (aoa - Aoa_alpha_stall_max)
                                    Cl = max(Cl, 0)
                                Cl_values.append(Cl)
                            Cd_values = [Cd0 + (cl**2) / (pi * e * AR) for cl in Cl_values]
                            # Plot
                            fig, ax = plt.subplots(figsize=(8, 5))
                            ax.plot(aoa_range, Cd_values, label="Cd vs AOA", color="purple")
                            ax.set_title("Drag Coefficient (Cd) vs Angle of Attack (AOA)")
                            ax.set_xlabel("Angle of Attack (degrees)")
                            ax.set_ylabel("Drag Coefficient (Cd)")
                            ax.grid(True)
                            ax.legend()
                            st.pyplot(fig)
                            
                     elif Graph_Plotter=="Cl vs Cd":
                            st.title("Drag Polar: Cl vs Cd Plotter")
                            # Inputs
                            initial_ao = st.number_input("Enter the Initial ao value with respect to NACA series:", value=6.28)
                            Aoa_alpha_stall_max = st.number_input("Enter the Stall Angle (degrees):", value=15.0)
                            Zero_lift_Aoa = st.number_input("Enter the Zero-lift angle of attack (degrees):", value=-2.0)
                            AR = st.number_input("Enter the Aspect Ratio of the wing:", value=6.0)
                            Cd0 = st.number_input("Enter the Zero-lift drag (Cd0):", value=0.02)
                            e = 0.95  # constant for now
                            pi=22/7
                            # Angle of attack range
                            aoa_range = np.linspace(Zero_lift_Aoa - 5, Aoa_alpha_stall_max + 10, 300)
                            a = initial_ao / (1 + (initial_ao / (pi * e * AR)))
                            Cl_max = a * (Aoa_alpha_stall_max - Zero_lift_Aoa)
                            Cl_values = []
                            for aoa in aoa_range:
                                if aoa <= Aoa_alpha_stall_max:
                                    Cl = a * (aoa - Zero_lift_Aoa)
                                else:
                                    Cl = Cl_max - 0.1 * (aoa - Aoa_alpha_stall_max)
                                    Cl = max(Cl, 0)
                                Cl_values.append(Cl)

                            Cd_values = [Cd0 + (cl**2) / (pi * e * AR) for cl in Cl_values]
                            # Plot
                            fig, ax = plt.subplots(figsize=(8, 5))
                            ax.plot(Cd_values, Cl_values, label='Cl vs Cd (Drag Polar)', color='green')
                            ax.set_title("Drag Polar: Cl vs Cd")
                            ax.set_xlabel("Drag Coefficient (Cd)")
                            ax.set_ylabel("Lift Coefficient (Cl)")
                            ax.grid(True)
                            ax.legend()
                            st.pyplot(fig)
                            
                     elif Graph_Plotter=="Aerodynamic efficiency vs Aoa":
                            st.title("Aerodynamic Efficiency Calculator")
                            st.subheader("Cl/Cd vs Angle of Attack (AOA)")
                            # Input fields
                            initial_ao = st.number_input("Initial ao (per NACA series)", value=6.28)
                            Aoa_alpha_stall_max = st.number_input("Stall Angle (degrees)", value=15.0)
                            Zero_lift_Aoa = st.number_input("Zero Lift Angle of Attack (degrees)", value=-2.0)
                            AR = st.number_input("Aspect Ratio of the wing", value=7.0)
                            Cd0 = st.number_input("Zero-lift drag value", value=0.02)
                            e = 0.95  # fixed
                            pi=22/7
                            # Run calculation on button click
                            if st.button("Calculate and Plot"):
                                aoa_range = np.linspace(Zero_lift_Aoa - 5, Aoa_alpha_stall_max + 10, 300)
                                a = initial_ao / (1 + (initial_ao / (pi * e * AR)))
                                
                                Cl_values = []
                                Cl_max = a * (Aoa_alpha_stall_max - Zero_lift_Aoa)
                                for aoa in aoa_range:
                                    if aoa <= Aoa_alpha_stall_max:
                                        Cl = a * (aoa - Zero_lift_Aoa)
                                    else:
                                        drop_rate = 0.1
                                        Cl = Cl_max - drop_rate * (aoa - Aoa_alpha_stall_max)
                                        Cl = max(Cl, 0)
                                    Cl_values.append(Cl)

                                Cd_values = [Cd0 + (cl**2) / (pi * e * AR) for cl in Cl_values]
                                efficiency_values = [cl / cd if cd != 0 else 0 for cl, cd in zip(Cl_values, Cd_values)]
                                # Plotting
                                fig, ax = plt.subplots(figsize=(10, 6))
                                ax.plot(aoa_range, efficiency_values, label='Cl/Cd vs AOA', color='green')
                                ax.set_title("Aerodynamic Efficiency (Cl/Cd) vs Angle of Attack (AOA)")
                                ax.set_xlabel("Angle of Attack (degrees)")
                                ax.set_ylabel("Aerodynamic Efficiency (Cl/Cd)")
                                ax.grid(True)
                                ax.legend()
                                st.pyplot(fig)
                        
                elif design_area == "Airfoil Section":
                            def Airfoil_Section(image_path):
                                try:
                                    base64_str = get_base64(image_path)
                                    st.markdown(
                                        f"""
                                        <style>
                                        .stApp {{
                                            background-image: url("data:image/png;base64,{base64_str}");
                                            background-size: cover;
                                            background-position: center;
                                            background-attachment: fixed;
                                        }}
                                        </style>
                                        """,
                                        unsafe_allow_html=True
                                    )
                                except FileNotFoundError:
                                    st.error("Background image not found. Please check the file path.")
                            # ✅ Set background image (Make sure the path is correct)
                            Airfoil_Section("flap-types-img_0712.jpg.optimal.jpg")
                            st.sidebar.write("## Airfoil Plotter")  
                            Airfoil_Section = st.sidebar.radio("Select Options", ["History of Airfoil", "Types of Airfoil", "Airfoil Calculation"])
                            if Airfoil_Section == "History of Airfoil":
                                            st.title("✈️ History of Airfoil")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                     The airfoil is a seemingly simple shape with a profound impact on human history. Designed to generate lift when air flows over it, the airfoil is at the heart of flight. From the dreams of ancient inventors to the precision of modern aerospace engineering, the journey of the airfoil is a remarkable story of innovation, science, and vision.
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            st.header("📜 Ancient Dreams and Early Ideas")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    The idea of flying like birds has fascinated humans for millennia. While the exact concept of an airfoil did not exist in ancient times, early civilizations showed a deep interest in the mechanics of flight.
                                                    In China, kites were flown as early as 500 BCE, hinting at an understanding of how air could interact with shaped surfaces. In Greece, legends like that of Daedalus and Icarus reveal humanity’s longing to conquer the skies.
                                                    One of the earliest known thinkers to study flight seriously was Leonardo da Vinci in the 15th century. He sketched designs of ornithopters — machines meant to mimic the flapping of bird wings — and made observations about airflow and wing surfaces.
                                                </div>
                                            </div>
                                            """,unsafe_allow_html=True)

                                            st.header("🧠 The Scientific Birth of Aerodynamics")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                        In the 18th and 19th centuries, the field of flight began to take on scientific form.
                                                        Sir George Cayley, an English engineer and inventor, is often regarded as the Father of Modern Aerodynamics. In the early 1800s, he proposed that lift, drag, and thrust were the three primary forces acting on a flying body. Most importantly, Cayley recognized that a curved wing could better generate lift.
                                                        Later, Otto Lilienthal, the “Glider King,” conducted over 2,000 gliding flights and provided the first recorded lift and drag data. His curved wing experiments laid the groundwork for modern airfoil development.
                                                </div>
                                            </div>    
                                            """, unsafe_allow_html=True)

                                            st.header("🛩️ The Wright Brothers and the First Powered Flight")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    In 1903, Orville and Wilbur Wright achieved the first powered, controlled, and sustained flight. Their success was built on careful testing of wing shapes, using their own wind tunnel to design efficient airfoils.
                                                    Their airfoil featured a curved upper surface and flatter lower surface — allowing air to move faster over the top and generating lift via pressure differences. This historic flight of the Wright Flyer was the breakthrough the world needed to truly take off.
                                                </div> 
                                            </div> 
                                            """, unsafe_allow_html=True)

                                            st.header("📊 Standardizing Airfoil Design: The NACA Era")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                        In the 1930s, the National Advisory Committee for Aeronautics (NACA) began to standardize airfoil design. Their families of airfoils, such as NACA 2412, became widely used and formed the backbone of modern aircraft wing engineering.
                                                        Each NACA number describes camber, position of maximum camber, and thickness. This systematic approach allowed engineers to optimize aircraft performance for speed, stability, and efficiency.
                                                </div>
                                            </div> 
                                            """, unsafe_allow_html=True)

                                            st.header("🚀 The Jet Age and Supersonic Flight")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                        With the development of jet aircraft, airfoils had to evolve. At high speeds, traditional airfoils experienced problems due to compressibility and shockwaves.
                                                        Innovations like swept wings and supercritical airfoils emerged to reduce drag and improve performance in transonic and supersonic regimes. Fighter jets and aircraft like the Concorde adopted these designs to meet new speed demands.
                                                </div>

                                            </div>
                                            """, unsafe_allow_html=True)

                                            st.header("🔬 Airfoils in the Modern Era")
                                            st.markdown("""
                                                <div style="
                                                    background-color: rgba(240, 242, 246, 0.3);
                                                    padding: 30px;
                                                    border-radius: 15px;
                                                    border: 1px solid rgba(255, 255, 255, 0.3);
                                                    box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                    font-size: 24px;
                                                    line-height: 1.8;
                                                    color: white;
                                                    backdrop-filter: blur(8px);
                                                    -webkit-backdrop-filter: blur(8px);
                                                    margin-bottom: 28px;
                                                ">
                                                    <div style="font-size: 28px;">
                                                        <strong>Modern airfoil design relies heavily on computational fluid dynamics (CFD).</strong> 
                                                        Engineers now simulate airflow in virtual environments, drastically reducing the need for physical prototypes.
                                                        <br><br>
                                                        Today, airfoils are used not only in airplanes but in:
                                                        <ul style="margin-top: 12px; margin-left: 20px;">
                                                            <li>🚁 Helicopter blades</li>
                                                            <li>🌬 Wind turbines</li>
                                                            <li>🏎 Racing car spoilers</li>
                                                            <li>🌊 Submarines</li>
                                                            <li>🚀 Spacecraft</li>
                                                        </ul>
                                                        <br>
                                                        Morphing airfoils — surfaces that can change shape in flight — are now being researched for adaptive performance.
                                                    </div>
                                                </div>
                                            """, unsafe_allow_html=True)

                                            st.header("🔮 The Future of Airfoil Technology")
                                            st.markdown("""
                                                <div style="
                                                    background-color: rgba(240, 242, 246, 0.3);
                                                    padding: 30px;
                                                    border-radius: 15px;
                                                    border: 1px solid rgba(255, 255, 255, 0.3);
                                                    box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                    font-size: 24px;
                                                    line-height: 1.8;
                                                    color: white;
                                                    backdrop-filter: blur(8px);
                                                    -webkit-backdrop-filter: blur(8px);
                                                    margin-bottom: 28px;
                                                ">
                                                    <div style="font-size: 28px;">
                                                        The future of airfoil design is tied to sustainability and space exploration. 
                                                        Electric aircraft, flying taxis, reusable rockets — all demand high-performance, lightweight, and efficient wing designs.
                                                        <br><br>
                                                        Emerging areas include:
                                                        <ul style="margin-top: 12px; margin-left: 20px;">
                                                            <li><strong>AI-driven design optimization</strong></li>
                                                            <li><strong>3D-printed airfoils</strong></li>
                                                            <li><strong>Bio-inspired wings</strong></li>
                                                            <li><strong>Materials with shape memory</strong></li>
                                                        </ul>
                                                        <br>
                                                        The airfoil, though a timeless concept, continues to evolve and inspire.
                                                    </div>
                                                </div>        
                                            """, unsafe_allow_html=True)
                                            
                                            with st.expander("💡 Did You Know?"):
                                                st.markdown("""
                                                <div style="
                                                    background-color: rgba(240, 242, 246, 0.3);
                                                    padding: 30px;
                                                    border-radius: 15px;
                                                    border: 1px solid rgba(255, 255, 255, 0.3);
                                                    box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                    font-size: 24px;
                                                    line-height: 1.8;
                                                    color: white;
                                                    backdrop-filter: blur(8px);
                                                    -webkit-backdrop-filter: blur(8px);
                                                    margin-bottom: 28px;
                                                ">
                                                    <div style="font-size: 28px;">
                                                        <li> Birds naturally adjust their wing shape — inspiring modern morphing airfoils.
                                                        <li> Submarines use hydrofoils, which are underwater airfoils, to steer and stabilize.
                                                        <li> Even Formula 1 cars use upside-down airfoils to create downforce, keeping them glued to the track.
                                                    </div> 
                                                </div> 
                                                """, unsafe_allow_html=True)

                                            st.header("🧭 Conclusion")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                        From ancient kites to supersonic jets, the airfoil has been central to the human quest for flight. What began with observation of birds has become a field of science driving modern transportation and exploration.
                                                        As technology continues to evolve, the airfoil remains a symbol of creativity, curiosity, and the enduring dream to fly.
                                                </div> 
                                             </div> 
                                            """, unsafe_allow_html=True)
                                            st.success("Thank you for exploring the History of Airfoil! 🚀")
                                            
                            elif Airfoil_Section == "Types of Airfoil":
                                        st.title("🌬️ Types of Airfoil")
                                        st.write("""
                                        <div style="
                                            background-color: rgba(240, 242, 246, 0.3);
                                            padding: 30px;
                                            border-radius: 15px;
                                            border: 1px solid rgba(255, 255, 255, 0.3);
                                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                            font-size: 24px;
                                            line-height: 1.8;
                                            color: white;
                                            backdrop-filter: blur(8px);
                                            -webkit-backdrop-filter: blur(8px);
                                            margin-bottom: 28px;
                                        ">
                                            <div style="font-size: 28px;">
                                                Airfoils are special shapes used in wings to generate lift. Based on their shape and purpose, there are several types of airfoils. Let’s look at the most common ones:
                                            </div>
                                        </div>
                                        """, unsafe_allow_html=True)

                                        st.header("1. Symmetrical Airfoil")
                                        st.write("""
                                        <div style="
                                            background-color: rgba(240, 242, 246, 0.3);
                                            padding: 30px;
                                            border-radius: 15px;
                                            border: 1px solid rgba(255, 255, 255, 0.3);
                                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                            font-size: 24px;
                                            line-height: 1.8;
                                            color: white;
                                            backdrop-filter: blur(8px);
                                            -webkit-backdrop-filter: blur(8px);
                                            margin-bottom: 28px;
                                        ">
                                            <div style="font-size: 28px;">
                                                <li> Same shape on top and bottom  
                                                <li> Stable and used in aerobatic aircraft  
                                                <li> No lift at zero angle of attack
                                            </div>
                                        </div>
                                        """, unsafe_allow_html=True)

                                        st.header("2. Cambered Airfoil")
                                        st.write("""
                                        <div style="
                                            background-color: rgba(240, 242, 246, 0.3);
                                            padding: 30px;
                                            border-radius: 15px;
                                            border: 1px solid rgba(255, 255, 255, 0.3);
                                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                            font-size: 24px;
                                            line-height: 1.8;
                                            color: white;
                                            backdrop-filter: blur(8px);
                                            -webkit-backdrop-filter: blur(8px);
                                            margin-bottom: 28px;
                                        ">
                                            <div style="font-size: 28px;">
                                                <li> Curved upper surface, flatter lower surface  
                                                <li> Produces lift at zero angle  
                                                <li> Common in passenger and small aircraft
                                            </div>
                                        </div>
                                        """, unsafe_allow_html=True)

                                        st.header("3. Thin Airfoil")
                                        st.write("""
                                        <div style="
                                            background-color: rgba(240, 242, 246, 0.3);
                                            padding: 30px;
                                            border-radius: 15px;
                                            border: 1px solid rgba(255, 255, 255, 0.3);
                                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                            font-size: 24px;
                                            line-height: 1.8;
                                            color: white;
                                            backdrop-filter: blur(8px);
                                            -webkit-backdrop-filter: blur(8px);
                                            margin-bottom: 28px;
                                        ">
                                            <div style="font-size: 28px;">
                                                <li> Very thin profile  
                                                <li> Low drag, suitable for high speeds  
                                                <li> Used in supersonic jets and missiles
                                            </div>
                                        </div>
                                        """, unsafe_allow_html=True)

                                        st.header("4. Supercritical Airfoil")
                                        st.write("""
                                        <div style="
                                            background-color: rgba(240, 242, 246, 0.3);
                                            padding: 30px;
                                            border-radius: 15px;
                                            border: 1px solid rgba(255, 255, 255, 0.3);
                                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                            font-size: 24px;
                                            line-height: 1.8;
                                            color: white;
                                            backdrop-filter: blur(8px);
                                            -webkit-backdrop-filter: blur(8px);
                                            margin-bottom: 28px;
                                        ">
                                            <div style="font-size: 28px;">
                                                <li> Flat upper surface, thick lower surface  
                                                <li> Delays shock waves in transonic flight  
                                                <li> Used in modern jetliners
                                            </div>
                                        </div>
                                        """, unsafe_allow_html=True)

                                        st.header("5. Laminar Flow Airfoil")
                                        st.write("""
                                        <div style="
                                            background-color: rgba(240, 242, 246, 0.3);
                                            padding: 30px;
                                            border-radius: 15px;
                                            border: 1px solid rgba(255, 255, 255, 0.3);
                                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                            font-size: 24px;
                                            line-height: 1.8;
                                            color: white;
                                            backdrop-filter: blur(8px);
                                            -webkit-backdrop-filter: blur(8px);
                                            margin-bottom: 28px;
                                        ">
                                            <div style="font-size: 28px;">
                                                <li> Smooth shape to reduce air friction  
                                                <li> Saves fuel by reducing drag  
                                                <li> Found in light and experimental aircraft
                                            </div>
                                        </div>
                                        """, unsafe_allow_html=True)

                                        st.header("6. Reflexed Airfoil")
                                        st.write("""
                                        <div style="
                                            background-color: rgba(240, 242, 246, 0.3);
                                            padding: 30px;
                                            border-radius: 15px;
                                            border: 1px solid rgba(255, 255, 255, 0.3);
                                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                            font-size: 24px;
                                            line-height: 1.8;
                                            color: white;
                                            backdrop-filter: blur(8px);
                                            -webkit-backdrop-filter: blur(8px);
                                            margin-bottom: 28px;
                                        ">
                                            <div style="font-size: 28px;">
                                                <li> Trailing edge bends upward  
                                                <li> Helps in tailless aircraft  
                                                <li> Used in flying wings and drones
                                            </div>
                                        </div>
                                        """, unsafe_allow_html=True)

                                        st.subheader("🛩️ Summary")
                                        st.write("""
                                        <div style="
                                            background-color: rgba(240, 242, 246, 0.3);
                                            padding: 30px;
                                            border-radius: 15px;
                                            border: 1px solid rgba(255, 255, 255, 0.3);
                                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                            font-size: 24px;
                                            line-height: 1.8;
                                            color: white;
                                            backdrop-filter: blur(8px);
                                            -webkit-backdrop-filter: blur(8px);
                                            margin-bottom: 28px;
                                        ">
                                            <div style="font-size: 28px;">
                                                Each airfoil type is designed for a specific purpose — from slow, stable flight to high-speed performance. Choosing the right airfoil depends on the aircraft’s mission.
                                            </div>
                                        </div>
                                        """, unsafe_allow_html=True)

                                        st.write("🚀 More features like interactive airfoil simulators are coming soon!")

                            elif Airfoil_Section == "Airfoil Calculation":
                                Airfoil_Calculation= st.sidebar.radio("Select Options", ["Airfoil Plotter", "Airfoil Calculation option"])
                                if Airfoil_Calculation=="Airfoil Plotter":
                                        st.title("NACA Airfoil Generator")
                                        # Fixing the selectbox syntax
                                        Airfoil_Plotter = st.selectbox("Select Airfoil Series", ["NACA 4-Series", "NACA 5-Series","NACA 6-Series","NACA 7-Series"])
                                        
                                        def naca4(m, p, t, num_points=100):
                                            x = np.linspace(0, 1, num_points)
                                            yt = (t / 0.2) * (0.2969 * np.sqrt(x) - 0.1260 * x - 0.3516 * x**2 + 0.2843 * x**3 - 0.1015 * x**4)
                                            yc = np.where(x < p, (m / p**2) * (2 * p * x - x**2), (m / (1 - p)**2) * ((1 - 2 * p) + 2 * p * x - x**2))
                                            dyc_dx = np.where(x < p, (2 * m / p**2) * (p - x), (2 * m / (1 - p)**2) * (p - x))
                                            theta = np.arctan(dyc_dx)
                                            xu, yu = x - yt * np.sin(theta), yc + yt * np.cos(theta)
                                            xl, yl = x + yt * np.sin(theta), yc - yt * np.cos(theta)
                                            return xu, yu, xl, yl

                                        def naca5(l, p, t, num_points=100):
                                            x = np.linspace(0, 1, num_points)
                                            m = l / 6  
                                            yc = np.where(x < p, (m / p**2) * (2 * p * x - x**2), (m / (1 - p)**2) * ((1 - 2 * p) + 2 * p * x - x**2))
                                            dyc_dx = np.where(x < p, (2 * m / p**2) * (p - x), (2 * m / (1 - p)**2) * (p - x))
                                            theta = np.arctan(dyc_dx)
                                            yt = (t / 0.2) * (0.2969 * np.sqrt(x) - 0.1260 * x - 0.3516 * x**2 + 0.2843 * x**3 - 0.1015 * x**4)
                                            xu = x - yt * np.sin(theta)
                                            yu = yc + yt * np.cos(theta)
                                            xl = x + yt * np.sin(theta)
                                            yl = yc - yt * np.cos(theta)
                                            return xu, yu, xl, yl

                                        def naca6_series(Cl, t, num_points=100):
                                            x = np.linspace(0, 1, num_points)
                                            m = Cl / 0.9  
                                             
                                            yc = np.where(x < p, (m / p**2) * (2 * p * x - x**2), (m / (1 - p)**2) * ((1 - 2 * p) + 2 * p * x - x**2))
                                            dyc_dx = np.where(x < p, (2 * m / p**2) * (p - x), (2 * m / (1 - p)**2) * (p - x))
                                            theta = np.arctan(dyc_dx)
                                            yt = (t / 0.2) * (0.2969 * np.sqrt(x) - 0.1260 * x - 0.3516 * x**2 + 0.2843 * x**3 - 0.1015 * x**4)
                                            xu = x - yt * np.sin(theta)
                                            yu = yc + yt * np.cos(theta)
                                            xl = x + yt * np.sin(theta)
                                            yl = yc - yt * np.cos(theta)
                                            return xu, yu, xl, yl

                                        def naca7_series(Cl, t, num_points=100):
                                            x = np.linspace(0, 1, num_points)
                                            m = Cl / 0.8  
                                            p = 0.5  
                                            yc = np.where(x < p, (m / p**2) * (2 * p * x - x**2), (m / (1 - p)**2) * ((1 - 2 * p) + 2 * p * x - x**2))
                                            dyc_dx = np.where(x < p, (2 * m / p**2) * (p - x), (2 * m / (1 - p)**2) * (p - x))
                                            theta = np.arctan(dyc_dx)
                                            yt = (t / 0.2) * (0.2969 * np.sqrt(x) - 0.1260 * x - 0.3516 * x**2 + 0.2843 * x**3 - 0.1015 * x**4)
                                            xu = x - yt * np.sin(theta)
                                            yu = yc + yt * np.cos(theta)
                                            xl = x + yt * np.sin(theta)
                                            yl = yc - yt * np.cos(theta)
                                            return xu, yu, xl, yl

                                        def plot_airfoil(series, m=0, l=0, Cl=0, p=0, t=0):
                                            fig, ax = plt.subplots()
                                            
                                            if series == "NACA 4-Series":
                                                xu, yu, xl, yl = naca4(m, p, t)
                                                
                                            elif series == "NACA 5-Series":
                                                xu, yu, xl, yl = naca5(l, p, t)
                                                
                                            elif series == "NACA 6-Series":     
                                                 xu, yu, xl, yl = naca6_series(Cl, t)

                                            elif series == "NACA 7-Series":
                                                 xu, yu, xl, yl = naca6_series(Cl, t)
                                                 
                                            else:
                                                return
                                            
                                            ax.plot(xu, yu, 'r', label="Upper Surface")
                                            ax.plot(xl, yl, 'b', label="Lower Surface")
                                            ax.set_xlabel("x")
                                            ax.set_ylabel("y")
                                            ax.set_title(series)
                                            ax.axis("equal")
                                            ax.legend()
                                            ax.grid()
                                            return fig

                                        # User inputs based on selected airfoil series
                                        if Airfoil_Plotter  == "NACA 4-Series":
                                            m = st.number_input("Maximum Camber (m) (100th of chord)", min_value=0.0, max_value=1.0, value=0.02)
                                            p = st.number_input("Position of Maximum Camber (p)", min_value=0.0, max_value=1.0, value=0.4)
                                            t = st.number_input("Maximum Thickness (t)", min_value=0.0, max_value=1.0, value=0.12)
                                            l = 0  # Not needed for NACA 4-series
                                            Cl= 0  # Not needed for NACA 4-series
                                            
                                        elif Airfoil_Plotter  == "NACA 5-Series":
                                            l = st.number_input("Lifting parameter (l)", min_value=0.0, max_value=1.0, value=0.3)
                                            p = st.number_input("Position of Maximum Camber (p)", min_value=0.0, max_value=1.0, value=0.4)
                                            t = st.number_input("Maximum Thickness (t)", min_value=0.0, max_value=1.0, value=0.12)
                                            m = 0  # Not needed for NACA 5-series
                                            Cl= 0  # Not needed for NACA 5-series
                                            
                                        elif Airfoil_Plotter  == "NACA 6-Series":
                                             l = 0   # Not needed for NACA 6-series
                                             m = 0   # Not needed for NACA 6-series
                                             p = 0.4 # for NACA 6-series
                                             Cl = st.number_input("Maximum Camber (m) (100th of chord)")
                                             t = st.number_input("Maximum Thickness (t)")

                                        elif Airfoil_Plotter  == "NACA 7-Series":
                                             l = 0   # Not needed for NACA 7-series
                                             m = 0   # Not needed for NACA 7-series
                                             p = 0.5 # for NACA 7-series
                                             Cl = st.number_input("Maximum Camber (m) (100th of chord)")
                                             t = st.number_input("Maximum Thickness (t)")

                                        # Generate airfoil button
                                        if st.button("Generate Airfoil"):
                                            fig = plot_airfoil(Airfoil_Plotter , m, l,Cl, p, t)
                                            st.pyplot(fig)
                                    
                                elif Airfoil_Calculation=="Airfoil Calculation option":
                                            Airfoil_Calculation_option= st.sidebar.radio("Select Options", ["For Incompressible Flow", "For compressible Flow"])

                                            if Airfoil_Calculation_option=="For Incompressible Flow":
                                                    # Title and description
                                                    st.title("Lift and Drag Calculator (Ony for incompessible flow)")

                                                    # Input fields
                                                    D_manometer = st.number_input("Density of manometer fluid (kg/m³)", value=1000.0)
                                                    delta_h = st.number_input("Height difference of manometer (m)", value=0.5)
                                                    D_Air = st.number_input("Air density (kg/m³)", value=1.225)
                                                    V_free = st.number_input("Free stream velocity (m/s)", value=50.0)
                                                    P_free = st.number_input("Free stream pressure (Pa)", value=101325.0)
                                                    S = st.number_input("Surface Area (S)", value=1.0)
                                                    AR = st.number_input("Aspect Ratio (AR)", value=6.0)
                                                    zero_lift_Aoa = st.number_input("Zero Lift AOA (deg)", value=0.0)
                                                    Aoa_alpha = st.number_input("Angle of Attack (deg)", value=5.0)
                                                    Cd0 = st.number_input("Zero Lift Drag Coefficient Cd0", value=0.02)
                                                    initial_ao = st.number_input("Initial Slope", value=0.1)

                                                    if st.button("Calculate"):
                                                        g = 9.8
                                                        pi = 22 / 7
                                                        e = 0.95

                                                        V2 = (((D_manometer * g * delta_h) + (0.5 * D_Air * V_free**2)) * (2 / D_Air)) ** 0.5
                                                        P2 = P_free - D_manometer * g * delta_h
                                                        Po = P_free + 0.5 * D_Air * V_free**2
                                                        Cp = 1 - (V2 / V_free) ** 2
                                                        a = initial_ao / (1 + (initial_ao / (pi * e * AR)))
                                                        Cl = a * (Aoa_alpha - zero_lift_Aoa)
                                                        L = ((P_free - P2) * S * Cl) / Cp
                                                        Cd = Cd0 + (Cl ** 2) / (pi * e * AR)
                                                        D = 0.5 * D_Air * V_free**2 * Cd

                                                        st.subheader("Results")
                                                        st.success(f"**V2**: {V2:.2f} m/s")
                                                        st.success(f"**P2**: {P2:.2f} Pa")
                                                        st.success(f"**Po**: {Po:.2f} Pa")
                                                        st.success(f"**Cp**: {Cp:.4f}")
                                                        st.success(f"**Cl**: {Cl:.4f}")
                                                        st.success(f"**Lift (L)**: {L:.4f} N")
                                                        st.success(f"**Drag (D)**: {D:.4f} N")
                                                        
                                            elif Airfoil_Calculation_option=="For compressible Flow":
                                                    # Constants
                                                    gamma = 1.4  # Ratio of specific heats
                                                    R = 287.05   # Specific gas constant for air (J/kg·K)
                                                    st.title("Aerodynamics Pressure Calculator (Ony for compessible flow)")
                                                    # Input fields
                                                    free_stream_pressure = st.number_input("Enter the free stream pressure (Pa):", value=101325.0)
                                                    free_stream_Density = st.number_input("Enter the free stream Density (kg/m³):", value=1.225)
                                                    free_stream_Velocity = st.number_input("Enter the free stream Velocity (m/s):", value=340.0)
                                                    pressure_at_point = st.number_input("Enter the Pressure at point A (Pa):", value=90000.0)

                                                    # Calculate only when all inputs are valid
                                                    if free_stream_Density > 0 and pressure_at_point > 0:
                                                        # Calculations
                                                        free_stream_Temperature = free_stream_pressure / (free_stream_Density * R)
                                                        free_stream_Mach_number = free_stream_Velocity / ((gamma * R * free_stream_Temperature) ** 0.5)
                                                        stagnation_temperature = free_stream_Temperature * (1 + ((gamma - 1)/2) * free_stream_Mach_number**2)
                                                        stagnation_pressure = free_stream_pressure * ((1 + ((gamma - 1)/2) * free_stream_Mach_number**2) ** (gamma / (gamma - 1)))
                                                        Mach_number_at_point = ((((stagnation_pressure / pressure_at_point) ** ((gamma - 1)/gamma)) - 1) * 2 / (gamma - 1))**0.5
                                                        T_A = stagnation_temperature / (1 + ((gamma - 1)/2) * Mach_number_at_point**2)
                                                        a_A = (gamma * R * T_A)**0.5
                                                        V_A = a_A * Mach_number_at_point

                                                        # Output
                                                        st.subheader("Results:")
                                                        st.success(f"**Free Stream Temperature:** {free_stream_Temperature:.2f} K")
                                                        st.success(f"**Free Stream Mach Number:** {free_stream_Mach_number:.3f}")
                                                        st.success(f"**Stagnation Temperature:** {stagnation_temperature:.2f} K")
                                                        st.success(f"**Stagnation Pressure:** {stagnation_pressure:.2f} Pa")
                                                        st.success(f"**Mach Number at Point A:** {Mach_number_at_point:.3f}")
                                                        st.success(f"**Temperature at Point A:** {T_A:.2f} K")
                                                        st.success(f"**Speed of Sound at A:** {a_A:.2f} m/s")
                                                        st.success(f"**Velocity at Point A:** {V_A:.2f} m/s")
                                                    else:
                                                        st.warning("Please enter valid (non-zero) values for density and pressure at point A.")
                elif design_area == "Aerodynamic Section":
                     Aerodynamic_Section = st.sidebar.radio("Select Options", ["Earth Atmosphere","Wind Tunnel"])
                     if Aerodynamic_Section  == "Earth Atmosphere":   
                        def Earth_Atmosphere(image_path):
                                    try:
                                        base64_str = get_base64(image_path)
                                        st.markdown(
                                            f"""
                                            <style>
                                            .stApp {{
                                                background-image: url("data:image/png;base64,{base64_str}");
                                                background-size: cover;
                                                background-position: fit;
                                                background-attachment: fixed;
                                            }}
                                            </style>
                                            """,
                                            unsafe_allow_html=True
                                        )
                                    except FileNotFoundError:
                                        st.error("Background image not found. Please check the file path.")
                        # ✅ Set background image (Make sure the path is correct)
                        Earth_Atmosphere("photo-1534294228306-bd54eb9a7ba8.jpg")
                        st.sidebar.write("## Earth Atmosphere")  
                        Earth_Atmosphere= st.sidebar.radio("Select Options",["History of Earth Atmosphere ", "Types of Earth Atmosphere Layer","Earth Atmosphere Pressure Density and Temperature Calculation"])

                        if  Earth_Atmosphere == "History of Earth Atmosphere ":  
                                    st.title("History of Earth Atmosphere ")
                                    # Title
                                    st.title("🌍 History of Earth's Atmosphere")
                                    # Introduction
                                    st.markdown("""
                                    <div style="
                                        background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        font-size: 24px;
                                        line-height: 1.8;
                                        color: white;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;
                                    ">
                                        <div style="font-size: 28px;">
                                            The Earth's atmosphere has undergone dramatic changes over billions of years, evolving from a toxic cloud of gases into the life-supporting air we breathe today.
                                            This journey is a fascinating story of volcanic eruptions, biological revolutions, and climate shifts.
                                        </div>
                                    </div>
                                    """, unsafe_allow_html=True)

                                    # Stage 1
                                    st.header("🪨 Stage 1: Primordial Atmosphere (~4.6 Billion Years Ago)")
                                    st.markdown("""
                                    <div style="
                                        background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        font-size: 24px;
                                        line-height: 1.8;
                                        color: white;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;
                                    ">
                                        <div style="font-size: 28px;">
                                            <li> Origin: Formed from the solar nebula during Earth's formation.  
                                            <li> Composition: Hydrogen (H₂), Helium (He), traces of methane and ammonia.  
                                            <li> Fate: Escaped due to weak gravity and intense solar wind.
                                        </div>
                                    </div>
                                    """, unsafe_allow_html=True)

                                    # Stage 2
                                    st.header("🌋 Stage 2: Secondary Atmosphere (~4.5 - 3.8 Billion Years Ago)")
                                    st.markdown("""
                                    <div style="
                                        background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        font-size: 24px;
                                        line-height: 1.8;
                                        color: white;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;
                                    ">
                                        <div style="font-size: 28px;">
                                            <li> Formed by: Volcanic outgassing.  
                                            <li> Main Gases: CO₂, H₂O vapor, N₂, SO₂ —still no oxygen!  
                                            <li> Water Forms: Cooling leads to ocean formation from condensed vapor.
                                       </div>
                                    </div>
                                    """, unsafe_allow_html=True)

                                    # Stage 3
                                    st.header("🌊 Stage 3: Origin of Life & Great Oxygenation (~3.5 - 2.4 Billion Years Ago)")
                                    st.markdown("""
                                    <div style="
                                        background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        font-size: 24px;
                                        line-height: 1.8;
                                        color: white;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;
                                    ">
                                        <div style="font-size: 28px;">
                                           <li> Life Appears: Simple, anaerobic microorganisms in oceans.  
                                           <li> Photosynthesis Begins: Cyanobacteria release O₂.  
                                           <li> The Great Oxygenation Event:  
                                              <li> Massive increase in oxygen.  
                                              <li> Many early organisms went extinct.  
                                              <li> Iron in oceans oxidized, forming banded iron layers.
                                       </div>
                                    </div>
                                    """, unsafe_allow_html=True)

                                    # Stage 4
                                    st.header("❄️ Stage 4: Proterozoic & Ice Ages (~2.4 - 0.5 Billion Years Ago)")
                                    st.markdown("""
                                    <div style="
                                        background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        font-size: 24px;
                                        line-height: 1.8;
                                        color: white;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;
                                    ">
                                        <div style="font-size: 28px;">
                                            <li> O₂ Rises Slowly: Leading to ozone (O₃) layer formation.  
                                            <li> Snowball Earth Events: Planet-wide ice ages due to atmospheric shifts and solar cycles.
                                       </div>
                                    </div>
                                    """, unsafe_allow_html=True)

                                    # Stage 5
                                    st.header("🐚 Stage 5: Phanerozoic Atmosphere (~541 Million Years Ago - Present)")
                                    st.markdown("""
                                    <div style="
                                        background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        font-size: 24px;
                                        line-height: 1.8;
                                        color: white;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;
                                    ">
                                        <div style="font-size: 28px;">
                                            <li> Oxygen Boom: Supports large, complex animals.  
                                            <li> Land Plants Emerge: Help regulate CO₂ and boost oxygen.  
                                            <li> Fluctuations:  
                                              <li> O₂ peaked ~35% during Carboniferous.  
                                              <li> Volcanism and extinctions altered gas levels.
                                       </div>
                                    </div>
                                    """, unsafe_allow_html=True)

                                    # Stage 6
                                    st.header("🏭 Stage 6: The Modern Atmosphere")
                                    st.markdown("""
                                    <div style="
                                        background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        font-size: 24px;
                                        line-height: 1.8;
                                        color: white;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;
                                    ">
                                        <div style="font-size: 28px;">
                                            <li>Current Composition:  
                                                  <li> Nitrogen (N₂): ~78%  
                                                  <li> Oxygen (O₂): ~21%  
                                                  <li> Argon (Ar): ~0.93%  
                                                  <li> Carbon Dioxide (CO₂): ~0.04%  
                                            <li> Human Impact:  
                                                  <li> Fossil fuels increase CO₂  
                                                  <li> Global warming and climate change accelerate atmospheric changes
                                       </div>
                                    </div>
                                    """, unsafe_allow_html=True)

                                    # Conclusion
                                    st.header("✅ Conclusion")
                                    st.markdown("""
                                    <div style="
                                        background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        font-size: 24px;
                                        line-height: 1.8;
                                        color: white;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;
                                    ">
                                        <div style="font-size: 28px;">
                                            The atmosphere has changed from a harsh, uninhabitable layer to a delicate and dynamic system that sustains life.
                                            Its history reminds us of our planet's resilience — and the importance of protecting its future.
                                       </div>
                                    </div>
                                    """, unsafe_allow_html=True)

                        elif  Earth_Atmosphere== "Types of Earth Atmosphere Layer":
                            
                                        # Title
                                        st.title("🌍 Types of Earth's Atmospheric Layers")
                                        # Intro
                                        st.markdown("""
                                        <div style="
                                            background-color: rgba(240, 242, 246, 0.3);
                                            padding: 30px;
                                            border-radius: 15px;
                                            border: 1px solid rgba(255, 255, 255, 0.3);
                                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                            font-size: 24px;
                                            line-height: 1.8;
                                            color: white;
                                            backdrop-filter: blur(8px);
                                            -webkit-backdrop-filter: blur(8px);
                                            margin-bottom: 28px;
                                        ">
                                            <div style="font-size: 28px;">
                                                The Earth's atmosphere is divided into five main layers, each with distinct features that affect weather, climate, communication, and space travel.
                                                Let's explore them from the surface upward.
                                              </div>
                                        </div>
                                        """, unsafe_allow_html=True)

                                        # Troposphere
                                        st.header("🏞️ 1. Troposphere (0–12 km)")
                                        st.markdown("""
                                        <div style="
                                            background-color: rgba(240, 242, 246, 0.3);
                                            padding: 30px;
                                            border-radius: 15px;
                                            border: 1px solid rgba(255, 255, 255, 0.3);
                                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                            font-size: 24px;
                                            line-height: 1.8;
                                            color: white;
                                            backdrop-filter: blur(8px);
                                            -webkit-backdrop-filter: blur(8px);
                                            margin-bottom: 28px;
                                        ">
                                            <div style="font-size: 28px;">
                                                <li> Closest to Earth's surface — where all life exists.  
                                                <li> Contains ~75% of atmospheric mass and most weather activity (clouds, rain, storms).  
                                                <li> Temperature decreases with altitude (~6.5°C per km).  
                                                <li> Top boundary: Tropopause  
                                                - ✈️ Fun Fact: Commercial jets fly at the upper edge of this layer.
                                            </div>
                                        </div>
                                        """, unsafe_allow_html=True)

                                        # Stratosphere
                                        st.header("🌤️ 2. Stratosphere (12–50 km)")
                                        st.markdown("""
                                        <div style="
                                            background-color: rgba(240, 242, 246, 0.3);
                                            padding: 30px;
                                            border-radius: 15px;
                                            border: 1px solid rgba(255, 255, 255, 0.3);
                                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                            font-size: 24px;
                                            line-height: 1.8;
                                            color: white;
                                            backdrop-filter: blur(8px);
                                            -webkit-backdrop-filter: blur(8px);
                                            margin-bottom: 28px;
                                        ">
                                            <div style="font-size: 28px;">
                                                <li> Above the troposphere; stable and layered air.  
                                                <li> Contains the ozone layer, which absorbs UV rays.  
                                                <li> Temperature increases with height due to ozone activity.  
                                                <li> Top boundary: Stratopause 
                                                <li> 🎈 Used by: Weather balloons, high-altitude aircraft.
                                            </div>
                                        </div>
                                        """, unsafe_allow_html=True)

                                        # Mesosphere
                                        st.header("☄️ 3. Mesosphere (50–85 km)")
                                        st.markdown("""
                                        <div style="
                                            background-color: rgba(240, 242, 246, 0.3);
                                            padding: 30px;
                                            border-radius: 15px;
                                            border: 1px solid rgba(255, 255, 255, 0.3);
                                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                            font-size: 24px;
                                            line-height: 1.8;
                                            color: white;
                                            backdrop-filter: blur(8px);
                                            -webkit-backdrop-filter: blur(8px);
                                            margin-bottom: 28px;
                                        ">
                                            <div style="font-size: 28px;">
                                                <li> Coldest layer (down to -90°C).  
                                                <li> Temperature drops with altitude.  
                                                <li> Burns up meteors — visible as shooting stars.  
                                                <li> Top boundary: Mesopause  
                                                <li> 🔬 Least explored due to access difficulty.
                                            </div>
                                        </div>
                                        """, unsafe_allow_html=True)

                                        # Thermosphere
                                        st.header("🌐 4. Thermosphere (85–600+ km)")
                                        st.markdown("""
                                        <div style="
                                            background-color: rgba(240, 242, 246, 0.3);
                                            padding: 30px;
                                            border-radius: 15px;
                                            border: 1px solid rgba(255, 255, 255, 0.3);
                                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                            font-size: 24px;
                                            line-height: 1.8;
                                            color: white;
                                            backdrop-filter: blur(8px);
                                            -webkit-backdrop-filter: blur(8px);
                                            margin-bottom: 28px;
                                        ">
                                            <div style="font-size: 28px;">
                                                <li> Extremely thin air; temperature rises sharply(up to 2000°C+).  
                                                <li> Home to auroras, satellites, and the ISS.  
                                                <li>Contains ionized gases vital for radio communication.  
                                                <li> 🛰 Satellites orbit in this layer.
                                            </div>
                                        </div>
                                        """, unsafe_allow_html=True)

                                        # Exosphere
                                        st.header("🚀 5. Exosphere (600–10,000 km)")
                                        st.markdown("""
                                        <div style="
                                            background-color: rgba(240, 242, 246, 0.3);
                                            padding: 30px;
                                            border-radius: 15px;
                                            border: 1px solid rgba(255, 255, 255, 0.3);
                                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                            font-size: 24px;
                                            line-height: 1.8;
                                            color: white;
                                            backdrop-filter: blur(8px);
                                            -webkit-backdrop-filter: blur(8px);
                                            margin-bottom: 28px;
                                        ">
                                            <div style="font-size: 28px;">
                                                <li> Outermost layer, gradually blending into space.  
                                                <li> Composed of hydrogen and helium atoms.  
                                                <li> Very thin — nearly a vacuum.  
                                                <li> 🛰 Some satellites orbit here with minimal drag.
                                            </div>
                                        </div>
                                        """, unsafe_allow_html=True)

                                        # Title
                                        st.title("🌍 Types of Earth's Atmospheric Layers")

                                        # Intro
                                        st.markdown("""
                                        The Earth's atmosphere is divided into five main layers, each with distinct features that affect weather, climate, communication, and space travel.
                                        Let's explore them from the surface upward.
                                        """)

                                        # Adding custom table with styling using HTML
                                        st.header("📊 Summary Table")
                                        st.markdown("""
                                        <div style="
                                            background-color: rgba(240, 242, 246, 0.3);
                                            padding: 30px;
                                            border-radius: 15px;
                                            border: 1px solid rgba(255, 255, 255, 0.3);
                                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                            font-size: 24px;
                                            line-height: 1.8;
                                            color: white;
                                            backdrop-filter: blur(8px);
                                            -webkit-backdrop-filter: blur(8px);
                                            margin-bottom: 28px;
                                        ">
                                            <table style="width:100%; font-size: 18px; border-collapse: collapse;">
                                                <tr>
                                                    <th style="border: 1px solid #ddd; padding: 8px; background-color: rgba(60, 60, 60, 0.7); color: white;">Layer</th>
                                                    <th style="border: 1px solid #ddd; padding: 8px; background-color: rgba(60, 60, 60, 0.7); color: white;">Altitude Range</th>
                                                    <th style="border: 1px solid #ddd; padding: 8px; background-color: rgba(60, 60, 60, 0.7); color: white;">Temp Trend</th>
                                                    <th style="border: 1px solid #ddd; padding: 8px; background-color: rgba(60, 60, 60, 0.7); color: white;">Key Features</th>
                                                </tr>
                                                <tr>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">Troposphere</td>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">0–12 km</td>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">↓ Decrease</td>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">Weather, life, airplanes</td>
                                                </tr>
                                                <tr>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">Stratosphere</td>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">12–50 km</td>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">↑ Increase</td>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">Ozone layer, jet stream</td>
                                                </tr>
                                                <tr>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">Mesosphere</td>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">50–85 km</td>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">↓ Decrease</td>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">Meteors burn, coldest layer</td>
                                                </tr>
                                                <tr>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">Thermosphere</td>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">85–600+ km</td>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">↑ Increase</td>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">Auroras, ISS, ionosphere</td>
                                                </tr>
                                                <tr>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">Exosphere</td>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">600–10,000 km</td>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">—</td>
                                                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">Space transition, satellite orbits</td>
                                                </tr>
                                            </table>
                                        </div>
                                        """, unsafe_allow_html=True)

                                        # Conclusion
                                        st.header("✅ Conclusion")
                                        st.markdown("""
                                        <div style="
                                            background-color: rgba(240, 242, 246, 0.3);
                                            padding: 30px;
                                            border-radius: 15px;
                                            border: 1px solid rgba(255, 255, 255, 0.3);
                                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                            font-size: 24px;
                                            line-height: 1.8;
                                            color: white;
                                            backdrop-filter: blur(8px);
                                            -webkit-backdrop-filter: blur(8px);
                                            margin-bottom: 28px;
                                        ">
                                            <div style="font-size: 28px;">
                                                Each layer of the Earth's atmosphere serves a unique purpose — from shielding us from harmful radiation to enabling space exploration and communication.
                                                Understanding these layers helps us appreciate how Earth protects and supports life.
                                            </div>
                                        </div>
                                        """, unsafe_allow_html=True)

                        elif  Earth_Atmosphere == "Earth Atmosphere Pressure Density and Temperature Calculation":
                            
                                            st.title("Atmosphere Properties Calculator")
                                            st.write("Details about of Pressure Density and Temperature")
                                            
                                            def atmosphere_properties(altitude):
                                                g = 9.80665  # Gravity (m/s^2)
                                                R = 287.05   # Specific gas constant for air (J/kgK)
                                                
                                                T0 = 288.16  # Temperature at sea level (K)
                                                P0 = 1.01325e5  # Pressure at sea level (Pa)
                                                D0 = 1.225  # Density at sea level (kg/m^3)
                                                
                                                if altitude == 0:
                                                    return T0, P0, D0
                                                
                                                elif 0 < altitude < 12000:
                                                    a = -6.5e-3
                                                    T = T0 + a * altitude
                                                    P = P0 * (T / T0) ** (-g / (a * R))
                                                    D = D0 * (T / T0) ** (-((g / (a * R)) + 1))
                                                    
                                                elif 11000 < altitude <= 25000:
                                                    H_initial = 11000
                                                    P_initial = 22633.06             
                                                    D_initial = 0.3639 
                                                    T = 216.66 
                                                    P = P_initial * math.exp((-g / (R * T)) * (altitude - H_initial))
                                                    D = D_initial * math.exp((-g / (R * T)) * (altitude - H_initial))
                                                    
                                                elif 25000 < altitude <= 47000:
                                                    a = 3e-3
                                                    H_initial = 25000
                                                    T_initial = 216.66 
                                                    P_initial = 2488.93             
                                                    D_initial = 0.0400
                                                    T = T_initial + a * (altitude - H_initial)
                                                    P = P0 * (T / T_initial) ** (-g / (a * R))
                                                    D = D0 * (T / T_initial) ** (-((g / (a * R)) + 1))

                                                 
                                                elif 47000 < altitude <= 53000:  # Stratopause
                                                    H_initial=47000
                                                    P_initial=4904.37              
                                                    D_initial= 0.0454 
                                                    T=282.66 # Constant temperature in tropopause (K)
                                                    P =  P_initial * math.exp((-g / (R * T)) * (altitude - H_initial))
                                                    D =D_initial* math.exp((-g / (R * T)) * (altitude - H_initial))

                                                elif 53000 < altitude <= 79000:
                                                    a = -4.5e-3  # Temperature lapse rate (K/m)
                                                    H_initial=53000 
                                                    T_initial=282.66 
                                                    P_initial=2374.86           
                                                    D_initial= 0.0220
                                                    T = T_initial + a * (altitude - H_initial)
                                                    P = P0 * (T / T_initial) ** (-g / (a * R))
                                                    D = D0 * (T / T_initial) ** (-((g / (a * R)) + 1))

                                                elif 79000< altitude <= 90000:
                                                    H_initial=79000
                                                    P_initial=1754.05             
                                                    D_initial= 0.0362  
                                                    T=165.66  # Constant temperature in tropopause (K)
                                                    P =  P_initial * math.exp((-g / (R * T)) * (altitude - H_initial))
                                                    D =D_initial* math.exp((-g / (R * T)) * (altitude - H_initial))

                                                elif 90000< altitude <= 105000:
                                                    a = 4e-3  # Temperature lapse rate (K/m)
                                                    H_initial=90000
                                                    T_initial=165.66 
                                                    P_initial=181.49         
                                                    D_initial= 0.0037
                                                    T = T_initial + a * (altitude - H_initial)
                                                    P = P0 * (T / T_initial) ** (-g / (a * R))
                                                    D = D0 * (T / T_initial) ** (-((g / (a * R)) + 1))    
                                                    
                                                else:
                                                    return "Altitude out of range", "-", "-"
                                                
                                                return round(T, 2), round(P, 2), round(D, 4)

                                            altitude = st.number_input("Enter Cruise Altitude (m):", min_value=0.0, step=100.0)
                                            if st.button("Calculate"):
                                                T, P, D = atmosphere_properties(altitude)
                                                st.success(f"**Temperature:** {T} K")
                                                st.success(f"**Pressure:** {P} Pa")
                                                st.success(f"**Density:** {D} kg/m³")
                                                                                        
                     elif Aerodynamic_Section == "Wind Tunnel":                
                                def wind_tunnel(image_path):
                                    try:
                                        base64_str = get_base64(image_path)
                                        st.markdown(
                                            f"""
                                            <style>
                                            .stApp {{
                                                background-image: url("data:image/png;base64,{base64_str}");
                                                background-size: cover;
                                                background-position: center;
                                                background-attachment: fixed;
                                            }}
                                            </style>
                                            """,
                                            unsafe_allow_html=True
                                        )
                                    except FileNotFoundError:
                                        st.error("Background image not found. Please check the file path.")
                                # ✅ Set background image (Make sure the path is correct)
                                wind_tunnel("MD-11_12ft_Wind_Tunnel_Test.jpg")
                                st.sidebar.write("## Wind Tunnel")  
                                wind_tunnel_option = st.sidebar.radio("Select Options", ["History of Wind Tunnel", "Types of Wind Tunnel", 
                                                                       "Low Subsonic Incompressible Wind Tunnel Design Calculation", 
                                                                        "Low Subsonic Compressible Wind Tunnel Design Calculation"])

                                if wind_tunnel_option == "History of Wind Tunnel":
                                            # Title
                                            st.title("🌬️ History of Wind Tunnel")
                                            # Introduction
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    Wind tunnels have been vital in the journey of flight, from understanding simple airflow to developing supersonic aircraft and spacecraft.
                                                    This timeline explores how wind tunnel technology has evolved over centuries.
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            # Section: Early Concepts
                                            st.header("📜 Early Concepts: The Foundations of Aerodynamics")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    The idea of studying airflow dates back to the Renaissance. Leonardo da Vinci sketched early concepts of air resistance, but without building a working tunnel.
                                                    In the 1700s, Benjamin Robins used primitive equipment to study projectile motion and air resistance, laying the groundwork for future aerodynamic research.
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            # Section: 19th Century
                                            st.header("🛠️ 19th Century: The Birth of the Wind Tunnel")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                        In 1871, British engineer Francis Herbert Wenham built the first recognized wind tunnel. It featured a 12-foot test section powered by a steam fan, allowing scientists to study airflow over models under controlled conditions.
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            st.info("🔍 Key Milestone: Wenham’s Wind Tunnel (1871) — A major step in aerodynamic testing with powered airflow.")

                                            # Section: 20th Century
                                            st.header("✈️ 20th Century: The Age of Aviation")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    The invention of powered flight in 1903 by the Wright brothers dramatically increased the need for aerodynamic testing.
                                                    <li> 1901: The Wright brothers built a small wind tunnel to test over 200 wing shapes.
                                                    <li> Governments and organizations like NACA (which later became NASA) built larger wind tunnels to support military and civil aviation.
                                                    <li> Wind tunnels were critical during World Wars for optimizing aircraft performance.
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            # Section: Modern Era
                                            st.header("🚀 Post-War and Modern Era: Supersonic and Beyond")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    With the rise of jet engines and space exploration, wind tunnels evolved to support high-speed and hypersonic testing.
                                                    <li> Hypersonic tunnels simulate speeds greater than Mach 5 for spacecraft and missiles.
                                                    <li> Computational Fluid Dynamics (CFD) now works hand-in-hand with wind tunnel testing to validate aerodynamic predictions.
                                                    Despite advances in simulation, physical wind tunnel testing remains essential.
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            # Section: Future
                                            st.header("🔮 The Future of Wind Tunnels")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    Modern tunnels use high-speed cameras, laser sensors, and advanced materials. They are also used in:
                                                    <li> Automotive and F1 car design
                                                    <li> Sports equipment testing
                                                    <li> Architectural wind load analysis
                                                    As green aviation and space exploration grow, so does the role of wind tunnels in shaping the future.
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            # Conclusion
                                            st.header("✅ Conclusion")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    From hand-carved wooden models to advanced hypersonic test chambers, wind tunnels represent our desire to master the skies.
                                                    Their history is a story of curiosity, innovation, and bold leaps toward the future.
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)
                                            
                                elif wind_tunnel_option == "Types of Wind Tunnel":
                                            # Title
                                            st.title("🌬️ Types of Wind Tunnel")
                                            # Introduction
                                            st.markdown("""
                                             <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    Wind tunnels come in various types depending on the speed, flow generation method, and specific testing requirements.
                                                    Let’s explore the different types of wind tunnels and how they are used in various industries.
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            # Section 1: Based on Airspeed
                                            st.header("🚀 1. Based on Airspeed")
                                            st.subheader("🔹 Subsonic Wind Tunnel")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    <li> Speed: Less than Mach 1  
                                                    <li> Use: Testing aircraft, vehicles, buildings, and sports gear  
                                                    <li> Note: Most widely used type for general aerodynamics.
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            st.subheader("🔹 Transonic Wind Tunnel")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    <li> Speed: Around Mach 1  
                                                    <li> Use: Studying flight characteristics near the speed of sound  
                                                    <li> Feature: Challenges include shock wave formation and flow instability.
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            st.subheader("🔹 Supersonic Wind Tunnel")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    <li> Speed: Between Mach 1 and Mach 5  
                                                    <li> Use: High-speed aircraft, missiles, and defense applications  
                                                    <li> Note: Uses special nozzles to control supersonic airflow.
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            st.subheader("🔹 Hypersonic Wind Tunnel")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    <li> Speed: Above Mach 5  
                                                    <li> Use: Spacecraft re-entry testing and hypersonic transport development  
                                                    <li> Note: Involves extreme temperatures and energy conditions.
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            # Section 2: Based on Flow Generation
                                            st.header("🔁 2. Based on Flow Generation")
                                            st.subheader("🔸 Open-Circuit Wind Tunnel")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    <li> Design: Air flows in and out freely  
                                                    <li> Pros: Simple, cost-effective  
                                                    <li> Cons: Limited control over air conditions
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            st.subheader("🔸 Closed-Circuit Wind Tunnel")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    <li> Design: Air is recirculated within the tunnel  
                                                    <li> Pros: Efficient and better control of testing conditions  
                                                    <li> Use: Advanced research in aerospace, automotive, etc.
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            # Section 3: Based on Flow Direction
                                            st.header("🧭 3. Based on Flow Direction")
                                            st.subheader("🔹 Horizontal Wind Tunnel")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    <li> Most common orientation  
                                                    <li> Suitable for all kinds of aerodynamic testing
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            st.subheader("🔹 Vertical Wind Tunnel")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    <li> Used for parachute, skydiving, and free-fall simulations  
                                                    <li> Air flows upward to suspend objects mid-air
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            # Section 4: Specialized Types
                                            st.header("⚙️ 4. Specialized Wind Tunnels")
                                            st.subheader("🔸 Environmental Wind Tunnel")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    <li> Simulates weather conditions (rain, snow, fog)  
                                                    <li> Used to test performance and safety under real-world environments
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            st.subheader("🔸 Flow Visualization Tunnel")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    <li> Uses smoke or laser to visualize airflow  
                                                    <li> Popular for educational demos and research on flow patterns
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)

                                            # Conclusion
                                            st.header("✅ Conclusion")
                                            st.markdown("""
                                            <div style="
                                                background-color: rgba(240, 242, 246, 0.3);
                                                padding: 30px;
                                                border-radius: 15px;
                                                border: 1px solid rgba(255, 255, 255, 0.3);
                                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                                font-size: 24px;
                                                line-height: 1.8;
                                                color: white;
                                                backdrop-filter: blur(8px);
                                                -webkit-backdrop-filter: blur(8px);
                                                margin-bottom: 28px;
                                            ">
                                                <div style="font-size: 28px;">
                                                    Wind tunnels play a critical role across industries — from designing aircraft to optimizing sports gear.
                                                    Each type is tailored to a specific range of speeds or testing scenarios, helping engineers understand and improve the performance of various designs.
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)
                                            
                                elif wind_tunnel_option == "Low Subsonic Incompressible Wind Tunnel Design Calculation":
                                    st.title("Low Subsonic Incompressible Wind Tunnel Design Calculation")
                                    st.write("Details about incompressible low subsonic wind tunnel design calculations.")
                                    def safe_eval(expression):
                                        try:
                                            return eval(expression, {"__builtins__": {}}, {"math": math})
                                        except:
                                            raise ValueError("Invalid mathematical expression")
                                        
                                    def calculate_wind_tunnel(Mach_number_at_test_section, option_1, option_2, option_3, width_of_test_section=None):
                                        try:
                                            # Constants
                                            ambient_temperature = 288.16  # Kelvin
                                            density_of_air = 1.225  # kg/m³
                                            P1 = 1.01325 * 10**5  # Atmospheric pressure in Pascals
                                            specific_heat_ratio_of_air = 1.4
                                            Universal_gas_constant = 287
                                            Area_of_test_section = 1  # Assume 1 m²

                                            # Velocity at test section
                                            Velocity_at_test_section = Mach_number_at_test_section * (specific_heat_ratio_of_air * Universal_gas_constant * ambient_temperature) ** 0.5
                                            Mass_flow_rate_at_test_section_area = density_of_air * Velocity_at_test_section * Area_of_test_section

                                            # Wind tunnel type
                                            Inlet_to_test_section_ratio = 2 if option_1 == "1" else 4
                                            Exit_to_test_section_ratio = 1.3

                                            # Test section
                                            if option_2 == "1":
                                                width_of_test_section = (Area_of_test_section) ** 0.5
                                                height_of_test_section = (Area_of_test_section) ** 0.5
                                            else:
                                                height_of_test_section = Area_of_test_section / width_of_test_section

                                            hydraulic_diameter_test_section = (2 * width_of_test_section * height_of_test_section) / (width_of_test_section + height_of_test_section)
                                            length_of_test_section = 3 * hydraulic_diameter_test_section  # K = 3

                                            # Inlet section
                                            Velocity_at_Inlet_section = Velocity_at_test_section / Inlet_to_test_section_ratio
                                            width_of_inlet_section = ((Inlet_to_test_section_ratio) ** 0.5) * width_of_test_section
                                            Height_of_inlet_section = ((Inlet_to_test_section_ratio) ** 0.5) * height_of_test_section
                                            hydraulic_diameter_Inlet_section = (2 * width_of_inlet_section * Height_of_inlet_section) / (width_of_inlet_section + Height_of_inlet_section)
                                            length_of_inlet_section = Inlet_to_test_section_ratio * hydraulic_diameter_Inlet_section

                                            # Outlet section
                                            Velocity_at_Exit_section = Velocity_at_test_section / Exit_to_test_section_ratio
                                            Exit_Area = (Area_of_test_section * Velocity_at_test_section) / (Velocity_at_Exit_section)

                                            if option_3 == "1":  # Circular outlet
                                                Radius_of_circular_test_section = (Exit_Area / math.pi) ** 0.5
                                                Angular_velocity = Velocity_at_Exit_section / Radius_of_circular_test_section
                                                Number_of_revolution = (Angular_velocity * 60) / (2 * math.pi)
                                                hydraulic_diameter_outlet_section = 2 * Radius_of_circular_test_section
                                            else:  # Rectangular outlet
                                                width_of_outlet_section = ((Exit_to_test_section_ratio) ** 0.5) * width_of_test_section
                                                Height_of_outlet_section = ((Exit_to_test_section_ratio) ** 0.5) * height_of_test_section
                                                hydraulic_diameter_outlet_section = (2 * width_of_outlet_section * Height_of_outlet_section) / (width_of_outlet_section + Height_of_outlet_section)

                                            theta_deg = 3  # Angle in degrees
                                            theta_rad = math.radians(theta_deg)
                                            tan_value = math.tan(theta_rad)
                                            length_of_exit_section = hydraulic_diameter_outlet_section / tan_value

                                            return {
                                                "Mass flow rate (kg/s)": Mass_flow_rate_at_test_section_area,
                                                
                                                "Velocity at Inlet section (m/s)": Velocity_at_Inlet_section,
                                                "Length of inlet section (m)": length_of_inlet_section,
                                                
                                                "Velocity at test section (m/s)": Velocity_at_test_section,
                                                "Length of test section (m)": length_of_test_section,
                                                
                                                "Velocity at Exit section (m/s)": Velocity_at_Exit_section,
                                                "Length of exit section (m)": length_of_exit_section,
                                                
                                                "Outlet shape": "Circular" if option_3 == "1" else "Rectangular",
                                                "Angular velocity (rad/s)": Angular_velocity if option_3 == "1" else None,
                                                "Number of revolutions (rpm)": Number_of_revolution if option_3 == "1" else None
                                            }
                                        except Exception as e:
                                            return {"Error": str(e)}

                                    Mach_number_at_test_section = st.text_input("Enter Mach number:", value="0.5")
                                    option_1 = st.radio("Select wind tunnel type:", ["1", "2"], format_func=lambda x: "Open" if x == "1" else "Closed")
                                    option_2 = st.radio("Select test section shape:", ["1", "2"], format_func=lambda x: "Square" if x == "1" else "Rectangular")
                                    width_of_test_section = None

                                    if option_2 == "2":
                                        width_of_test_section = st.text_input("Width of test section (m):", value="0.5")
                                    option_3 = st.radio("Select outlet section shape:", ["1", "2"], format_func=lambda x: "Circular" if x == "1" else "Rectangular")

                                    if st.button("Calculate"):
                                        try:
                                            Mach_number_at_test_section = safe_eval(Mach_number_at_test_section)
                                            if width_of_test_section:
                                                width_of_test_section = safe_eval(width_of_test_section)
                                            results = calculate_wind_tunnel(Mach_number_at_test_section, option_1, option_2, option_3, width_of_test_section)
                                            for key, value in results.items():
                                                if value is not None:
                                                    st.success(f"{key}: {value:.2f}" if isinstance(value, (int, float)) else f"{key}: {value}")
                                        except Exception as e:
                                            st.error(f"Invalid input: {e}")    

                                elif wind_tunnel_option == "Low Subsonic Compressible Wind Tunnel Design Calculation":
                                    st.title("Low Subsonic Compressible Wind Tunnel Design Calculation")
                                    st.write("Details about compressible low subsonic wind tunnel design calculations.")
                                    
                                    def solve(
                                        ambient_pressure, ambient_temperature, ambient_density,
                                        Inlet_Mach_number, Test_Mach_Number, Test_section_area
                                    ):
                                        # Constants
                                        specific_heat_ratio = 1.4
                                        R = 287  # Specific gas constant for air (J/kg·K)
                                        Specific_heat_at_constant_pressure = specific_heat_ratio * R / (specific_heat_ratio - 1)  # Cp

                                        # Stagnation Temperature Calculation
                                        Stagnation_to_inlet_temperature_ratio = (1 + ((specific_heat_ratio - 1) / 2) * pow(Inlet_Mach_number, 2))
                                        Stagnation_temperature = Stagnation_to_inlet_temperature_ratio * ambient_temperature
                                        Test_section_to_Inlet_temperature_ratio = Stagnation_to_inlet_temperature_ratio / (1 + ((specific_heat_ratio - 1) / 2) * pow(Test_Mach_Number, 2))
                                        Test_section_temperature = Test_section_to_Inlet_temperature_ratio * ambient_temperature

                                        # Velocity Calculation
                                        Inlet_velocity = (2 * Specific_heat_at_constant_pressure * (Stagnation_temperature - ambient_temperature)) ** 0.5
                                        Test_section_velocity = (2 * Specific_heat_at_constant_pressure * (Stagnation_temperature - Test_section_temperature)) ** 0.5

                                        # Density Calculation
                                        Test_section_density = ambient_density * (Test_section_to_Inlet_temperature_ratio) ** (-1 / (specific_heat_ratio - 1))

                                        # Area Ratio Calculation
                                        Inlet_to_test_section_area_ratio = ((Test_section_to_Inlet_temperature_ratio) ** (-1 / (specific_heat_ratio - 1))) * (Test_section_velocity / Inlet_velocity)
                                        Inlet_Area = Test_section_area * Inlet_to_test_section_area_ratio

                                        # Pressure at test section
                                        Pressure_at_test_section = Test_section_density * R * Test_section_temperature

                                        return {
                                            "Stagnation Temperature": Stagnation_temperature,
                                            "Test Section Temperature": Test_section_temperature,
                                            "Inlet Velocity": Inlet_velocity,
                                            "Test Section Velocity": Test_section_velocity,
                                            "Test Section Density": Test_section_density,
                                            "Inlet to Test Section Area Ratio": Inlet_to_test_section_area_ratio,
                                            "Inlet Area": Inlet_Area,
                                            "Pressure at Test Section": Pressure_at_test_section
                                        }

                                    # Streamlit UI
                                    input_labels = [
                                        "Ambient Pressure (Pa)", "Ambient Temperature (K)", "Ambient Density (kg/m³)",
                                        "Inlet Mach Number", "Test Section Mach Number", "Test Section Area (m²)"
                                    ]

                                    def get_input(label):
                                        try:
                                            return eval(st.text_input(label, "0.0"))
                                        except Exception:
                                            st.warning(f"Invalid input for {label}, using default value 0.0")
                                            return 0.0

                                    inputs = [get_input(label) for label in input_labels]
                                    if st.button("Solve"):
                                        results = solve(*inputs)
                                        for key, value in results.items():
                                            st.success(f"{key}: {value:.2f}")

        def Knowledge_Area():
            Knowledge_Area = st.sidebar.radio("Select Options", ["Available Topic Wise Notes", "Educational Video"])
            if Knowledge_Area == "Available Topic Wise Notes":
                    def Available_Topic_Wise_Notes_For_Download(image_path):
                        try:
                            base64_str = get_base64(image_path)
                            st.markdown(
                                f"""
                                <style>
                                .stApp {{
                                    background-image: url("data:image/png;base64,{base64_str}");
                                    background-size: cover;
                                    background-position: center;
                                    background-attachment: fixed;
                                }}
                                </style>
                                """,
                                unsafe_allow_html=True
                            )
                        except FileNotFoundError:
                            st.error("Background image not found. Please check the file path.")
                    # ✅ Set background image (Make sure the path is correct)
                    Available_Topic_Wise_Notes_For_Download("White Orange 3D Illustration Marketing Blog Banner.jpg")
                    UPLOAD_DIR = "uploads"

                    def save_uploaded_file(uploaded_file, subject):
                        subject_path = os.path.join(UPLOAD_DIR, subject)
                        os.makedirs(subject_path, exist_ok=True)
                        save_path = os.path.join(subject_path, uploaded_file.name)
                        with open(save_path, "wb") as f:
                            f.write(uploaded_file.getbuffer())
                        return save_path

                    def delete_file(subject, filename):
                        file_path = os.path.join(UPLOAD_DIR, subject, filename)
                        if os.path.exists(file_path):
                            os.remove(file_path)
                            return True
                        return False

                    def delete_subject(subject):
                        subject_path = os.path.join(UPLOAD_DIR, subject)
                        if os.path.isdir(subject_path):
                            shutil.rmtree(subject_path)
                            return True
                        return False

                    def main():
                        st.title("📘 Available Topic Notes by Subject Wise")

                        os.makedirs(UPLOAD_DIR, exist_ok=True)

                        # Developer Mode Section
                        if st.sidebar.checkbox("🛠 Developer Mode"):
                            st.subheader("Upload Notes")
                            subject = st.text_input("Enter subject name")
                            uploaded_file = st.file_uploader("Upload PDF Note", type=["pdf"])
                            if uploaded_file and subject:
                                file_path = save_uploaded_file(uploaded_file, subject)
                                st.success(f"✅ File '{uploaded_file.name}' uploaded under subject: {subject}")

                            # Delete File Section
                            st.subheader("🗑 Delete Uploaded File")
                            subjects = [d for d in os.listdir(UPLOAD_DIR) if os.path.isdir(os.path.join(UPLOAD_DIR, d))]
                            if subjects:
                                selected_subject = st.selectbox("Select subject to delete file from", subjects, key="delete_file_subject")
                                subject_path = os.path.join(UPLOAD_DIR, selected_subject)
                                pdf_files = [f for f in os.listdir(subject_path) if f.endswith(".pdf")]

                                if pdf_files:
                                    selected_file_to_delete = st.selectbox("Select file to delete", pdf_files)
                                    if st.button("Delete File"):
                                        if delete_file(selected_subject, selected_file_to_delete):
                                            st.success(f"✅ Deleted '{selected_file_to_delete}' successfully.")
                                            st.rerun()
                                        else:
                                            st.error("❌ File could not be deleted.")
                                else:
                                    st.info("No PDF notes available under this subject.")
                            else:
                                st.info("No subjects available.")

                            # Delete Subject Section
                            st.subheader("🗂 Delete Subject (All Files Inside Will Be Deleted)")
                            if subjects:
                                selected_subject_to_delete = st.selectbox("Select subject to delete entirely", subjects, key="delete_subject")
                                if st.button("Delete Subject"):
                                    if delete_subject(selected_subject_to_delete):
                                        st.success(f"✅ Subject '{selected_subject_to_delete}' deleted successfully.")
                                        st.rerun()
                                    else:
                                        st.error("❌ Subject could not be deleted.")
                            else:
                                st.info("No subjects to delete.")

                        # Download Section
                        st.subheader("📥 Download Topic Notes by Subject Wise")
                        subjects = [d for d in os.listdir(UPLOAD_DIR) if os.path.isdir(os.path.join(UPLOAD_DIR, d))]

                        if subjects:
                            selected_subject = st.selectbox("Select a subject", subjects, key="download_subject")
                            subject_path = os.path.join(UPLOAD_DIR, selected_subject)
                            pdf_files = [f for f in os.listdir(subject_path) if f.endswith(".pdf")]

                            if pdf_files:
                                for pdf in pdf_files:
                                    pdf_path = os.path.join(subject_path, pdf)
                                    with open(pdf_path, "rb") as f:
                                        st.download_button(label=f"Download {pdf}", data=f, file_name=pdf, mime="application/pdf")
                            else:
                                st.info("No PDF notes available under this subject.")
                        else:
                            st.warning("No subjects found. Please upload notes using Developer Mode.")

                    if __name__ == "__main__":
                        main()
                          
            elif Knowledge_Area == "Educational Video":
                    def Educational_Video(image_path):
                        try:
                            base64_str = get_base64(image_path)
                            st.markdown(
                                f"""
                                <style>
                                .stApp {{
                                    background-image: url("data:image/png;base64,{base64_str}");
                                    background-size: cover;
                                    background-position: center;
                                    background-attachment: fixed;
                                }}
                                </style>
                                """,
                                unsafe_allow_html=True
                            )
                        except FileNotFoundError:
                            st.error("Background image not found. Please check the file path.")
                    # ✅ Set background image (Make sure the path is correct)
                    Educational_Video("1070169.png")
                    # Directories
                    VIDEO_DIR = "videos"
                    os.makedirs(VIDEO_DIR, exist_ok=True)
                    # Set DEVELOPER_MODE to True for the developer, False for users
                    DEVELOPER_MODE = st.sidebar.checkbox("Enable Developer Mode", value=True)
                    st.title("📽️ Subject-Wise Video Uploader & Player")
                    # Developer Section
                    if DEVELOPER_MODE:
                        st.subheader("🎥 Developer: Upload a Video")

                        subject = st.text_input("Enter subject name")
                        uploaded_file = st.file_uploader("Upload Video", type=["mp4", "mov", "avi", "mkv"])

                        if uploaded_file and subject:
                            subject_path = os.path.join(VIDEO_DIR, subject)
                            os.makedirs(subject_path, exist_ok=True)
                            video_path = os.path.join(subject_path, uploaded_file.name)

                            with open(video_path, "wb") as f:
                                f.write(uploaded_file.getbuffer())

                            st.success(f"✅ Video '{uploaded_file.name}' uploaded under subject '{subject}'!")

                        st.subheader("🗑 Delete a Video")
                        subjects = [d for d in os.listdir(VIDEO_DIR) if os.path.isdir(os.path.join(VIDEO_DIR, d))]
                        if subjects:
                            selected_subject = st.selectbox("Select subject to delete from", subjects, key="delete_subject")
                            video_files = [f for f in os.listdir(os.path.join(VIDEO_DIR, selected_subject))
                                           if f.endswith((".mp4", ".mov", ".avi", ".mkv"))]
                            if video_files:
                                selected_video_to_delete = st.selectbox("Select video to delete", video_files)
                                if st.button("Delete Video"):
                                    video_to_delete_path = os.path.join(VIDEO_DIR, selected_subject, selected_video_to_delete)
                                    if os.path.exists(video_to_delete_path):
                                        os.remove(video_to_delete_path)
                                        st.success(f"✅ Deleted '{selected_video_to_delete}' successfully.")
                                        st.rerun()
                                    else:
                                        st.error("❌ Video file not found.")
                            else:
                                st.info("No videos available under this subject.")
                        else:
                            st.info("No subjects available for deletion.")

                    else:
                        st.warning("Developer Mode is disabled. You can only view videos.")

                    # Viewer Section
                    st.subheader("📺 Watch Videos by Subject")
                    subjects = [d for d in os.listdir(VIDEO_DIR) if os.path.isdir(os.path.join(VIDEO_DIR, d))]
                    if subjects:
                        selected_subject = st.selectbox("Select a subject", subjects, key="view_subject")
                        subject_path = os.path.join(VIDEO_DIR, selected_subject)
                        video_files = [f for f in os.listdir(subject_path) if f.endswith((".mp4", ".mov", ".avi", ".mkv"))]

                        if video_files:
                            selected_video = st.selectbox("Select a Video", video_files)
                            video_path = os.path.join(subject_path, selected_video)
                            st.video(video_path)
                        else:
                            st.info("No videos available in this subject.")
                    else:
                        st.warning("No subjects found. Please upload videos in Developer Mode.")

        def Feedback_Area():
            Feedback_Area = st.sidebar.radio("Select Options", ["Feedback of Website","Technical Error Value Feedback"])
            if  Feedback_Area== "Feedback of Website":
                    # Function to set background
                    def Feedback_of_Website(image_path):
                        try:
                            base64_str = get_base64(image_path)
                            st.markdown(
                                f"""
                                <style>
                                .stApp {{
                                    background-image: url("data:image/png;base64,{base64_str}");
                                    background-size: cover;
                                    background-position: center;
                                    background-attachment: fixed;
                                }}
                                </style>
                                """,
                                unsafe_allow_html=True
                            )
                        except FileNotFoundError:
                            st.error("Background image not found. Please check the file path.")
                    # ✅ Set background image (Make sure the path is correct)
                    Feedback_of_Website("time-for-feedback-message-written-on-blue-wooden-stick-with-yellow-background-conceptual-time-for-feedback-symbol-copy-space-photo.jpg")
           
            elif  Feedback_Area== "Technical Error Value Feedback":
                    # Function to set background
                    def Feedback_of_Website(image_path):
                        try:
                            base64_str = get_base64(image_path)
                            st.markdown(
                                f"""
                                <style>
                                .stApp {{
                                    background-image: url("data:image/png;base64,{base64_str}");
                                    background-size: cover;
                                    background-position: center;
                                    background-attachment: fixed;
                                }}
                                </style>
                                """,
                                unsafe_allow_html=True
                            )
                        except FileNotFoundError:
                            st.error("Background image not found. Please check the file path.")
                    # ✅ Set background image (Make sure the path is correct)
                    Feedback_of_Website("480537.png")

        def New_Notification_Update():
                    # Function to set background
                    def New_Notification_Update(image_path):
                        try:
                            base64_str = get_base64(image_path)
                            st.markdown(
                                f"""
                                <style>
                                .stApp {{
                                    background-image: url("data:image/png;base64,{base64_str}");
                                    background-size: cover;
                                    background-position: center;
                                    background-attachment: fixed;
                                }}
                                </style>
                                """,
                                unsafe_allow_html=True
                            )
                        except FileNotFoundError:
                            st.error("Background image not found. Please check the file path.")
                    # ✅ Set background image (Make sure the path is correct)
                    New_Notification_Update("premium_photo-1682309572625-791e25352998.jpeg")
                    
        def Contact_Details():
            # Function to set background
            def Contact_Details(image_path):
                try:
                    base64_str = get_base64(image_path)
                    st.markdown(
                        f"""
                        <style>
                        .stApp {{
                            background-image: url("data:image/png;base64,{base64_str}");
                            background-size: cover;
                            background-position: center;
                            background-attachment: fixed;
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True
                    )
                except FileNotFoundError:
                    st.error("Background image not found. Please check the file path.")
            # ✅ Set background image (Make sure the path is correct)
            Contact_Details("Purple and White Simple Technology YouTube Video Intro.jpg")
            Contact_Details = st.sidebar.radio("Select Options", ["Contact Details"])
            if Contact_Details=="Contact Details":
                    # ✅ Contact & Social Media
                    st.header("Get in Touch")
                    st.write("📍 Location: New Delhi")
                    st.write("📧 Email: amandeepoct97@gmail.com")
                    st.write("🌐 Website: https://amandeepsinghportfolio.streamlit.app/")
                    
                    # ✅ Social Media Links
                    st.header("Connect with Linkedin")
                    st.markdown("""
                    [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/amandeep-singh-ae?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) 
                    """)
                    
        # --- Setup Session State ---
        if 'page' not in st.session_state:
            st.session_state.page = 'Home'

        # --- CSS Hover Style ---
        st.markdown("""
            <style>
            .nav-link {
                display: block;
                padding: 12px;
                margin-bottom: 8px;
                background-color: #1f77b4;
                color: white;
                text-decoration: none;
                border-radius: 6px;
                text-align: center;
                transition: 0.3s;
            }
            .nav-link:hover {
                background-color: #4fa3d1;
                color: white;
            }
            </style>
        """, unsafe_allow_html=True)

        # --- Sidebar Navigation ---
        st.sidebar.markdown("## 🚀 Navigation")

        nav_links = {
            "Home": "Home",
            "About": "About",
            "Design Area": "Design Area",
            "Knowledge Area":"Knowledge Area",
            "Feedback Area":"Feedback Area",
            "New Notification Update":"New Notification Update",
            "Contact Details":"Contact Details"
            
        }

        for key, label in nav_links.items():
            if st.sidebar.button(label):
                st.session_state.page = key

        if st.session_state.page == "Home":
             st.balloons()
             Home()
            
        elif st.session_state.page == "About":
            about()
                    
        elif st.session_state.page == "Design Area":
            design_area()

        elif st.session_state.page == "Knowledge Area":
            Knowledge_Area()

        elif st.session_state.page == "Feedback Area":  
           Feedback_Area()

        elif st.session_state.page == "New Notification Update":  
           New_Notification_Update()   
           
        elif st.session_state.page == "Contact Details":  
          Contact_Details()
            
# ---------- MAIN ----------
def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""

    if st.session_state.logged_in:
        welcome_page()
    else:
        login_page()

# Run the app
main()

   
