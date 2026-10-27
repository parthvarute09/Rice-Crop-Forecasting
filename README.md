# 🌾 Rice Crop Yield Forecasting System

## 📌 Project Overview

The **Rice Crop Yield Forecasting System** is a machine learning-based project designed to predict rice crop yield using relevant agricultural, environmental, and climatic factors.

The system aims to support farmers, researchers, and agricultural planners by providing data-driven yield estimates that can help with crop planning, resource management, and agricultural decision-making.

## 🎯 Objectives

- Predict rice crop yield using machine learning techniques.
- Analyze factors that influence rice production.
- Explore agricultural datasets through data cleaning and exploratory data analysis (EDA).
- Build a predictive model and evaluate its performance.
- Support informed agricultural planning and decision-making.

## ✨ Key Features

- Agricultural dataset preprocessing and cleaning.
- Exploratory data analysis and visualization.
- Feature selection and model training.
- Rice crop yield prediction.
- Model performance evaluation.
- Potential integration with a user-friendly prediction interface.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Data Manipulation:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Development Environment:**  VS Code
- **Version Control:** Git and GitHub


## 📊 Dataset

The project uses agricultural data relevant to rice cultivation and yield forecasting.

Potential input features may include:

- Year and cultivation season
- Cultivated area
- Rainfall
- Temperature
- Soil characteristics
- Fertilizer usage
- Rice production and historical yield

The exact features depend on the dataset used in the implementation.

**Target variable:** Rice crop yield, measured in the unit provided by the dataset, such as tonnes per hectare.

## ⚙️ Project Workflow

1. **Data Collection:** Obtain a relevant rice cultivation or agricultural dataset.
2. **Data Preprocessing:** Handle missing values, duplicates, inconsistent data, and categorical variables.
3. **Exploratory Data Analysis:** Identify patterns and relationships between agricultural factors and crop yield.
4. **Feature Engineering:** Select and prepare suitable input variables.
5. **Model Training:** Train appropriate machine learning regression algorithms.
6. **Model Evaluation:** Evaluate predictions using suitable regression metrics.
7. **Yield Forecasting:** Generate predictions for new input data.
8. **Visualization:** Present results through charts, tables, or an optional dashboard.

## 🤖 Machine Learning Algorithms

Depending on the implementation, the following regression algorithms can be evaluated:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

Model selection should be based on evaluation results rather than assumed performance.

## 📈 Model Evaluation

The model can be evaluated using:

- **MAE (Mean Absolute Error):** Measures the average absolute prediction error.
- **MSE (Mean Squared Error):** Measures the average squared prediction error.
- **RMSE (Root Mean Squared Error):** Measures prediction error in the target variable's units.
- **R² Score:** Measures how well the model explains variation in the target variable.


## 🚀 Getting Started

### Prerequisites

Install Python and Git. Basic knowledge of Python and machine learning is helpful.

### 1. Clone the repository

```bash
git clone https://github.com/parthvarute09/Rice-Crop-Forecasting.git
```

### 2. Open the project folder

```bash
cd Rice-Crop-Forecasting
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

If your repository contains a `requirements.txt` file:

```bash
python -m pip install -r requirements.txt
```

Otherwise, install the libraries used by your notebook or application. For example:

```bash
python -m pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### 5. Run the project

Open the relevant notebook in Jupyter:

```bash
jupyter notebook
```

Then open the project's notebook and run the cells in order.

*The exact commands may differ depending on your project files and whether you have built a notebook, Python script, or web application.*

## 📁 Suggested Project Structure

```text
Rice-Crop-Forecasting/
│
├── data/
│   └── rice_yield_dataset.csv
│
├── notebooks/
│   └── rice_crop_forecasting.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   └── prediction.py
│
├── models/
│   └── trained_model.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
```

This is a suggested structure; retain only the files and folders that actually exist in your repository.

## 🌱 Applications

- Rice production planning
- Agricultural data analysis
- Crop yield estimation
- Farming resource management
- Agricultural research and decision support

## 🔮 Future Enhancements

- Integrate real-time weather data.
- Add soil and regional agricultural information.
- Compare multiple machine learning models.
- Build a web-based prediction interface using Streamlit.
- Display historical yield trends and forecast visualizations.
- Expand forecasting to additional regions and cultivation seasons.

## 👨‍💻 Author

**Parth Varute**

GitHub: [@parthvarute09](https://github.com/parthvarute09)

## ⭐ Support

If you find this project useful, consider giving the repository a star on GitHub.
