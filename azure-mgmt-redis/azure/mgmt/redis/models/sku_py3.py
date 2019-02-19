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


class Sku(Model):
    """SKU parameters supplied to the create Redis operation.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The type of Redis cache to deploy. Valid values:
     (Basic, Standard, Premium). Possible values include: 'Basic', 'Standard',
     'Premium'
    :type name: str or ~azure.mgmt.redis.models.SkuName
    :param family: Required. The SKU family to use. Valid values: (C, P). (C =
     Basic/Standard, P = Premium). Possible values include: 'C', 'P'
    :type family: str or ~azure.mgmt.redis.models.SkuFamily
    :param capacity: Required. The size of the Redis cache to deploy. Valid
     values: for C (Basic/Standard) family (0, 1, 2, 3, 4, 5, 6), for P
     (Premium) family (1, 2, 3, 4).
    :type capacity: int
    """

    _validation = {
        'name': {'required': True},
        'family': {'required': True},
        'capacity': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'family': {'key': 'family', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(self, *, name, family, capacity: int, **kwargs) -> None:
        super(Sku, self).__init__(**kwargs)
        self.name = name
        self.family = family
        self.capacity = capacity
