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


class StorageAccountUpdateParameters(Model):
    """The storage account update parameters.

    :param active_key_name: The current active storage account key name.
    :type active_key_name: str
    :param auto_regenerate_key: whether keyvault should manage the storage
     account for the user.
    :type auto_regenerate_key: bool
    :param regeneration_period: The key regeneration time duration specified
     in ISO-8601 format.
    :type regeneration_period: str
    :param storage_account_attributes: The attributes of the storage account.
    :type storage_account_attributes:
     ~azure.keyvault.v2016_10_01.models.StorageAccountAttributes
    :param tags: Application specific metadata in the form of key-value pairs.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'active_key_name': {'key': 'activeKeyName', 'type': 'str'},
        'auto_regenerate_key': {'key': 'autoRegenerateKey', 'type': 'bool'},
        'regeneration_period': {'key': 'regenerationPeriod', 'type': 'str'},
        'storage_account_attributes': {'key': 'attributes', 'type': 'StorageAccountAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, active_key_name: str=None, auto_regenerate_key: bool=None, regeneration_period: str=None, storage_account_attributes=None, tags=None, **kwargs) -> None:
        super(StorageAccountUpdateParameters, self).__init__(**kwargs)
        self.active_key_name = active_key_name
        self.auto_regenerate_key = auto_regenerate_key
        self.regeneration_period = regeneration_period
        self.storage_account_attributes = storage_account_attributes
        self.tags = tags
