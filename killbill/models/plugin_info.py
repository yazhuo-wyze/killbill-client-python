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



class PluginInfo(object):
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
        'bundle_symbolic_name': 'Str',
        'plugin_key': 'Str',
        'plugin_name': 'Str',
        'version': 'Str',
        'state': 'Str',
        'is_selected_for_start': 'Bool',
        'services': 'List[PluginServiceInfo]'
    }

    attribute_map = {
        'bundle_symbolic_name': 'bundleSymbolicName',
        'plugin_key': 'pluginKey',
        'plugin_name': 'pluginName',
        'version': 'version',
        'state': 'state',
        'is_selected_for_start': 'isSelectedForStart',
        'services': 'services'
    }

    def __init__(self, bundle_symbolic_name=None, plugin_key=None, plugin_name=None, version=None, state=None, is_selected_for_start=None, services=None):  # noqa: E501
        """PluginInfo - a model defined in Swagger"""  # noqa: E501

        self._bundle_symbolic_name = None
        self._plugin_key = None
        self._plugin_name = None
        self._version = None
        self._state = None
        self._is_selected_for_start = None
        self._services = None
        self.discriminator = None

        if bundle_symbolic_name is not None:
            self.bundle_symbolic_name = bundle_symbolic_name
        if plugin_key is not None:
            self.plugin_key = plugin_key
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if version is not None:
            self.version = version
        if state is not None:
            self.state = state
        if is_selected_for_start is not None:
            self.is_selected_for_start = is_selected_for_start
        if services is not None:
            self.services = services

    @property
    def bundle_symbolic_name(self):
        """Gets the bundle_symbolic_name of this PluginInfo.  # noqa: E501


        :return: The bundle_symbolic_name of this PluginInfo.  # noqa: E501
        :rtype: Str
        """
        return self._bundle_symbolic_name

    @bundle_symbolic_name.setter
    def bundle_symbolic_name(self, bundle_symbolic_name):
        """Sets the bundle_symbolic_name of this PluginInfo.


        :param bundle_symbolic_name: The bundle_symbolic_name of this PluginInfo.  # noqa: E501
        :type: Str
        """


        self._bundle_symbolic_name = bundle_symbolic_name

    @property
    def plugin_key(self):
        """Gets the plugin_key of this PluginInfo.  # noqa: E501


        :return: The plugin_key of this PluginInfo.  # noqa: E501
        :rtype: Str
        """
        return self._plugin_key

    @plugin_key.setter
    def plugin_key(self, plugin_key):
        """Sets the plugin_key of this PluginInfo.


        :param plugin_key: The plugin_key of this PluginInfo.  # noqa: E501
        :type: Str
        """


        self._plugin_key = plugin_key

    @property
    def plugin_name(self):
        """Gets the plugin_name of this PluginInfo.  # noqa: E501


        :return: The plugin_name of this PluginInfo.  # noqa: E501
        :rtype: Str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this PluginInfo.


        :param plugin_name: The plugin_name of this PluginInfo.  # noqa: E501
        :type: Str
        """


        self._plugin_name = plugin_name

    @property
    def version(self):
        """Gets the version of this PluginInfo.  # noqa: E501


        :return: The version of this PluginInfo.  # noqa: E501
        :rtype: Str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PluginInfo.


        :param version: The version of this PluginInfo.  # noqa: E501
        :type: Str
        """


        self._version = version

    @property
    def state(self):
        """Gets the state of this PluginInfo.  # noqa: E501


        :return: The state of this PluginInfo.  # noqa: E501
        :rtype: Str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PluginInfo.


        :param state: The state of this PluginInfo.  # noqa: E501
        :type: Str
        """


        self._state = state

    @property
    def is_selected_for_start(self):
        """Gets the is_selected_for_start of this PluginInfo.  # noqa: E501


        :return: The is_selected_for_start of this PluginInfo.  # noqa: E501
        :rtype: Bool
        """
        return self._is_selected_for_start

    @is_selected_for_start.setter
    def is_selected_for_start(self, is_selected_for_start):
        """Sets the is_selected_for_start of this PluginInfo.


        :param is_selected_for_start: The is_selected_for_start of this PluginInfo.  # noqa: E501
        :type: Bool
        """


        self._is_selected_for_start = is_selected_for_start

    @property
    def services(self):
        """Gets the services of this PluginInfo.  # noqa: E501


        :return: The services of this PluginInfo.  # noqa: E501
        :rtype: List[PluginServiceInfo]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this PluginInfo.


        :param services: The services of this PluginInfo.  # noqa: E501
        :type: List[PluginServiceInfo]
        """


        self._services = services

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
        if not isinstance(other, PluginInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
