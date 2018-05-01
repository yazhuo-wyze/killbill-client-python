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


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from killbill.api_client import ApiClient


class UsageApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_usage(self, subscription_id=None, api_key=None, api_secret=None, **kwargs):  # noqa: E501
        """Retrieve usage for a subscription  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_usage(subscription_id, api_key, api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param Str subscription_id: (required)
        :param Str api_key: (required)
        :param Str api_secret: (required)
        :param Date start_date:
        :param Date end_date:
        :return: RolledUpUsage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_all_usage_with_http_info(subscription_id, api_key, api_secret, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_usage_with_http_info(subscription_id, api_key, api_secret, **kwargs)  # noqa: E501
            return data

    def get_all_usage_with_http_info(self, subscription_id=None, api_key=None, api_secret=None, **kwargs):  # noqa: E501
        """Retrieve usage for a subscription  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_usage_with_http_info(subscription_id, api_key, api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param Str subscription_id: (required)
        :param Str api_key: (required)
        :param Str api_secret: (required)
        :param Date start_date:
        :param Date end_date:
        :return: RolledUpUsage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id', 'api_key', 'api_secret', 'start_date', 'end_date']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_usage" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params or
                params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `get_all_usage`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_all_usage`")  # noqa: E501
        # verify the required parameter 'api_secret' is set
        if ('api_secret' not in params or
                params['api_secret'] is None):
            raise ValueError("Missing the required parameter `api_secret` when calling `get_all_usage`")  # noqa: E501

        if 'subscription_id' in params and not re.search('\\w+-\\w+-\\w+-\\w+-\\w+', params['subscription_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `subscription_id` when calling `get_all_usage`, must conform to the pattern `/\\w+-\\w+-\\w+-\\w+-\\w+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'subscription_id' in params:
            path_params['subscriptionId'] = params['subscription_id']  # noqa: E501

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501

        header_params = {}
        if 'api_key' in params:
            header_params['X-Killbill-ApiKey'] = params['api_key']  # noqa: E501
        if 'api_secret' in params:
            header_params['X-Killbill-ApiSecret'] = params['api_secret']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/usages/{subscriptionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RolledUpUsage',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_usage(self, subscription_id=None, unit_type=None, api_key=None, api_secret=None, **kwargs):  # noqa: E501
        """Retrieve usage for a subscription and unit type  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_usage(subscription_id, unit_type, api_key, api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param Str subscription_id: (required)
        :param Str unit_type: (required)
        :param Str api_key: (required)
        :param Str api_secret: (required)
        :param Date start_date:
        :param Date end_date:
        :return: RolledUpUsage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_usage_with_http_info(subscription_id, unit_type, api_key, api_secret, **kwargs)  # noqa: E501
        else:
            (data) = self.get_usage_with_http_info(subscription_id, unit_type, api_key, api_secret, **kwargs)  # noqa: E501
            return data

    def get_usage_with_http_info(self, subscription_id=None, unit_type=None, api_key=None, api_secret=None, **kwargs):  # noqa: E501
        """Retrieve usage for a subscription and unit type  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_usage_with_http_info(subscription_id, unit_type, api_key, api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param Str subscription_id: (required)
        :param Str unit_type: (required)
        :param Str api_key: (required)
        :param Str api_secret: (required)
        :param Date start_date:
        :param Date end_date:
        :return: RolledUpUsage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id', 'unit_type', 'api_key', 'api_secret', 'start_date', 'end_date']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_usage" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params or
                params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `get_usage`")  # noqa: E501
        # verify the required parameter 'unit_type' is set
        if ('unit_type' not in params or
                params['unit_type'] is None):
            raise ValueError("Missing the required parameter `unit_type` when calling `get_usage`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_usage`")  # noqa: E501
        # verify the required parameter 'api_secret' is set
        if ('api_secret' not in params or
                params['api_secret'] is None):
            raise ValueError("Missing the required parameter `api_secret` when calling `get_usage`")  # noqa: E501

        if 'subscription_id' in params and not re.search('\\w+-\\w+-\\w+-\\w+-\\w+', params['subscription_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `subscription_id` when calling `get_usage`, must conform to the pattern `/\\w+-\\w+-\\w+-\\w+-\\w+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'subscription_id' in params:
            path_params['subscriptionId'] = params['subscription_id']  # noqa: E501
        if 'unit_type' in params:
            path_params['unitType'] = params['unit_type']  # noqa: E501

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501

        header_params = {}
        if 'api_key' in params:
            header_params['X-Killbill-ApiKey'] = params['api_key']  # noqa: E501
        if 'api_secret' in params:
            header_params['X-Killbill-ApiSecret'] = params['api_secret']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/usages/{subscriptionId}/{unitType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RolledUpUsage',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def record_usage(self, body=None, created_by=None, api_key=None, api_secret=None, **kwargs):  # noqa: E501
        """Record usage for a subscription  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.record_usage(body, created_by, api_key, api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param SubscriptionUsageRecord body: (required)
        :param Str created_by: (required)
        :param Str api_key: (required)
        :param Str api_secret: (required)
        :param Str reason:
        :param Str comment:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.record_usage_with_http_info(body, created_by, api_key, api_secret, **kwargs)  # noqa: E501
        else:
            (data) = self.record_usage_with_http_info(body, created_by, api_key, api_secret, **kwargs)  # noqa: E501
            return data

    def record_usage_with_http_info(self, body=None, created_by=None, api_key=None, api_secret=None, **kwargs):  # noqa: E501
        """Record usage for a subscription  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.record_usage_with_http_info(body, created_by, api_key, api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param SubscriptionUsageRecord body: (required)
        :param Str created_by: (required)
        :param Str api_key: (required)
        :param Str api_secret: (required)
        :param Str reason:
        :param Str comment:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'created_by', 'api_key', 'api_secret', 'reason', 'comment']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method record_usage" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `record_usage`")  # noqa: E501
        # verify the required parameter 'created_by' is set
        if ('created_by' not in params or
                params['created_by'] is None):
            raise ValueError("Missing the required parameter `created_by` when calling `record_usage`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `record_usage`")  # noqa: E501
        # verify the required parameter 'api_secret' is set
        if ('api_secret' not in params or
                params['api_secret'] is None):
            raise ValueError("Missing the required parameter `api_secret` when calling `record_usage`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'created_by' in params:
            header_params['X-Killbill-CreatedBy'] = params['created_by']  # noqa: E501
        if 'reason' in params:
            header_params['X-Killbill-Reason'] = params['reason']  # noqa: E501
        if 'comment' in params:
            header_params['X-Killbill-Comment'] = params['comment']  # noqa: E501
        if 'api_key' in params:
            header_params['X-Killbill-ApiKey'] = params['api_key']  # noqa: E501
        if 'api_secret' in params:
            header_params['X-Killbill-ApiSecret'] = params['api_secret']  # noqa: E501

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
            '/1.0/kb/usages', 'POST',
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
