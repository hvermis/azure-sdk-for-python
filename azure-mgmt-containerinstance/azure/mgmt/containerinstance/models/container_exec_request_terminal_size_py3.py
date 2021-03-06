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


class ContainerExecRequestTerminalSize(Model):
    """The size of the terminal.

    :param rows: The row size of the terminal
    :type rows: int
    :param cols: The column size of the terminal
    :type cols: int
    """

    _attribute_map = {
        'rows': {'key': 'rows', 'type': 'int'},
        'cols': {'key': 'cols', 'type': 'int'},
    }

    def __init__(self, *, rows: int=None, cols: int=None, **kwargs) -> None:
        super(ContainerExecRequestTerminalSize, self).__init__(**kwargs)
        self.rows = rows
        self.cols = cols
