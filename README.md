*** This is my personal AI Assistant ***

--> This personal assistant converts speech to text by recognizing the speech, by using various packages like pyttsx3, speech_recognition.

--> This code is a voice-controlled assistant application that can perform various tasks like browsing the web, sending emails, taking screenshots, playing songs, and interacting with an AI chatbot.

**These are the libraries used in the script:**

**pyttsx3:** Text-to-speech conversion library.
**speech_recognition:** Recognizes speech input from the user.
**datetime:** Provides date and time functions.
**wikipedia**: Fetches summaries from Wikipedia.
**pyautogui:** Takes screenshots.
**json and requests:** Handle API requests and responses.
**openai:** Interface with OpenAI API.
**pywhatkit:** Performs various tasks like playing YouTube videos and sending WhatsApp messages.
**smtplib**: Sends emails.
**sample:** A custom module presumably for playing and controlling songs.
**os:** Executes system commands.


**Configuration**

**headers:** Authorization header for API requests.
**url:** API endpoint for the chatbot.
**payload:** Data sent to the API for processing.
**x:** Initializes the text-to-speech engine.

**How to Use the Script**

**1) Setup:** Ensure all required libraries are installed using pip install pyttsx3 speechrecognition wikipedia pyautogui json requests openai pywhatkit smtplib.

**2) API Keys:** Replace "Bearer YOUR_API_KEY" with your actual API key for the chatbot service.

**3) Email Credentials:** Update the sendemail function with your email and password.

**4 Run the Script:** Execute the script. The assistant will greet you and await voice commands.

**5) Commands:** Use voice commands to perform tasks like checking the time or date, browsing the web, sending messages, and more.

**6)Voice Input:** Speak clearly into the microphone when prompted.



**To use this script, you need the following:**

**Python Environment:** Ensure you have Python installed (preferably Python 3.6+).
**Microphone:** A working microphone for voice input.
**Email Account:** A Gmail account for sending emails.
**API Key:** An API key for the AI chatbot service.

**Usage Instructions**
**Initial Greeting:**
The assistant will greet you based on the current time.

**Voice Commands:**
Speak clearly into the microphone. The assistant will recognize and process your commands.


**Commands:**

**Greet:** "Good morning"
**Time:** "What is the time?"
**Date:** "What's the date today?"
**Wikipedia:** "Tell me about Python programming"
**YouTube:** "Open YouTube" (then specify the video/topic)
**Browser:** "Open Chrome" (then specify the search query)
**WhatsApp:** "Send in WhatsApp" (provide recipient and message)
**Email:** "Send email" (provide recipient and message)
**Remember:** "Remember [data]"
**Retrieve:** "Speak out data"
**Song Control**: "Play a song" / "Pause the song" / "Unpause" / "Stop"
**Shutdown/Restart**: "Shutdown my PC" / "Restart my PC"
**AI Chatbot:** Any general query

In this way, we can use and implement various ideas by using this AI Assistant.
