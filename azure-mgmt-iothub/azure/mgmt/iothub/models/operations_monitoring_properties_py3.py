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


class OperationsMonitoringProperties(Model):
    """The operations monitoring properties for the IoT hub. The possible keys to
    the dictionary are Connections, DeviceTelemetry, C2DCommands,
    DeviceIdentityOperations, FileUploadOperations, Routes, D2CTwinOperations,
    C2DTwinOperations, TwinQueries, JobsOperations, DirectMethods.

    :param events:
    :type events: dict[str, str or
     ~azure.mgmt.iothub.models.OperationMonitoringLevel]
    """

    _attribute_map = {
        'events': {'key': 'events', 'type': '{str}'},
    }

    def __init__(self, *, events=None, **kwargs) -> None:
        super(OperationsMonitoringProperties, self).__init__(**kwargs)
        self.events = events