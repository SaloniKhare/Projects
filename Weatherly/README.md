# 🌤️ Weatherly

**Weatherly – Real-Time Weather Forecast Web App (HTML, CSS, JS + Weather API)**

Weatherly is a simple and elegant web application that lets users get real-time weather information for cities using a weather API.  
It displays current weather, temperature, description, and an hourly forecast for the next 24 hours. :contentReference[oaicite:0]{index=0}

---

## 🛠️ Built With

- **HTML** – Markup structure of the app  
- **CSS** – Styling and responsive layout  
- **JavaScript** – Dynamic API calls and DOM updates  
- **Weather API** – Fetches weather data (forecast + current conditions)

---

## 🚀 Features

✔ Search weather by city  
✔ Shows current temperature and weather description  
✔ Displays hourly forecast for the next 24 hours  
✔ Uses browser geolocation to fetch weather for current location  
✔ Default city weather shown when app loads

---

## 📁 Project Structure
Weatherly/
│
├── index.html # Main webpage
├── style.css # App styling
├── script.js # Weather API logic
├── icons/ # Weather icons (SVG files)
└── README.md

---

## 📡 How It Works

1. **User enters a city name** and presses Enter  
2. App constructs a Weather API request with your API key  
3. Weather data (current + forecast) is fetched via JavaScript  
4. DOM updates with:
   - Temperature
   - Weather description
   - Hourly forecast
5. If geolocation is enabled, clicking the location button fetches local weather

> The app uses modern JavaScript to fetch weather details and update the UI dynamically. 

