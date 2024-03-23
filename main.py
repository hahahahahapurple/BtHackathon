app = create_app()
app.secret_key = os.urandom(12)
date = '2022/1/19'
oauth = OAuth(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
