import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
    
    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.close()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS wydatki (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kategoria TEXT NOT NULL,
            kwota REAL NOT NULL,
            data TEXT NOT NULL
        )
        '''
        self.execute(query)

    def add_wydatek(self, kategoria, kwota, data):
        query = '''
        INSERT INTO wydatki (kategoria, kwota, data)
        VALUES (?, ?, ?)
        '''
        self.execute(query, (kategoria, kwota, data))

    def fetch_all(self, query, params=None):
        if params is None:
            params = ()
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_all_wydatki(self):
        query = "SELECT * FROM wydatki"
        return self.fetch_all(query)

    def deleta_wydatki(self, wydatek_id):
        self.cursor.execute("DELETE FROM wydatki WHERE id = ?", (wydatek_id,))
        self.conn.commit()

    def update_wydatek(self, wydatek_id, kategoria, kwota, data):
        query = """
        UPDATE wydatki
        SET kategoria = ?, kwota = ?, data = ?
        WHERE id = ?
        """
        self.execute(query, (kategoria, kwota, data, wydatek_id))
        self.conn.commit()

    def get_avg_monthly(self):
        query = """
        SELECT kategoria, strftime('%Y-%m', data) AS month, sum(kwota) 
        FROM wydatki 
        GROUP BY kategoria, month
        """
        return self.fetch_all(query)

    def execute(self, query, params=None):
        if params is None:
            params = ()
        self.cursor.execute(query, params)
        self.conn.commit()