# Step-by-Step Vercel Deployment Guide

## Prerequisites

- Vercel account (free tier works fine)
- GitHub account with your project pushed
- Git installed locally

## Option 1: Automatic Deployment (Recommended)

### Step 1: Connect GitHub to Vercel
1. Go to https://vercel.com/dashboard
2. Click **"New Project"**
3. Click **"Import Git Repository"**
4. Select **GitHub** and authorize if needed
5. Find and select `Indian-Housing-Project`
6. Click **"Import"**

### Step 2: Configure Project
- Framework: **Other** (Flask)
- Root Directory: **./** (default)
- Build Command: **Already set in vercel.json** ✓
- Output Directory: **.vercel_build_output** (leave default)

### Step 3: Deploy
- Click **"Deploy"**
- Wait 2-5 minutes for build
- You'll get a live URL like: `https://indian-housing-project-xyz.vercel.app`

✅ **Done!** Auto-deployments enabled on GitHub push

---

## Option 2: Manual Deployment (CLI)

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Login
```bash
vercel login
```
- Select GitHub authentication
- Complete the browser flow

### Step 3: Deploy to Staging
```bash
cd c:\Users\manas\Downloads\archive\Indian-Housing-Project
vercel
```
- Select: **Yes, link to existing project**
- Or: Create new project
- Staging URL generated in ~2 minutes

### Step 4: Deploy to Production
```bash
vercel --prod
```
- Production URL will be your final deployment

---

## Option 3: GitHub Actions (Advanced)

Automatic deployment on every git push:

1. Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy to Vercel
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Vercel
        run: npx vercel --prod
        env:
          VERCEL_TOKEN: ${{ secrets.VERCEL_TOKEN }}
          VERCEL_PROJECT_ID: ${{ secrets.VERCEL_PROJECT_ID }}
          VERCEL_ORG_ID: ${{ secrets.VERCEL_ORG_ID }}
```

2. Add GitHub secrets (from Vercel Dashboard)
3. Push to main → Auto-deployment

---

## Testing Your Deployment

### 1. Test Web Form
```
Visit: https://your-domain/
Fill form and click "Predict Price"
```

### 2. Test API
```powershell
$headers = @{"Content-Type"="application/json"}
$body = @{
    lcr = 0.1
    lpz = 0.1
    ia = 0.1
    wp = 0
    pl = 0.1
    rph = 5
    age = 50
    dis = 5
    ha = 1
    tax = 300
    ptratio = 15
    ld = 30
    lip = 10
} | ConvertTo-Json

Invoke-WebRequest `
  -Uri "https://your-domain/api/predict" `
  -Method POST `
  -Headers $headers `
  -Body $body
```

### 3. Health Check
```bash
curl https://your-domain/health
```
Expected response: `{"status":"healthy"}`

---

## Project Structure After Deploy

```
Your Vercel Domain (e.g., indian-housing-project.vercel.app)
├── GET  /              → Show web form
├── POST /              → Handle form predictions
├── POST /api/predict   → JSON API predictions
└── GET  /health        → Health check endpoint
```

---

## Environment Variables (Optional)

If you need to add environment variables:

1. Go to Vercel Dashboard
2. Select your project
3. Settings → Environment Variables
4. Add:
   ```
   PYTHON_VERSION=3.10
   FLASK_ENV=production
   ```
5. Redeploy: Click "Deployments" → Select latest → Click "Redeploy"

---

## Monitoring & Logs

### View Deployment Logs
1. Vercel Dashboard
2. Your Project
3. Deployments tab
4. Click latest deployment
5. View build and runtime logs

### Common Issues & Fixes

| Issue | Solution |
|-------|----------|
| Build failed | Check logs for error, usually missing imports |
| "Model not found" | Ensure `artifacts/` folder is in git |
| Timeout | Already fixed with reduced dependencies |
| 404 error | Check route paths in api.py |
| CORS errors | Already handled in api.py |

---

## Useful Commands

```bash
# Check deployment status
vercel status

# View logs
vercel logs

# List deployments
vercel list

# Delete a deployment
vercel remove <url>

# View project settings
vercel env ls
```

---

## Performance Tips

1. **Cold Start**: First request takes 5-10s (normal for serverless)
2. **Caching**: Enable Vercel caching in settings for faster builds
3. **Regions**: Deploy to nearest region for lower latency
4. **Monitoring**: Use Vercel Analytics for performance insights

---

## Support & Troubleshooting

### Where to Find Errors
1. **Build Failed**: Vercel Dashboard → Deployments → Logs
2. **Runtime Error**: Vercel Dashboard → Functions → Logs
3. **Local Testing**: Run `python api.py` locally first

### Getting Help
- Vercel Docs: https://vercel.com/docs
- GitHub Issues: Check project repository
- Local Testing: Run `python api.py` to verify

---

## Success! 🎉

Once deployed:
- Share URL with users
- API endpoint ready for integration
- Auto-scaling on high traffic
- Free HTTPS certificate included
- Monitoring and analytics available

Your Indian Housing Price Prediction app is now live! 🚀
