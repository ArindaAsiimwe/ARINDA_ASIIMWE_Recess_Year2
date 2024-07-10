from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Hiii Flask'

# if __name__ == '__main__':
#     app.run(debug=True)

species_list = [
    {"name": "Elephant", "habitat": "Africa"},
    {"name": "Lion", "habitat": "Africa"},
    {"name": "Tiger", "habitat": "Africa"},
    {"name": "Penguin", "habitat": "Antarctica"},
    {"name": "Ostrich", "habitat": "Antarcticta"},
    {"name": "Chimpanzee", "habitat": "Africa"},
]

@app.route('/')
def index():
    return render_template("index.html", species_list=species_list)

@app.route('/add', methods=['GET', 'POST'])
def add_species():
    if request.method == 'POST':
        name = request.form['name']
        habitat = request.form['habitat']
        species_list.append({"name": name, "habitat": habitat})
        return redirect(url_for('index'))
    return render_template('add_species.html')

if __name__ == "__main__":
    app.run(debug=True)

