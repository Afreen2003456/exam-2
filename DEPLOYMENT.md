# 🚀 Deployment Guide: Airline Data Analytics Dashboard

## 📋 Quick Deploy Options

### Option 1: Deploy to Render (Recommended - Free)

1. **Create GitHub Repository:**
   ```bash
   # Push your code to GitHub (follow GitHub steps below)
   ```

2. **Deploy to Render:**
   - Go to [render.com](https://render.com)
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Use these settings:
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 4`
     - **Environment**: `Python 3`
   - Click "Deploy"

### Option 2: Deploy to Railway

1. **Deploy to Railway:**
   - Go to [railway.app](https://railway.app)
   - Click "Deploy from GitHub repo"
   - Connect your repository
   - Railway will auto-detect Python and deploy

### Option 3: Deploy to Heroku

1. **Deploy to Heroku:**
   - Install Heroku CLI
   - Login: `heroku login`
   - Create app: `heroku create your-airline-dashboard`
   - Push: `git push heroku main`

## 📱 GitHub Repository Setup

### Step 1: Create Repository on GitHub
1. Go to [github.com](https://github.com)
2. Click "+" → "New repository"
3. Name: `airline-data-analytics-dashboard`
4. Description: `🛩️ Global airline data analytics web application with worldwide flight insights`
5. Make it **Public**
6. Click "Create repository"

### Step 2: Push Your Code
```bash
# Add GitHub remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/airline-data-analytics-dashboard.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## 🌐 Environment Variables for Deployment

Set these environment variables in your deployment platform:

```
FLASK_ENV=production
HOST=0.0.0.0
PORT=8080
SECRET_KEY=your-secure-random-key
AVIATIONSTACK_API_KEY=your_api_key_optional
```

## 🛠️ Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py

# Access at: http://localhost:8080
```

## 🎯 Features

- ✈️ **300 Worldwide Flights**: Global route data
- 🌍 **54 International Airports**: Major global hubs
- 🏢 **45 Global Airlines**: From all continents
- 📊 **Interactive Charts**: Real-time visualizations
- 🔍 **Advanced Filtering**: Search by routes and airports
- 📱 **Mobile Responsive**: Works on all devices

## 🚀 Live Demo URLs (After Deployment)

- **Render**: `https://your-app-name.onrender.com`
- **Railway**: `https://your-app-name.up.railway.app`
- **Heroku**: `https://your-app-name.herokuapp.com`

## 📞 Support

- Check logs in your deployment platform
- Ensure all environment variables are set
- Verify requirements.txt includes all dependencies

---

**Built with ❤️ using Flask, Python, and modern web technologies** 