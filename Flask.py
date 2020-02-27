from flask import Flask, render_template
import MyWeatherApi as Mwa

app = Flask(__name__,static_url_path='/Flask')


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',
                           location=Mwa.get_location(),
                           temp=Mwa.get_temp(),
                           press=Mwa.get_pressure(),
                           humid=Mwa.get_humidity(),
                           weather_id=Mwa.get_weather_id(),
                           desc=Mwa.get_weather_desc(),
                           wind=Mwa.get_wind(),
                           sunrise=Mwa.get_sunrise(),
                           sunset=Mwa.get_sunset(),
                           icon=Mwa.get_icon(),
                           date=Mwa.get_date(),
                           holiday=Mwa.get_holiday())


if __name__ == '__main__':
    app.run()