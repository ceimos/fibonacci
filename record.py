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
                    DATE DATE, 
                    TIME TIME,
                    MODE CHAR(30),
                    REMARK VARCHAR DEFAULT NULL, 
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
                    main (AMOUNT,DATE,TIME,MODE,REMARK,CATEGORY)
                    VALUES(?,?,?,?,?,?);''',values)
        self.close_database()

    #FetchCategory_Values
    def fetch_categories(self):
        self.connect_database(primary_database_name)
        results=self.cur.execute('''
                            SELECT DISTINCT category FROM main;
        ''')
        results=results.fetchall()
        self.close_database()
        lis=[]
        for i in range(len(results)):
            lis.append(results[i][0])
        return lis
    
    def fetch_rows_all(self):
        self.connect_database(primary_database_name)
        results=self.cur.execute('''
                            SELECT category,remark,
                            strftime("%d",date),
                            strftime("%H:%M",time),
                            mode,amount
                            FROM main
                            ORDER BY sno DESC;
        ''')
        results=results.fetchall()
        self.close_database()
        return results
    
    def data_for_pie_chart(self):
        self.connect_database(primary_database_name)
        self.results=self.cur.execute(
            '''
                SELECT SUM(amount)
                FROM main
                GROUP BY category;
            '''
        )
        lis=[]
        for rows in self.results.fetchall():lis.append(rows[0])
        self.close_database()
        return lis
    
    def data_for_bar_month(self):
        self.connect_database(primary_database_name)
        self.results=self.cur.execute(
            '''
                SELECT strftime('%m',date) AS month, SUM(amount)
                FROM main
                GROUP BY month;
            '''
        )
        lis={'months':[],'volume':[]}
        for rows in self.results.fetchall():lis['volume'].append(rows[1]);lis['months'].append(rows[0])
        self.close_database()
        return lis
    
    def data_for_bar_year(self):
        self.connect_database(primary_database_name)
        self.results=self.cur.execute(
            '''
                SELECT strftime('%Y',date) AS year, SUM(amount)
                FROM main
                GROUP BY year;
            '''
        )
        lis={'years':[],'volume':[]}
        for rows in self.results.fetchall():lis['volume'].append(rows[1]);lis['years'].append(rows[0])
        self.close_database()
        return lis

    def Tests(self): #USE for debugging.
        self.connect_database(primary_database_name)
        self.results=self.cur.execute(
            '''
            SELECT * FROM category;
            ''')
        for rows in self.results.fetchall():print(rows)
        self.close_database()

if __name__=='__main__':
    Db=DbOperation()
    print(Db.data_for_bar_month())