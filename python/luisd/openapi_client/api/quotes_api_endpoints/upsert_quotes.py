# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
from urllib3._collections import HTTPHeaderDict

from openapi_client import api_client, exceptions
import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from openapi_client.schemas import (  # noqa: F401
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
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    InstantiationMetadata,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    NumberBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)

from openapi_client.model.lusid_validation_problem_details import LusidValidationProblemDetails
from openapi_client.model.lusid_problem_details import LusidProblemDetails
from openapi_client.model.upsert_quotes_response import UpsertQuotesResponse
from openapi_client.model.upsert_quote_request import UpsertQuoteRequest

# path params


class ScopeSchema(
    _SchemaValidator(
        max_length=64,
        min_length=1,
        regex=[{
            'pattern': r'^[a-zA-Z0-9\-_]+$',  # noqa: E501
        }],
    ),
    _SchemaTypeChecker(typing.Union[none_type, str, ]),
    StrBase,
    NoneBase,
    Schema
):

    def __new__(
        cls,
        *args: typing.Union[str, None, ],
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
    ) -> 'ScopeSchema':
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
        )
RequestRequiredPathParams = typing.TypedDict(
    'RequestRequiredPathParams',
    {
        'scope': ScopeSchema,
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


request_path_scope = api_client.PathParameter(
    name="scope",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ScopeSchema,
    required=True,
)
# body param


class SchemaForRequestBodyApplicationJsonPatchjson(
    _SchemaTypeChecker(typing.Union[frozendict, none_type, ]),
    DictBase,
    NoneBase,
    Schema
):

    @classmethod
    @property
    def _additional_properties(cls) -> typing.Type['UpsertQuoteRequest']:
        return UpsertQuoteRequest

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, None, ],
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'SchemaForRequestBodyApplicationJsonPatchjson':
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
            **kwargs,
        )


class SchemaForRequestBodyApplicationJson(
    _SchemaTypeChecker(typing.Union[frozendict, none_type, ]),
    DictBase,
    NoneBase,
    Schema
):

    @classmethod
    @property
    def _additional_properties(cls) -> typing.Type['UpsertQuoteRequest']:
        return UpsertQuoteRequest

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, None, ],
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
            **kwargs,
        )


class SchemaForRequestBodyTextJson(
    _SchemaTypeChecker(typing.Union[frozendict, none_type, ]),
    DictBase,
    NoneBase,
    Schema
):

    @classmethod
    @property
    def _additional_properties(cls) -> typing.Type['UpsertQuoteRequest']:
        return UpsertQuoteRequest

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, None, ],
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'SchemaForRequestBodyTextJson':
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
            **kwargs,
        )


class SchemaForRequestBodyApplicationJson(
    _SchemaTypeChecker(typing.Union[frozendict, none_type, ]),
    DictBase,
    NoneBase,
    Schema
):

    @classmethod
    @property
    def _additional_properties(cls) -> typing.Type['UpsertQuoteRequest']:
        return UpsertQuoteRequest

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, None, ],
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
            **kwargs,
        )


request_body_request_body = api_client.RequestBody(
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
)
_path = '/api/quotes/{scope}'
_method = 'POST'
_auth = [
    'oauth2',
]
SchemaFor200ResponseBodyTextPlain = UpsertQuotesResponse
SchemaFor200ResponseBodyApplicationJson = UpsertQuotesResponse
SchemaFor200ResponseBodyTextJson = UpsertQuotesResponse


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


class UpsertQuotes(api_client.Api):

    def upsert_quotes(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] = unset,
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
        [EARLY ACCESS] UpsertQuotes: Upsert quotes
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestPathParams, path_params)

        _path_params = {}
        for parameter in (
            request_path_scope,
        ):
            parameter_data = path_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        _fields = None
        _body = None
        if body is not unset:
            serialized_data = request_body_request_body.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=_path,
            method=_method,
            path_params=_path_params,
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
