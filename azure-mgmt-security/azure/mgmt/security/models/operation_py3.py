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


class Operation(Model):
    """Possible operation in the REST API of Microsoft.Security.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Name of the operation
    :vartype name: str
    :ivar origin: Where the operation is originated
    :vartype origin: str
    :param display:
    :type display: ~azure.mgmt.security.models.OperationDisplay
    """

    _validation = {
        'name': {'readonly': True},
        'origin': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(self, *, display=None, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.origin = None
        self.display = display
