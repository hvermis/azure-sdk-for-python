# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SmsChannelProperties(Model):
    """The parameters to provide for the Sms channel.

    All required parameters must be populated in order to send to Azure.

    :param phone: Required. The Sms phone
    :type phone: str
    :param account_sid: Required. The Sms account SID. Value only returned
     through POST to the action Channel List API, otherwise empty.
    :type account_sid: str
    :param auth_token: Required. The Sms auth token. Value only returned
     through POST to the action Channel List API, otherwise empty.
    :type auth_token: str
    :param is_validated: Whether this channel is validated for the bot
    :type is_validated: bool
    :param is_enabled: Required. Whether this channel is enabled for the bot
    :type is_enabled: bool
    """

    _validation = {
        'phone': {'required': True},
        'account_sid': {'required': True},
        'auth_token': {'required': True},
        'is_enabled': {'required': True},
    }

    _attribute_map = {
        'phone': {'key': 'phone', 'type': 'str'},
        'account_sid': {'key': 'accountSID', 'type': 'str'},
        'auth_token': {'key': 'authToken', 'type': 'str'},
        'is_validated': {'key': 'isValidated', 'type': 'bool'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(SmsChannelProperties, self).__init__(**kwargs)
        self.phone = kwargs.get('phone', None)
        self.account_sid = kwargs.get('account_sid', None)
        self.auth_token = kwargs.get('auth_token', None)
        self.is_validated = kwargs.get('is_validated', None)
        self.is_enabled = kwargs.get('is_enabled', None)
