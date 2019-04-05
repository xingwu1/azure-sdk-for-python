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


class SnapshotUpdate(Model):
    """Snapshot update resource.

    :param os_type: the Operating System type. Possible values include:
     'Windows', 'Linux'
    :type os_type: str or
     ~azure.mgmt.compute.v2018_09_30.models.OperatingSystemTypes
    :param disk_size_gb: If creationData.createOption is Empty, this field is
     mandatory and it indicates the size of the VHD to create. If this field is
     present for updates or creation with other options, it indicates a resize.
     Resizes are only allowed if the disk is not attached to a running VM, and
     can only increase the disk's size.
    :type disk_size_gb: int
    :param encryption_settings_collection: Encryption settings collection used
     be Azure Disk Encryption, can contain multiple encryption settings per
     disk or snapshot.
    :type encryption_settings_collection:
     ~azure.mgmt.compute.v2018_09_30.models.EncryptionSettingsCollection
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param sku:
    :type sku: ~azure.mgmt.compute.v2018_09_30.models.SnapshotSku
    """

    _attribute_map = {
        'os_type': {'key': 'properties.osType', 'type': 'OperatingSystemTypes'},
        'disk_size_gb': {'key': 'properties.diskSizeGB', 'type': 'int'},
        'encryption_settings_collection': {'key': 'properties.encryptionSettingsCollection', 'type': 'EncryptionSettingsCollection'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'SnapshotSku'},
    }

    def __init__(self, *, os_type=None, disk_size_gb: int=None, encryption_settings_collection=None, tags=None, sku=None, **kwargs) -> None:
        super(SnapshotUpdate, self).__init__(**kwargs)
        self.os_type = os_type
        self.disk_size_gb = disk_size_gb
        self.encryption_settings_collection = encryption_settings_collection
        self.tags = tags
        self.sku = sku