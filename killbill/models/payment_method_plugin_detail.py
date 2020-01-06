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

    OpenAPI spec version: 0.21.8-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class PaymentMethodPluginDetail(object):
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
        'external_payment_method_id': 'Str',
        'is_default_payment_method': 'Bool',
        'properties': 'List[PluginProperty]'
    }

    attribute_map = {
        'external_payment_method_id': 'externalPaymentMethodId',
        'is_default_payment_method': 'isDefaultPaymentMethod',
        'properties': 'properties'
    }

    def __init__(self, external_payment_method_id=None, is_default_payment_method=None, properties=None):  # noqa: E501
        """PaymentMethodPluginDetail - a model defined in Swagger"""  # noqa: E501

        self._external_payment_method_id = None
        self._is_default_payment_method = None
        self._properties = None
        self.discriminator = None

        if external_payment_method_id is not None:
            self.external_payment_method_id = external_payment_method_id
        if is_default_payment_method is not None:
            self.is_default_payment_method = is_default_payment_method
        if properties is not None:
            self.properties = properties

    @property
    def external_payment_method_id(self):
        """Gets the external_payment_method_id of this PaymentMethodPluginDetail.  # noqa: E501


        :return: The external_payment_method_id of this PaymentMethodPluginDetail.  # noqa: E501
        :rtype: Str
        """
        return self._external_payment_method_id

    @external_payment_method_id.setter
    def external_payment_method_id(self, external_payment_method_id):
        """Sets the external_payment_method_id of this PaymentMethodPluginDetail.


        :param external_payment_method_id: The external_payment_method_id of this PaymentMethodPluginDetail.  # noqa: E501
        :type: Str
        """


        self._external_payment_method_id = external_payment_method_id

    @property
    def is_default_payment_method(self):
        """Gets the is_default_payment_method of this PaymentMethodPluginDetail.  # noqa: E501


        :return: The is_default_payment_method of this PaymentMethodPluginDetail.  # noqa: E501
        :rtype: Bool
        """
        return self._is_default_payment_method

    @is_default_payment_method.setter
    def is_default_payment_method(self, is_default_payment_method):
        """Sets the is_default_payment_method of this PaymentMethodPluginDetail.


        :param is_default_payment_method: The is_default_payment_method of this PaymentMethodPluginDetail.  # noqa: E501
        :type: Bool
        """


        self._is_default_payment_method = is_default_payment_method

    @property
    def properties(self):
        """Gets the properties of this PaymentMethodPluginDetail.  # noqa: E501


        :return: The properties of this PaymentMethodPluginDetail.  # noqa: E501
        :rtype: List[PluginProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this PaymentMethodPluginDetail.


        :param properties: The properties of this PaymentMethodPluginDetail.  # noqa: E501
        :type: List[PluginProperty]
        """


        self._properties = properties

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
        if not isinstance(other, PaymentMethodPluginDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
