# importing libraries
from flask import Flask

# creating app
app = Flask(__name__)


# defining application route
@app.route("/")
def index():
    return "Kubernetes Assignment"


if __name__ == "__main__":
    # running app
    app.run()
