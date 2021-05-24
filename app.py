from flask import Flask, render_template, request
from movieRecommender import recommend

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def show_index_html():
    return render_template('index.html')

@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
        pay = request.form['pay']
        movies,genres,directors,homepages,vote_averages = recommend(pay)
        return render_template('index.html',movies = movies,genres = genres,directors = directors, homepages=homepages,vote_averages=vote_averages)

if __name__ == '__main__':
    app.run(debug=True)