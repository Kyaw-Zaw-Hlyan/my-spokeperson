# My Spokeperson - Premium Content Management System

A full-stack web application for managing and storing premium content with a modern React frontend and FastAPI backend, integrated with Supabase storage.

## 🎯 Project Overview

**My Spokeperson** is a content management application that allows users to:
- Submit content with automatic word count validation (max 150 words)
- Save content securely to Supabase cloud storage
- Retrieve stored content by subject
- Real-time feedback and validation

### Key Features
- ✅ **FastAPI Backend** - High-performance Python API
- ✅ **React Frontend** - Modern, responsive UI with real-time word count
- ✅ **Supabase Integration** - Cloud storage for all content
- ✅ **CORS Enabled** - Full cross-origin support for local development
- ✅ **Input Validation** - Subject and content validation
- ✅ **Word Count Tracking** - Real-time word counting (max 150 words)
- ✅ **Error Handling** - Comprehensive error feedback
- ✅ **Beautiful UI** - Premium dark theme with glass morphism design

---

## 📁 Project Structure

```
my-spokeperson/
├── main folder/
│   ├── app.py              # FastAPI backend server
│   └── README.md           # Project documentation
├── api/
│   └── index.py            # Vercel serverless function entry point
├── Frontend/
│   └── UI_app/
│       ├── package.json    # React dependencies
│       ├── public/
│       │   └── index.html  # HTML entry point
│       └── src/
│           ├── index.js    # React DOM render
│           ├── App.jsx     # Main App component
│           └── App.css     # Styling
├── data storage/           # Sample data files (generated at runtime)
├── .env                    # Environment variables (NEVER commit)
├── .gitignore              # Git ignore rules
└── venv/                   # Python virtual environment
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn
- Supabase account with project setup

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/Kyaw-Zaw-Hlyan/my-spokeperson.git
cd my-spokeperson
```

#### 2. Setup Python Backend
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn supabase python-dotenv pydantic

# Create .env file with your Supabase credentials
echo SUPABASE_URL=your_url > .env
echo SUPABASE_KEY=your_key >> .env
```

#### 3. Setup React Frontend
```bash
cd Frontend/UI_app

# Install dependencies
npm install

# Start development server (runs on http://localhost:3000)
npm start
```

#### 4. Run FastAPI Server
```bash
cd main\ folder

# Start server (runs on http://localhost:8000)
python app.py
```

---

## 📡 API Endpoints

### 1. **POST /api/save**
Save new content to Supabase

**Request:**
```json
{
  "subject": "Machine Learning",
  "content": "Machine learning is a subset of artificial intelligence..."
}
```

**Response (Success):**
```json
{
  "message": "Content saved successfully to Supabase: Machine Learning.txt",
  "word_count": 45,
  "subject": "Machine Learning"
}
```

**Validation Rules:**
- Subject: Required, cannot be empty
- Content: Required, cannot be empty
- Word Count: Maximum 150 words

### 2. **GET /api/read/{subject}**
Retrieve content by subject

**Response:**
```json
{
  "subject": "Machine Learning",
  "content": "Machine learning is a subset of artificial intelligence...",
  "word_count": 45
}
```

### 3. **GET /**
Health check endpoint

**Response:**
```json
{
  "message": "FastAPI server is running"
}
```

---

## 🎨 Frontend Components

### App Component (`src/App.jsx`)
Main React component featuring:
- Subject input field
- Content textarea with real-time word count
- Submit button (disabled when word limit exceeded)
- Feedback messages for success/error states
- Loading state during API calls

### Styling (`src/App.css`)
- Dark gradient background with animated floating elements
- Glass morphism card design
- Responsive layout for mobile and desktop
- Premium animations and transitions
- Error state styling with visual feedback

---

## 🔧 Environment Variables

Create a `.env` file in the project root:

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-public-key
```

**⚠️ Important:** `.env` is in `.gitignore` - never commit credentials to GitHub!

---

## 🌐 Deployment to Vercel

### Prerequisites
- Vercel account
- GitHub repository connected to Vercel

### Steps

1. **Connect Repository**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Select your GitHub repository
   - Authorize Vercel

2. **Configure Environment Variables**
   - In Vercel project settings → Environment Variables
   - Add `SUPABASE_URL` and `SUPABASE_KEY`

3. **Set Build Command**
   - Build Command: `cd Frontend/UI_app && npm install && npm run build`
   - Output Directory: `Frontend/UI_app/build`

4. **Deploy**
   - Push to main branch
   - Vercel automatically deploys
   - Get your live URL

### API Deployment
- FastAPI endpoint via `/api/index.py` (Vercel serverless function)
- Update React frontend to call deployed API instead of localhost

---

## 📝 Development Workflow

### Local Development
```bash
# Terminal 1: Start FastAPI backend
cd "main folder"
python app.py

# Terminal 2: Start React frontend
cd Frontend/UI_app
npm start

# Open http://localhost:3000 in browser
```

### Git Workflow
```bash
# Make changes
git add .
git commit -m "Your descriptive message"
git push origin main
```

---

## 🔐 Security Notes

- ✅ Environment variables are properly secured in `.gitignore`
- ✅ CORS is configured for localhost only in development
- ✅ Input validation on both frontend and backend
- ✅ Supabase provides row-level security
- ⚠️ Update CORS origins when deploying to production

---

## 🐛 Troubleshooting

### "Permission denied" on git push
- Generate Personal Access Token on GitHub
- Update remote URL with token
- See [GitHub Token Setup](#)

### CORS errors in console
- Ensure FastAPI is running on `http://localhost:8000`
- Check CORS middleware configuration in `app.py`
- Verify frontend origin is in allowed list

### Supabase connection errors
- Verify `.env` file exists and has correct credentials
- Check Supabase project status
- Ensure bucket name "Business Contents" exists

### Word count not working
- Clear browser cache
- Ensure latest version of App.jsx is loaded
- Check browser console for JavaScript errors

---

## 📦 Dependencies

### Backend
- **fastapi**: 0.109+ (High-performance Python web framework)
- **uvicorn**: 0.27+ (ASGI server)
- **supabase**: 2.0+ (Supabase client)
- **python-dotenv**: 1.0+ (Environment variable management)
- **pydantic**: 2.0+ (Data validation)

### Frontend
- **react**: 18.2.0+
- **react-dom**: 18.2.0+
- **react-scripts**: 5.0.1+

---

## 📄 File Descriptions

| File | Purpose |
|------|---------|
| `main folder/app.py` | FastAPI backend with CORS, Supabase integration |
| `api/index.py` | Vercel serverless function wrapper |
| `Frontend/UI_app/src/App.jsx` | Main React component with form logic |
| `Frontend/UI_app/src/App.css` | Premium styling and animations |
| `.gitignore` | Excludes sensitive files from git |
| `.env` | Local environment variables (not committed) |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

This project is open source and available under the MIT License.

---

## 📧 Contact & Support

For issues, questions, or suggestions:
- GitHub Issues: [Open an issue](https://github.com/Kyaw-Zaw-Hlyan/my-spokeperson/issues)
- Email: your-email@example.com

---

## 🎓 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Supabase Guide](https://supabase.com/docs)
- [Vercel Deployment Guide](https://vercel.com/docs)

---

**Last Updated:** February 7, 2026
**Project Status:** Active Development
