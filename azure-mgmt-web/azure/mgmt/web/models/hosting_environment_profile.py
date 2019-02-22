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


class HostingEnvironmentProfile(Model):
    """Specification for an App Service Environment to use for this resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID of the App Service Environment.
    :type id: str
    :ivar name: Name of the App Service Environment.
    :vartype name: str
    :ivar type: Resource type of the App Service Environment.
    :vartype type: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(HostingEnvironmentProfile, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = None
        self.type = None
