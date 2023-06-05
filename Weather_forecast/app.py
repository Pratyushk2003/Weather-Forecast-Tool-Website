from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, static_folder='templates/static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    api_key = "4ad55236ac002885716669d0e486ec53"  # Replace with your actual OpenWeatherMap API key.
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {'q': city, 'appid': api_key}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        weather = data["weather"][0]["main"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        windspeed = data["wind"]["speed"]
        description = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]
        weather_data = {
            'location': city,
            'weather': weather,
            'temperature': temperature,
            'humidity': humidity,
            'windspeed': windspeed,
            'description': description,
            'icon': f"http://openweathermap.org/img/w/{icon}.png"
        }

        return jsonify(weather_data)
    except requests.exceptions.RequestException as err:
        return jsonify({'error': 'Failed to fetch weather data.'})

if __name__ == '__main__':
    app.run(debug=True)
