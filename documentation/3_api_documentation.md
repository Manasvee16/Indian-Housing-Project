# API Documentation

## Overview
This document describes the API endpoints available in the Indian Housing Project. The API provides functionality for predicting house prices based on various input parameters.

## Base URL
For local development: `http://localhost:8080`

## Endpoints

### 1. Predict House Price
Predicts the price of a house based on input parameters.

#### Endpoint: `/`
- **Method**: POST
- **Content-Type**: application/x-www-form-urlencoded

#### Request Parameters

| Parameter | Type    | Description                                    | Required |
|-----------|---------|------------------------------------------------|----------|
| lcr       | float   | Local Crime Rate                               | Yes      |
| lpz       | float   | Large Plot Zoning                              | Yes      |
| ia        | float   | Industrial Area                                | Yes      |
| wp        | float   | Waterfront Property                            | Yes      |
| pl        | float   | Pollution Level                                | Yes      |
| rph       | float   | Average Rooms per House                        | Yes      |
| age       | float   | Property Age                                   | Yes      |
| dis       | float   | Distance to Employment Hubs                    | Yes      |
| ha        | float   | Highway Accessibility                          | Yes      |
| tax       | float   | Full-value property tax rate per ₹10,00,000   | Yes      |
| ptratio   | float   | School Pupil-Teacher Ratio                     | Yes      |
| ld        | float   | Local Demographics                             | Yes      |
| lip       | float   | Lower Income Population                        | Yes      |

#### Example Request
```bash
curl -X POST http://localhost:8080 \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "lcr=0.5&lpz=0.3&ia=0.2&wp=0&pl=0.4&rph=6.5&age=30&dis=5.2&ha=0.8&tax=300&ptratio=15.3&ld=0.6&lip=0.2"
```

#### Response
Returns a webpage with the predicted house price in ₹1,00,000s.

Example Response:
```
25.40
```

### 2. Get Prediction Form
Retrieves the HTML form for entering prediction parameters.

#### Endpoint: `/`
- **Method**: GET
- **Content-Type**: text/html

#### Response
Returns an HTML page containing the prediction form.

## Error Handling

The API returns appropriate HTTP status codes:

- 200: Successful request
- 400: Bad request (invalid parameters)
- 500: Internal server error

Error responses include a message explaining the error.

Example error response:
```json
{
    "error": "Invalid input parameters",
    "message": "All fields must be numeric values"
}
```

## Rate Limiting
- Maximum 100 requests per minute per IP address
- Excess requests will receive a 429 (Too Many Requests) response

## Data Validation
- All numeric fields must be positive numbers
- Missing fields will result in a 400 Bad Request response
- Invalid data types will result in a 400 Bad Request response

## Security
- The API implements basic input validation
- All inputs are sanitized before processing
- CORS is enabled for web clients

## Testing the API
You can use the provided test suite:

```bash
python -m pytest tests/test_api.py
```

## Changelog

### Version 1.0.0
- Initial release
- Basic prediction functionality
- Form-based interface

## Support
For API support, please contact the development team or raise an issue on the project's GitHub repository.