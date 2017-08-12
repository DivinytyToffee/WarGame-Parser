import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QDesktopWidget, QGridLayout, QLabel, \
    QLineEdit, QWidget, QAction, QFrame, QPushButton,  QTableWidget, QTableWidgetItem, QMessageBox, QComboBox
from PyQt5.QtGui import QIcon, QPixmap
import urllib.request
import wargaming_class_s as wg


application_id = 'ff260aebae4d7ba6d1164685003616f4'


class TankWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.players_tech = QComboBox(self)
        self.players_tech.setGeometry(10, 5, 180, 30)
        self.players_tech.addItem('')
        self.filling_player_tech()

        self.setGeometry(300, 300, 800, 550)
        self.setWindowTitle('Font dialog')
        self.show()

    def filling_player_tech(self):
        account_id = FuckingGrid().account_id
        account = wg.Account(account_id, application_id)
        tankopedia = wg.Tankopedia(application_id)
        parser = wg.Parser(account, tankopedia)
        for i in parser.player_technique().tank_id_list():
            self.players_tech.addItem(\
                QIcon(QPixmap().loadFromData\
                          (urllib.request.urlopen(parser.tanks_list(i).images()['contour_icon']).read())),\
                ' ' + parser.tanks_list(str(i)).name())


class FuckingGrid(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    account_id = None

    def initUI(self):

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(['Nickname', 'Account ID'])

        nickname_label = QLabel('Nickname')
        self.nickname_line = QLineEdit()
        self.nickname_line.setDisabled(True)

        clan_name_label = QLabel('Clan Name')
        self.clan_name_line = QLineEdit()
        self.clan_name_line.setDisabled(True)

        create_data_label = QLabel("Data create's")
        self.create_data_line = QLineEdit()
        self.create_data_line.setDisabled(True)

        rating_label = QLabel('Rating')
        self.rating_line = QLineEdit()
        self.rating_line.setDisabled(True)

        tech_count_label = QLabel('Quantity of equipment')
        self.tech_count_line = QLineEdit()
        self.tech_count_line.setDisabled(True)

        achi_count_label = QLabel('Number of achievements')
        self.achi_count_line = QLineEdit()
        self.achi_count_line.setDisabled(True)

        self.enter_nickname = QLineEdit()


        self.btn_nickname_text = QPushButton('Search nicknames')
        self.btn_nickname_text.clicked.connect(self.print_nickname)

        self.btn_tanks_window = QPushButton('Technique')
        self.btn_tanks_window.clicked.connect(self.tanks_window)

        self.table_widget.doubleClicked.connect(self.table_double_click)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.table_widget, 1, 0, 7, 1)
        grid.addWidget(nickname_label, 1, 1)
        grid.addWidget(self.nickname_line, 1, 2)
        grid.addWidget(clan_name_label, 2, 1)
        grid.addWidget(self.clan_name_line, 2, 2)
        grid.addWidget(create_data_label, 3, 1)
        grid.addWidget(self.create_data_line, 3, 2)
        grid.addWidget(rating_label, 4, 1)
        grid.addWidget(self.rating_line, 4, 2)
        grid.addWidget(tech_count_label, 5, 1)
        grid.addWidget(self.tech_count_line, 5, 2)
        grid.addWidget(achi_count_label, 6, 1)
        grid.addWidget(self.achi_count_line, 6, 2)
        grid.addWidget(self.enter_nickname, 8, 0)
        grid.addWidget(self.btn_nickname_text, 8, 1)
        grid.addWidget(self.btn_tanks_window, 8, 2)

        self.setLayout(grid)
        self.setMinimumSize(100, 200)

    def print_nickname(self):
        if self.enter_nickname.text() and len(self.enter_nickname.text()) >= 3:
            plyers_list = wg.request_players_nickname(application_id, self.enter_nickname.text())
            self.table_widget.setRowCount(len((plyers_list)))
            for x in range(len(plyers_list)):
                self.table_widget.setItem(x, 0, QTableWidgetItem(plyers_list[x]['nickname']))
                self.table_widget.setItem(x, 1, QTableWidgetItem(str(plyers_list[x]['account_id'])))
        else:
            QMessageBox.question(self, 'Error', "Enter nickname or they part(min 3 signs)", QMessageBox.Ok,
                                 QMessageBox.Ok)

    def table_double_click(self, me):
        selected_account_id = QTableWidgetItem.text(self.table_widget.item(me.row(), me.column()))
        tank_id = '0'
        account = wg.Account(selected_account_id, application_id)
        tankopedia = wg.Tankopedia(application_id)
        parser = wg.Parser(account, tankopedia)
        FuckingGrid.account_id = self.set_account_id(parser)
        self.nickname_line.setText(parser.personal_data().nickname())
        if parser.personal_data().clan_id():
            self.clan_name_line.setText(account.request_clans(parser.personal_data().clan_id())\
                                            ['data'][str(parser.personal_data().clan_id())]['name'])
        else:
            self.clan_name_line.setText('In the clan does not consist')
        self.create_data_line.setText(str(parser.personal_data().created_at()))
        self.rating_line.setText(str(parser.personal_data().global_rating()))
        self.tech_count_line.setText(str(len(parser.player_technique().tank_id_list())))
        self.achi_count_line.setText(str(len(parser.player_achievment().achievements())))

    def tanks_window(self):
        tanks_win = TankWindow()
        tanks_win.exec_()

    def set_account_id(self, parser):
        return parser.personal_data().account_id()

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.fgrid = FuckingGrid()
        self.setCentralWidget(self.fgrid)
        self.resize(800, 550)
        self.center()
        self.setWindowTitle('GUI')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())