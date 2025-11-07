# System Architecture Documentation

## Overview
The Indian Housing Project is a machine learning-based system designed to predict housing prices in India. This document outlines the system's architecture, components, and their interactions.

## System Components

### 1. Web Interface (Flask Application)
- Entry point: `app.py`
- Handles user interactions through a web interface
- Processes form submissions and displays predictions
- Routes:
  - GET `/`: Displays the prediction form
  - POST `/`: Processes user input and returns predictions

### 2. Data Pipeline Components
Located in `src/components/`:

#### 2.1 Data Ingestion (`Data_ingestion.py`)
- Handles data loading and splitting
- Creates training and test datasets
- Output locations: `Artifacts/` directory

#### 2.2 Data Transformation (`Data_transformation.py`)
- Performs feature preprocessing
- Handles scaling and encoding
- Manages data transformations for model training

#### 2.3 Model Training (`Model_trainer.py`)
- Implements model training logic
- Uses CatBoostRegressor algorithm
- Handles model parameter tuning

#### 2.4 Model Evaluation (`Model_evaluation.py`)
- Evaluates model performance
- Generates performance metrics
- Validates model accuracy

### 3. Pipeline Management
Located in `src/pipelines/`:

#### 3.1 Training Pipeline
- Orchestrates the entire training process
- Manages workflow from data ingestion to model creation

#### 3.2 Prediction Pipeline
- Handles real-time predictions
- Processes user input data
- Returns formatted predictions

### 4. Utility Components
- Exception handling (`exception.py`)
- Logging functionality (`logger.py`)
- Helper functions (`utils.py`)

## Data Flow

1. **Data Ingestion Flow**
   ```
   Raw Data → Data Ingestion → Train/Test Split → Artifacts Storage
   ```

2. **Training Flow**
   ```
   Training Data → Data Transformation → Model Training → Model Evaluation → Model Storage
   ```

3. **Prediction Flow**
   ```
   User Input → Data Preprocessing → Model Prediction → Formatted Output
   ```

## Technology Stack

- **Web Framework**: Flask
- **ML Libraries**: 
  - scikit-learn
  - CatBoost
  - XGBoost
- **Data Processing**: 
  - Pandas
  - NumPy
- **Visualization**:
  - Seaborn
  - Matplotlib
- **MLOps Tools**:
  - DVC
  - MLflow

## Infrastructure Requirements

### Development Environment
- Python 3.x
- Virtual Environment (Conda recommended)
- Required packages as listed in `requirements.txt`

### Production Environment
- AWS infrastructure (as configured)
- MLflow tracking server
- Containerization support (Docker)