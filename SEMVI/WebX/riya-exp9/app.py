from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    error = None

    if request.method == 'POST':
        city = request.form.get('city')
        api_key = '8f4373e270af467d9d691204251004'  # 🔁 Replace with your real API key
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

        print(f"[DEBUG] Requesting URL: {url}")  # ✅ Show full API URL

        try:
            response = requests.get(url)
            print(f"[DEBUG] Status Code: {response.status_code}")
            print(f"[DEBUG] API Raw Response: {response.text}")

            if response.status_code == 200:
                data = response.json()
                
                # Check for actual API error in JSON
                if 'error' in data:
                    error = data['error']['message']
                    print(f"[DEBUG] API Error: {error}")
                else:
                    # Extract useful weather info
                    weather = {
                        'city': data['location']['name'],
                        'region': data['location']['region'],
                        'country': data['location']['country'],
                        'temperature': data['current']['temp_c'],
                        'condition': data['current']['condition']['text'],
                        'icon': data['current']['condition']['icon']
                    }
                    print(f"[DEBUG] Weather Data Parsed: {weather}")
            else:
                error = "Failed to get data from Weather API."

        except Exception as e:
            error = f"An error occurred: {str(e)}"
            print(f"[ERROR] {error}")

    return render_template('weather.html', weather=weather, error=error)

if __name__ == '__main__':
    app.run(debug=True)
