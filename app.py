from Flask_bootstrap import bootstrap

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        usermane = resquest.form.get('username')
        print(username)
        return f"<h1>username:{username}foi recebido!</h1>"
    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run()          