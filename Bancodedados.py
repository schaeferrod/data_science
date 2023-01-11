import sqlite3
conexao = sqlite3.connect("sapatos.db")
cursor = conexao.cursor()
cursor.execute("select brand from shoes")
resultado = cursor.fetchone()
print(resultado)
cursor.execute('''
   create table shoes(
        id char(10) Primary Key,
        brand char(10) NOT NULL,
        type char(250) NOT NULL,
        color char(250) NOT NULL,
        price decimal(8,2) NOT NULL,
        desc varchar(750) NULL
        );
    ''')
cursor.execute('''
    insert into shoes
        (id
        ,brand
        ,type
        ,color
        ,price
        ,desc)
    VALUES
        ('14535974'
        ,'Gucci'
        ,'Slippers'
        ,'Pink'
        ,'695.00'
        ,NULL
        );
        
    ''')
