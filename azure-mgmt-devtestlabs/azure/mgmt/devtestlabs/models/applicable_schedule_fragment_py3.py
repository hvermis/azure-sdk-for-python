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

from .update_resource_py3 import UpdateResource


class ApplicableScheduleFragment(UpdateResource):
    """Schedules applicable to a virtual machine. The schedules may have been
    defined on a VM or on lab level.

    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    :param lab_vms_shutdown: The auto-shutdown schedule, if one has been set
     at the lab or lab resource level.
    :type lab_vms_shutdown: ~azure.mgmt.devtestlabs.models.ScheduleFragment
    :param lab_vms_startup: The auto-startup schedule, if one has been set at
     the lab or lab resource level.
    :type lab_vms_startup: ~azure.mgmt.devtestlabs.models.ScheduleFragment
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'lab_vms_shutdown': {'key': 'properties.labVmsShutdown', 'type': 'ScheduleFragment'},
        'lab_vms_startup': {'key': 'properties.labVmsStartup', 'type': 'ScheduleFragment'},
    }

    def __init__(self, *, tags=None, lab_vms_shutdown=None, lab_vms_startup=None, **kwargs) -> None:
        super(ApplicableScheduleFragment, self).__init__(tags=tags, **kwargs)
        self.lab_vms_shutdown = lab_vms_shutdown
        self.lab_vms_startup = lab_vms_startup
