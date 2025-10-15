# Airbnb Market Analysis & Interactive Dashboard - Madrid

![Project Status](https://img.shields.io/badge/status-complete-green)
![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-ff4b4b)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

An in-depth analysis of the Airbnb market in Madrid, from data cleaning and exploratory data analysis to a fully interactive web dashboard built with Streamlit.

---


### 📖 Table of Contents
* [Project Overview](#-project-overview)
* [Key Features](#-key-features)
* [Tech Stack & Libraries](#-tech-stack--libraries)
* [Getting Started](#-getting-started)
* [Project Structure](#-project-structure)
* [Key Insights & Findings](#-key-insights--findings)
* [Future Improvements](#-future-improvements)
* [Contact](#-contact)

---

### 🎯 Project Overview

This project performs a comprehensive analysis of the Airbnb landscape in Madrid, Spain. The primary goal is to leverage data analysis techniques to uncover key drivers of pricing, popularity, and geographical distribution of rental properties.

The project is divided into two main parts:
1.  **Exploratory Data Analysis (EDA):** A detailed investigation conducted in a Jupyter Notebook to clean the data, handle outliers, and visualize key relationships between variables.
2.  **Interactive Dashboard:** A user-friendly web application built with Streamlit that allows users to dynamically filter and explore the dataset, providing on-the-fly metrics and map visualizations.

This repository serves as a demonstration of a complete data analysis workflow, from raw data to actionable insights and interactive communication.

---

### ✨ Key Features

*   **Data Cleaning & Preprocessing:**
    *   Systematic handling of missing values and data type corrections.
    *   Robust outlier detection and filtering for price analysis, ensuring a focus on the representative market.
*   **Exploratory Data Analysis (EDA):**
    *   In-depth analysis of price distribution, property types, and geographical concentrations.
    *   Visualizations of price variations across different Madrid neighborhoods.
    *   Correlation analysis to identify key relationships between numerical features.
*   **Interactive Streamlit Dashboard:**
    *   Dynamic filtering by neighborhood, room type, and price range.
    *   Real-time metrics on the number of listings and average price based on user selection.
    *   An interactive map that visualizes the geographical location of filtered properties.

---

### 🛠️ Tech Stack & Libraries

*   **Language:** Python
*   **Data Manipulation & Analysis:** Pandas, NumPy
*   **Data Visualization:** Matplotlib, Seaborn
*   **Interactive Web App:** Streamlit
*   **Development Environment:** Visual Studio Code, Jupyter Notebook

---

### 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

#### **Prerequisites**
*   [Git](https://git-scm.com/)
*   [Python 3.9+](https://www.python.org/downloads/)

#### **Installation & Setup**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/[your-username]/airbnb-madrid-analysis.git
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd airbnb-madrid-analysis
    ```

3.  **Create and activate a virtual environment:**
    *   **Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   **macOS / Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

#### **Usage**

1.  **To explore the Exploratory Data Analysis:**
    Open the `notebooks/01-EDA-Airbnb-Madrid.ipynb` file in VS Code or Jupyter Lab.

2.  **To launch the interactive dashboard:**
    Run the following command in your terminal from the project's root directory:
    ```bash
    streamlit run src/app.py
    ```
    Your web browser will automatically open with the running application.

---

### 📁 Project Structure

```
airbnb-madrid-analysis/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── data/
│   └── listings.csv.gz         # Raw dataset from Inside Airbnb
│
├── notebooks/
│   └── 01-EDA-Airbnb-Madrid.ipynb # In-depth exploratory data analysis
│
└── src/
    └── app.py                  # Source code for the Streamlit dashboard
```

---

### 📊 Key Insights & Findings

The analysis revealed several key trends in the Madrid Airbnb market:

*   **Geographical Concentration:** The vast majority of listings, along with the highest prices, are concentrated in the central districts, particularly **Centro**, **Salamanca**, and **Chamberí**.
*   **Dominant Property Type:** `Entire home/apt` is the most common and most expensive type of listing, indicating a market geared towards tourists seeking full privacy.
*   **Price Drivers:** The number of people a property accommodates (`accommodates`, `bedrooms`, `beds`) is the strongest positive correlate with price.
*   **Superhost Impact:** "Superhosts" consistently receive higher ratings and are able to charge a slight premium compared to standard hosts, suggesting that quality and reputation are valued by consumers.

---

### 🌱 Future Improvements

*   **Machine Learning Model:** Develop a regression model (e.g., XGBoost, Random Forest) to predict nightly prices based on property features.
*   **Amenity Analysis:** Perform Natural Language Processing (NLP) on the `amenities` column to identify which specific amenities have the highest impact on price and ratings.
*   **Time Series Analysis:** If historical data were available, analyze trends in pricing and occupancy over time to identify seasonality.
*   **Deployment:** Deploy the Streamlit application to a cloud service like Streamlit Community Cloud or Heroku for public access.
