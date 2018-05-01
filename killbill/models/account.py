# coding: utf-8

#
# Copyright 2014-2017 Groupon, Inc.
# Copyright 2014-2017 The Billing Project, LLC
#
# The Billing Project, LLC licenses this file to you under the Apache License, version 2.0
# (the "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 0.19.11-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class Account(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_id': 'Str',
        'name': 'Str',
        'first_name_length': 'Int',
        'external_key': 'Str',
        'email': 'Str',
        'bill_cycle_day_local': 'Int',
        'currency': 'Str',
        'parent_account_id': 'Str',
        'is_payment_delegated_to_parent': 'Bool',
        'payment_method_id': 'Str',
        'reference_time': 'Datetime',
        'time_zone': 'Str',
        'address1': 'Str',
        'address2': 'Str',
        'postal_code': 'Str',
        'company': 'Str',
        'city': 'Str',
        'state': 'Str',
        'country': 'Str',
        'locale': 'Str',
        'phone': 'Str',
        'notes': 'Str',
        'is_migrated': 'Bool',
        'is_notified_for_invoices': 'Bool',
        'account_balance': 'Float',
        'account_cba': 'Float',
        'audit_logs': 'List[AuditLog]'
    }

    attribute_map = {
        'account_id': 'accountId',
        'name': 'name',
        'first_name_length': 'firstNameLength',
        'external_key': 'externalKey',
        'email': 'email',
        'bill_cycle_day_local': 'billCycleDayLocal',
        'currency': 'currency',
        'parent_account_id': 'parentAccountId',
        'is_payment_delegated_to_parent': 'isPaymentDelegatedToParent',
        'payment_method_id': 'paymentMethodId',
        'reference_time': 'referenceTime',
        'time_zone': 'timeZone',
        'address1': 'address1',
        'address2': 'address2',
        'postal_code': 'postalCode',
        'company': 'company',
        'city': 'city',
        'state': 'state',
        'country': 'country',
        'locale': 'locale',
        'phone': 'phone',
        'notes': 'notes',
        'is_migrated': 'isMigrated',
        'is_notified_for_invoices': 'isNotifiedForInvoices',
        'account_balance': 'accountBalance',
        'account_cba': 'accountCBA',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, account_id=None, name=None, first_name_length=None, external_key=None, email=None, bill_cycle_day_local=None, currency=None, parent_account_id=None, is_payment_delegated_to_parent=False, payment_method_id=None, reference_time=None, time_zone=None, address1=None, address2=None, postal_code=None, company=None, city=None, state=None, country=None, locale=None, phone=None, notes=None, is_migrated=False, is_notified_for_invoices=False, account_balance=None, account_cba=None, audit_logs=None):  # noqa: E501
        """Account - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._name = None
        self._first_name_length = None
        self._external_key = None
        self._email = None
        self._bill_cycle_day_local = None
        self._currency = None
        self._parent_account_id = None
        self._is_payment_delegated_to_parent = None
        self._payment_method_id = None
        self._reference_time = None
        self._time_zone = None
        self._address1 = None
        self._address2 = None
        self._postal_code = None
        self._company = None
        self._city = None
        self._state = None
        self._country = None
        self._locale = None
        self._phone = None
        self._notes = None
        self._is_migrated = None
        self._is_notified_for_invoices = None
        self._account_balance = None
        self._account_cba = None
        self._audit_logs = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if name is not None:
            self.name = name
        if first_name_length is not None:
            self.first_name_length = first_name_length
        if external_key is not None:
            self.external_key = external_key
        if email is not None:
            self.email = email
        if bill_cycle_day_local is not None:
            self.bill_cycle_day_local = bill_cycle_day_local
        if currency is not None:
            self.currency = currency
        if parent_account_id is not None:
            self.parent_account_id = parent_account_id
        if is_payment_delegated_to_parent is not None:
            self.is_payment_delegated_to_parent = is_payment_delegated_to_parent
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if reference_time is not None:
            self.reference_time = reference_time
        if time_zone is not None:
            self.time_zone = time_zone
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if postal_code is not None:
            self.postal_code = postal_code
        if company is not None:
            self.company = company
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if country is not None:
            self.country = country
        if locale is not None:
            self.locale = locale
        if phone is not None:
            self.phone = phone
        if notes is not None:
            self.notes = notes
        if is_migrated is not None:
            self.is_migrated = is_migrated
        if is_notified_for_invoices is not None:
            self.is_notified_for_invoices = is_notified_for_invoices
        if account_balance is not None:
            self.account_balance = account_balance
        if account_cba is not None:
            self.account_cba = account_cba
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def account_id(self):
        """Gets the account_id of this Account.  # noqa: E501


        :return: The account_id of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Account.


        :param account_id: The account_id of this Account.  # noqa: E501
        :type: Str
        """


        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this Account.  # noqa: E501


        :return: The name of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Account.


        :param name: The name of this Account.  # noqa: E501
        :type: Str
        """


        self._name = name

    @property
    def first_name_length(self):
        """Gets the first_name_length of this Account.  # noqa: E501


        :return: The first_name_length of this Account.  # noqa: E501
        :rtype: Int
        """
        return self._first_name_length

    @first_name_length.setter
    def first_name_length(self, first_name_length):
        """Sets the first_name_length of this Account.


        :param first_name_length: The first_name_length of this Account.  # noqa: E501
        :type: Int
        """


        self._first_name_length = first_name_length

    @property
    def external_key(self):
        """Gets the external_key of this Account.  # noqa: E501


        :return: The external_key of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """Sets the external_key of this Account.


        :param external_key: The external_key of this Account.  # noqa: E501
        :type: Str
        """


        self._external_key = external_key

    @property
    def email(self):
        """Gets the email of this Account.  # noqa: E501


        :return: The email of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Account.


        :param email: The email of this Account.  # noqa: E501
        :type: Str
        """


        self._email = email

    @property
    def bill_cycle_day_local(self):
        """Gets the bill_cycle_day_local of this Account.  # noqa: E501


        :return: The bill_cycle_day_local of this Account.  # noqa: E501
        :rtype: Int
        """
        return self._bill_cycle_day_local

    @bill_cycle_day_local.setter
    def bill_cycle_day_local(self, bill_cycle_day_local):
        """Sets the bill_cycle_day_local of this Account.


        :param bill_cycle_day_local: The bill_cycle_day_local of this Account.  # noqa: E501
        :type: Int
        """


        self._bill_cycle_day_local = bill_cycle_day_local

    @property
    def currency(self):
        """Gets the currency of this Account.  # noqa: E501


        :return: The currency of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Account.


        :param currency: The currency of this Account.  # noqa: E501
        :type: Str
        """

        allowed_values = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYR", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SPL", "SRD", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWD", "BTC"]  # noqa: E501
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"  # noqa: E501
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def parent_account_id(self):
        """Gets the parent_account_id of this Account.  # noqa: E501


        :return: The parent_account_id of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._parent_account_id

    @parent_account_id.setter
    def parent_account_id(self, parent_account_id):
        """Sets the parent_account_id of this Account.


        :param parent_account_id: The parent_account_id of this Account.  # noqa: E501
        :type: Str
        """


        self._parent_account_id = parent_account_id

    @property
    def is_payment_delegated_to_parent(self):
        """Gets the is_payment_delegated_to_parent of this Account.  # noqa: E501


        :return: The is_payment_delegated_to_parent of this Account.  # noqa: E501
        :rtype: Bool
        """
        return self._is_payment_delegated_to_parent

    @is_payment_delegated_to_parent.setter
    def is_payment_delegated_to_parent(self, is_payment_delegated_to_parent):
        """Sets the is_payment_delegated_to_parent of this Account.


        :param is_payment_delegated_to_parent: The is_payment_delegated_to_parent of this Account.  # noqa: E501
        :type: Bool
        """


        self._is_payment_delegated_to_parent = is_payment_delegated_to_parent

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this Account.  # noqa: E501


        :return: The payment_method_id of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this Account.


        :param payment_method_id: The payment_method_id of this Account.  # noqa: E501
        :type: Str
        """


        self._payment_method_id = payment_method_id

    @property
    def reference_time(self):
        """Gets the reference_time of this Account.  # noqa: E501


        :return: The reference_time of this Account.  # noqa: E501
        :rtype: Datetime
        """
        return self._reference_time

    @reference_time.setter
    def reference_time(self, reference_time):
        """Sets the reference_time of this Account.


        :param reference_time: The reference_time of this Account.  # noqa: E501
        :type: Datetime
        """


        self._reference_time = reference_time

    @property
    def time_zone(self):
        """Gets the time_zone of this Account.  # noqa: E501


        :return: The time_zone of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this Account.


        :param time_zone: The time_zone of this Account.  # noqa: E501
        :type: Str
        """


        self._time_zone = time_zone

    @property
    def address1(self):
        """Gets the address1 of this Account.  # noqa: E501


        :return: The address1 of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this Account.


        :param address1: The address1 of this Account.  # noqa: E501
        :type: Str
        """


        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this Account.  # noqa: E501


        :return: The address2 of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Account.


        :param address2: The address2 of this Account.  # noqa: E501
        :type: Str
        """


        self._address2 = address2

    @property
    def postal_code(self):
        """Gets the postal_code of this Account.  # noqa: E501


        :return: The postal_code of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Account.


        :param postal_code: The postal_code of this Account.  # noqa: E501
        :type: Str
        """


        self._postal_code = postal_code

    @property
    def company(self):
        """Gets the company of this Account.  # noqa: E501


        :return: The company of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this Account.


        :param company: The company of this Account.  # noqa: E501
        :type: Str
        """


        self._company = company

    @property
    def city(self):
        """Gets the city of this Account.  # noqa: E501


        :return: The city of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Account.


        :param city: The city of this Account.  # noqa: E501
        :type: Str
        """


        self._city = city

    @property
    def state(self):
        """Gets the state of this Account.  # noqa: E501


        :return: The state of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Account.


        :param state: The state of this Account.  # noqa: E501
        :type: Str
        """


        self._state = state

    @property
    def country(self):
        """Gets the country of this Account.  # noqa: E501


        :return: The country of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Account.


        :param country: The country of this Account.  # noqa: E501
        :type: Str
        """


        self._country = country

    @property
    def locale(self):
        """Gets the locale of this Account.  # noqa: E501


        :return: The locale of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this Account.


        :param locale: The locale of this Account.  # noqa: E501
        :type: Str
        """


        self._locale = locale

    @property
    def phone(self):
        """Gets the phone of this Account.  # noqa: E501


        :return: The phone of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Account.


        :param phone: The phone of this Account.  # noqa: E501
        :type: Str
        """


        self._phone = phone

    @property
    def notes(self):
        """Gets the notes of this Account.  # noqa: E501


        :return: The notes of this Account.  # noqa: E501
        :rtype: Str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Account.


        :param notes: The notes of this Account.  # noqa: E501
        :type: Str
        """


        self._notes = notes

    @property
    def is_migrated(self):
        """Gets the is_migrated of this Account.  # noqa: E501


        :return: The is_migrated of this Account.  # noqa: E501
        :rtype: Bool
        """
        return self._is_migrated

    @is_migrated.setter
    def is_migrated(self, is_migrated):
        """Sets the is_migrated of this Account.


        :param is_migrated: The is_migrated of this Account.  # noqa: E501
        :type: Bool
        """


        self._is_migrated = is_migrated

    @property
    def is_notified_for_invoices(self):
        """Gets the is_notified_for_invoices of this Account.  # noqa: E501


        :return: The is_notified_for_invoices of this Account.  # noqa: E501
        :rtype: Bool
        """
        return self._is_notified_for_invoices

    @is_notified_for_invoices.setter
    def is_notified_for_invoices(self, is_notified_for_invoices):
        """Sets the is_notified_for_invoices of this Account.


        :param is_notified_for_invoices: The is_notified_for_invoices of this Account.  # noqa: E501
        :type: Bool
        """


        self._is_notified_for_invoices = is_notified_for_invoices

    @property
    def account_balance(self):
        """Gets the account_balance of this Account.  # noqa: E501


        :return: The account_balance of this Account.  # noqa: E501
        :rtype: Float
        """
        return self._account_balance

    @account_balance.setter
    def account_balance(self, account_balance):
        """Sets the account_balance of this Account.


        :param account_balance: The account_balance of this Account.  # noqa: E501
        :type: Float
        """


        self._account_balance = account_balance

    @property
    def account_cba(self):
        """Gets the account_cba of this Account.  # noqa: E501


        :return: The account_cba of this Account.  # noqa: E501
        :rtype: Float
        """
        return self._account_cba

    @account_cba.setter
    def account_cba(self, account_cba):
        """Sets the account_cba of this Account.


        :param account_cba: The account_cba of this Account.  # noqa: E501
        :type: Float
        """


        self._account_cba = account_cba

    @property
    def audit_logs(self):
        """Gets the audit_logs of this Account.  # noqa: E501


        :return: The audit_logs of this Account.  # noqa: E501
        :rtype: List[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this Account.


        :param audit_logs: The audit_logs of this Account.  # noqa: E501
        :type: List[AuditLog]
        """


        self._audit_logs = audit_logs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
