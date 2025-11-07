# Developer Guide

## Project Structure

```
Indian_Housing_Project/
├── Artifacts/               # Model artifacts and processed data
├── dataset/                 # Raw dataset files
├── documentation/           # Project documentation
├── notebooks/              # Jupyter notebooks for analysis
├── src/                    # Source code
│   ├── components/         # Core components
│   ├── pipelines/         # Processing pipelines
│   └── utils/             # Utility functions
├── static/                # Static files (CSS, JS)
├── templates/             # HTML templates
├── tests/                 # Test files
└── app.py                 # Main application file
```

## Code Style Guidelines

### Python Code Style
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Include docstrings for classes and functions
- Maximum line length: 79 characters
- Use 4 spaces for indentation

Example:
```python
def calculate_metric(data: pd.DataFrame) -> float:
    """
    Calculate performance metric for the model.

    Args:
        data (pd.DataFrame): Input data for calculation

    Returns:
        float: Calculated metric value
    """
    return metric_value
```

### Documentation Standards
- Use docstrings for all public functions and classes
- Include type hints for function parameters
- Document exceptions that may be raised
- Add inline comments for complex logic

## Development Workflow

### 1. Setting Up Development Environment
```bash
# Create virtual environment
conda create -p venv python==3.8 -y
conda activate venv/

# Install dependencies
pip install -r requirements.txt
```

### 2. Making Changes

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes following the code style guidelines

3. Run tests:
   ```bash
   pytest tests/
   ```

4. Update documentation if needed

### 3. Commit Guidelines

- Use clear, descriptive commit messages
- Follow conventional commits format:
  ```
  feat: add new prediction feature
  fix: correct data transformation bug
  docs: update API documentation
  test: add tests for model evaluation
  ```

### 4. Pull Request Process

1. Update your branch with main:
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. Push your changes:
   ```bash
   git push origin feature/your-feature-name
   ```

3. Create a Pull Request with:
   - Clear description of changes
   - Any related issues
   - Test results
   - Documentation updates

## Testing

### Unit Tests
- Write tests for all new features
- Place tests in the `tests/` directory
- Use pytest for testing
- Maintain test coverage above 80%

Example test:
```python
def test_data_transformation():
    # Arrange
    data = load_test_data()
    
    # Act
    result = transform_data(data)
    
    # Assert
    assert result.shape[0] == data.shape[0]
    assert "transformed_column" in result.columns
```

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_transformation.py

# Run with coverage report
pytest --cov=src tests/
```

## Debugging

### Logging
- Use the built-in logging system
- Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
- Log files are stored in `logs/`

Example:
```python
from src.logger import logging

logging.info("Starting data transformation")
try:
    # Your code here
    logging.debug("Transformation completed")
except Exception as e:
    logging.error(f"Error in transformation: {str(e)}")
```

### Error Handling
- Use custom exceptions when appropriate
- Handle exceptions at appropriate levels
- Log all errors with context

Example:
```python
from src.exception import CustomException

try:
    # Your code here
except Exception as e:
    raise CustomException(e, sys)
```

## Performance Considerations

### Data Processing
- Use efficient data structures
- Implement batch processing for large datasets
- Consider memory usage in transformations

### Model Training
- Use appropriate batch sizes
- Implement early stopping
- Monitor resource usage

## Deployment

### Local Deployment
```bash
python app.py
```

### Production Deployment
Refer to the deployment documentation for detailed instructions.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Follow coding standards
4. Write/update tests
5. Update documentation
6. Submit pull request

## Support

- Check existing issues on GitHub
- Contact the development team
- Review the documentation