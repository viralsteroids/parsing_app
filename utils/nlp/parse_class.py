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
