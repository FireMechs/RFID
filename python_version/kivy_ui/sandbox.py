import random
import sqlite3

class SandBox():
    No_data = 'No Data'
    def __init__(self):
        self.key_tag = ['keyIsJumaJoels','keyIsClaudios','keyIsKelvins','keyIsEricos']
        self.card_tag = ['cardIsEricos', 'cardIsJumaJoels', 'cardIsClaudios', 'cardIsKelvins']

    def randomizeKey(self):
        random.shuffle(self.key_tag)
        return random.choice(self.key_tag)

    def randomizeCard(self):
        random.shuffle(self.card_tag)
        return random.choice(self.card_tag)

    def check_with_db(self, item, row_pos):
        self.row_data = []
        conn = sqlite3.connect('sandbox.db')
        with conn:
            cur = conn.cursor()
            cur.execute('select * from t_data')
            while True:
                row = cur.fetchone()
                if row == None:
                    break
                elif row[row_pos] == item:
                    self.row_data = row

        conn.close()
        return self.row_data

    def handle_data(self):
        # first handle the key
        self.key_val_db = []
        self.key_val = self.randomizeKey()
        self.key_val_db = self.check_with_db(self.key_val, 4)
        if not self.key_val_db:
            return self.key_val_db.append(self.No_data)
        else:
            self.checkForCard(self.key_val_db[-1])
            return self.key_val_db

    def checkForCard(self, item):
        print(item)