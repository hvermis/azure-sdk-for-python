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


class DiagnosticsDescription(Model):
    """Describes the diagnostics options available.

    :param sinks: List of supported sinks that can be referenced.
    :type sinks: list[~azure.servicefabric.models.DiagnosticsSinkProperties]
    :param enabled: Status of whether or not sinks are enabled.
    :type enabled: bool
    :param default_sink_refs: The sinks to be used if diagnostics is enabled.
     Sink choices can be overridden at the service and code package level.
    :type default_sink_refs: list[str]
    """

    _attribute_map = {
        'sinks': {'key': 'sinks', 'type': '[DiagnosticsSinkProperties]'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'default_sink_refs': {'key': 'defaultSinkRefs', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(DiagnosticsDescription, self).__init__(**kwargs)
        self.sinks = kwargs.get('sinks', None)
        self.enabled = kwargs.get('enabled', None)
        self.default_sink_refs = kwargs.get('default_sink_refs', None)
