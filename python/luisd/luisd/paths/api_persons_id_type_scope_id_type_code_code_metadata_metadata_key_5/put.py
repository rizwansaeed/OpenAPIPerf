# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
import functools  # noqa: F401
from urllib3._collections import HTTPHeaderDict

from luisd import api_client, exceptions
import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from luisd.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    NoneClass,
    BoolClass,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)

from luisd.model.upsert_person_access_metadata_request import UpsertPersonAccessMetadataRequest
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.resource_list_of_access_metadata_value_of import ResourceListOfAccessMetadataValueOf

from . import path

# query params


class EffectiveAtSchema(
    _SchemaTypeChecker(typing.Union[NoneClass, str, ]),
    StrBase,
    NoneBase,
    Schema
):

    def __new__(
        cls,
        *args: typing.Union[str, None, ],
        _configuration: typing.Optional[Configuration] = None,
    ) -> 'EffectiveAtSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
RequestRequiredQueryParams = typing.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing.TypedDict(
    'RequestOptionalQueryParams',
    {
        'effectiveAt': EffectiveAtSchema,
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_effective_at = api_client.QueryParameter(
    name="effectiveAt",
    style=api_client.ParameterStyle.FORM,
    schema=EffectiveAtSchema,
    explode=True,
)
# path params
IdTypeScopeSchema = StrSchema
IdTypeCodeSchema = StrSchema


class CodeSchema(
    _SchemaValidator(
        max_length=64,
        min_length=1,
        regex=[{
            'pattern': r'^[a-zA-Z0-9\-_]+$',  # noqa: E501
        }],
    ),
    StrSchema
):
    pass
MetadataKeySchema = StrSchema
RequestRequiredPathParams = typing.TypedDict(
    'RequestRequiredPathParams',
    {
        'idTypeScope': IdTypeScopeSchema,
        'idTypeCode': IdTypeCodeSchema,
        'code': CodeSchema,
        'metadataKey': MetadataKeySchema,
    }
)
RequestOptionalPathParams = typing.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_id_type_scope = api_client.PathParameter(
    name="idTypeScope",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdTypeScopeSchema,
    required=True,
)
request_path_id_type_code = api_client.PathParameter(
    name="idTypeCode",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdTypeCodeSchema,
    required=True,
)
request_path_code = api_client.PathParameter(
    name="code",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CodeSchema,
    required=True,
)
request_path_metadata_key = api_client.PathParameter(
    name="metadataKey",
    style=api_client.ParameterStyle.SIMPLE,
    schema=MetadataKeySchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJsonPatchjson = UpsertPersonAccessMetadataRequest
SchemaForRequestBodyApplicationJson = UpsertPersonAccessMetadataRequest
SchemaForRequestBodyTextJson = UpsertPersonAccessMetadataRequest
SchemaForRequestBodyApplicationJson = UpsertPersonAccessMetadataRequest


request_body_upsert_person_access_metadata_request = api_client.RequestBody(
    content={
        'application/json-patch+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonPatchjson),
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaForRequestBodyTextJson),
        'application/*+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'oauth2',
]
SchemaFor200ResponseBodyTextPlain = ResourceListOfAccessMetadataValueOf
SchemaFor200ResponseBodyApplicationJson = ResourceListOfAccessMetadataValueOf
SchemaFor200ResponseBodyTextJson = ResourceListOfAccessMetadataValueOf


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyTextPlain,
        SchemaFor200ResponseBodyApplicationJson,
        SchemaFor200ResponseBodyTextJson,
    ]
    headers: Unset = unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'text/plain': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextPlain),
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextJson),
    },
)
SchemaFor400ResponseBodyTextPlain = LusidValidationProblemDetails
SchemaFor400ResponseBodyApplicationJson = LusidValidationProblemDetails
SchemaFor400ResponseBodyTextJson = LusidValidationProblemDetails


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor400ResponseBodyTextPlain,
        SchemaFor400ResponseBodyApplicationJson,
        SchemaFor400ResponseBodyTextJson,
    ]
    headers: Unset = unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'text/plain': api_client.MediaType(
            schema=SchemaFor400ResponseBodyTextPlain),
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyTextJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = LusidProblemDetails


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor0ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'text/plain',
    'application/json',
    'text/json',
)


class BaseApi(api_client.Api):

    def _upsert_person_access_metadata(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson],
        query_params: RequestQueryParams = frozendict(),
        path_params: RequestPathParams = frozendict(),
        content_type: str = 'application/json-patch+json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        [EARLY ACCESS] UpsertPersonAccessMetadata: Upsert a Person Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_id_type_scope,
            request_path_id_type_code,
            request_path_code,
            request_path_metadata_key,
        ):
            parameter_data = path_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        prefix_separator_iterator = None
        for parameter in (
            request_query_effective_at,
        ):
            parameter_data = query_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        if body is unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_upsert_person_access_metadata_request.serialize(body, content_type)
        _headers.add('Content-Type', content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='put'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                default_response = _status_code_to_response.get('default')
                if default_response:
                    api_response = default_response.deserialize(response, self.api_client.configuration)
                else:
                    api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class UpsertPersonAccessMetadata(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def upsert_person_access_metadata(
        self: BaseApi,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson],
        query_params: RequestQueryParams = frozendict(),
        path_params: RequestPathParams = frozendict(),
        content_type: str = 'application/json-patch+json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._upsert_person_access_metadata(
            body=body,
            query_params=query_params,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def put(
        self: BaseApi,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson],
        query_params: RequestQueryParams = frozendict(),
        path_params: RequestPathParams = frozendict(),
        content_type: str = 'application/json-patch+json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._upsert_person_access_metadata(
            body=body,
            query_params=query_params,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


