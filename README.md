# 🎮 Gaming Assistant: Sigma Version

**Your Ultimate AI-Powered Gaming Companion**

Welcome to the Gaming Assistant - an intelligent chatbot designed specifically for gamers! Whether you're looking for game recommendations, need help with strategies, or want to troubleshoot technical issues, this AI assistant has got you covered across all gaming platforms.

---

## 🎯 About

The Gaming Assistant: Sigma Version is a specialized AI chatbot built with Streamlit and powered by Groq's Llama 3.3 70B model. This intelligent assistant offers personalized gaming advice, recommendations, and support across multiple gaming platforms including PC, console, mobile, and retro gaming.

What makes this assistant unique is its **adaptive personality system** - you can choose from three distinct interaction styles to match your preferences, making every conversation feel natural and engaging.

---

## ✨ Features

- 🎲 **Smart Game Recommendations** - Get personalized game suggestions based on your preferences and gaming history
- 🏆 **Expert Gaming Strategies** - Access pro-level tips, tactics, and strategies for competitive gaming
- 🔧 **Technical Support** - Troubleshoot gaming issues and optimize your gaming setup for better performance
- 📱 **Multi-Platform Expertise** - Support for PC, Console (PS5, Xbox, Switch), Mobile, and Retro gaming
- 🎨 **Game Development Insights** - Learn about game design principles and development processes
- 🤖 **Adaptive AI Personalities** - Choose from Friendly, Professional, or Humorous interaction styles
- 💬 **Real-time Chat Interface** - Seamless conversation experience with instant responses
- 🎯 **Context-Aware Responses** - AI remembers your conversation history for more relevant advice

---

## 🛠️ Technologies Used

- **Backend Framework:** Python 3.9+
- **Web Framework:** Streamlit 1.28.1
- **AI Model:** Groq API (Llama 3.3 70B Versatile)
- **Environment Management:** python-dotenv
- **Deployment:** Streamlit Cloud
- **Version Control:** Git & GitHub

### Dependencies
```
streamlit==1.28.1
groq==0.32.0
python-dotenv==1.0.0
```

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.9 or higher
- Groq API Key (free registration at [Groq Console](https://console.groq.com))

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/[username]/ai-chatbox.git
   cd ai-chatbox
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**

   Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```

   Add your Groq API key to the `.env` file:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

5. **Access the Application**

   Open your browser and navigate to:
   - Local URL: `http://localhost:8501`
   - Network URL: `http://[your-ip]:8501`

---

## ☁️ Deployment

### Deploy to Streamlit Cloud

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository
   - Add your `GROQ_API_KEY` in the secrets section
   - Click "Deploy"

3. **Environment Variables**

   In Streamlit Cloud secrets, add:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```

---

## 🌐 Live Demo

🔗 **[Try the Gaming Assistant Live](https://your-app-url.streamlit.app)**

*Experience the AI gaming assistant in action without any setup required!*

---

## 📸 Screenshots

> **Note:** Add screenshots of your application here to showcase the user interface and features.

*Coming soon - Screenshots will be added to demonstrate:*
- Main chat interface
- Personality selection sidebar
- Sample conversations
- Mobile responsive design

---

## 🔑 API Key Setup

### Getting Your Groq API Key

1. **Sign Up for Groq**
   - Visit [Groq Console](https://console.groq.com)
   - Create a free account

2. **Generate API Key**
   - Navigate to the API Keys section
   - Click "Create API Key"
   - Copy your API key

3. **Add to Environment**
   - Add the key to your `.env` file
   - For Streamlit Cloud: Add to secrets section
   - Keep your API key secure and never commit it to version control

### API Usage
- **Model:** Llama 3.3 70B Versatile
- **Max Tokens:** 1000 per response
- **Temperature:** Adaptive (0.3-0.9 based on personality)
- **Rate Limits:** Check Groq documentation for current limits

---

## 🚀 Future Improvements

### Planned Features
- 🎮 **Game Library Integration** - Connect with Steam, Epic Games, and other platforms
- 📊 **Gaming Statistics Dashboard** - Track your gaming habits and preferences
- 🏆 **Achievement System** - Unlock badges for using different features
- 🌍 **Multi-language Support** - Support for multiple languages
- 🎵 **Voice Chat Integration** - Voice-to-text and text-to-speech capabilities
- 📱 **Mobile App** - Native mobile application
- 🤝 **Community Features** - Share recommendations with other users

### Technical Enhancements
- Advanced conversation memory
- Custom AI model fine-tuning
- Performance optimizations
- Enhanced UI/UX design

---

## 👨‍💻 Author

**[Your Name]**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/your-profile)
- Email: your.email@example.com

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/[username]/ai-chatbox/issues).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ⭐ Show Your Support

Give a ⭐️ if this project helped you! Your support motivates continued development and improvements.

---

*Made with ❤️ for the gaming community*
