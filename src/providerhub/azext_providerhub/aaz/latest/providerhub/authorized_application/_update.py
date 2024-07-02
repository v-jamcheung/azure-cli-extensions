# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "providerhub authorized-application update",
)
class Update(AAZCommand):
    """Update the authorized application.

    :example: authorized-application update
        az providerhub authorized-application update -n "8b51e6a7-7814-42bd-aa17-3fb1837b3b7a" --data-authorizations "[{{role:ServiceOwner}}]" --provider-namespace "{providerNamespace}"
    """

    _aaz_info = {
        "version": "2024-04-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.providerhub/providerregistrations/{}/authorizedapplications/{}", "2024-04-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.application_id = AAZUuidArg(
            options=["-n", "--name", "--application-id"],
            help="The application ID.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.provider_namespace = AAZStrArg(
            options=["--provider-namespace"],
            help="The name of the resource provider hosted within ProviderHub.",
            required=True,
            id_part="name",
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.data_authorizations = AAZListArg(
            options=["--data-authorizations"],
            arg_group="Properties",
            help="The authorizations that determine the level of data access permissions on the specified resource types.",
            nullable=True,
        )
        _args_schema.provider_authorization = AAZObjectArg(
            options=["--provider-authorization"],
            arg_group="Properties",
            help="The resource provider authorization.",
            nullable=True,
        )

        data_authorizations = cls._args_schema.data_authorizations
        data_authorizations.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.data_authorizations.Element
        _element.resource_types = AAZListArg(
            options=["resource-types"],
            help="The resource types from the defined resource types in the provider namespace that the application can access. If no resource types are specified and the role is service owner, the default is * which is all resource types",
            nullable=True,
        )
        _element.role = AAZStrArg(
            options=["role"],
            help="The ownership role the application has on the resource types. The service owner role gives the application owner permissions. The limited owner role gives elevated permissions but does not allow all the permissions of a service owner, such as read/write on internal metadata.",
            enum={"LimitedOwner": "LimitedOwner", "ServiceOwner": "ServiceOwner"},
        )

        resource_types = cls._args_schema.data_authorizations.Element.resource_types
        resource_types.Element = AAZStrArg(
            nullable=True,
        )

        provider_authorization = cls._args_schema.provider_authorization
        provider_authorization.managed_by_role_definition_id = AAZStrArg(
            options=["managed-by-role-definition-id"],
            help="The managed by role definition ID for the application.",
            nullable=True,
        )
        provider_authorization.role_definition_id = AAZStrArg(
            options=["role-definition-id"],
            help="The role definition ID for the application.",
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AuthorizedApplicationsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.AuthorizedApplicationsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class AuthorizedApplicationsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.ProviderHub/providerRegistrations/{providerNamespace}/authorizedApplications/{applicationId}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "applicationId", self.ctx.args.application_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "providerNamespace", self.ctx.args.provider_namespace,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-04-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_authorized_application_read(cls._schema_on_200)

            return cls._schema_on_200

    class AuthorizedApplicationsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.ProviderHub/providerRegistrations/{providerNamespace}/authorizedApplications/{applicationId}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "applicationId", self.ctx.args.application_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "providerNamespace", self.ctx.args.provider_namespace,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-04-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_authorized_application_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType)

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("dataAuthorizations", AAZListType, ".data_authorizations")
                properties.set_prop("providerAuthorization", AAZObjectType, ".provider_authorization")

            data_authorizations = _builder.get(".properties.dataAuthorizations")
            if data_authorizations is not None:
                data_authorizations.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.dataAuthorizations[]")
            if _elements is not None:
                _elements.set_prop("resourceTypes", AAZListType, ".resource_types")
                _elements.set_prop("role", AAZStrType, ".role", typ_kwargs={"flags": {"required": True}})

            resource_types = _builder.get(".properties.dataAuthorizations[].resourceTypes")
            if resource_types is not None:
                resource_types.set_elements(AAZStrType, ".")

            provider_authorization = _builder.get(".properties.providerAuthorization")
            if provider_authorization is not None:
                provider_authorization.set_prop("managedByRoleDefinitionId", AAZStrType, ".managed_by_role_definition_id")
                provider_authorization.set_prop("roleDefinitionId", AAZStrType, ".role_definition_id")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_authorized_application_read = None

    @classmethod
    def _build_schema_authorized_application_read(cls, _schema):
        if cls._schema_authorized_application_read is not None:
            _schema.id = cls._schema_authorized_application_read.id
            _schema.name = cls._schema_authorized_application_read.name
            _schema.properties = cls._schema_authorized_application_read.properties
            _schema.system_data = cls._schema_authorized_application_read.system_data
            _schema.type = cls._schema_authorized_application_read.type
            return

        cls._schema_authorized_application_read = _schema_authorized_application_read = AAZObjectType()

        authorized_application_read = _schema_authorized_application_read
        authorized_application_read.id = AAZStrType(
            flags={"read_only": True},
        )
        authorized_application_read.name = AAZStrType(
            flags={"read_only": True},
        )
        authorized_application_read.properties = AAZObjectType()
        authorized_application_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        authorized_application_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_authorized_application_read.properties
        properties.data_authorizations = AAZListType(
            serialized_name="dataAuthorizations",
        )
        properties.provider_authorization = AAZObjectType(
            serialized_name="providerAuthorization",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        data_authorizations = _schema_authorized_application_read.properties.data_authorizations
        data_authorizations.Element = AAZObjectType()

        _element = _schema_authorized_application_read.properties.data_authorizations.Element
        _element.resource_types = AAZListType(
            serialized_name="resourceTypes",
        )
        _element.role = AAZStrType(
            flags={"required": True},
        )

        resource_types = _schema_authorized_application_read.properties.data_authorizations.Element.resource_types
        resource_types.Element = AAZStrType()

        provider_authorization = _schema_authorized_application_read.properties.provider_authorization
        provider_authorization.managed_by_role_definition_id = AAZStrType(
            serialized_name="managedByRoleDefinitionId",
        )
        provider_authorization.role_definition_id = AAZStrType(
            serialized_name="roleDefinitionId",
        )

        system_data = _schema_authorized_application_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.id = cls._schema_authorized_application_read.id
        _schema.name = cls._schema_authorized_application_read.name
        _schema.properties = cls._schema_authorized_application_read.properties
        _schema.system_data = cls._schema_authorized_application_read.system_data
        _schema.type = cls._schema_authorized_application_read.type


__all__ = ["Update"]