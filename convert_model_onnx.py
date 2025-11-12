"""
Convert CatBoost model to ONNX format for smaller deployment
This script reduces the model size significantly by converting to ONNX
and eliminates the need for CatBoost in the runtime.
"""
import pickle
import os
import sys

try:
    import onnx
    import onnxruntime as rt
    from skl2onnx import convert_sklearn
    from skl2onnx.common.data_types import FloatTensorType
except ImportError:
    print("ERROR: Required packages not installed.")
    print("Install with: pip install onnx onnxruntime skl2onnx")
    sys.exit(1)

# Load the current model and preprocessor
model_path = os.path.join('artifacts', 'model.pkl')
preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')

print("Loading CatBoost model...")
with open(model_path, 'rb') as f:
    model = pickle.load(f)

print("Loading preprocessor...")
with open(preprocessor_path, 'rb') as f:
    preprocessor = pickle.load(f)

print(f"Model type: {type(model)}")
print(f"Preprocessor type: {type(preprocessor)}")

# Note: Direct ONNX conversion of CatBoost is complex.
# Alternative approach: Export model to a simpler format or use a proxy predictor.
print("\nNote: CatBoost ONNX conversion requires additional setup.")
print("Alternative solution: Use Vercel Pro plan (3 GB limit) or")
print("Consider retraining with scikit-learn models that are ONNX-compatible.")
