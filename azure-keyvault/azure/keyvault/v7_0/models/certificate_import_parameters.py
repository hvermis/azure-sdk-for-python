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


class CertificateImportParameters(Model):
    """The certificate import parameters.

    All required parameters must be populated in order to send to Azure.

    :param base64_encoded_certificate: Required. Base64 encoded representation
     of the certificate object to import. This certificate needs to contain the
     private key.
    :type base64_encoded_certificate: str
    :param password: If the private key in base64EncodedCertificate is
     encrypted, the password used for encryption.
    :type password: str
    :param certificate_policy: The management policy for the certificate.
    :type certificate_policy: ~azure.keyvault.v7_0.models.CertificatePolicy
    :param certificate_attributes: The attributes of the certificate
     (optional).
    :type certificate_attributes:
     ~azure.keyvault.v7_0.models.CertificateAttributes
    :param tags: Application specific metadata in the form of key-value pairs.
    :type tags: dict[str, str]
    """

    _validation = {
        'base64_encoded_certificate': {'required': True},
    }

    _attribute_map = {
        'base64_encoded_certificate': {'key': 'value', 'type': 'str'},
        'password': {'key': 'pwd', 'type': 'str'},
        'certificate_policy': {'key': 'policy', 'type': 'CertificatePolicy'},
        'certificate_attributes': {'key': 'attributes', 'type': 'CertificateAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(CertificateImportParameters, self).__init__(**kwargs)
        self.base64_encoded_certificate = kwargs.get('base64_encoded_certificate', None)
        self.password = kwargs.get('password', None)
        self.certificate_policy = kwargs.get('certificate_policy', None)
        self.certificate_attributes = kwargs.get('certificate_attributes', None)
        self.tags = kwargs.get('tags', None)
