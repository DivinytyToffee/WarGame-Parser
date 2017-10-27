import urllib.request as req
import json
from AdditionalMethods import *


class Account:
    def __init__(self, account_id, application_id):
        self.__account_id = account_id
        self.__application_id = application_id

    def __del__(self):
        del self.__account_id
        del self.__application_id

    def request_clans(self, clan_id):
        url = 'https://api.worldoftanks.ru/wgn/clans/info/?application_id=' + str(self.__application_id) + \
              '&clan_id=' + str(clan_id)
        response = json.loads(req.urlopen(url).read().decode('utf-8'))
        return response

    def request_personal_data(self):
        url = 'https://api.worldoftanks.ru/wot/account/info/\
        ?application_id=' + str(self.__application_id) + '&account_id=' + str(self.__account_id)
        response = json.loads(req.urlopen(url).read().decode('utf-8'))
        return response

    def request_player_s_technique(self):
        url = 'https://api.worldoftanks.ru/wot/account/tanks/\
        ?application_id=' + str(self.__application_id) + '&account_id=' + str(self.__account_id)
        response = json.loads(req.urlopen(url).read().decode('utf-8'))
        return response

    def request_player_s_achievements(self):
        url = 'https://api.worldoftanks.ru/wot/account/achievements/\
        ?application_id=' + str(self.__application_id) + '&account_id=' + str(self.__account_id)
        response = json.loads(req.urlopen(url).read().decode('utf-8'))
        return response

    def request_data_clan(self, clan_id):
        url = 'https://api.worldoftanks.ru/wot/globalmap/claninfo/?application_id=' + str(self.__application_id) + \
              '&clan_id=' + str(clan_id)
        response = json.loads(req.urlopen(url).read().decode('utf-8'))
        return response


