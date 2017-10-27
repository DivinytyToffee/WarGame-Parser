import sys
import requests
from PyQt5.QtGui import QPixmap, QIcon
import json
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QAction, QMessageBox, \
QWidget, QFrame, QTableWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QTableWidgetItem, QMessageBox, QWidget, \
    QLabel, QComboBox

import wargaming_class_s as wg

application_id = 'ff260aebae4d7ba6d1164685003616f4'


class AchievementsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 300)
        self.setWindowTitle('Achievements')
        self.show()


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
        self.enter_nickname.setText('RipHanter___________EVIL')


        self.btn_nickname_text = QPushButton('Search nicknames')
        self.btn_nickname_text.clicked.connect(self.print_nickname)

        self.btn_tanks_window = QPushButton('Technique')
        self.btn_tanks_window.clicked.connect(self.tanks_window)

        self.btn_achivment_window = QPushButton('Achievements')
        self.btn_achivment_window.clicked.connect(self.achievements_window)

        self.table_widget.doubleClicked.connect(self.table_double_click)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.table_widget, 1, 0, 8, 1)
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
        grid.addWidget(self.enter_nickname, 9, 0)
        grid.addWidget(self.btn_nickname_text, 9, 1)
        grid.addWidget(self.btn_tanks_window, 9, 2)
        # grid.addWidget(self.btn_achivment_window, 8, 2)

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

    def achievements_window(self):
        achv_win = AchievementsWindow()
        achv_win.exec_()

    def set_account_id(self, parser):
        return parser.personal_data().account_id()


class TankWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.players_tech = QComboBox(self)
        self.players_tech.setGeometry(9, 5, 180, 25)
        self.players_tech.addItem('')
        self.filling_player_tech()
        self.players_tech.activated[str].connect(self.onActivated)

        # self.tank_picture_frame = QFrame(self)
        # self.tank_picture_frame.setGeometry(200, 5, 180, 180)
        # self.tank_picture_frame.set

        self.label_max_weight = QLabel(self)
        self.label_max_weight.move(10, 35)
        self.label_max_weight.setText('Real weight(kg): ')


        self.label_hull_weight = QLabel(self)
        self.label_hull_weight.move(10, 65)
        self.label_hull_weight.setText('Hull weight(kg): ')

        self.label_turret = QLabel(self)
        self.label_turret.move(10, 95)
        self.label_turret.setText('Turret characteristics: ')

        self.label_suspension = QLabel(self)
        self.label_suspension.move(10, 125)
        self.label_suspension.setText('Characteristics of running gear: ')

        self.label_is_default = QLabel(self)
        self.label_is_default.move(10, 155)
        self.label_is_default.setText('Basic equipment: ')

        self.label_ammo = QLabel(self)
        self.label_ammo.move(10, 185)
        self.label_ammo.setText('Characteristics of the projectile shells: ')

        self.label_gun = QLabel(self)
        self.label_gun.move(10, 215)
        self.label_gun.setText('Characteristics of the gun: ')

        self.label_weight = QLabel(self)
        self.label_weight.move(10, 245)
        self.label_weight.setText('Weight(kg): ')

        self.label_modules = QLabel(self)
        self.label_modules.move(10, 275)
        self.label_modules.setText('Installed modules: ')

        self.label_max_ammo = QLabel(self)
        self.label_max_ammo.move(10, 305)
        self.label_max_ammo.setText('Ammunition kit: ')

        self.label_profile_id = QLabel(self)
        self.label_profile_id.move(10, 335)
        self.label_profile_id.setText('Equipment ID: ')

        self.label_radio = QLabel(self)
        self.label_radio.move(10, 365)
        self.label_radio.setText('Characteristics of the radio station: ')

        self.label_siege = QLabel(self)
        self.label_siege.move(10, 395)
        self.label_siege.setText('Characteristics of machines in siege mode: ')

        self.label_speed_forward = QLabel(self)
        self.label_speed_forward.move(10, 425)
        self.label_speed_forward.setText('Max speed(km/h): ')

        self.label_speed_backward = QLabel(self)
        self.label_speed_backward.move(10, 455)
        self.label_speed_backward.setText('Max backward speed(km/h): ')

        self.label_hull_hp = QLabel(self)
        self.label_hull_hp.move(10, 485)
        self.label_hull_hp.setText('Body strength: ')

        self.label_armor = QLabel(self)
        self.label_armor.move(10, 515)
        self.label_armor.setText('Armour: ')

        self.label_hp = QLabel(self)
        self.label_hp.move(10, 545)
        self.label_hp.setText('Strength: ')

        self.label_engine = QLabel(self)
        self.label_engine.move(10, 575)
        self.label_engine.setText('Engine characteristics: ')

        self.setGeometry(300, 300, 1380, 600)
        self.setWindowTitle('Tech')
        self.show()

    @staticmethod
    def dict_tech_player():
        account_id = FuckingGrid().account_id
        account = wg.Account(account_id, application_id)
        tankopedia = wg.Tankopedia(application_id)
        parser = wg.Parser(account, tankopedia)
        dict_tech_player = {parser.tanks_list(str(x)).name(): x for x in parser.player_technique().tank_id_list()}
        return dict_tech_player

    def filling_player_tech(self):
        parser = self.parser()
        for i in parser.player_technique().tank_id_list():
            rs = requests.get(parser.tanks_list(str(i)).images()['contour_icon'])

            pixmap = QPixmap()
            pixmap.loadFromData(rs.content)

            icon = QIcon(pixmap)
            name = ' ' + parser.tanks_list(str(i)).name()
            self.players_tech.addItem(icon, name)

    def parser(self):
        return wg.Parser(wg.Account(FuckingGrid().account_id, application_id), wg.Tankopedia(application_id))

    def comon_method_oA(self, tank_id):
        tank = wg.Tankopedia(application_id)
        tank_charac = tank.tech_characteristic(tank_id)['data'][tank_id]
        return tank_charac


    def onActivated(self, text):
        tank_id_oa = str(self.dict_tech_player()[text[1:]])
        print(tank_id_oa)
        #######################################################
        self.label_ammo.setText('Characteristics of the projectile shells: ')
        for i in self.comon_method_oA(tank_id_oa)['ammo']:
            self.label_ammo.setText(self.label_ammo.text() + " ".join(i['type'].split('_')) + ': dam: ' + \
                                    json.dumps(i['damage']) + ', pen: ' + json.dumps(i['penetration']) + '  ')
        self.label_ammo.adjustSize()
        #######################################################
        self.label_max_weight.setText('Real weight(kg): ')
        self.label_max_weight.setText(self.label_max_weight.text() + \
                                      str(self.comon_method_oA(tank_id_oa)['max_weight']) \
                                      + 'kg')
        self.label_max_weight.adjustSize()
        #######################################################
        self.label_hull_weight.setText('Hull weight(kg): ')
        self.label_hull_weight.setText(self.label_hull_weight.text() + \
                                       str(self.comon_method_oA(tank_id_oa)['hull_weight']) \
                                       + 'kg')
        self.label_hull_weight.adjustSize()
        #######################################################
        self.label_turret.setText('Turret characteristics: ')
        self.label_turret.setText(self.label_turret.text() + \
                                  self.comon_method_oA(tank_id_oa)['turret']['name'] \
                                  + ' Weight(kg): ' \
                                  + str(self.comon_method_oA(tank_id_oa)['turret']['weight']) \
                                  + ' Traverse angle, left (deg): ' \
                                  + str(self.comon_method_oA(tank_id_oa)['turret']['traverse_left_arc']) \
                                  + ' Traverse angle, right (deg): ' \
                                  + str(self.comon_method_oA(tank_id_oa)['turret']['traverse_right_arc']) \
                                  + ' hp: ' \
                                  + str(self.comon_method_oA(tank_id_oa)['turret']['hp']) \
                                  +' Traverse speed(deg/s): ' \
                                  + str(self.comon_method_oA(tank_id_oa)['turret']['traverse_speed'])
                                  + ' View range (m): ' \
                                  + str(self.comon_method_oA(tank_id_oa)['turret']['view_range']))
        self.label_turret.adjustSize()
        #######################################################
        self.label_suspension.setText('Characteristics of running gear: ')
        self.label_suspension.setText(self.label_suspension.text() + \
                                      self.comon_method_oA(tank_id_oa)['suspension']['name'] \
                                      + ' Weight(kg): ' \
                                      + str(self.comon_method_oA(tank_id_oa)['suspension']['weight']) \
                                      + ' Traverse speed (deg/s): ' \
                                      + str(self.comon_method_oA(tank_id_oa)['suspension']['traverse_speed']) \
                                      + ' Load limit (kg): ' \
                                      + str(self.comon_method_oA(tank_id_oa)['suspension']['load_limit']))
        self.label_suspension.adjustSize()
        #######################################################
        self.label_is_default.setText('Basic equipment: ')
        self.label_is_default.setText(self.label_is_default.text() + \
                                      str(self.comon_method_oA(tank_id_oa)['is_default']))
        self.label_is_default.adjustSize()
        #######################################################
        self.label_gun.setText('Characteristics of the gun: ')
        self.label_gun.setText(self.label_gun.text() + \
                               self.comon_method_oA(tank_id_oa)['gun']['name'] \
                               + ' Caliber (mm): '
                               + str(self.comon_method_oA(tank_id_oa)['gun']['caliber']) \
                               + ' Dispersion at 100 m (m): ' \
                               + str(self.comon_method_oA(tank_id_oa)['gun']['dispersion']) \
                               + ' Rate of fire (rounds/min) ' \
                               + str(self.comon_method_oA(tank_id_oa)['gun']['fire_rate']) \
                               + ' Aiming time (s): ' \
                               + str(self.comon_method_oA(tank_id_oa)['gun']['aim_time']) \
                               +' Reload time (s): ' \
                               + str(self.comon_method_oA(tank_id_oa)['gun']['reload_time']) \
                               + ' Traverse speed (deg/s): ' \
                               + str(self.comon_method_oA(tank_id_oa)['gun']['traverse_speed']))
        self.label_gun.adjustSize()
        #######################################################
        self.label_weight.setText('Weight(kg): ')
        self.label_weight.setText(self.label_weight.text() + \
                                  str(self.comon_method_oA(tank_id_oa)['weight']))
        self.label_weight.adjustSize()
        #######################################################
        k = self.parser().tanks_characteristics(self.dict_tech_player()[text[1:]]).modules()
        file = open('data/modules.json')
        modules_dict = json.loads(file.read())
        self.label_modules.setText('Installed modules: ')
        for i in k:
            if k.get(i) != None:
                self.label_modules.setText(self.label_modules.text() + modules_dict['data'][str(k.get(i))]['name'] \
                                           + ', ')
            else:
                continue
        self.label_modules.adjustSize()
        #######################################################
        self.label_max_ammo.setText('Ammunition kit: ')
        self.label_max_ammo.setText(self.label_max_ammo.text() + \
                                    str(self.comon_method_oA(tank_id_oa)['max_ammo']))
        self.label_max_ammo.adjustSize()
        #######################################################
        self.label_profile_id.setText('Equipment ID: ')
        self.label_profile_id.setText(self.label_profile_id.text() + \
                                      self.comon_method_oA(tank_id_oa)['profile_id'])
        self.label_profile_id.adjustSize()
        #######################################################
        self.label_radio.setText('Characteristics of the radio station: ')
        self.label_radio.setText(self.label_radio.text() + \
                                 self.comon_method_oA(tank_id_oa)['radio']['name'] \
                                 + ' Signal range: ' \
                                 + str(self.comon_method_oA(tank_id_oa)['radio']['signal_range']) \
                                 + ' Weight: ' \
                                 + str(self.comon_method_oA(tank_id_oa)['radio']['weight']))
        self.label_radio.adjustSize()
        #######################################################
        self.label_siege.setText('Characteristics of machines in siege mode: ')
        self.label_siege.setText(self.label_siege.text() + \
                                 str(self.comon_method_oA(tank_id_oa)['siege']))
        self.label_siege.adjustSize()
        #######################################################
        self.label_speed_forward.setText('Max speed(km/h): ')
        self.label_speed_forward.setText(self.label_speed_forward.text() + \
                                         str(self.comon_method_oA(tank_id_oa)['speed_forward']))
        self.label_speed_forward.adjustSize()
        #######################################################
        self.label_speed_backward.setText('Max backward speed(km/h): ')
        self.label_speed_backward.setText(self.label_speed_backward.text() + \
                                          str(self.comon_method_oA(tank_id_oa)['speed_backward']))
        self.label_speed_backward.adjustSize()
        #######################################################
        self.label_hull_hp.setText('Body strength: ')
        self.label_hull_hp.setText(self.label_hull_hp.text() + \
                                   str(self.comon_method_oA(tank_id_oa)['hull_hp']))
        self.label_hull_hp.adjustSize()
        #######################################################
        self.label_armor.setText('Armour: ')
        if self.comon_method_oA(tank_id_oa)['armor']['turret'] != None:
            self.label_armor.setText(self.label_armor.text() + \
                                     'Turret: ' \
                                     + ' front - ' \
                                     + str(self.comon_method_oA(tank_id_oa)['armor']['turret']['front']) \
                                     + ' sides - ' \
                                     + str(self.comon_method_oA(tank_id_oa)['armor']['turret']['sides']) \
                                     + ' rear - ' \
                                     + str(self.comon_method_oA(tank_id_oa)['armor']['turret']['rear']) \
                                     + ' Hull: ' \
                                     + ' front - ' \
                                     + str(self.comon_method_oA(tank_id_oa)['armor']['hull']['front']) \
                                     + ' sides - ' \
                                     + str(self.comon_method_oA(tank_id_oa)['armor']['hull']['sides']) \
                                     + ' rear - ' \
                                     + str(self.comon_method_oA(tank_id_oa)['armor']['hull']['rear']))
        else:
            self.label_armor.setText(self.label_armor.text() + \
                                     'Turret: None' \
                                     + ' Hull: ' \
                                     + ' front - ' \
                                     + str(
                self.comon_method_oA(tank_id_oa)['armor']['hull']['front']) \
                                     + ' sides - ' \
                                     + str(
                self.comon_method_oA(tank_id_oa)['armor']['hull']['sides']) \
                                     + ' rear - ' \
                                     + str(
                self.comon_method_oA(tank_id_oa)['armor']['hull']['rear']))
        self.label_armor.adjustSize()
        #####################################################
        self.label_hp.setText('Strength: ')
        self.label_hp.setText(self.label_hp.text() + \
                              str(self.comon_method_oA(tank_id_oa)['hp']))
        self.label_hp.adjustSize()
        #####################################################
        self.label_engine.setText('Engine characteristics: ')
        self.label_engine.setText(self.label_engine.text() + \
                                  str(self.comon_method_oA(tank_id_oa)['engine']['name']) \
                                  + ' Engine Power (hp): ' \
                                  + str(self.comon_method_oA(tank_id_oa)['engine']['power']) \
                                  + ' Chance of engine fire: ' \
                                  + str(self.comon_method_oA(tank_id_oa)['engine']['fire_chance']) \
                                  + ' Weight(kg): ' \
                                  + str(self.comon_method_oA(tank_id_oa)['engine']['weight']))
        self.label_engine.adjustSize()


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tankopedia = wg.Tankopedia(application_id)
        exitAction = QAction(QIcon('icon/cancel.svg'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        update_data_action = QAction(QIcon('icon/download.svg'), 'Update tanks date', self)
        update_data_action.setShortcut('Ctrl+U')
        update_data_action.setStatusTip('Update all *.json files')
        update_data_action.triggered.connect(self.update_files)
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(update_data_action)


        self.fgrid = FuckingGrid()
        self.setCentralWidget(self.fgrid)
        self.resize(800, 550)
        self.center()
        self.setWindowTitle('GUI')
        self.show()

    def update_files(self):
        self.statusBar().showMessage('Start update')
        wg.Tankopedia(application_id).loads_in_files()
        QMessageBox.about(self, 'Message', "All files update's")
        self.statusBar().showMessage('')

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())