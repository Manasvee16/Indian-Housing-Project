# Setup and Installation Guide

## Prerequisites

- Python 3.x
- Git
- Conda (recommended) or virtualenv
- AWS account (for production deployment)

## Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Manasvee16/Indian-Housing-Project
cd Indian-Housing-Project
```

### 2. Environment Setup

#### Using Conda (Recommended)
```bash
conda create -p <Environment_Name> python==3.10 -y
conda activate <Environment_Name>/
```

#### Using virtualenv (Alternative)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

### 1. Environment Variables

Create a `.env` file in the project root with the following configurations:

```env
MLFLOW_TRACKING_URI=<your_mlflow_tracking_uri>
MLFLOW_TRACKING_USERNAME=<your_username>
MLFLOW_TRACKING_PASSWORD=<your_password>
```

### 2. AWS Configuration

1. Set up AWS credentials:
   ```bash
   aws configure
   ```
   Enter your:
   - AWS Access Key ID
   - AWS Secret Access Key
   - Default region
   - Output format

2. Or set environment variables:
   ```bash
   export AWS_ACCESS_KEY_ID=<your_access_key>
   export AWS_SECRET_ACCESS_KEY=<your_secret_key>
   ```

## Running the Application

### 1. Development Server

```bash
python app.py
```
The application will be available at `http://localhost:8080`

### 2. Running Tests

```bash
pytest tests/
```

### 3. Training the Model

```bash
python src/pipelines/Training_pipeline.py
```

## MLflow Setup

1. Start MLflow tracking server:
   ```bash
   mlflow server --backend-store-uri <your_storage_location> --default-artifact-root <your_artifact_location>
   ```

2. Access MLflow UI at `http://localhost:5000`

## Troubleshooting

### Common Issues

1. **Package Installation Failures**
   - Ensure you're using the correct Python version
   - Try upgrading pip: `pip install --upgrade pip`
   - Install system dependencies if required

2. **MLflow Connection Issues**
   - Verify MLflow tracking URI is correct
   - Check network connectivity
   - Ensure credentials are properly set

3. **Model Training Errors**
   - Verify data files are in the correct location
   - Check available system memory
   - Ensure all required dependencies are installed

### Getting Help

- Check the project's GitHub Issues page
- Review the error logs in `logs/` directory
- Contact the development team

## Production Deployment

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t indian-housing-project .
   ```

2. Run the container:
   ```bash
   docker run -p 8080:8080 indian-housing-project
   ```

### AWS Deployment

Refer to the separate AWS deployment guide in the `documentation/deployment/` directory.