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

from .resource_py3 import Resource


class Formula(Resource):
    """A formula for creating a VM, specifying an image base and other parameters.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The identifier of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    :param description: The description of the formula.
    :type description: str
    :param author: The author of the formula.
    :type author: str
    :param os_type: The OS type of the formula.
    :type os_type: str
    :ivar creation_date: The creation date of the formula.
    :vartype creation_date: datetime
    :param formula_content: The content of the formula.
    :type formula_content:
     ~azure.mgmt.devtestlabs.models.LabVirtualMachineCreationParameter
    :param vm: Information about a VM from which a formula is to be created.
    :type vm: ~azure.mgmt.devtestlabs.models.FormulaPropertiesFromVm
    :ivar provisioning_state: The provisioning status of the resource.
    :vartype provisioning_state: str
    :ivar unique_identifier: The unique immutable identifier of a resource
     (Guid).
    :vartype unique_identifier: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'creation_date': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'unique_identifier': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'author': {'key': 'properties.author', 'type': 'str'},
        'os_type': {'key': 'properties.osType', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
        'formula_content': {'key': 'properties.formulaContent', 'type': 'LabVirtualMachineCreationParameter'},
        'vm': {'key': 'properties.vm', 'type': 'FormulaPropertiesFromVm'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'unique_identifier': {'key': 'properties.uniqueIdentifier', 'type': 'str'},
    }

    def __init__(self, *, location: str=None, tags=None, description: str=None, author: str=None, os_type: str=None, formula_content=None, vm=None, **kwargs) -> None:
        super(Formula, self).__init__(location=location, tags=tags, **kwargs)
        self.description = description
        self.author = author
        self.os_type = os_type
        self.creation_date = None
        self.formula_content = formula_content
        self.vm = vm
        self.provisioning_state = None
        self.unique_identifier = None
