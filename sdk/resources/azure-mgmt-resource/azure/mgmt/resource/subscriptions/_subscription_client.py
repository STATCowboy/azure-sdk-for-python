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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import SubscriptionClientConfiguration



class SubscriptionClient(MultiApiClientMixin, SDKClient):
    """All resource groups and resources exist within subscriptions. These operation enable you get information about your subscriptions and tenants. A tenant is a dedicated instance of Azure Active Directory (Azure AD) for your organization.

    This ready contains multiple API versions, to help you deal with all Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, uses latest API version available on public Azure.
    For production, you should stick a particular api-version and/or profile.
    The profile sets a mapping between the operation group and an API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :ivar config: Configuration for client.
    :vartype config: SubscriptionClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2019-06-01'
    _PROFILE_TAG = "azure.mgmt.resource.subscriptions.SubscriptionClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(self, credentials, api_version=None, base_url=None, profile=KnownProfiles.default):
        self.config = SubscriptionClientConfiguration(credentials, base_url)
        super(SubscriptionClient, self).__init__(
            credentials,
            self.config,
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2016-06-01: :mod:`v2016_06_01.models<azure.mgmt.resource.subscriptions.v2016_06_01.models>`
           * 2018-06-01: :mod:`v2018_06_01.models<azure.mgmt.resource.subscriptions.v2018_06_01.models>`
           * 2019-06-01: :mod:`v2019_06_01.models<azure.mgmt.resource.subscriptions.v2019_06_01.models>`
        """
        if api_version == '2016-06-01':
            from .v2016_06_01 import models
            return models
        elif api_version == '2018-06-01':
            from .v2018_06_01 import models
            return models
        elif api_version == '2019-06-01':
            from .v2019_06_01 import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2016-06-01: :class:`Operations<azure.mgmt.resource.subscriptions.v2016_06_01.operations.Operations>`
           * 2018-06-01: :class:`Operations<azure.mgmt.resource.subscriptions.v2018_06_01.operations.Operations>`
           * 2019-06-01: :class:`Operations<azure.mgmt.resource.subscriptions.v2019_06_01.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2016-06-01':
            from .v2016_06_01.operations import Operations as OperationClass
        elif api_version == '2018-06-01':
            from .v2018_06_01.operations import Operations as OperationClass
        elif api_version == '2019-06-01':
            from .v2019_06_01.operations import Operations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def subscriptions(self):
        """Instance depends on the API version:

           * 2016-06-01: :class:`SubscriptionsOperations<azure.mgmt.resource.subscriptions.v2016_06_01.operations.SubscriptionsOperations>`
           * 2018-06-01: :class:`SubscriptionsOperations<azure.mgmt.resource.subscriptions.v2018_06_01.operations.SubscriptionsOperations>`
           * 2019-06-01: :class:`SubscriptionsOperations<azure.mgmt.resource.subscriptions.v2019_06_01.operations.SubscriptionsOperations>`
        """
        api_version = self._get_api_version('subscriptions')
        if api_version == '2016-06-01':
            from .v2016_06_01.operations import SubscriptionsOperations as OperationClass
        elif api_version == '2018-06-01':
            from .v2018_06_01.operations import SubscriptionsOperations as OperationClass
        elif api_version == '2019-06-01':
            from .v2019_06_01.operations import SubscriptionsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def tenants(self):
        """Instance depends on the API version:

           * 2016-06-01: :class:`TenantsOperations<azure.mgmt.resource.subscriptions.v2016_06_01.operations.TenantsOperations>`
           * 2018-06-01: :class:`TenantsOperations<azure.mgmt.resource.subscriptions.v2018_06_01.operations.TenantsOperations>`
           * 2019-06-01: :class:`TenantsOperations<azure.mgmt.resource.subscriptions.v2019_06_01.operations.TenantsOperations>`
        """
        api_version = self._get_api_version('tenants')
        if api_version == '2016-06-01':
            from .v2016_06_01.operations import TenantsOperations as OperationClass
        elif api_version == '2018-06-01':
            from .v2018_06_01.operations import TenantsOperations as OperationClass
        elif api_version == '2019-06-01':
            from .v2019_06_01.operations import TenantsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))
