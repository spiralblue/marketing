import csv

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('compare.html', var1=5)


@app.route('/output', methods=['POST'])
def update():
    # var1 = request.form['var1']
    data = request.form  # results in an empty dict: `ImmutableMultiDict([])`
    var1 = 5  # so the return-statement does not break
    print(data)  # I know that this method is called, as `data` (empty dict) is printed when I change the sliders value
    return render_template('compare.html', var1=var1, output=f'Output\nVariable 1 = {var1}')

@app.route('/slider/<value>',methods = ['GET','POST'])
def slider(value):
    return jsonify({'value': value})


if __name__ == '__main__':
    app.run(debug=True)


with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)