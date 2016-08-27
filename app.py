from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.vars={}

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
        app.vars['ticker'] = request.form['ticker']
        return render_template('graph.html', ticker=app.vars['ticker'])
    else:
        return render_template('index.html')

 @app.route('/graph')
 def graph():
 	return render_template('graph.html')

if __name__ == '__main__':
  app.run(port=33507)
