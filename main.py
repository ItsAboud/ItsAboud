from flet import *  
import sqlite3

conn = sqlite3.connect("dato.db",check_same_thread=False)
cursor = conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS student(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               stdname Text,
               stdmaill TEXT,
               stdphone TEXT,
               stdaddress TEXT,
               sthtml INTEGER,
               stjavascript INTEGER,
               stcsharp INTEGER,
               stphotoshop INTEGER,
               stadobepremiere INTEGER,
               stthreeD INTEGER
               )""")
conn.commit()


def main(page:page): 
    page.title = 'CodePalette'
    page.scroll = 'auto'
    page.window.top = 1
    page.window.left = 960
    page.window.width = 390
    page.window.height = 740
    page.bgcolor = 'white'
    page.theme_mode = ThemeMode.LIGHT

#########################

    tabe_name = 'student'
    query = f'SELECT COUNT(*) FROM {tabe_name}'
    cursor.execute(query)
    result = cursor.fetchone()
    row_count = result[0]
    
    def add(e):
        cursor.execute("INSERT INTO student (stdname,stdmaill,stdphone,stdaddress,sthtml,stjavascript,stcsharp,stphotoshop,stadobepremiere,stthreeD) VALUES(?,?,?,?,?,?,?,?,?,?)",(tname.value,tmail.value,tphone.value,taddress.value,html.value,javascript.value,csharp.value,photoshop.value,adobepremiere.value,threeD.value))
        conn.commit()
        
    def show(e):
            page.clean()
            c = conn.cursor()
            c.execute("SELECT * FROM student")
            users = c.fetchall()
            print(users)

            if not users == "":
                keys = ['id','stdname','stdmaill','stdphone','stdaddress','sthtml','stjavascript','stcsharp','stphotoshop','stadobepremiere','stthreeD']
                result = [dict(zip(keys,values)) for values in users]
                for x in result:

                    ######### Marks #########
                    m = x['sthtml']
                    a = x['stjavascript']
                    f = x['stcsharp']
                    r = x['stphotoshop']
                    d = x['stadobepremiere']
                    c = x['stthreeD']
                    res = m + a + f + r + d + c 
                    if res < 50:
                       a = Text('❌Failing',size=19,color='red')
                    if res > 50:
                       a = Text('✅successful',size=19,color='green')



                    page.add(
                      Card(
                            color='black',
                            content=Container(
                                    content=Column([
                                         ListTile(
                                              leading = Icon(icons.PERSON),
                                              title=Text('Name : '+ x['stdname'], color='white'),
                                              subtitle = Text('Student Email :'+ x['stdmaill'], color='amber')
                                         ),
                                         Row([
                                              Text('Phone :'+ x['stdphone'], color='green'),
                                              Text('Address :'+ x['stdaddress'], color='orange')
                                         ],alignment=MainAxisAlignment.CENTER),

                                        Row([
                                             Text('Html :' + str(x['sthtml']), color='blue'),
                                             Text('Javascript :' + str(x['stjavascript']), color='blue'),
                                             Text('C# :' + str(x['stcsharp']),color='blue')
                                        ],alignment=MainAxisAlignment.START),
                                        Row([
                                             Text('Photoshop :' + str(x['stphotoshop']), color='pink'),
                                             Text('Adobe Premiere :' + str(x['stadobepremiere']), color='pink'),
                                             Text('3D Designer :' + str(x['stthreeD']), color='pink')
                                        ],alignment=MainAxisAlignment.START),


                                        Row([
                                            a
                                        ],alignment=MainAxisAlignment.CENTER)
                                         
                                    ])
                            )
                        )
                    )
                page.update()

    ######### Feils #########
    tname = TextField(label='students name',icon=icons.PERSON,rtl=True,height=38)
    tmail = TextField(label='Email',icon=icons.MAIL,rtl=True,height=38)
    tphone = TextField(label='Phone Number',icon=icons.PHONE,rtl=True,height=38)
    taddress = TextField(label='the address',icon=icons.LOCATION_CITY,rtl=True,height=38)
    #########################

    ######### Feils #########
    marktext = Text("Student Marks",text_align='center',weight='bold')
    html = TextField(label='HTML',width=110,rtl=True,height=38)
    javascript = TextField(label='JavaScript',width=110,rtl=True,height=38)
    csharp = TextField(label='C#',width=110,rtl=True,height=38)
    photoshop = TextField(label='Photoshop',width=110,rtl=True,height=38)
    adobepremiere = TextField(label='Adobe Premiere',width=110,rtl=True,height=38)
    threeD = TextField(label='3D designer',width=110,rtl=True,height=38)
    #########################

    addbuttn = ElevatedButton(
        "Add a new student",
        width=170,
        style=ButtonStyle(bgcolor='green',color='white',padding=15),
        on_click=add
    )

    showbuttn = ElevatedButton(
        "View all students",
        width=170,
        style=ButtonStyle(bgcolor='green',color='white',padding=15),
        on_click=show
    )


    page.add (
        Row([
            Image(src="home2.gif",width=280)

        ],alignment=MainAxisAlignment.CENTER),

        Row([
            Text("Welcome to the CodePalette application",size=18,font_family="Segoe MDL2 Assets",color='black')

        ],alignment=MainAxisAlignment.CENTER),

        Row([
            Text("Number of registered students :",size=18,font_family="Segoe MDL2 Assets",color='blue'),
            Text(row_count,size=18,font_family="Segoe MDL2 Assets",color='green'),
        ],alignment=MainAxisAlignment.CENTER),
        tname,
        tmail,
        tphone,
        taddress,

        Row([
            marktext
        ],alignment=MainAxisAlignment.CENTER),

         Row([
            html,javascript,csharp
        ],alignment=MainAxisAlignment.CENTER),

         Row([
            photoshop,adobepremiere,threeD
        ],alignment=MainAxisAlignment.CENTER),
        
        Row([
            addbuttn,showbuttn
        ],alignment=MainAxisAlignment.CENTER)
    )


    page.update()
app(main) 
