# Data Documentation

## Dataset Overview

### Source
- Dataset: Indian Housing Dataset
- Location: `dataset/IndianHousing.csv`
- Format: CSV
- Size: [Size in MB/GB]
- Records: [Number of records]

## Data Dictionary

### Features

| Feature Name | Description | Data Type | Range/Units | Notes |
|-------------|-------------|-----------|-------------|--------|
| LCR | Local Crime Rate | Float | 0-1 | Normalized crime rate in the area |
| LPZ | Large Plot Zoning | Float | 0-1 | Proportion of large residential plots |
| IA | Industrial Area | Float | 0-1 | Proximity to industrial zones |
| WP | Waterfront Property | Float | 0-1 | Binary indicator for waterfront |
| PL | Pollution Level | Float | 0-1 | Environmental pollution index |
| RPH | Rooms per House | Float | Positive | Average number of rooms |
| AGE | Property Age | Float | Years | Age of the property |
| DIS | Distance to Employment | Float | Kilometers | Distance to employment hubs |
| HA | Highway Accessibility | Float | 0-1 | Ease of highway access |
| TAX | Property Tax Rate | Float | ₹ | Per ₹10,00,000 |
| PTRATIO | Pupil-Teacher Ratio | Float | Ratio | School education quality indicator |
| LD | Local Demographics | Float | 0-1 | Demographic composition index |
| LIP | Lower Income Population | Float | 0-1 | Proportion of lower income residents |

### Target Variable

| Feature Name | Description | Data Type | Range/Units | Notes |
|-------------|-------------|-----------|-------------|--------|
| MEDV | Median Value | Float | ₹1,00,000s | Median value of owner-occupied homes |

## Data Processing Pipeline

### 1. Data Ingestion
- Source: `src/components/Data_ingestion.py`
- Process:
  1. Load raw data from CSV
  2. Split into training (80%) and test (20%) sets
  3. Save processed datasets in Artifacts directory

### 2. Data Transformation
- Source: `src/components/Data_transformation.py`
- Steps:
  1. Handle missing values
  2. Feature scaling
  3. Outlier detection and treatment
  4. Feature encoding (if applicable)

### 3. Data Quality Checks
- Null value detection
- Outlier identification
- Data type validation
- Range checks

## Data Preprocessing

### Missing Value Treatment
- Strategy: Mean/Median imputation
- Implementation: sklearn.impute
- Applicable features: All numeric features

### Feature Scaling
- Method: StandardScaler
- Implementation: sklearn.preprocessing
- Applied to: All numeric features
- Formula: z = (x - μ) / σ

### Outlier Treatment
- Detection: IQR method
- Treatment: Capping at 1.5 * IQR
- Implementation: Custom function in utils.py

## Data Flow

### Training Data Flow
```
Raw Data → Data Ingestion → Data Transformation → Model Training
```

### Prediction Data Flow
```
User Input → Data Validation → Preprocessing → Model Prediction
```

## Data Storage

### Directory Structure
```
Indian_Housing_Project/
├── dataset/
│   └── IndianHousing.csv      # Raw data
├── Artifacts/
│   ├── raw_data.csv           # Processed raw data
│   ├── train_data.csv         # Training dataset
│   └── test_data.csv          # Test dataset
```

### File Formats
- CSV files for raw and processed data
- Pickle files for preprocessed features
- JSON for configuration and metadata

## Data Validation Rules

### Input Validation
1. **Numeric Fields**
   - All features must be numeric
   - No negative values allowed
   - Must be within specified ranges

2. **Required Fields**
   - All fields are mandatory
   - No empty values allowed

### Quality Checks
1. **Range Validation**
   ```python
   assert 0 <= data['LCR'] <= 1
   assert data['RPH'] > 0
   assert data['AGE'] >= 0
   ```

2. **Type Validation**
   ```python
   assert data.dtypes['TAX'] in ['float64', 'float32']
   ```

## Data Update Process

### Frequency
- Dataset updates: Monthly
- Quality checks: Daily
- Validation rules: Quarterly review

### Update Procedure
1. Backup existing data
2. Load new data
3. Run validation checks
4. Process through pipeline
5. Update production dataset

## Data Security

### Access Control
- Raw data: Restricted access
- Processed data: Team access
- Production data: Service account access

### Data Protection
- Encryption at rest
- Secure transfer protocols
- Regular backup procedures

## Monitoring and Maintenance

### Data Quality Monitoring
- Daily automated checks
- Weekly quality reports
- Monthly comprehensive review

### Performance Metrics
- Data processing time
- Memory usage
- Error rates
- Data drift detection

## Troubleshooting

### Common Issues
1. Missing Values
   - Check source data completeness
   - Verify transformation pipeline

2. Data Type Mismatches
   - Validate input data types
   - Check transformation functions

3. Range Violations
   - Verify input data ranges
   - Check scaling functions

### Resolution Steps
1. Identify error source
2. Review relevant logs
3. Apply appropriate fixes
4. Validate results
5. Update documentation

## Support

### Contact Information
- Data Team: [Contact details]
- Support Hours: [Hours]
- Emergency Contact: [Contact details]

### Documentation Updates
- Last Updated: [Date]
- Version: 1.0