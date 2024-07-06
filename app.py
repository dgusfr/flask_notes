from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Função para carregar notas de um arquivo JSON
def load_notes():
    if os.path.exists('notes.json'):
        with open('notes.json', 'r') as f:
            return json.load(f)
    return []

# Função para salvar notas em um arquivo JSON
def save_notes(notes):
    with open('notes.json', 'w') as f:
        json.dump(notes, f)

@app.route('/')
def index():
    notes = load_notes()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    notes = load_notes()
    notes.append({'title': title, 'content': content})
    save_notes(notes)
    flash('Note added successfully!')
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_note(index):
    notes = load_notes()
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        notes[index] = {'title': title, 'content': content}
        save_notes(notes)
        flash('Note updated successfully!')
        return redirect(url_for('index'))
    note = notes[index]
    return render_template('edit.html', note=note, index=index)

@app.route('/delete/<int:index>', methods=['POST'])
def delete_note():
    notes = load_notes()
    del notes[index]
    save_notes(notes)
    flash('Note deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
