from init import init_app


app = init_app(__name__)


@app.route('/')
def welcome():
    return 'Welcome to Crayon Task'


if __name__ == "__main__":
    app.run(debug=True)

