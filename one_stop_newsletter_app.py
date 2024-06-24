from flask import Flask, render_template
from newsletter_scrapping import data_scraper

df_data_dict = data_scraper()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", data = df_data_dict, enumerate=enumerate)

if __name__ == '__main__':
	app.run()