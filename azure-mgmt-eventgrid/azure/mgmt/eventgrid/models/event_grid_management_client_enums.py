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

from enum import Enum


class EventSubscriptionProvisioningState(str, Enum):

    creating = "Creating"
    updating = "Updating"
    deleting = "Deleting"
    succeeded = "Succeeded"
    canceled = "Canceled"
    failed = "Failed"
    awaiting_manual_action = "AwaitingManualAction"


class TopicProvisioningState(str, Enum):

    creating = "Creating"
    updating = "Updating"
    deleting = "Deleting"
    succeeded = "Succeeded"
    canceled = "Canceled"
    failed = "Failed"


class ResourceRegionType(str, Enum):

    regional_resource = "RegionalResource"
    global_resource = "GlobalResource"


class TopicTypeProvisioningState(str, Enum):

    creating = "Creating"
    updating = "Updating"
    deleting = "Deleting"
    succeeded = "Succeeded"
    canceled = "Canceled"
    failed = "Failed"
