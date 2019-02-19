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


class Noise(Model):
    """Properties describing noise level of the image.

    :param noise_level: An enum value indicating level of noise. Possible
     values include: 'Low', 'Medium', 'High'
    :type noise_level: str or
     ~azure.cognitiveservices.vision.face.models.NoiseLevel
    :param value: A number indicating level of noise level ranging from 0 to
     1. [0, 0.25) is under exposure. [0.25, 0.75) is good exposure. [0.75, 1]
     is over exposure. [0, 0.3) is low noise level. [0.3, 0.7) is medium noise
     level. [0.7, 1] is high noise level.
    :type value: float
    """

    _attribute_map = {
        'noise_level': {'key': 'noiseLevel', 'type': 'NoiseLevel'},
        'value': {'key': 'value', 'type': 'float'},
    }

    def __init__(self, *, noise_level=None, value: float=None, **kwargs) -> None:
        super(Noise, self).__init__(**kwargs)
        self.noise_level = noise_level
        self.value = value
