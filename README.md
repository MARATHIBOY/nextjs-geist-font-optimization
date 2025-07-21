# Sign Language Recognition App

This is a [Next.js](https://nextjs.org) project that provides real-time sign language recognition using AI. The app supports American Sign Language (ASL), British Sign Language (BSL), and Indian Sign Language (ISL) with voice output and session data export capabilities.

## Features

- **Real-time Recognition**: Live camera feed with AI-powered sign language recognition
- **Multi-language Support**: Supports ASL, BSL, and ISL
- **Voice Output**: Text-to-speech for recognized signs
- **Session Logging**: Track all recognized signs during a session
- **Data Export**: Export session data as Python pickle (.pkl) files for analysis
- **Modern UI**: Clean, responsive interface with dark mode support

## Prerequisites

- **Node.js** (version 16 or higher)
- **Python 3.7+** (required for pickle export functionality)
- **OpenRouter API Key** (for AI recognition)

## Getting Started

### 1. Install Dependencies

```bash
npm install
```

### 2. Configure API Key

1. Get your OpenRouter API key from [OpenRouter.ai](https://openrouter.ai)
2. Create a `.env.local` file in the project root
3. Add your API key:
   ```
   OPENROUTER_API_KEY=sk-or-your-actual-key-here
   ```

### 3. Run the Development Server

```bash
npm run dev
```

Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.

### 4. Access the Sign Language Recognition

Navigate to `/sign-language` to start using the recognition feature.

## Usage

1. **Start Recognition**: Click "Start Recognition" to begin capturing gestures
2. **Make Signs**: Position your hands clearly in front of the camera
3. **View Results**: Recognized text appears below the video feed
4. **Export Session**: Click "Download Session" to export your session data as a .pkl file
5. **Clear Session**: Reset the session logs with "Clear Session"

## Session Data Export

The app can export your recognition session as a Python pickle file containing:

- **Session ID**: Unique identifier for the session
- **Timestamps**: Start and end times
- **Recognition Data**: All recognized signs with timestamps
- **Metadata**: Browser info, app version, etc.

### Using Exported Data

```python
import pickle

# Load the exported session data
with open('session_data_[timestamp].pkl', 'rb') as f:
    session_data = pickle.load(f)

print(f"Total recognitions: {session_data['totalRecognitions']}")
print(f"Session duration: {session_data['startTime']} to {session_data['endTime']}")

# Access individual recognitions
for recognition in session_data['recognizedTexts']:
    print(f"{recognition['timestamp']}: {recognition['text']}")
```

## Project Structure

```
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   ├── recognize/     # AI recognition endpoint
│   │   │   └── export/        # Session export endpoint
│   │   ├── sign-language/     # Main recognition page
│   │   └── page.tsx           # Home page
│   └── components/
│       └── SignLanguageRecognizer.tsx  # Main recognition component
├── python/
│   └── export_session.py      # Python script for pickle conversion
└── public/                    # Static assets
```

## API Endpoints

- `POST /api/recognize` - Process camera frames for sign recognition
- `POST /api/export` - Export session data as pickle file

## Troubleshooting

### Recognition Issues
- Ensure good lighting on your hands
- Keep hands 1-3 feet from camera
- Make clear, distinct gestures
- Check that your OpenRouter API key is valid

### Export Issues
- Ensure Python 3.7+ is installed and accessible as `python3`
- Check browser console for detailed error messages
- Verify you have recognition data before attempting export

## Technologies Used

- **Next.js 15** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **OpenRouter API** - AI recognition via GPT-4o
- **Python** - Pickle file generation
- **Web APIs** - Camera access and speech synthesis

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
