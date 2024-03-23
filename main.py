app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

@app.route('/')
def hello_world():
  return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='True')
