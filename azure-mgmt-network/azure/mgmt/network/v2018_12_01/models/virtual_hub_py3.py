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


class VirtualHub(Resource):
    """VirtualHub Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param virtual_wan: The VirtualWAN to which the VirtualHub belongs
    :type virtual_wan: ~azure.mgmt.network.v2018_12_01.models.SubResource
    :param vpn_gateway: The VpnGateway associated with this VirtualHub
    :type vpn_gateway: ~azure.mgmt.network.v2018_12_01.models.SubResource
    :param p2_svpn_gateway: The P2SVpnGateway associated with this VirtualHub
    :type p2_svpn_gateway: ~azure.mgmt.network.v2018_12_01.models.SubResource
    :param express_route_gateway: The expressRouteGateway associated with this
     VirtualHub
    :type express_route_gateway:
     ~azure.mgmt.network.v2018_12_01.models.SubResource
    :param virtual_network_connections: list of all vnet connections with this
     VirtualHub.
    :type virtual_network_connections:
     list[~azure.mgmt.network.v2018_12_01.models.HubVirtualNetworkConnection]
    :param address_prefix: Address-prefix for this VirtualHub.
    :type address_prefix: str
    :param route_table: The routeTable associated with this virtual hub.
    :type route_table:
     ~azure.mgmt.network.v2018_12_01.models.VirtualHubRouteTable
    :param provisioning_state: The provisioning state of the resource.
     Possible values include: 'Succeeded', 'Updating', 'Deleting', 'Failed'
    :type provisioning_state: str or
     ~azure.mgmt.network.v2018_12_01.models.ProvisioningState
    :ivar etag: Gets a unique read-only string that changes whenever the
     resource is updated.
    :vartype etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'virtual_wan': {'key': 'properties.virtualWan', 'type': 'SubResource'},
        'vpn_gateway': {'key': 'properties.vpnGateway', 'type': 'SubResource'},
        'p2_svpn_gateway': {'key': 'properties.p2SVpnGateway', 'type': 'SubResource'},
        'express_route_gateway': {'key': 'properties.expressRouteGateway', 'type': 'SubResource'},
        'virtual_network_connections': {'key': 'properties.virtualNetworkConnections', 'type': '[HubVirtualNetworkConnection]'},
        'address_prefix': {'key': 'properties.addressPrefix', 'type': 'str'},
        'route_table': {'key': 'properties.routeTable', 'type': 'VirtualHubRouteTable'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, location: str=None, tags=None, virtual_wan=None, vpn_gateway=None, p2_svpn_gateway=None, express_route_gateway=None, virtual_network_connections=None, address_prefix: str=None, route_table=None, provisioning_state=None, **kwargs) -> None:
        super(VirtualHub, self).__init__(id=id, location=location, tags=tags, **kwargs)
        self.virtual_wan = virtual_wan
        self.vpn_gateway = vpn_gateway
        self.p2_svpn_gateway = p2_svpn_gateway
        self.express_route_gateway = express_route_gateway
        self.virtual_network_connections = virtual_network_connections
        self.address_prefix = address_prefix
        self.route_table = route_table
        self.provisioning_state = provisioning_state
        self.etag = None
