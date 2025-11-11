# Vercel Deployment Guide

## Issues Fixed

1. ✅ **Import Error in app.py**: Removed incorrect import of `app` from flask
2. ✅ **Python Version Mismatch**: Updated vercel.json to use Python 3.10
3. ✅ **Missing Build Configuration**: Added buildCommand to vercel.json
4. ✅ **Dependencies**: Using core dependencies for faster deployment

## Deployment Steps

### 1. Install Vercel CLI (if not already installed)
```bash
npm install -g vercel
```

### 2. Login to Vercel
```bash
vercel login
```

### 3. Deploy the Project
```bash
vercel
```

Or deploy directly from GitHub:
```bash
vercel --prod
```

### 4. Set Environment Variables (if needed)
In Vercel Dashboard → Project Settings → Environment Variables, add:
- `PYTHON_VERSION=3.10` (already in vercel.json)

## Files Modified/Created

1. **app.py** - Fixed import statement
2. **vercel.json** - Updated configuration for latest Vercel Python runtime
3. **.vercelignore** - Excludes unnecessary files from deployment
4. **requirements-minimal.txt** - Optimized dependencies for faster deployment
5. **build.sh** - Build script for deployment

## Key Points

- The project uses Flask for the web framework
- Machine learning models are stored in `artifacts/` folder (model.pkl and preprocessor.pkl)
- Template files are in `templates/` folder
- Static CSS is in `static/` folder
- Python 3.10 is used for Vercel deployment

## Troubleshooting

If deployment still fails:

1. Check Vercel build logs for specific errors
2. Ensure all required files are in the repository:
   - artifacts/model.pkl
   - artifacts/preprocessor.pkl
   - templates/index.html
   - static/style.css

3. Try using the minimal requirements:
   ```bash
   vercel env add VERCEL_PYTHON_DEBUG_LOGS true
   ```

4. Check that the project is pushed to GitHub and connected to Vercel

## Local Testing Before Deployment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py
```

The app will be available at http://localhost:5000
