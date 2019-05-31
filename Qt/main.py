import sys
import os
import sqlite3
import requests
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
import geocoder

connection = sqlite3.connect('database.db')


loginForm = uic.loadUiType(os.path.join(os.getcwd(), 'login.ui'))[0]
registerForm = uic.loadUiType(os.path.join(os.getcwd(), 'register.ui'))[0]
mainFormm = uic.loadUiType(os.path.join(os.getcwd(), 'main.ui'))[0]


class loginClass(loginForm, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mainWindow = None
        self.loginButton.clicked.connect(self.login)
        self.registerButton.clicked.connect(self.register)

    def login(self):
        username = self.usernameField.text()
        password = self.passwordField.text()
        stmt = "SELECT name, phone, username, password FROM users WHERE username = (?) AND password = (?)"
        args = (username, password)
        result = connection.execute(stmt, args)
        for row in result:
            if row[2] == username and row[3] == password:
                self.mainWindow = mainClass(row)
                self.close()
                self.mainWindow.show()

    def register(self):
        self.registerWindow = registerClass()
        self.close()
        self.registerWindow.show()


class registerClass(registerForm, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.registerButton.clicked.connect(self.register)

    def register(self):
        name = self.nameField.text()
        phone = self.phoneField.text()
        username = self.usernameField.text()
        password = self.passwordField.text()
        stmt = "INSERT INTO users(name, phone, username, password) values (?, ?, ?, ?)"
        args = (name, phone, username, password)
        connection.execute(stmt, args)
        connection.commit()
        stmt = "SELECT name, phone, username, password FROM users WHERE username = (?) AND password = (?)"
        args = (username, password)
        result = connection.execute(stmt, args)
        for row in result:
            if row[2] == username and row[3] == password:
                self.mainWindow = mainClass(row)
                self.close()
                self.mainWindow.show()
                break


class mainClass(mainFormm, QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.setupUi(self)
        self.user = user
        self.helloBox.setText(f"hello {self.user[0]}")
        self.historyBox.setText("Previous locations:")
        g = geocoder.ip('me')
        lat = g.latlng[0]
        lon = g.latlng[1]
        self.locationBox.setText(f"Current location:\n #lon: {lon}\n #lat: {lat}")
        r = requests.get(r'https://map.ir/static', params={'width': 390, 'height': 300, 'zoom_level': 12, 'markers': 'color:origin|label:Map|'+str(lon)+','+str(lat)}, headers = {'x-api-key':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjU4ZDZjNGQ4YTFmY2M1N2U2OWEzOTQ2MjA3Mjg2YmMzZjVkOGFkOWMwOWNiMTVlNjVhMmE2MTk3MjM0NzQyNDk3MWUwYTI5YjEyMGFmNTRmIn0.eyJhdWQiOiJteWF3ZXNvbWVhcHAiLCJqdGkiOiI1OGQ2YzRkOGExZmNjNTdlNjlhMzk0NjIwNzI4NmJjM2Y1ZDhhZDljMDljYjE1ZTY1YTJhNjE5NzIzNDc0MjQ5NzFlMGEyOWIxMjBhZjU0ZiIsImlhdCI6MTU1ODE2MTAwMSwibmJmIjoxNTU4MTYxMDAxLCJleHAiOjE1NTgxNjQ2MDEsInN1YiI6IiIsInNjb3BlcyI6WyJiYXNpYyIsImVtYWlsIl19.dEvjipQtrDBcIT9N0BJnH_ds70Z9rE3tR6Nkyt0y0_VFlXq8VD-DsCUy5IRfThaujghvcxLZE6DD_pS5PnkFzfx2tKwJpfJjHhztWxZyrnWnmHd7u6zBkXnaCE4_Sa0jqEu797xnslkOjUoim-4sDkNn6kNaVkvLHTtQj6mpkTZUujkpi6y_UZplfNGR0erWv9UfhsjUwhcrIULCqJPDKjDvIJd8817aREfueQiCu92kmE-ez-jZKPgS93PBIc3KO8KSQzSHg4gn36EOFUeCN8ra0Obfr-gfcz605Ty4DKFUz3mXZRCRViBbNFRNSiSnml3gn1l3oC9GAgYomseUUQ'})
        img = r.content
        with open('loc.png', 'wb') as f:
            f.write(img)

        pixmap = QPixmap('loc.png')
        self.mapBox.setPixmap(pixmap)


app = QApplication(sys.argv)

loginWindow = loginClass()
loginWindow.show()

sys.exit(app.exec())
