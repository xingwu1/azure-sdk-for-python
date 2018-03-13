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


class UsageStatistics(Model):
    """Statistics related to pool usage information.

    :param start_time: The start time of the time range covered by the
     statistics.
    :type start_time: datetime
    :param last_update_time: The time at which the statistics were last
     updated. All statistics are limited to the range between startTime and
     lastUpdateTime.
    :type last_update_time: datetime
    :param dedicated_core_time: The aggregated wall-clock time of the
     dedicated compute node cores being part of the pool.
    :type dedicated_core_time: timedelta
    """

    _validation = {
        'start_time': {'required': True},
        'last_update_time': {'required': True},
        'dedicated_core_time': {'required': True},
    }

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'iso-8601'},
        'dedicated_core_time': {'key': 'dedicatedCoreTime', 'type': 'duration'},
    }

    def __init__(self, start_time, last_update_time, dedicated_core_time):
        super(UsageStatistics, self).__init__()
        self.start_time = start_time
        self.last_update_time = last_update_time
        self.dedicated_core_time = dedicated_core_time
