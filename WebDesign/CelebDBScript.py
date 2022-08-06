import sqlite3

def create_table():
    conn = sqlite3.connect('Celeb.db')
    c = conn.cursor()

    c.execute("CREATE TABLE celeb(name text, pic text, intro text)")
    conn.commit()
    print("Table created")

    conn.close()


def inser_celeb():
    conn = sqlite3.connect('Celeb.db')
    c = conn.cursor()

    c.execute("""INSERT INTO celeb(name, pic, intro) VALUES('AP Dhillon','img/AP.jpg',"Amritpal Singh Dhillon, known popularly as AP Dhillon, is an Indian singer, rapper, songwriter and record producer associated with Punjabi music")""")
    c.execute("INSERT INTO celeb(name, pic, intro) VALUES('Chota Bheem','img/CB.jpg','Bheem and his friends have fun and adventures in the mythical village of Dholakpur.')")
    c.execute("INSERT INTO celeb(name, pic, intro) VALUES('Diljit Dosanjh','img/DD.jpg','Diljit Dosanjh is an Indian singer-songwriter, actor, film producer and television presenter who works in Punjabi and Hindi cinema.')")
    c.execute("INSERT INTO celeb(name, pic, intro) VALUES('One Direction','img/OD.jpg','One Direction, often shortened to 1D, are an English-Irish pop boy band formed in London, England in 2010.')")
    c.execute("INSERT INTO celeb(name, pic, intro) VALUES('Shizuka','img/shizuka.jpg','Shizuka Minamoto, usually called Shizu-chan or Shizuka-chan, is a main character of the Doraemon series.')")
    
    conn.commit()
    conn.close()

def generateWebPages():
    conn = sqlite3.connect("Celeb.db")

    c = conn.cursor()

    c.execute("SELECT * From celeb")

    records = c.fetchall()

    for row in records:
        print(row)
        fileName = str(row[0]) + ".html"
        htmlObj= open(fileName,"w")

        htmlObj.write("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>"""+ row [0]+"""</title>
        </head>
        <body>
            <header style="background-color: skyblue; color: gold;">
            <nav>
                <ul style="text-decoration: none; display: inline; padding-left: 5px;">
                    <li>Home</li>
                </ul>
            </nav>
            </header>
        <div>
            <img src='"""+ row[1] +"""' alt='""" + row[0] +"""'>
            <h1>""" + row[0] +"""</h1>
            <br>
            <hr>
            <br>
            <p>
                """+ row[2]+"""
            </p>
        </div>
        <footer style="background-color: skyblue; color: greenyellow; height: 50px;">
            Created by: Abhishek Behgal
        </footer>
        </body>
        </html>
        """)

create_table()
inser_celeb()
generateWebPages()
