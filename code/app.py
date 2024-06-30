from flask import Flask #Flask, web dev stuff
from views import views #Template usage

#Code
app = Flask(__name__)
app.register_blueprint(views, url_prefix='/')

if __name__ == "__main__":
    app.run(debug=True, port=8000)
