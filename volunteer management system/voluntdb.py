import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employee(
            id Integer Primary Key,
            name text,
            degree text,
            year_of_study text,
            section text,
            date_of_birth text,
            contact_number text,
            alternate_number text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, degree, year_of_study, section, date_of_birth, contact_number, alternate_number, address):
        self.cur.execute("insert into employee values (NULL,?,?,?,?,?,?,?,?)",
                         (name, degree, year_of_study, section, date_of_birth, contact_number,alternate_number, address))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from employee")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from employee where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, degree,year_of_study, section, date_of_birth, contact_number, alternate_number, address):
        self.cur.execute(
            "update employee set name=?, degree=?, Year_of_study=?, section=?, date_of_birth=?, contact_number=?,alternate_number=?, address=? where id=?",
            (name, degree, year_of_study,section , date_of_birth, contact_number, alternate_number, address, id))
        self.con.commit()
