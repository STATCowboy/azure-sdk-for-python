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

import uuid
from msrest.pipeline import ClientRawResponse
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling

from .. import models


class SupportTicketsOperations(object):
    """SupportTicketsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Api version. Constant value: "2019-05-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2019-05-01-preview"

        self.config = config

    def check_name_availability(
            self, name, type, custom_headers=None, raw=False, **operation_config):
        """Check the availability of a resource name. This API should to be used
        to check the uniqueness of the name for support ticket creation for the
        selected subscription.

        :param name: The resource name to validate
        :type name: str
        :param type: The type of resource. Possible values include:
         'Microsoft.Support/supportTickets', 'Microsoft.Support/communications'
        :type type: str or ~azure.mgmt.support.models.Type
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CheckNameAvailabilityOutput or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.support.models.CheckNameAvailabilityOutput or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ExceptionResponseException<azure.mgmt.support.models.ExceptionResponseException>`
        """
        check_name_availability_input = models.CheckNameAvailabilityInput(name=name, type=type)

        # Construct URL
        url = self.check_name_availability.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(check_name_availability_input, 'CheckNameAvailabilityInput')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ExceptionResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('CheckNameAvailabilityOutput', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    check_name_availability.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Support/checkNameAvailability'}

    def list(
            self, top=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Lists all the support tickets for an Azure subscription. <br/><br/>You
        can also filter the support tickets by <i>Status</i> or
        <i>CreatedDate</i> using the $filter parameter. Output will be a paged
        result with <i>nextLink</i>, using which you can retrieve the next set
        of support tickets. <br/><br/>Support ticket data is available for 12
        months after ticket creation. If a ticket was created more than 12
        months ago, a request for data might cause an error.

        :param top: The number of values to return in the collection. Default
         is 25 and max is 100.
        :type top: int
        :param filter: The filter to apply on the operation. We support 'odata
         v4.0' filter semantics. <a target='_blank'
         href='https://docs.microsoft.com/odata/concepts/queryoptions-overview'>Learn
         more</a> <br/><i>Status</i> filter can only be used with 'eq'
         operator. For <i>CreatedDate</i> filter, the supported operators are
         'gt' and 'ge'. When using both filters, combine them using the logical
         'AND'.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of SupportTicketDetails
        :rtype:
         ~azure.mgmt.support.models.SupportTicketDetailsPaged[~azure.mgmt.support.models.SupportTicketDetails]
        :raises:
         :class:`ExceptionResponseException<azure.mgmt.support.models.ExceptionResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ExceptionResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.SupportTicketDetailsPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets'}

    def get(
            self, support_ticket_name, custom_headers=None, raw=False, **operation_config):
        """Gets details for a specific support ticket in an Azure subscription.
        <br/><br/>Support ticket data is available for 12 months after ticket
        creation. If a ticket was created more than 12 months ago, a request
        for data might cause an error.

        :param support_ticket_name: Support ticket name
        :type support_ticket_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SupportTicketDetails or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.support.models.SupportTicketDetails or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ExceptionResponseException<azure.mgmt.support.models.ExceptionResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'supportTicketName': self._serialize.url("support_ticket_name", support_ticket_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ExceptionResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SupportTicketDetails', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}'}

    def update(
            self, support_ticket_name, severity=None, contact_details=None, custom_headers=None, raw=False, **operation_config):
        """This API allows you to update the severity level or your contact
        information in the support ticket. <br/><br/> Note: The severity levels
        cannot be changed if a support ticket is actively being worked upon by
        an Azure support engineer. In such a case, contact your support
        engineer to request severity update by adding a new communication using
        the Communications API.

        :param support_ticket_name: Support ticket name
        :type support_ticket_name: str
        :param severity: Severity level. Possible values include: 'minimal',
         'moderate', 'critical'
        :type severity: str or ~azure.mgmt.support.models.SeverityLevel
        :param contact_details: Contact details to be updated on the support
         ticket.
        :type contact_details: ~azure.mgmt.support.models.UpdateContactProfile
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SupportTicketDetails or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.support.models.SupportTicketDetails or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ExceptionResponseException<azure.mgmt.support.models.ExceptionResponseException>`
        """
        update_support_ticket = models.UpdateSupportTicket(severity=severity, contact_details=contact_details)

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'supportTicketName': self._serialize.url("support_ticket_name", support_ticket_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(update_support_ticket, 'UpdateSupportTicket')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ExceptionResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SupportTicketDetails', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}'}


    def _create_initial(
            self, support_ticket_name, create_support_ticket_parameters, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'supportTicketName': self._serialize.url("support_ticket_name", support_ticket_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(create_support_ticket_parameters, 'SupportTicketDetails')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 202]:
            raise models.ExceptionResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SupportTicketDetails', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create(
            self, support_ticket_name, create_support_ticket_parameters, custom_headers=None, raw=False, polling=True, **operation_config):
        """Creates a new support ticket for Quota increase, Technical, Billing,
        and Subscription Management issues for the specified subscription.
        <br/><br/>A paid technical support plan is required to create a support
        ticket using this API. <a href='https://aka.ms/supportticketAPI'>Learn
        more</a> <br/><br/> Use the Services API to map the right Service Id to
        the issue type. For example: For billing tickets set *serviceId* to
        *'/providers/Microsoft.Support/services/517f2da6-78fd-0498-4e22-ad26996b1dfc'*.
        <br/> For Technical issues, the Service id will map to the Azure
        service you want to raise a support ticket for. <br/><br/>Always call
        the Services and ProblemClassifications API to get the most recent set
        of services and problem categories required for support ticket
        creation.

        :param support_ticket_name: Support ticket name.
        :type support_ticket_name: str
        :param create_support_ticket_parameters: Support ticket request
         payload.
        :type create_support_ticket_parameters:
         ~azure.mgmt.support.models.SupportTicketDetails
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns SupportTicketDetails or
         ClientRawResponse<SupportTicketDetails> if raw==True
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~azure.mgmt.support.models.SupportTicketDetails]
         or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[~azure.mgmt.support.models.SupportTicketDetails]]
        :raises:
         :class:`ExceptionResponseException<azure.mgmt.support.models.ExceptionResponseException>`
        """
        raw_result = self._create_initial(
            support_ticket_name=support_ticket_name,
            create_support_ticket_parameters=create_support_ticket_parameters,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('SupportTicketDetails', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    create.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}'}
