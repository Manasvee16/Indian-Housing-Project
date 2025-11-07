# Table of Contents

- [About The Project](#about-the-project)
- [About the Data](#about-the-data)
  - [Target Variable](#target-variable)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
- [Installation Steps](#installation-steps)
- [Setup](#setup)
  - [MLflow Tracking](#mlflow-tracking)
- [Usage and Configuration](#usage-and-configuration)
- [License](#license)

## About The Project

This project aims to develop a machine learning model that accurately predicts housing prices using the Indian Housing dataset. By analyzing various features of houses, such as crime rate, number of rooms, and accessibility to highways, the model provides valuable insights for potential buyers or sellers in estimating housing prices. The project utilizes the powerful CatBoostRegressor algorithm for optimal performance and incorporates techniques like data preprocessing, exploratory data analysis, and model training. The trained model can be used as a tool to make informed decisions in the real estate market.

## About the Data

1. LCR: Local Crime Rate
2. LPZ: Large Plot Zoning
3. IA: Industrial Area
4. WP: Waterfront Property
5. PL: Pollution Level
6. RPH: Average Rooms per House
7. AGE: Property Age
8. DIS: Distance to Employment Hubs
9. HA: Highway Accessibility
10. TAX: Full-value property tax rate per ₹10,00,000
11. PTRATIO: School Pupil-Teacher Ratio
12. LD: Local Demographics
13. LIP: Lower Income Population

### Target Variable

- MEDV: Median value of owner-occupied homes in ₹1,00,000s

## Technology Stack

- Pandas
- Numpy
- Scikit-learn
- Flask
- DVC
- MLFlow
- Seaborn
- Matplotlib

## Getting Started

This will help you understand how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

## Installation Steps

### Option 1: Installation from GitHub

Follow these steps to install and set up the project directly from the GitHub repository:

1. **Clone the Repository**

   - Open your terminal or command prompt.
   - Navigate to the directory where you want to install the project.
   - Run the following command to clone the GitHub repository:
     ```
     git clone https://github.com/Manasvee16/Indian-Housing-Project
     ```

2. **Create a Virtual Environment** (Optional but recommended)

   - It's a good practice to create a virtual environment to manage project dependencies. Run the following command:
     ```
     conda create -p <Environment_Name> python==<python version> -y
     ```

3. **Activate the Virtual Environment** (Optional)

   - Activate the virtual environment based on your operating system:
     ```
     conda activate <Environment_Name>/
     ```

4. **Install Dependencies**

   - Navigate to the project directory:
     ```
     cd [project_directory]
     ```
   - Run the following command to install project dependencies:
     ```
     pip install -r requirements.txt
     ```

5. **Run the Project**

   - Start the project by running the appropriate command.
     ```
     python app.py
     ```

6. **Access the Project**
   - Open a web browser or the appropriate client to access the project.


## Setup

### MLflow Tracking

We use MLflow to log and track our machine learning experiments. The MLFLOW_TRACKING_URI environment variable is set to the DagsHub repository's MLflow tracking URI.

```bash
export MLFLOW_TRACKING_URI=<MLFLOW_TRACKING_URI>

export MLFLOW_TRACKING_USERNAME=<MLFLOW_TRACKING_USERNAME>

export MLFLOW_TRACKING_PASSWORD=<MLFLOW_TRACKING_PASSWORD>
```

## Usage and Configuration

This project requires Amazon Web Services Access Key ID and Secret Access Key for interacting with AWS services. Follow these steps to configure your project to use AWS keys:

1. **Obtain Your AWS Access Key ID and Secret Access Key**:

   - Log in to the AWS Management Console.
   - Open the IAM (Identity and Access Management) dashboard.
   - Create a new IAM user or use an existing one.
   - Attach the necessary policies to the user.
   - Generate an access key for the user. Save these keys securely.

2. **Configuration**:
   - Store your AWS Access Key ID and Secret Access Key securely. Do not hardcode them directly in your code or expose them in public repositories. Instead, use environment variables or a configuration file to manage them securely.

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

