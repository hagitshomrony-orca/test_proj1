def get_user(user_id):
    conn = sqlite3.connect("app1.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return cursor.fetchone()

def run_command(cmd):
    subprocess.run(cmd, shell=True)