class Tankopedia:
    def __init__(self, application_id):
        self.__application_id = application_id

    def __del__(self):
        del self.__application_id

    def __technique(self):
        url = 'https://api.worldoftanks.ru/wot/encyclopedia/vehicles/?application_id=' + str(self.__application_id)
        response = json.loads(req.urlopen(url).read().decode('utf-8'))
        return response

    def __technicals_characterictic(self, tank_id):
        url = 'https://api.worldoftanks.ru/wot/encyclopedia/vehicleprofile/?application_id=' + \
              str(self.__application_id) + '&tank_id=' + str(tank_id)
        response = json.loads(req.urlopen(url).read().decode('utf-8'))
        return response

    def __achievment(self):
        url = 'https://api.worldoftanks.ru/wot/encyclopedia/achievements/?application_id=' + str(self.__application_id)
        response = json.loads(req.urlopen(url).read().decode('utf-8'))
        return response

    def __information_about_tankopedia(self):
        url = 'https://api.worldoftanks.ru/wot/encyclopedia/info/?application_id=' + str(self.__application_id)
        response = json.loads(req.urlopen(url).read().decode('utf-8'))
        return response

    def __game_maps(self):
        url = 'https://api.worldoftanks.ru/wot/encyclopedia/arenas/?application_id=' + str(self.__application_id)
        response = json.loads(req.urlopen(url).read().decode('utf-8'))
        return response

    def __equipment(self):
        url = 'https://api.worldoftanks.ru/wot/encyclopedia/provisions/?application_id=' + str(self.__application_id)
        response = json.loads(req.urlopen(url).read().decode('utf-8'))
        return response

    def __personal_combat_missions(self):
        url = 'https://api.worldoftanks.ru/wot/encyclopedia/personalmissions/?application_id=' + \
              str(self.__application_id)
        response = json.loads(req.urlopen(url).read().decode('utf-8'))
        return response

    def __personal_reserve(self):
        url = 'https://api.worldoftanks.ru/wot/encyclopedia/boosters/?application_id=' + str(self.__application_id)
        response = json.loads(req.urlopen(url).read().decode('utf-8'))
        return response

    def __equipment_assembling(self, tank_id):
        url = 'https://api.worldoftanks.ru/wot/encyclopedia/vehicleprofiles/?application_id=' \
              + str(self.__application_id) + '&tank_id=5953' + str(tank_id)
        response = json.loads(req.urlopen(url).read().decode('utf-8'))
        return response

    def __modules(self):
        url = 'https://api.worldoftanks.ru/wot/encyclopedia/modules/?application_id=' + str(self.__application_id)
        response = json.loads(req.urlopen(url).read().decode('utf-8'))
        return response

    def update_tech(self, tank_id):
        with open('tanks_characteristics.txt', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.__technicals_characterictic(tank_id), f, sort_keys=True, indent=4, separators=(',', ': ')))
        print('All characteristics of the configuration of technology added to the tanks_characteristics.txt')

        with open('equipment_assembling.txt', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.__equipment_assembling(tank_id), f, sort_keys=True, indent=4, separators=(',', ': ')))
        print('All characteristics equipment assembling are added to the equipment_assembling.txt')

    def tech_characteristic(self, tank_id):
        return self.__technicals_characterictic(tank_id)

    def instal_modules(self, tank_id):
        return self.__equipment_assembling(tank_id)

    def loads_in_files(self):
        with open('data/tanks_list.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.__technique(), f, sort_keys=True, indent=4, separators=(',', ': ')))
        print('All available technique recorded in tanks_list.json')

        with open('data/tanks_achievements.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.__achievment(), f, sort_keys=True, indent=4, separators=(',', ': ')))
        print('All achievements added to the tanks_achievement.json')

        with open('data/tankopedia_info.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.__information_about_tankopedia(), f, sort_keys=True, indent=4, separators=(',', ': ')))
        print('Information about tankopedia added to the tankopedia_info.json')

        with open('data/game_maps.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.__game_maps(), f, sort_keys=True, indent=4, separators=(',', ': ')))
        print('Added description game maps to the game_maps.json')

        with open('data/equipment.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.__equipment(), f, sort_keys=True, indent=4, separators=(',', ': ')))
        print('All available equipment and equipment are added to the equipment.json')

        with open('data/personal_combat_mission.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.__personal_combat_missions(), f, sort_keys=True, indent=4, separators=(',', ': ')))
        print('All personal combat mission are added to the personal_combat_mission.json')

        with open('data/personal_reserve.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.__personal_reserve(), f, sort_keys=True, indent=4, separators=(',', ': ')))
        print('All info about personal reserve are added to the personal_reserve.json')

        with open('data/modules.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.__modules(), f, sort_keys=True, indent=4, separators=(',', ': ')))
        print('A list of available modules that can be installed on the equipment, such as engines, towers, etc\
        are added to the modules.json')


class Parser:
    def __init__(self, account, tankopedia):
        self.__account = account
        self.__tankopedia = tankopedia

    def __del__(self):
        del self.__account
        del self.__tankopedia

    def __personal_data_internal(self):
        return self.__account.request_personal_data()

    def personal_data(self):
        personal_data = PersonalDataAdditionalMethods(self.__personal_data_internal())
        return personal_data

    def __player_technique_internal(self):
        return self.__account.request_player_s_technique()

    def player_technique(self):
        player_s_technique = PlayerTechniqueAdditionalMethods(self.__player_technique_internal())
        return player_s_technique

    def __personal_achievment_internal(self):
        return self.__account.request_player_s_achievements()

    def player_achievment(self):
        player_achievment = PlayerAchievmentAdditionalMethods(self.__personal_achievment_internal())
        return player_achievment

    @staticmethod
    def __tanks_list_internal():
        f = open('data/tanks_list.json', 'r').read()
        list_out = json.loads(f)
        return list_out

    def tanks_list(self, tank_id):
        tanks = TanksAdditionalMethods(self.__tanks_list_internal(), tank_id)
        return tanks

    @staticmethod
    def __tank_characteristics_internal():
        f = open('data/tanks_characteristics.json', 'r').read()
        list_out = json.loads(f)
        return list_out

    def tanks_characteristics(self, tank_id):
        characteristics = CharacteristicsAdditionalMethods(Tankopedia(\
            'ff260aebae4d7ba6d1164685003616f4').tech_characteristic(tank_id), tank_id)
        return characteristics

    def clans_data(self, clan_id):
        return self.__account.request_data_clan(clan_id)

    @staticmethod
    def __tanks_achievments_internal():
        f = open('data/tanks_achievments.json', 'r').read()
        list_out = json.loads(f)
        return list_out

    def tanks_achievments(self, account_id):
        achievments = AchievmentAdditionalMethods(self.__personal_achievment_internal(), account_id)
        return achievments


def request_players_nickname(application_id, nickname):
    url = 'https://api.worldoftanks.ru/wot/account/list/?application_id=' + str(application_id) + \
          '&search=' + nickname
    response = json.loads(req.urlopen(url).read().decode('utf-8'))
    return response['data']
