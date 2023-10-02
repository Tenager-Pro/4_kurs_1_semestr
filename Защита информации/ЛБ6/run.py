import sqlite3
from flask import Flask, redirect, render_template, session, url_for, request


def delete_dangerous(s):
    l = ["\\", '"', "'", "\0", ]
    for i in l:
        if i in s:
            s = s.replace(i, '') 
    return s


app = Flask(__name__)
# Секретный ключ, необходимый для сессии 
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# Этот код выполняется если URL-путь пустой 
@app.route('/')
def index():
    # Если пользователь есть в сессии загружаем шаблон index.html 
    if 'username' in session:
        return render_template('index.html') 
    # Перенаправление на страницу login 
    return redirect(url_for('login'))

@app.route('/login') 
def login():
    if 'username' in session:
        return redirect(url_for('index')) 
    return render_template('login.html')

@app.route('/login/authentication', methods=['POST', 'GET']) 
def authentication():
    login = request.form['login'] 
    password = request.form['pass'] 
    login = delete_dangerous(str(login))
    password = delete_dangerous(str(password)) 
    conn = sqlite3.connect('test_db.sqlite') 
    cursor = conn.cursor()
    # Пытаемся получить число совпадений с пользователем и паролем 
    cursor.execute("SELECT COUNT(*) FROM users WHERE login = '%s' AND pass = '%s'" % (login, password,)) 
    res = cursor.fetchone() 
    conn.close()
    # Если есть совпадения то добавляем имя в сессию 
    if res[0] != 0:
        session['username'] = request.form['login'] 
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/logout') 
def logout():
# Удаляем сессию
    session.pop('username', None) 
    return redirect(url_for('login'))

if  __name__ == '__main__':
    # host, port, debug_mode 
    app.run('127.0.0.1', 80, True)
