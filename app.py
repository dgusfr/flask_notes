from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['fname']
    # Aqui você pode processar o nome ou fazer o que for necessário com ele
    return f"Nome recebido: {nome}"

if __name__ == '__main__':
    app.run(debug=True)
