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


class LabDetails(Model):
    """This represents the details about a lab that the User is in, and its state.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: Name of the lab
    :type name: str
    :param provisioning_state: The provisioning state of the lab.
    :type provisioning_state: str
    :param id: The Id of the lab.
    :type id: str
    :ivar usage_quota: The maximum duration a user can use a VM in this lab.
    :vartype usage_quota: timedelta
    """

    _validation = {
        'usage_quota': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'usage_quota': {'key': 'usageQuota', 'type': 'duration'},
    }

    def __init__(self, **kwargs):
        super(LabDetails, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.id = kwargs.get('id', None)
        self.usage_quota = None
