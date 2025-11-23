# adult-tobacco-consumption-dash
Final Project for DSE 6000
📘 Adult Tobacco Consumption Dashboard — README
🧭 Overview

This project is an interactive Data Storytelling Dashboard built using the Plotly Dash framework.
The dashboard explores Adult Tobacco Consumption in the United States, using datasets sourced from the CDC (Centers for Disease Control and Prevention).

The project includes:

Data cleaning & transformation

Exploratory Data Analysis (EDA)

Interactive plots (10+ visualizations)

Predictive analytics using machine learning

A user-friendly Dash interface

Deployment to Google Cloud Platform (GCP) (coming soon)

✨ Features

🧹 Data Cleaning & Preprocessing

📊 10 interactive visualizations built with Plotly

🤖 Machine Learning predictions (multiple models evaluated)

🖥️ Dash web app UI for interacting with data and models

☁️ Containerized with Docker and prepared for Cloud Run deployment

🔀 Git branching workflow for team collaboration

🚀 Local Development Setup Guide

Follow the steps below to set up and run the project on your local machine.

✅ 1. Clone the Repository
git clone https://github.com/USERNAME/adult-tobacco-consumption-dash.git
cd adult-tobacco-consumption-dash

✅ 2. Create a Python Virtual Environment

Make sure you have Python 3.9+ installed.

macOS / Linux
python3 -m venv venv
source venv/bin/activate

Windows (PowerShell)
python -m venv venv
venv\Scripts\activate

✅ 3. Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt

✅ 4. Project Structure
project/
│── data/
│    ├── raw/           # Raw CDC datasets
│    └── cleaned/       # Cleaned datasets 
│
│── src/
│    ├── data_loading.py
│    ├── data_cleaning.py
│    ├── eda_plots.py
│    ├── model_training.py
│    └── model_inference.py
│
│── app.py              # Main Dash application
│── requirements.txt
│── Dockerfile
│── README.md
│── .gitignore
│── venv/               # Local environment (ignored)

✅ 5. Running the Dash App Locally

With the virtual environment activated:

python app.py


Then open the app in your browser:

http://127.0.0.1:8050


or

http://localhost:8050

✅ 6. Selecting the Virtual Environment in VS Code

Open the project in VS Code

Press: Ctrl + Shift + P

Search: Python: Select Interpreter

Choose:

./venv/bin/python


This ensures your code runs using the correct environment.

✅ 7. Installing New Packages

Install a new dependency:

pip install package-name


Update requirements.txt:

pip freeze > requirements.txt

✅ 8. Git Branching Workflow (Recommended)

Use a clean, modern branching strategy:

Branch	Purpose
main	Production-ready/stable code
dev	Active development
feature/<name>	Individual feature/work tasks
Example flow:
git checkout -b feature/data-cleaning
# work on code…
git add .
git commit -m "Added initial cleaning logic"
git push origin feature/data-cleaning


Then open a Pull Request into dev.

🔒 9. Environment Variables (Optional)

If needed, create a .env file:

DEBUG=True
SECRET_KEY="..."


Your .env file is automatically ignored by .gitignore.

☁️ Cloud Deployment (Coming Soon)

Documentation for deployment to Google Cloud Run will be added in a later phase, including:

Building Docker containers

Authenticating with GCP

Pushing images to Artifact Registry

Deploying via Cloud Run

Generating a public service URL

(The team should complete local development first.)

📄 License

MIT License (optional — you can choose another).

👥 Contributors

Add team member names here.