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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.operations import Operations
from .operations.deployments_operations import DeploymentsOperations
from .operations.providers_operations import ProvidersOperations
from .operations.resources_operations import ResourcesOperations
from .operations.resource_groups_operations import ResourceGroupsOperations
from .operations.tags_operations import TagsOperations
from .operations.deployment_operations import DeploymentOperations
from . import models


class ResourceManagementClientConfiguration(AzureConfiguration):
    """Configuration for ResourceManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(ResourceManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-resource/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class ResourceManagementClient(SDKClient):
    """Provides operations for working with resources and resource groups.

    :ivar config: Configuration for client.
    :vartype config: ResourceManagementClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.resource.resources.v2018_05_01.operations.Operations
    :ivar deployments: Deployments operations
    :vartype deployments: azure.mgmt.resource.resources.v2018_05_01.operations.DeploymentsOperations
    :ivar providers: Providers operations
    :vartype providers: azure.mgmt.resource.resources.v2018_05_01.operations.ProvidersOperations
    :ivar resources: Resources operations
    :vartype resources: azure.mgmt.resource.resources.v2018_05_01.operations.ResourcesOperations
    :ivar resource_groups: ResourceGroups operations
    :vartype resource_groups: azure.mgmt.resource.resources.v2018_05_01.operations.ResourceGroupsOperations
    :ivar tags: Tags operations
    :vartype tags: azure.mgmt.resource.resources.v2018_05_01.operations.TagsOperations
    :ivar deployment_operations: DeploymentOperations operations
    :vartype deployment_operations: azure.mgmt.resource.resources.v2018_05_01.operations.DeploymentOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = ResourceManagementClientConfiguration(credentials, subscription_id, base_url)
        super(ResourceManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-05-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.deployments = DeploymentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.providers = ProvidersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.resources = ResourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.resource_groups = ResourceGroupsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.tags = TagsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.deployment_operations = DeploymentOperations(
            self._client, self.config, self._serialize, self._deserialize)
