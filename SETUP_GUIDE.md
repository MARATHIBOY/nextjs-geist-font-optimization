# Sign Language Recognition App - Setup Guide

## 🚨 **Issue: Not Getting Gestures Recognized**

The application is working correctly, but you're seeing 401 errors because the OpenRouter API key is missing. Here's how to fix this:

## ✅ **Step-by-Step Setup:**

### **1. Get Your OpenRouter API Key**
1. Go to [OpenRouter.ai](https://openrouter.ai)
2. Sign up for a free account
3. Navigate to your dashboard
4. Copy your API key (starts with `sk-or-...`)

### **2. Configure Your API Key**
1. Open the `.env.local` file in your project root
2. Replace `your_openrouter_api_key_here` with your actual API key:
   ```
   OPENROUTER_API_KEY=sk-or-your-actual-key-here
   ```

### **3. Restart the Application**
1. Stop the current dev server (Ctrl+C)
2. Run `npm run dev` again
3. Visit `http://localhost:8000/sign-language`

### **4. Test the Recognition**
1. Click "Start Recognition"
2. Allow camera access
3. Make clear sign language gestures
4. You should see recognized text appear

## 🔧 **Troubleshooting Tips:**

### **If Still Not Working:**
- **Check API Key**: Ensure the key is correctly copied without extra spaces
- **Check Console**: Open browser dev tools (F12) to see detailed errors
- **Test API**: Try a simple gesture like "hello" or "thank you"
- **Lighting**: Ensure good lighting on your hands
- **Distance**: Keep hands 1-3 feet from camera

### **Common Issues:**
- **401 Error**: API key not configured
- **No Recognition**: API key might be invalid or expired
- **Camera Issues**: Check browser permissions

## 📱 **Testing Gestures:**
Try these basic signs for testing:
- **Hello**: Wave your hand
- **Thank you**: Touch chin and move hand forward
- **Yes**: Nodding gesture
- **No**: Shaking head gesture

## 🎯 **Expected Behavior:**
Once configured, you should see:
1. "Recognizing..." briefly appears
2. Recognized text shows up
3. Voice speaks the recognized text

The application is fully functional - you just need to add your API key to start recognizing gestures!
