from flask import Flask, render_template, request
from KannadaCrawler import call_crawler
app=Flask("KannadaCrawler")


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/demo', methods = ['POST', 'GET'])
def demo():
    parm = request.form['ip']
    
    data = call_crawler(parm)
    return render_template(
        'home.html', data = data
    )

if __name__=="__main__":
    app.run()