import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Загрузить конфигурацию
app.config.from_pyfile('config.py')

# Временная переменная для vk_id (замените на свой vk_id для тестирования)
TEMP_VK_ID = 376393143

# Подключение к базе данных
def get_db_connection():
    return mysql.connector.connect(
        host=app.config['DB_HOST'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        database=app.config['DB_NAME']
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT balance, total_balance, clicks FROM players WHERE vk_id=%s', (TEMP_VK_ID,))
    result = cursor.fetchone()
    balance = result[0] if result else 0
    total_balance = result[1] if result else 0
    clicks = result[2] if result else 0
    conn.close()
    return render_template('index.html', balance=balance, total_balance=total_balance, clicks=clicks)

@app.route('/click', methods=['POST'])
def click():
    conn = get_db_connection()
    cursor = conn.cursor()
    increment = random.randint(1, 7)
    cursor.execute("""
        UPDATE players 
        SET balance = balance + %s, 
            total_balance = total_balance + %s, 
            clicks = clicks + 1 
        WHERE vk_id = %s
    """, (increment, increment, TEMP_VK_ID))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        new_nickname = request.form['nickname']
        cursor.execute('UPDATE players SET nickname=%s WHERE vk_id=%s', (new_nickname, TEMP_VK_ID))
        conn.commit()
    
    cursor.execute('SELECT nickname, balance, total_balance, start_date, clicks FROM players WHERE vk_id=%s', (TEMP_VK_ID,))
    result = cursor.fetchone()
    nickname = result[0] if result else 'Unknown'
    balance = result[1] if result else 0
    total_balance = result[2] if result else 0
    start_date = result[3] if result else 'Unknown'
    clicks = result[4] if result else 0
    conn.close()
    return render_template('profile.html', nickname=nickname, balance=balance, total_balance=total_balance, start_date=start_date, clicks=clicks)

@app.route('/tops')
def tops():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Получение топ пользователей по балансу
    cursor.execute('SELECT nickname, balance FROM players ORDER BY balance DESC LIMIT 10')
    top_balance_players = cursor.fetchall()
    
    # Получение топ пользователей по кликам
    cursor.execute('SELECT nickname, clicks FROM players ORDER BY clicks DESC LIMIT 10')
    top_miner_players = cursor.fetchall()
    
    conn.close()
    return render_template('tops.html', top_balance_players=top_balance_players, top_miner_players=top_miner_players)

if __name__ == '__main__':
    app.run(debug=True)