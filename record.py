import sqlite3
primary_database_name='fibonacci_data.db'

class DbOperation(): #CONVENTION - USE 'Db' as object name to instanciate this class.

    def __init__(self):

        self.connect_database(primary_database_name)

        self.cur.execute('''
                    CREATE TABLE 
                    IF NOT EXISTS 
                    main 
                    (SNO INTEGER PRIMARY KEY, 
                    AMOUNT INTEGER, 
                    DATE, TIME, 
                    REMARK VARCHAR, 
                    CATEGORY CHAR(60)); 
                    ''')
        
        self.cur.execute('''
                    CREATE TABLE 
                    IF NOT EXISTS 
                    category 
                    (SNO INTEGER PRIMARY KEY, 
                    CATEGORY VARCHAR); 
                    ''')
        self.close_database()
        
    def connect_database(self,database):
        self.connection=sqlite3.connect(database)
        self.cur=self.connection.cursor()

    def close_database(self):
        self.connection.commit()
        self.connection.close()

    def add_category(self,value):
        self.connect_database(primary_database_name)
        self.cur.execute('''
                    INSERT INTO
                    category (CATEGORY)
                    VALUES(?);''',(value,))
        self.close_database()

    #Insert Expense
    def record_expense(self, values : tuple) -> None:
        self.connect_database(primary_database_name)
        self.cur.execute('''
                    INSERT INTO
                    main (AMOUNT,DATE,TIME,REMARK,CATEGORY)
                    VALUES(?,?,?,?,?);''',values)
        self.close_database()

    #FetchCategory_Values
    def fetch_categories(self):
        self.connect_database(primary_database_name)
        results=self.cur.execute('''
                            SELECT DISTINCT CATEGORY FROM CATEGORY;
        ''')
        results=results.fetchall()
        self.close_database()
        lis=[]
        for i in range(len(results)):
            lis.append(results[i][0])
        return lis
    

    def Tests(self): #USE for debugging.
        self.connect_database(primary_database_name)
        self.results=self.cur.execute(
            '''
            SELECT * FROM category;
            ''')
        for rows in self.results.fetchall():print(rows)
        self.close_database()

'''
Db=DbOperation()
Db.add_category('mango')
Db.Tests()
'''