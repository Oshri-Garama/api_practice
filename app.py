from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/weather/<city>')
def weather(city):
    # Get temperature from weather API corresponding to given city
    weather__api_token = 'a7e9b7cd83166d594a42858290bbc541'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'units': 'metric', 'appid': weather__api_token}
    response = requests.get(url = url, params = params)

    temperature = int(response.json()['main']['temp'])

    # Get image url from giphy of the given city from API and hold insert it into IMG html tag
    giphy_api_token = '2vghJ4ZIBQ4JFPr773qWWoMMf5WuME8a'
    url = 'http://api.giphy.com/v1/gifs/translate'
    params = {'s': city, 'api_key': giphy_api_token}
    response = requests.get(url=url, params=params)

    city_image_url = str(response.json()['data']['images']['downsized_large']['url'])

    # Get another url from giphy which describe the state of the temperature in the given city
    temp_state = 'scarf' if temperature < 24 else 'bathingsuit'
    params = {'s': temp_state, 'api_key': giphy_api_token}
    response = requests.get(url=url, params=params)
    temp_image_url = str(response.json()['data']['images']['original']['url'])

    render_page = '''
                    <h1 style="color: powderblue;font-family: verdana;text-align: center;">Temperature in %s is %s celsius</h1> 
                    <div style="color: powderblue;font-family: verdana;text-align: center;">
                        <h2>A gif is worth a thousand words</h2>
                        <img src=%s/> 
                        <h3>My suggest for you is to wear a %s</h3>
                        <h3>maybe consider buying something like in the gif blow</h3>
                        <img src=%s/>
                    </div>
                  ''' % (city, temperature, city_image_url, temp_state, temp_image_url)

    return render_page


if __name__ == "__main__":
    app.run()