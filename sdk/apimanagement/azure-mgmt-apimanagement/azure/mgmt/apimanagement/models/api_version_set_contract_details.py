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


class ApiVersionSetContractDetails(Model):
    """An API Version Set contains the common configuration for a set of API
    Versions relating .

    :param id: Identifier for existing API Version Set. Omit this value to
     create a new Version Set.
    :type id: str
    :param name: The display Name of the API Version Set.
    :type name: str
    :param description: Description of API Version Set.
    :type description: str
    :param versioning_scheme: An value that determines where the API Version
     identifer will be located in a HTTP request. Possible values include:
     'Segment', 'Query', 'Header'
    :type versioning_scheme: str or ~azure.mgmt.apimanagement.models.enum
    :param version_query_name: Name of query parameter that indicates the API
     Version if versioningScheme is set to `query`.
    :type version_query_name: str
    :param version_header_name: Name of HTTP header parameter that indicates
     the API Version if versioningScheme is set to `header`.
    :type version_header_name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'versioning_scheme': {'key': 'versioningScheme', 'type': 'str'},
        'version_query_name': {'key': 'versionQueryName', 'type': 'str'},
        'version_header_name': {'key': 'versionHeaderName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApiVersionSetContractDetails, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.versioning_scheme = kwargs.get('versioning_scheme', None)
        self.version_query_name = kwargs.get('version_query_name', None)
        self.version_header_name = kwargs.get('version_header_name', None)
