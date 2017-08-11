class TanksAdditionalMethods:

    def __init__(self, tank_list, tank_id):
        self.__tank_id = tank_id
        self.__tank_list = tank_list['data'][str(tank_id)]

    def __del__(self):
        del self.__tank_list
        del self.__tank_id

    def __main_maethod(self, key):
        return self.__tank_list[str(key)]

    def name(self):
        """Название техники"""
        return self.__main_maethod('name')

    def tank_id(self):
        """Идентификатор техники"""
        return self.__main_maethod('tank_id')

    def is_premium(self):
        """Показывает, является ли техника премиум техникой"""
        return self.__main_maethod('is_premium')

    def modules_tree(self):
        """Информация об исследовании модулей"""
        return self.__main_maethod('modules_tree')

    def turrets(self):
        """Список идентификаторов совместимых башен"""
        return self.__main_maethod('turrets')

    def images(self):
        """Изображения техники"""
        return self.__main_maethod('images')

    def next_tanks(self):
        """Список доступной для исследования техники в виде пар:
            -идентификатор исследуемой техники
            -стоимость исследования в опыте"""
        return self.__main_maethod('next_tanks')

    def tag(self):
        """Тег техники"""
        return self.__main_maethod('tag')

    def guns(self):
        """Список идентификаторов совместимых орудий"""
        return self.__main_maethod('guns')

    def provisions(self):
        """Список идентификаторов совместимого оборудования и снаряжения"""
        return self.__main_maethod('provisions')

    def nation(self):
        """Нация"""
        return self.__main_maethod('nation')

    def description(self):
        """Описание техники"""
        return self.__main_maethod('description')

    def prices_xp(self):
        """Список значений стоимости исследования в виде пар:
        -идентификатор родительской техники
        -стоимость исследованния в опыте"""
        return self.__main_maethod('prices_xp')

    def is_gift(self):
        """Показывает, является ли техника подарочной"""
        return self.__main_maethod('is_gift')

    def price_credit(self):
        """Стоимость в кредитах"""
        return self.__main_maethod('price_credit')

    def price_gold(self):
        """Стоимость в золоте"""
        return self.__main_maethod('price_gold')

    def suspensions(self):
        """Список идентификаторов совместимых ходовых"""
        return self.__main_maethod('suspensions')

    def is_premium_igr(self):
        """Указывает технику IGR. Действительно только для корейского региона"""
        return self.__main_maethod('is_premium_igr')

    def radios(self):
        """Список идентификаторов устанавливаемых радиостанций"""
        return self.__main_maethod('radios')

    def type(self):
        """Тип техники"""
        return self.__main_maethod('type')

    def short_name(self):
        """Сокращённое название техники"""
        return self.__main_maethod('short_name')

    def default_profile(self):
        """Характеристики базовой комплектации"""
        return self.__main_maethod('default_profile')

    def engines(self):
        """Список идентификаторов совместимых двигателей"""
        return self.__main_maethod('engines')

    def tier(self):
        """Уровень"""
        return self.__main_maethod('tier')

    def crew(self):
        """Экипаж"""
        return self.__main_maethod('crew')


