from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configuração do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'notetaking_app'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO notes (title, content) VALUES (%s, %s)', (title, content))
    mysql.connection.commit()
    flash('Note added successfully!')
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        cursor.execute('UPDATE notes SET title = %s, content = %s WHERE id = %s', (title, content, id))
        mysql.connection.commit()
        flash('Note updated successfully!')
        return redirect(url_for('index'))
    cursor.execute('SELECT * FROM notes WHERE id = %s', (id,))
    note = cursor.fetchone()
    return render_template('edit.html', note=note)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_note():
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM notes WHERE id = %s', (id,))
    mysql.connection.commit()
    flash('Note deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
