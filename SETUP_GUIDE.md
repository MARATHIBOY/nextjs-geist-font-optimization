# Sign Language Recognition App - Setup Guide

## 🚨 **Issue: Not Getting Gestures Recognized**

The application is working correctly, but you're seeing 401 errors because the OpenRouter API key is missing. Here's how to fix this:

## ✅ **Step-by-Step Setup:**

### **1. Install Prerequisites**
Before starting, ensure you have:
- **Node.js** (version 16 or higher)
- **Python 3.7+** (required for session export feature)

To check if Python is installed:
```bash
python3 --version
# Should show Python 3.7.0 or higher
```

If Python is not installed:
- **Windows**: Download from [python.org](https://python.org)
- **macOS**: Use `brew install python3` or download from python.org
- **Linux**: Use `sudo apt install python3` (Ubuntu/Debian) or equivalent

### **2. Get Your OpenRouter API Key**
1. Go to [OpenRouter.ai](https://openrouter.ai)
2. Sign up for a free account
3. Navigate to your dashboard
4. Copy your API key (starts with `sk-or-...`)

### **3. Configure Your API Key**
1. Open the `.env.local` file in your project root
2. Replace `your_openrouter_api_key_here` with your actual API key:
   ```
   OPENROUTER_API_KEY=sk-or-your-actual-key-here
   ```

### **4. Install Dependencies**
```bash
npm install
```

### **5. Start the Application**
1. Run the development server:
   ```bash
   npm run dev
   ```
2. Visit `http://localhost:8000/sign-language`

### **6. Test the Recognition**
1. Click "Start Recognition"
2. Allow camera access
3. Make clear sign language gestures
4. You should see recognized text appear

## 🆕 **New Feature: Session Data Export**

The app now includes a powerful session export feature that saves your recognition data as Python pickle files:

### **How to Use:**
1. Start a recognition session and make some gestures
2. Click "Download Session" to export your data
3. A `.pkl` file will be downloaded to your computer

### **What's Included in the Export:**
- Session ID and timestamps
- All recognized signs with individual timestamps
- Session metadata (browser info, app version)
- Total recognition count

### **Using Exported Data:**
```python
import pickle

# Load your session data
with open('session_data_[timestamp].pkl', 'rb') as f:
    data = pickle.load(f)

# Analyze your session
print(f"Total signs recognized: {data['totalRecognitions']}")
for sign in data['recognizedTexts']:
    print(f"{sign['timestamp']}: {sign['text']}")
```

## 🔧 **Troubleshooting Tips:**

### **Recognition Issues:**
- **Check API Key**: Ensure the key is correctly copied without extra spaces
- **Check Console**: Open browser dev tools (F12) to see detailed errors
- **Test API**: Try a simple gesture like "hello" or "thank you"
- **Lighting**: Ensure good lighting on your hands
- **Distance**: Keep hands 1-3 feet from camera

### **Export Issues:**
- **Python Not Found**: Ensure Python 3.7+ is installed and accessible as `python3`
- **Permission Errors**: Check that the app has write permissions
- **No Data**: You need to have some recognized signs before exporting
- **Browser Issues**: Try a different browser if downloads fail

### **Common Error Messages:**
- **401 Error**: API key not configured or invalid
- **"Python process timeout"**: Python installation issue or system overload
- **"No session data to export"**: Start recognition and make some gestures first
- **Camera Issues**: Check browser permissions for camera access

## 📱 **Testing Gestures:**
Try these basic signs for testing:
- **Hello**: Wave your hand
- **Thank you**: Touch chin and move hand forward
- **Yes**: Nodding gesture
- **No**: Shaking head gesture
- **Please**: Circular motion on chest
- **Sorry**: Fist on chest, circular motion

## 🎯 **Expected Behavior:**
Once configured, you should see:
1. "Recognizing..." briefly appears during processing
2. Recognized text shows up in the display area
3. Voice speaks the recognized text automatically
4. Session summary shows recognition count
5. Export button becomes enabled after first recognition

## 🔍 **Advanced Features:**

### **Session Management:**
- **Session Logs**: View recent recognitions in the session summary
- **Clear Session**: Reset all session data with one click
- **Continuous Recognition**: App captures gestures every 3 seconds during active sessions

### **Data Analysis:**
The exported pickle files can be used for:
- Personal progress tracking
- Research and analysis
- Integration with other Python tools
- Machine learning model training data

## 🚀 **Performance Tips:**
- Close other camera-using applications
- Use good lighting for better recognition accuracy
- Keep background simple and uncluttered
- Make gestures clearly and hold briefly
- Wait for "Recognizing..." to complete before next gesture

The application is fully functional - you just need to add your API key and ensure Python is installed to use all features!
