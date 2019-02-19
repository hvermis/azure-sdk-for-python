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


class DataTableResponseColumn(Model):
    """Column definition.

    :param column_name: Name of the column
    :type column_name: str
    :param data_type: Data type which looks like 'String' or 'Int32'.
    :type data_type: str
    :param column_type: Column Type
    :type column_type: str
    """

    _attribute_map = {
        'column_name': {'key': 'columnName', 'type': 'str'},
        'data_type': {'key': 'dataType', 'type': 'str'},
        'column_type': {'key': 'columnType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DataTableResponseColumn, self).__init__(**kwargs)
        self.column_name = kwargs.get('column_name', None)
        self.data_type = kwargs.get('data_type', None)
        self.column_type = kwargs.get('column_type', None)
