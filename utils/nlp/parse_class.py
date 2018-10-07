#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from natasha import (
    NamesExtractor,
    AddressExtractor,
    DatesExtractor,
    MoneyExtractor
)


class NLP(object):
    def __init__(self, text):
        self._text = text

    def parse_date(self):
        """ Парсер даты

        :return:
        """
        extractor = DatesExtractor()
        matches = extractor(self._text)
        return [{
            'day': _.fact.as_json.get('day'),
            'month': _.fact.as_json.get('month'),
            'year': _.fact.as_json.get('year')
        } for _ in matches]

    def parse_fio(self):
        """ Парсер фио

        :return:
        """
        extractor = NamesExtractor()
        matches = extractor(self._text)
        return [{
            'first': _.fact.as_json.get('first'),
            'middle': _.fact.as_json.get('middle'),
            'last': _.fact.as_json.get('last')
        } for _ in matches]

    def parse_cash(self):
        """ Парсер Денежной суммы
        :return:
        """
        extractor = MoneyExtractor()
        matches = extractor(self._text)
        return [{
            'integer': _.fact.as_json.get('integer'),
            'coins': _.fact.as_json.get('coins'),
            'fraction': _.fact.as_json.get('fraction'),
            'multiplier': _.fact.as_json.get('multiplier'),
            'currency': _.fact.as_json.get('currency'),
        } for _ in matches]

    def parse_address(self):
        """ Парсер адреса

        :return:
        """
        extractor = AddressExtractor()
        matches = extractor(self._text)
        address = []
        for _ in matches:
            if _.fact.as_json.get('parts'):
                row = []
                for x in _.fact.as_json.get('parts'):
                    if x.get('name'):
                        row.append(x.get('name'))
                address.append(', '.join(row))
        return address

    def result(self):
        """ Структурированный результат

        :return:
        """
        return {
            'original_text': self._text,
            'names': self.parse_fio(),
            'dates': self.parse_date(),
            'addresses': self.parse_address(),
            'cashes': self.parse_cash()
        }


if __name__ == '__main__':
    res = NLP('''Офис и шоу-рум в Красноярске работает с 14.00 до 17.00 по адресу г.Красноряск ул.Парижской Коммуны,14 оф.14.
Юридический адрес: 129344, г. Москва, ул. Искры, дом 31, корпус 1, пом. II комната 7А.
г. Пятигорск, ул. Февральская, д. 54
Дмитровское шоссе, д.157, стр.9
603070, г. Нижний Новгород, ул. Акимова 22 «А»
Адрес: | г. Санкт-Петербург, ул. Шамшева, д. 8 (ДК им.В.А.Шелгунова)
Факт. и юр. адрес: 426052, г. Ижевск, ул. Лесозаводская 23/110
Адрес: Россия г. Санкт-Петербург ул. Чехова 14 оф23
129085, Москва, ул.Годовикова д.9  (Бизнес-центр "Калибр").
Почтовый адрес: Россия, 693010 г. Южно-Сахалинск, Комсомольская, 154, оф. 600
ул. Менжинского, 4г ст. А
344010, РФ, г. Ростов-на-Дону, ул. Красноармейская д.208, офис 302.
Юридический адрес 308000, Белгородская обл., г.Белгород, ул.Н.Островского, д.5
Юридический, физический и фактический адрес: 350072, г. Краснодар, ул. Московская, 5.
10 июня 1991 года 1000 рублей 50 копеек 1 доллар Российская Федерация, Тверская область, Кимрский район, пгт.  Белый Городок, улица Заводская дом 11
Свердловская обл., г. Екатеринбург, Барвинка 21''')
    b = res.result()
    a=10

