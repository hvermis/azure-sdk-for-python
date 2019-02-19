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

from .resource import Resource


class AvailabilitySet(Resource):
    """Specifies information about the availability set that the virtual machine
    should be assigned to. Virtual machines specified in the same availability
    set are allocated to different nodes to maximize availability. For more
    information about availability sets, see [Manage the availability of
    virtual
    machines](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-manage-availability?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json).
    <br><br> For more information on Azure planned maintenance, see [Planned
    maintenance for virtual machines in
    Azure](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-planned-maintenance?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json)
    <br><br> Currently, a VM can only be added to availability set at creation
    time. An existing VM cannot be added to an availability set.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param platform_update_domain_count: Update Domain count.
    :type platform_update_domain_count: int
    :param platform_fault_domain_count: Fault Domain count.
    :type platform_fault_domain_count: int
    :param virtual_machines: A list of references to all virtual machines in
     the availability set.
    :type virtual_machines:
     list[~azure.mgmt.compute.v2017_03_30.models.SubResource]
    :ivar statuses: The resource status information.
    :vartype statuses:
     list[~azure.mgmt.compute.v2017_03_30.models.InstanceViewStatus]
    :param sku: Sku of the availability set
    :type sku: ~azure.mgmt.compute.v2017_03_30.models.Sku
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'statuses': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'platform_update_domain_count': {'key': 'properties.platformUpdateDomainCount', 'type': 'int'},
        'platform_fault_domain_count': {'key': 'properties.platformFaultDomainCount', 'type': 'int'},
        'virtual_machines': {'key': 'properties.virtualMachines', 'type': '[SubResource]'},
        'statuses': {'key': 'properties.statuses', 'type': '[InstanceViewStatus]'},
        'sku': {'key': 'sku', 'type': 'Sku'},
    }

    def __init__(self, **kwargs):
        super(AvailabilitySet, self).__init__(**kwargs)
        self.platform_update_domain_count = kwargs.get('platform_update_domain_count', None)
        self.platform_fault_domain_count = kwargs.get('platform_fault_domain_count', None)
        self.virtual_machines = kwargs.get('virtual_machines', None)
        self.statuses = None
        self.sku = kwargs.get('sku', None)
