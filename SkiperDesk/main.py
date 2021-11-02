from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3




class SkiperDesk(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_pallet = "BlueGray"

        # Create & Connect to DB
        conn = sqlite3.connect('SkiperDesk.db')

        # Create A Cursor
        c = conn.cursor()

        # Create A Table
        c.execute('''CREATE TABLE if not exists tasks(task text)''')

        #Commit Changes
        conn.commit()

        #Close connection
        conn.close()

        return Builder.load_file('SkiperDesk.kv')

    def save_task(self):
        # Create & Connect to DB
        conn = sqlite3.connect('SkiperDesk.db')

        # Create A Cursor
        c = conn.cursor()

        # Create A Cursor
        c.execute("INSERT INTO tasks VALUES (:first)",
                    {
                        'first': self.root.ids.task_input.text,
                    })
        # Add message
        self.root.ids.task_label.text = f'{self.root.ids.task_input.text} Added'

        # Clear the input box
        self.root.ids.task_input.text = ''

        # Create A Table
        c.execute("""CREATE TABLE if not exists tasks(task text)""")

        # Commit Changes
        conn.commit()

        # Close connection
        conn.close()

    def show_tasks(self):
        # Create & Connect to DB
        conn = sqlite3.connect('SkiperDesk.db')

        # Create A Cursor
        c = conn.cursor()

        # Grab from db
        c.execute("SELECT * FROM tasks")
        records = c.fetchall()

        word = ''
        # Loop thru records
        for record in records:
            word = f'{word}\n{record[0]}'
            self.root.ids.task_label.text = f'{word}'

        # Commit Changes
        conn.commit()

        # Close connection
        conn.close()


SkiperDesk().run()