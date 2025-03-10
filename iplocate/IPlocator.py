from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import logging
import webbrowser

def location(ip: str):
    response = requests.get(f"http://ip-api.com/json/{ip}?lang=ru")
    if response.status_code == 404:
        print("Oops")
    result = response.json()
    if result["status"] == "fail":
        return "Enter the correct IP address"

    record = []

    for key, value in result.items():
        record.append(value)
        print(f"[{key.title()}]: {value}")
    return tuple(record)


def get_external_ip_reliable():
    services = [
        'https://api.ipify.org?format=json',
        'https://api.my-ip.io/ip.json',
        'https://ifconfig.me/ip'   
    ]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    for url in services:
        try:
            if 'json' in url:
                response = requests.get(url, headers=headers, timeout=3)
                response.raise_for_status()
                data = response.json()
                if 'ip' in data:
                    return data['ip']
                else:
                    logging.error(f"Сервис {url} вернул неожиданный JSON: {data}")
                    return data
            else:
                response = requests.get(url, headers=headers, timeout=3)
                response.raise_for_status()
                return response.text.strip()
        except requests.exceptions.RequestException as e:
            logging.error(f"Ошибка при запросе к {url}: {e}")
            pass   
    return None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 504)
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ip_change = QtWidgets.QLabel(self.centralwidget)
        self.ip_change.setGeometry(QtCore.QRect(10, 0, 411, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ip_change.setFont(font)
        self.ip_change.setObjectName("ip_change")
        self.determine_your_ip_button = QtWidgets.QPushButton(self.centralwidget)
        self.determine_your_ip_button.setGeometry(QtCore.QRect(460, 10, 221, 61))
        self.determine_your_ip_button.setObjectName("determine_your_ip_button")
        self.copy_your_ip_button = QtWidgets.QPushButton(self.centralwidget)
        self.copy_your_ip_button.setGeometry(QtCore.QRect(460, 80, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.copy_your_ip_button.setFont(font)
        self.copy_your_ip_button.setObjectName("copy_your_ip_button")
        self.copy_your_ip_button.clicked.connect(self.copy_ip_to_clipboard)
        self.determine_address = QtWidgets.QLabel(self.centralwidget)
        self.determine_address.setGeometry(QtCore.QRect(10, 170, 650, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.determine_address.setFont(font)
        self.determine_address.setObjectName("determine_address")
        self.IP_input = QtWidgets.QTextEdit(self.centralwidget)
        self.IP_input.setGeometry(QtCore.QRect(210, 240, 241, 51))
        self.IP_input.setObjectName("IP_input")
        self.enter_ip = QtWidgets.QLabel(self.centralwidget)
        self.enter_ip.setGeometry(QtCore.QRect(10, 240, 201, 51))
        self.enter_ip.setObjectName("enter_ip")
        self.your_country_change = QtWidgets.QLabel(self.centralwidget)
        self.your_country_change.setGeometry(QtCore.QRect(10, 40, 421, 31))
        self.your_country_change.setObjectName("your_country_change")
        self.your_city_change = QtWidgets.QLabel(self.centralwidget)
        self.your_city_change.setGeometry(QtCore.QRect(10, 80, 411, 31))
        self.your_city_change.setObjectName("your_city_change")
        self.determine_address_button = QtWidgets.QPushButton(self.centralwidget)
        self.determine_address_button.setGeometry(QtCore.QRect(10, 300, 441, 51))
        self.determine_address_button.setObjectName("determine_address_button")
        self.country_change = QtWidgets.QLabel(self.centralwidget)
        self.country_change.setGeometry(QtCore.QRect(10, 360, 401, 21))
        self.country_change.setObjectName("country_change")
        self.city_change = QtWidgets.QLabel(self.centralwidget)
        self.city_change.setGeometry(QtCore.QRect(10, 390, 411, 21))
        self.city_change.setObjectName("city_change")
        self.view_on_the_map_front_ = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.view_on_the_map_front_.setGeometry(QtCore.QRect(460, 300, 211, 51))
        self.view_on_the_map_front_.setObjectName("view_on_the_map_front_")
        self.view_on_the_map_back_button = QtWidgets.QPushButton(self.centralwidget)
        self.view_on_the_map_back_button.setGeometry(QtCore.QRect(460, 300, 211, 51))
        self.view_on_the_map_back_button.setText("")
        self.view_on_the_map_back_button.setObjectName("view_on_the_map_back_button")
        self.tg = QtWidgets.QLabel(self.centralwidget)
        self.tg.setGeometry(QtCore.QRect(480, 430, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.tg.setFont(font)
        self.tg.setObjectName("tg")
        self.view_on_the_map_back_button.raise_()
        self.ip_change.raise_()
        self.determine_your_ip_button.raise_()
        self.copy_your_ip_button.raise_()
        self.determine_address.raise_()
        self.IP_input.raise_()
        self.enter_ip.raise_()
        self.your_country_change.raise_()
        self.your_city_change.raise_()
        self.determine_address_button.raise_()
        self.country_change.raise_()
        self.city_change.raise_()
        self.view_on_the_map_front_.raise_()
        self.tg.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ip_change.setText(_translate("MainWindow", "your IP address"))
        self.determine_your_ip_button.setText(_translate("MainWindow", "determine my IP"))
        self.determine_your_ip_button.clicked.connect(self.determine_your_ip)
        self.copy_your_ip_button.setText(_translate("MainWindow", "copy to clipboard"))
        self.determine_address.setText(_translate("MainWindow", "determine address\n If you leave the field empty, your location will be determined."))
        self.enter_ip.setText(_translate("MainWindow", "enter the IP address:"))
        self.your_country_change.setText(_translate("MainWindow", "country:"))
        self.your_city_change.setText(_translate("MainWindow", "city:"))
        self.determine_address_button.setText(_translate("MainWindow", "determine address"))
        self.determine_address_button.clicked.connect(self.determine_input_ip)
        self.country_change.setText(_translate("MainWindow", "country:"))
        self.city_change.setText(_translate("MainWindow", "city:"))
        self.view_on_the_map_front_.setText(_translate("MainWindow", "view on the map"))
        self.view_on_the_map_front_.clicked.connect(self.get_link_map)
        self.tg.setText(_translate("MainWindow", "tg: @world_adm1n"))

    def determine_your_ip(self):
        ip = get_external_ip_reliable()
        if ip:
            self.ip_change.setText(ip)
            country = location(ip)[1]
            city = location(ip)[5]
            self.your_country_change.setText(f'country: {country}')
            self.your_city_change.setText(f'city: {city}')
        else:
            self.ip_change.setText("couldn't determine the ip")
    def copy_ip_to_clipboard(self):
        clpbrd = QtWidgets.QApplication.clipboard()
        clpbrd.setText(self.ip_change.text())
    def determine_input_ip(self):
       input_value = self.IP_input.toPlainText()
       location_request = location(input_value)
       if location_request[0] == "success":
            country = location(input_value)[1]
            city = location(input_value)[5]
            self.country_change.setText(f'country: {country}')
            self.city_change.setText(f'city: {city}')
       else:
           msg = QtWidgets.QMessageBox()
           msg.setIcon(QtWidgets.QMessageBox.Information)  
           msg.setText("Enter your IP address correctly!")
           msg.setWindowTitle("Error")
           msg.setStandardButtons(QtWidgets.QMessageBox.Ok)  
           msg.exec_()


    def get_link_map(self):
        input_value = self.IP_input.toPlainText()
        location_request = location(input_value)
        if location_request[0] == "success":
            lat = location(input_value)[7]
            lon = location(input_value)[8]
            link = f'https://www.latlong.net/c/?lat={lat}&long={lon}'
            webbrowser.open(link)
           

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
