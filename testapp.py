# 1. Import Flask
from flask import Flask

# 2. Create an app
app = Flask(__name__)


# 3. Define index route
@app.route("/")
def home():
    print("test")
    return "Welcome to my 'Home' page!"


# 6. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