class CharacteristicsAdditionalMethods:

    def __init__(self, vench_list, tank_id):
        self.__tank_id = tank_id
        self.__vench_list = vench_list['data'][str(tank_id)]

    def __del__(self):
        del self.__vench_list
        del self.__tank_id

    def max_weight(self):
        """редельная масса (кг)"""
        return self.__vench_list['max_weight']

    def hull_weight(self):
        """Масса корпуса (кг)"""
        return self.__vench_list['hull_weight']

    def turret(self):
        """Характеристики башни"""
        return self.__vench_list['turret']

    def suspension(self):
        """Характеристики ходовой"""
        return self.__vench_list['suspension']

    def is_default(self):
        """Базовая комплектация"""
        return self.__vench_list['is_default']

    def ammo(self):
        """Харатеристики снарядов орудия"""
        return self.__vench_list['ammo']

    def tank_id(self):
        """дентификатор техники"""
        return self.__vench_list['tank_id']

    def gun(self):
        """Характеристики орудия"""
        return self.__vench_list['gun']

    def weight(self):
        """Масса (кг)"""
        return self.__vench_list['weight']

    def modules(self):
        """Установленные модули"""
        return self.__vench_list['modules']

    def max_ammo(self):
        """Боекомплект"""
        return self.__vench_list['max_ammo']

    def profile_id(self):
        """Идентификатор комплектации техники"""
        return self.__vench_list['profile_id']

    def radio(self):
        """Характеристики радиостанции"""
        return self.__vench_list['radio']

    def siege(self):
        """Характеристики машин в осадном режиме"""
        return self.__vench_list['siege']

    def speed_forward(self):
        """Максимальная скорость"""
        return self.__vench_list['speed_forward']

    def hull_hp(self):
        """Прочность корпуса"""
        return self.__vench_list['hull_hp']

    def armor(self):
        """Бронирование"""
        return self.__vench_list['armor']

    def hp(self):
        """Прочность"""
        return self.__vench_list['hp']

    def speed_backward(self):
        """Макс. скорость заднего хода (км/ч)"""
        return self.__vench_list['speed_backward']

    def engine(self):
        """Характеристики двигателя"""
        return self.__vench_list['engine']


class PersonalDataAdditionalMethods:

    def __init__(self, personal_data):
        per_data = personal_data['data']
        per_data = [x for x in per_data]
        per_data = "".join(per_data)
        self.__personal_data = personal_data['data'][per_data]

    def __del__(self):
        del self.__personal_data

    def all_data(self):
        return self.__personal_data

    def last_battle_time(self):
        return self.__personal_data['last_battle_time']

    def created_at(self):
        return self.__personal_data['created_at']

    def clan_id(self):
        return self.__personal_data['clan_id']

    def global_rating(self):
        return self.__personal_data['global_rating']

    def statistics(self):
        return self.__personal_data['statistics']

    def private(self):
        return self.__personal_data['private']

    def client_language(self):
        return self.__personal_data['client_language']

    def logout_at(self):
        return self.__personal_data['logout_at']

    def updated_at(self):
        return self.__personal_data['updated_at']

    def nickname(self):
        return self.__personal_data['nickname']

    def account_id(self):
        return self.__personal_data['account_id']


class PlayerTechniqueAdditionalMethods:

    def __init__(self, player_technique):
        player_tech = player_technique['data']
        player_tech = [x for x in player_tech]
        player_tech = "".join(player_tech)
        self.__player_technique = player_technique['data'][player_tech]

    def __del__(self):
        del self.__player_technique

    def list_tech(self):
        return self.__player_technique

    def tank_id_list(self):
        tanks_id = [x['tank_id'] for x in self.list_tech()]
        return tanks_id

    def statistic(self):
        statistics = [x['statistics'] for x in self.list_tech()]
        return statistics

    def mark_of_mastery(self):
        mark_of_mastery = [x['mark_of_mastery'] for x in self.list_tech()]
        return mark_of_mastery


class PlayerAchievmentAdditionalMethods:

    def __init__(self, player_achievment):
        play_achiev = player_achievment['data']
        play_achiev = [x for x in play_achiev]
        play_achiev = "".join(play_achiev)
        self.__player_achievment = player_achievment['data'][play_achiev]

    def all_info(self):
        return self.__player_achievment

    def achievements(self):
        return self.all_info()['achievements']

    def frags(self):
        return self.all_info()['frags']

    def max_series(self):
        return self.all_info()['max_series']


class AchievmentAdditionalMethods:

    def __init__(self, achievment_list, account_id):
        self.__achievment_list = achievment_list['data'][str(account_id)]
        self.__account_id = account_id

    def __del__(self):
        del self.__achievment_list
        del self.__account_id

    def max_series(self):
        """"""
        return self.__achievment_list['max_series']

    def frags(self):
        return self.__achievment_list['frags']

    def achievements(self):
        return self.__achievment_list['achievements']
