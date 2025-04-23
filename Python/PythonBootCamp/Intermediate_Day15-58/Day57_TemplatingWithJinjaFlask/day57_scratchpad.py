
from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

currentDate = datetime.datetime.now().year

@app.route('/')
def home_page():
    # currentDate = datetime.datetime.now().year
    # current_year = currentDate.strftime("%Y")
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number, cur_yr=currentDate)

@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    agify_url = f"https://api.agify.io?name={name}"
    agify_response = requests.get(agify_url)
    agify_data = agify_response.json()
    age = agify_data['age']
    return render_template('guess.html', cur_yr=currentDate, check_name=name, gender=gender, age=age)

@app.route('/blog/<num>')
def blog_page(num):
    print(num)
    blog_url = f"https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', cur_yr=currentDate, posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)