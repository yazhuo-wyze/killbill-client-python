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


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from killbill.api_client import ApiClient


class NodesInfoApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_nodes_info(self, **kwargs):  # noqa: E501
        """Retrieve all the nodes infos  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_nodes_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: List[PluginInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_nodes_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_nodes_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_nodes_info_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve all the nodes infos  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_nodes_info_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: List[PluginInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_nodes_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/nodesInfo', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='List[PluginInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trigger_node_command(self, body=None, created_by=None, **kwargs):  # noqa: E501
        """Trigger a node command  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.trigger_node_command(body, created_by, async=True)
        >>> result = thread.get()

        :param async bool
        :param NodeCommand body: (required)
        :param Str created_by: (required)
        :param Bool local_node_only:
        :param Str reason:
        :param Str comment:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.trigger_node_command_with_http_info(body, created_by, **kwargs)  # noqa: E501
        else:
            (data) = self.trigger_node_command_with_http_info(body, created_by, **kwargs)  # noqa: E501
            return data

    def trigger_node_command_with_http_info(self, body=None, created_by=None, **kwargs):  # noqa: E501
        """Trigger a node command  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.trigger_node_command_with_http_info(body, created_by, async=True)
        >>> result = thread.get()

        :param async bool
        :param NodeCommand body: (required)
        :param Str created_by: (required)
        :param Bool local_node_only:
        :param Str reason:
        :param Str comment:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'created_by', 'local_node_only', 'reason', 'comment']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trigger_node_command" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `trigger_node_command`")  # noqa: E501
        # verify the required parameter 'created_by' is set
        if ('created_by' not in params or
                params['created_by'] is None):
            raise ValueError("Missing the required parameter `created_by` when calling `trigger_node_command`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'local_node_only' in params:
            query_params.append(('localNodeOnly', params['local_node_only']))  # noqa: E501

        header_params = {}
        if 'created_by' in params:
            header_params['X-Killbill-CreatedBy'] = params['created_by']  # noqa: E501
        if 'reason' in params:
            header_params['X-Killbill-Reason'] = params['reason']  # noqa: E501
        if 'comment' in params:
            header_params['X-Killbill-Comment'] = params['comment']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/nodesInfo', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
