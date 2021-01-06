from flask import Flask,render_template
app = Flask(__name__)

posts = [
      {
         'author':'Mohit Rajput',
         'title':'Blog post',
         'content':'First Post',
         'date_posted':'Jan 5, 2021' 
      },
      {
          'author':'Jane Doe',
          'title': 'Blog Post',
          'content':'Second Post',
          'date_posted':'Jan 6, 2021'
      }

]

@app.route("/")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',posts = posts)

if __name__=="__main__" :
    app.run(debug=True)   