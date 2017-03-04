from flask import Flask, render_template
from breitlon import get_article_list

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', article_list=get_article_list())
	
if __name__ == "__main__":
	app.run()