from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/weather/<city>')
def weather(city):
    # Get temperature from weather API corresponding to given city
    weather__api = 'a7e9b7cd83166d594a42858290bbc541'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'units': 'metric', 'appid': weather__api}
    response = requests.get(url = url, params = params)
    temperature = int(response.json()['main']['temp'])

    # Get image url from giphy of the given city from API and hold insert it into IMG html tag
    giphy_api = '2vghJ4ZIBQ4JFPr773qWWoMMf5WuME8a'
    url = 'http://api.giphy.com/v1/gifs/translate'
    params = {'s': city, 'api_key': giphy_api}
    response = requests.get(url=url, params=params)
    img_url = str(response.json()['data']['images']['downsized_large']['url'])
    city_image = '<img src=%s/>' % img_url

    # Get another url from giphy which describe the state of the temperature in the given city
    temp_state = 'cold' if temperature < 24 else 'warm'
    params = {'s': temp_state, 'api_key': giphy_api}
    response = requests.get(url=url, params=params)
    img_url = str(response.json()['data']['images']['original']['url'])
    temp_image = '<img src=%s/>' % img_url

    render_page = 'Temperature in %s is %s <br> This is %s: %s <br> %s' % (city, temperature, city, city_image, temp_image )

    return render_page


if __name__ == "__main__":
    app.run()