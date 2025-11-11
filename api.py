"""
Vercel-compatible Flask app with proper serverless handling
"""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

try:
    from src.pipelines.Prediction_Pipleline import CustomData, PredictPipeline
except ImportError as e:
    print(f"Import Error: {e}")
    # Fallback for missing modules
    PredictPipeline = None
    CustomData = None

app = Flask(__name__, 
            template_folder='templates',
            static_folder='static',
            static_url_path='/static')

# Enable CORS for cross-origin requests
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def predict_datapoints():
    """Main prediction endpoint"""
    try:
        if request.method == 'GET':
            # Return the form
            return render_template('index.html')
        
        # POST request - make prediction
        if request.method == 'POST':
            try:
                # Get form data
                form_data = {
                    'lcr': float(request.form.get('lcr', 0)),
                    'lpz': float(request.form.get('lpz', 0)),
                    'ia': float(request.form.get('ia', 0)),
                    'wp': float(request.form.get('wp', 0)),
                    'pl': float(request.form.get('pl', 0)),
                    'rph': float(request.form.get('rph', 0)),
                    'age': float(request.form.get('age', 0)),
                    'dis': float(request.form.get('dis', 0)),
                    'ha': float(request.form.get('ha', 0)),
                    'tax': float(request.form.get('tax', 0)),
                    'ptratio': float(request.form.get('ptratio', 0)),
                    'ld': float(request.form.get('ld', 0)),
                    'lip': float(request.form.get('lip', 0))
                }
                
                # Create prediction data
                data = CustomData(**form_data)
                pred_df = data.get_data_as_dataframe()
                
                # Make prediction
                predict_pipeline = PredictPipeline()
                result = predict_pipeline.predict(pred_df)
                formatted_result = f"{result[0]:.2f}"
                
                # Return result
                return render_template('index.html', results=formatted_result)
                
            except Exception as e:
                error_msg = f"Error during prediction: {str(e)}"
                return render_template('index.html', error=error_msg), 500
    
    except Exception as e:
        error_msg = f"Server error: {str(e)}"
        return jsonify({"error": error_msg}), 500

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """JSON API endpoint for predictions"""
    try:
        data = request.get_json()
        
        custom_data = CustomData(
            lcr=float(data.get('lcr', 0)),
            lpz=float(data.get('lpz', 0)),
            ia=float(data.get('ia', 0)),
            wp=float(data.get('wp', 0)),
            pl=float(data.get('pl', 0)),
            rph=float(data.get('rph', 0)),
            age=float(data.get('age', 0)),
            dis=float(data.get('dis', 0)),
            ha=float(data.get('ha', 0)),
            tax=float(data.get('tax', 0)),
            ptratio=float(data.get('ptratio', 0)),
            ld=float(data.get('ld', 0)),
            lip=float(data.get('lip', 0))
        )
        
        pred_df = custom_data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(pred_df)
        
        return jsonify({
            "success": True,
            "prediction": float(result[0]),
            "formatted": f"{result[0]:.2f}"
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for Vercel"""
    return jsonify({"status": "healthy"}), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({"error": "Internal server error"}), 500

# Vercel handler
handler = app

# Development server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
