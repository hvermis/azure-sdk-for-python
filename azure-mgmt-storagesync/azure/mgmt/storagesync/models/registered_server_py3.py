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

from .proxy_resource_py3 import ProxyResource


class RegisteredServer(ProxyResource):
    """Registered Server resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param server_certificate: Registered Server Certificate
    :type server_certificate: str
    :param agent_version: Registered Server Agent Version
    :type agent_version: str
    :param server_os_version: Registered Server OS Version
    :type server_os_version: str
    :param server_management_error_code: Registered Server Management Error
     Code
    :type server_management_error_code: int
    :param last_heart_beat: Registered Server last heart beat
    :type last_heart_beat: str
    :param provisioning_state: Registered Server Provisioning State
    :type provisioning_state: str
    :param server_role: Registered Server serverRole
    :type server_role: str
    :param cluster_id: Registered Server clusterId
    :type cluster_id: str
    :param cluster_name: Registered Server clusterName
    :type cluster_name: str
    :param server_id: Registered Server serverId
    :type server_id: str
    :param storage_sync_service_uid: Registered Server storageSyncServiceUid
    :type storage_sync_service_uid: str
    :param last_workflow_id: Registered Server lastWorkflowId
    :type last_workflow_id: str
    :param last_operation_name: Resource Last Operation Name
    :type last_operation_name: str
    :param discovery_endpoint_uri: Resource discoveryEndpointUri
    :type discovery_endpoint_uri: str
    :param resource_location: Resource Location
    :type resource_location: str
    :param service_location: Service Location
    :type service_location: str
    :param friendly_name: Friendly Name
    :type friendly_name: str
    :param management_endpoint_uri: Management Endpoint Uri
    :type management_endpoint_uri: str
    :param monitoring_configuration: Monitoring Configuration
    :type monitoring_configuration: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'server_certificate': {'key': 'properties.serverCertificate', 'type': 'str'},
        'agent_version': {'key': 'properties.agentVersion', 'type': 'str'},
        'server_os_version': {'key': 'properties.serverOSVersion', 'type': 'str'},
        'server_management_error_code': {'key': 'properties.serverManagementErrorCode', 'type': 'int'},
        'last_heart_beat': {'key': 'properties.lastHeartBeat', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'server_role': {'key': 'properties.serverRole', 'type': 'str'},
        'cluster_id': {'key': 'properties.clusterId', 'type': 'str'},
        'cluster_name': {'key': 'properties.clusterName', 'type': 'str'},
        'server_id': {'key': 'properties.serverId', 'type': 'str'},
        'storage_sync_service_uid': {'key': 'properties.storageSyncServiceUid', 'type': 'str'},
        'last_workflow_id': {'key': 'properties.lastWorkflowId', 'type': 'str'},
        'last_operation_name': {'key': 'properties.lastOperationName', 'type': 'str'},
        'discovery_endpoint_uri': {'key': 'properties.discoveryEndpointUri', 'type': 'str'},
        'resource_location': {'key': 'properties.resourceLocation', 'type': 'str'},
        'service_location': {'key': 'properties.serviceLocation', 'type': 'str'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'management_endpoint_uri': {'key': 'properties.managementEndpointUri', 'type': 'str'},
        'monitoring_configuration': {'key': 'properties.monitoringConfiguration', 'type': 'str'},
    }

    def __init__(self, *, server_certificate: str=None, agent_version: str=None, server_os_version: str=None, server_management_error_code: int=None, last_heart_beat: str=None, provisioning_state: str=None, server_role: str=None, cluster_id: str=None, cluster_name: str=None, server_id: str=None, storage_sync_service_uid: str=None, last_workflow_id: str=None, last_operation_name: str=None, discovery_endpoint_uri: str=None, resource_location: str=None, service_location: str=None, friendly_name: str=None, management_endpoint_uri: str=None, monitoring_configuration: str=None, **kwargs) -> None:
        super(RegisteredServer, self).__init__(**kwargs)
        self.server_certificate = server_certificate
        self.agent_version = agent_version
        self.server_os_version = server_os_version
        self.server_management_error_code = server_management_error_code
        self.last_heart_beat = last_heart_beat
        self.provisioning_state = provisioning_state
        self.server_role = server_role
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.server_id = server_id
        self.storage_sync_service_uid = storage_sync_service_uid
        self.last_workflow_id = last_workflow_id
        self.last_operation_name = last_operation_name
        self.discovery_endpoint_uri = discovery_endpoint_uri
        self.resource_location = resource_location
        self.service_location = service_location
        self.friendly_name = friendly_name
        self.management_endpoint_uri = management_endpoint_uri
        self.monitoring_configuration = monitoring_configuration
