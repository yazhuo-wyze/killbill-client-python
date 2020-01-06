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



class Entity(object):
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
        'id': 'Str',
        'created_date': 'Datetime',
        'updated_date': 'Datetime'
    }

    attribute_map = {
        'id': 'id',
        'created_date': 'createdDate',
        'updated_date': 'updatedDate'
    }

    def __init__(self, id=None, created_date=None, updated_date=None):  # noqa: E501
        """Entity - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_date = None
        self._updated_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_date is not None:
            self.created_date = created_date
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def id(self):
        """Gets the id of this Entity.  # noqa: E501


        :return: The id of this Entity.  # noqa: E501
        :rtype: Str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Entity.


        :param id: The id of this Entity.  # noqa: E501
        :type: Str
        """


        self._id = id

    @property
    def created_date(self):
        """Gets the created_date of this Entity.  # noqa: E501


        :return: The created_date of this Entity.  # noqa: E501
        :rtype: Datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this Entity.


        :param created_date: The created_date of this Entity.  # noqa: E501
        :type: Datetime
        """


        self._created_date = created_date

    @property
    def updated_date(self):
        """Gets the updated_date of this Entity.  # noqa: E501


        :return: The updated_date of this Entity.  # noqa: E501
        :rtype: Datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this Entity.


        :param updated_date: The updated_date of this Entity.  # noqa: E501
        :type: Datetime
        """


        self._updated_date = updated_date

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
        if not isinstance(other, Entity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
