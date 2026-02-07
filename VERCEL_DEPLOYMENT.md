# 🚀 Vercel Deployment Guide for My Spokeperson

Complete step-by-step instructions to deploy your full-stack application to Vercel.

---

## ✅ Pre-Deployment Checklist

Before deploying, ensure:

- [ ] GitHub repository is up-to-date: https://github.com/Kyaw-Zaw-Hlyan/my-spokeperson
- [ ] All code is committed and pushed to `main` branch
- [ ] `.env` file is in `.gitignore` (never commit credentials)
- [ ] `.gitignore` contains: `node_modules/`, `venv/`, `.env`, `build/`, `__pycache__/`
- [ ] Supabase project is active and bucket "Business Contents" exists
- [ ] You have Vercel account linked to GitHub

---

## 📋 Step-by-Step Deployment

### Step 1: Connect GitHub Repository to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click **"Add New..."** → **"Project"**
3. Click **"Import Git Repository"**
4. Search for **`my-spokeperson`** in your GitHub repos
5. Click **"Import"**

### Step 2: Configure Build Settings

In the import dialog, configure:

**Framework Preset:** Select **"Create React App"**

**Build Command:**
```bash
cd Frontend/UI_app && npm install && npm run build
```

**Output Directory:**
```
Frontend/UI_app/build
```

**Root Directory:** Leave as `.` (root)

### Step 3: Add Environment Variables

In the **Environment Variables** section, add:

```
SUPABASE_URL = https://okamezraqxjcotfpptaz.supabase.co
SUPABASE_KEY = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9rYW1lenJhcXhqY290ZnBwdGF6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njk3MjE4NjIsImV4cCI6MjA4NTI5Nzg2Mn0.GhwD13agUiJnK9k8LFTySo052jxKnky8uNRvsV4L3lo
```

⚠️ **Important:** In production, consider using Vercel's Secret Manager for sensitive keys.

### Step 4: Deploy

1. Click **"Deploy"**
2. Wait for build to complete (usually 2-3 minutes)
3. Once successful, you'll get a URL like: `https://my-spokeperson.vercel.app`

---

## 🔗 Update Frontend API URL

After deployment, update your React frontend to use the Vercel API endpoint:

**File:** `Frontend/UI_app/src/App.jsx` (around line 76)

**Replace:**
```javascript
const response = await fetch('http://127.0.0.1:8000/api/save', {
```

**With:**
```javascript
const response = await fetch('https://your-vercel-domain.vercel.app/api/save', {
```

Or use environment variables:
```javascript
const API_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:8000';
const response = await fetch(`${API_URL}/api/save`, {
```

Then add to `.env.local`:
```
REACT_APP_API_URL=https://your-vercel-domain.vercel.app
```

---

## 🔄 Automatic Deployments

Vercel automatically deploys when you push to the `main` branch:

```bash
# Make changes locally
git add .
git commit -m "Update feature"
git push origin main

# Vercel automatically builds and deploys!
# Check progress at https://vercel.com/dashboard
```

---

## 📊 Monitoring & Logs

### View Deployment Logs
1. Go to your Vercel project dashboard
2. Click **"Deployments"** tab
3. Click any deployment to see logs
4. Check **"Functions"** tab for serverless function logs

### View Build Logs
1. Go to **"Deployments"** → Click deployment
2. Scroll to **"Build Logs"** section
3. Expand to see full build output

### Monitor Performance
1. Go to **"Analytics"** tab
2. View real-time metrics:
   - Response times
   - Error rates
   - Bandwidth usage
   - Requests per minute

---

## 🐛 Troubleshooting Common Issues

### Build Fails: "Cannot find module 'react'"
**Solution:**
- Ensure `Frontend/UI_app/package.json` exists
- Check build command includes `npm install`
- Verify `package.json` is in correct directory

### Build Fails: "Python dependencies not found"
**Solution:**
- FastAPI isn't required for Vercel frontend deployment
- If deploying backend as serverless function, add `requirements.txt`

### Frontend loads but API calls fail
**Solution:**
- Check CORS configuration in backend
- Verify environment variables are set in Vercel
- Check browser console for exact error
- Ensure backend API is deployed/running

### "Module not found: App.css"
**Solution:**
- Verify CSS import path is correct
- Check file permissions
- Clear build cache and redeploy

---

## 🔐 Security Considerations

### Protect Sensitive Data
✅ Store secrets in Vercel Environment Variables, NOT in code
✅ Use `.gitignore` for `.env` files
✅ Rotate API keys regularly
✅ Use read-only API keys where possible

### CORS Configuration
Update `main folder/app.jsx` to allow your Vercel domain:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://your-vercel-domain.vercel.app"  # Add this
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE"],
    allow_headers=["*"],
)
```

---

## 📈 Performance Tips

### Frontend Optimization
- Enable code splitting with React.lazy()
- Optimize images (compress before uploading)
- Use CSS modules for smaller bundle
- Enable gzip compression (automatic on Vercel)

### Backend Optimization
- Cache Supabase responses
- Implement request rate limiting
- Use connection pooling for database
- Monitor API response times

### Vercel Configuration
Add `vercel.json` in root:

```json
{
  "builds": [
    {
      "src": "Frontend/UI_app/package.json",
      "use": "@vercel/static-builds"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "/api/index.py"
    },
    {
      "src": "/(.*)",
      "dest": "/index.html"
    }
  ]
}
```

---

## 🎯 Next Steps After Deployment

1. **Test Production**
   - Visit your Vercel URL
   - Test saving content
   - Check word count validation
   - Verify Supabase integration

2. **Set Up Custom Domain** (Optional)
   - In Vercel project settings → Domains
   - Add your custom domain
   - Configure DNS records

3. **Enable Analytics**
   - Vercel → Analytics → Enable
   - Track user behavior and performance

4. **Set Up Monitoring**
   - Enable real-time alerts
   - Monitor error rates
   - Track performance metrics

5. **Document Deployment**
   - Keep this guide updated
   - Document any custom configurations
   - Create deployment checklist for team

---

## 📞 Support & Resources

- **Vercel Docs:** https://vercel.com/docs
- **Vercel Status:** https://www.vercelstatus.com/
- **GitHub Issues:** https://github.com/Kyaw-Zaw-Hlyan/my-spokeperson/issues
- **React Deployment:** https://create-react-app.dev/deployment/vercel/

---

## ✨ You're Ready!

Your application is now live on Vercel! 🎉

**Your live URL:** `https://my-spokeperson.vercel.app`

**Repository:** https://github.com/Kyaw-Zaw-Hlyan/my-spokeperson

Share your app, monitor its performance, and iterate based on feedback!

---

*Last Updated: February 7, 2026*
