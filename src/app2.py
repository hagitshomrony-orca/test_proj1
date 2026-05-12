def get_user1(user_id):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return cursor.fetchone()

def run_command1(cmd):
    subprocess.run(cmd, shell=True)
