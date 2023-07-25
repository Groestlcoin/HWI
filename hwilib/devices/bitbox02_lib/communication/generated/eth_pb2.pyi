"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from . import antiklepto_pb2
import builtins
from . import common_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ETHCoin:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ETHCoinEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ETHCoin.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ETH: _ETHCoin.ValueType  # 0
    RopstenETH: _ETHCoin.ValueType  # 1
    """Removed in v9.14.0 - deprecated"""

    RinkebyETH: _ETHCoin.ValueType  # 2
    """Removed in v9.14.0 - deprecated"""

class ETHCoin(_ETHCoin, metaclass=_ETHCoinEnumTypeWrapper):
    """Kept for backwards compatibility. Use chain_id instead, introduced in v9.10.0."""
    pass

ETH: ETHCoin.ValueType  # 0
RopstenETH: ETHCoin.ValueType  # 1
"""Removed in v9.14.0 - deprecated"""

RinkebyETH: ETHCoin.ValueType  # 2
"""Removed in v9.14.0 - deprecated"""

global___ETHCoin = ETHCoin


class ETHPubRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _OutputType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _OutputTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ETHPubRequest._OutputType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ADDRESS: ETHPubRequest._OutputType.ValueType  # 0
        XPUB: ETHPubRequest._OutputType.ValueType  # 1
    class OutputType(_OutputType, metaclass=_OutputTypeEnumTypeWrapper):
        pass

    ADDRESS: ETHPubRequest.OutputType.ValueType  # 0
    XPUB: ETHPubRequest.OutputType.ValueType  # 1

    KEYPATH_FIELD_NUMBER: builtins.int
    COIN_FIELD_NUMBER: builtins.int
    OUTPUT_TYPE_FIELD_NUMBER: builtins.int
    DISPLAY_FIELD_NUMBER: builtins.int
    CONTRACT_ADDRESS_FIELD_NUMBER: builtins.int
    CHAIN_ID_FIELD_NUMBER: builtins.int
    @property
    def keypath(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    coin: global___ETHCoin.ValueType
    """Deprecated: use chain_id instead."""

    output_type: global___ETHPubRequest.OutputType.ValueType
    display: builtins.bool
    contract_address: builtins.bytes
    chain_id: builtins.int
    """If non-zero, `coin` is ignored and `chain_id` is used to identify the network."""

    def __init__(self,
        *,
        keypath: typing.Optional[typing.Iterable[builtins.int]] = ...,
        coin: global___ETHCoin.ValueType = ...,
        output_type: global___ETHPubRequest.OutputType.ValueType = ...,
        display: builtins.bool = ...,
        contract_address: builtins.bytes = ...,
        chain_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["chain_id",b"chain_id","coin",b"coin","contract_address",b"contract_address","display",b"display","keypath",b"keypath","output_type",b"output_type"]) -> None: ...
global___ETHPubRequest = ETHPubRequest

class ETHSignRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COIN_FIELD_NUMBER: builtins.int
    KEYPATH_FIELD_NUMBER: builtins.int
    NONCE_FIELD_NUMBER: builtins.int
    GAS_PRICE_FIELD_NUMBER: builtins.int
    GAS_LIMIT_FIELD_NUMBER: builtins.int
    RECIPIENT_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    HOST_NONCE_COMMITMENT_FIELD_NUMBER: builtins.int
    CHAIN_ID_FIELD_NUMBER: builtins.int
    coin: global___ETHCoin.ValueType
    """Deprecated: use chain_id instead."""

    @property
    def keypath(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    nonce: builtins.bytes
    """smallest big endian serialization, max. 16 bytes"""

    gas_price: builtins.bytes
    """smallest big endian serialization, max. 16 bytes"""

    gas_limit: builtins.bytes
    """smallest big endian serialization, max. 16 bytes"""

    recipient: builtins.bytes
    """20 byte recipient"""

    value: builtins.bytes
    """smallest big endian serialization, max. 32 bytes"""

    data: builtins.bytes
    @property
    def host_nonce_commitment(self) -> antiklepto_pb2.AntiKleptoHostNonceCommitment: ...
    chain_id: builtins.int
    """If non-zero, `coin` is ignored and `chain_id` is used to identify the network."""

    def __init__(self,
        *,
        coin: global___ETHCoin.ValueType = ...,
        keypath: typing.Optional[typing.Iterable[builtins.int]] = ...,
        nonce: builtins.bytes = ...,
        gas_price: builtins.bytes = ...,
        gas_limit: builtins.bytes = ...,
        recipient: builtins.bytes = ...,
        value: builtins.bytes = ...,
        data: builtins.bytes = ...,
        host_nonce_commitment: typing.Optional[antiklepto_pb2.AntiKleptoHostNonceCommitment] = ...,
        chain_id: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["host_nonce_commitment",b"host_nonce_commitment"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["chain_id",b"chain_id","coin",b"coin","data",b"data","gas_limit",b"gas_limit","gas_price",b"gas_price","host_nonce_commitment",b"host_nonce_commitment","keypath",b"keypath","nonce",b"nonce","recipient",b"recipient","value",b"value"]) -> None: ...
global___ETHSignRequest = ETHSignRequest

class ETHSignMessageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COIN_FIELD_NUMBER: builtins.int
    KEYPATH_FIELD_NUMBER: builtins.int
    MSG_FIELD_NUMBER: builtins.int
    HOST_NONCE_COMMITMENT_FIELD_NUMBER: builtins.int
    CHAIN_ID_FIELD_NUMBER: builtins.int
    coin: global___ETHCoin.ValueType
    """Deprecated: use chain_id instead."""

    @property
    def keypath(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    msg: builtins.bytes
    @property
    def host_nonce_commitment(self) -> antiklepto_pb2.AntiKleptoHostNonceCommitment: ...
    chain_id: builtins.int
    """If non-zero, `coin` is ignored and `chain_id` is used to identify the network."""

    def __init__(self,
        *,
        coin: global___ETHCoin.ValueType = ...,
        keypath: typing.Optional[typing.Iterable[builtins.int]] = ...,
        msg: builtins.bytes = ...,
        host_nonce_commitment: typing.Optional[antiklepto_pb2.AntiKleptoHostNonceCommitment] = ...,
        chain_id: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["host_nonce_commitment",b"host_nonce_commitment"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["chain_id",b"chain_id","coin",b"coin","host_nonce_commitment",b"host_nonce_commitment","keypath",b"keypath","msg",b"msg"]) -> None: ...
global___ETHSignMessageRequest = ETHSignMessageRequest

class ETHSignResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SIGNATURE_FIELD_NUMBER: builtins.int
    signature: builtins.bytes
    """65 bytes, last byte is the recid"""

    def __init__(self,
        *,
        signature: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["signature",b"signature"]) -> None: ...
global___ETHSignResponse = ETHSignResponse

class ETHSignTypedMessageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _DataType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _DataTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ETHSignTypedMessageRequest._DataType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: ETHSignTypedMessageRequest._DataType.ValueType  # 0
        BYTES: ETHSignTypedMessageRequest._DataType.ValueType  # 1
        UINT: ETHSignTypedMessageRequest._DataType.ValueType  # 2
        INT: ETHSignTypedMessageRequest._DataType.ValueType  # 3
        BOOL: ETHSignTypedMessageRequest._DataType.ValueType  # 4
        ADDRESS: ETHSignTypedMessageRequest._DataType.ValueType  # 5
        STRING: ETHSignTypedMessageRequest._DataType.ValueType  # 6
        ARRAY: ETHSignTypedMessageRequest._DataType.ValueType  # 7
        STRUCT: ETHSignTypedMessageRequest._DataType.ValueType  # 8
    class DataType(_DataType, metaclass=_DataTypeEnumTypeWrapper):
        pass

    UNKNOWN: ETHSignTypedMessageRequest.DataType.ValueType  # 0
    BYTES: ETHSignTypedMessageRequest.DataType.ValueType  # 1
    UINT: ETHSignTypedMessageRequest.DataType.ValueType  # 2
    INT: ETHSignTypedMessageRequest.DataType.ValueType  # 3
    BOOL: ETHSignTypedMessageRequest.DataType.ValueType  # 4
    ADDRESS: ETHSignTypedMessageRequest.DataType.ValueType  # 5
    STRING: ETHSignTypedMessageRequest.DataType.ValueType  # 6
    ARRAY: ETHSignTypedMessageRequest.DataType.ValueType  # 7
    STRUCT: ETHSignTypedMessageRequest.DataType.ValueType  # 8

    class MemberType(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        TYPE_FIELD_NUMBER: builtins.int
        SIZE_FIELD_NUMBER: builtins.int
        STRUCT_NAME_FIELD_NUMBER: builtins.int
        ARRAY_TYPE_FIELD_NUMBER: builtins.int
        type: global___ETHSignTypedMessageRequest.DataType.ValueType
        size: builtins.int
        struct_name: typing.Text
        """if type==STRUCT, name of struct type."""

        @property
        def array_type(self) -> global___ETHSignTypedMessageRequest.MemberType:
            """if type==ARRAY, type of elements"""
            pass
        def __init__(self,
            *,
            type: global___ETHSignTypedMessageRequest.DataType.ValueType = ...,
            size: builtins.int = ...,
            struct_name: typing.Text = ...,
            array_type: typing.Optional[global___ETHSignTypedMessageRequest.MemberType] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["array_type",b"array_type"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["array_type",b"array_type","size",b"size","struct_name",b"struct_name","type",b"type"]) -> None: ...

    class Member(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        NAME_FIELD_NUMBER: builtins.int
        TYPE_FIELD_NUMBER: builtins.int
        name: typing.Text
        @property
        def type(self) -> global___ETHSignTypedMessageRequest.MemberType: ...
        def __init__(self,
            *,
            name: typing.Text = ...,
            type: typing.Optional[global___ETHSignTypedMessageRequest.MemberType] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["type",b"type"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["name",b"name","type",b"type"]) -> None: ...

    class StructType(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        NAME_FIELD_NUMBER: builtins.int
        MEMBERS_FIELD_NUMBER: builtins.int
        name: typing.Text
        @property
        def members(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ETHSignTypedMessageRequest.Member]: ...
        def __init__(self,
            *,
            name: typing.Text = ...,
            members: typing.Optional[typing.Iterable[global___ETHSignTypedMessageRequest.Member]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["members",b"members","name",b"name"]) -> None: ...

    CHAIN_ID_FIELD_NUMBER: builtins.int
    KEYPATH_FIELD_NUMBER: builtins.int
    TYPES_FIELD_NUMBER: builtins.int
    PRIMARY_TYPE_FIELD_NUMBER: builtins.int
    HOST_NONCE_COMMITMENT_FIELD_NUMBER: builtins.int
    chain_id: builtins.int
    @property
    def keypath(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def types(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ETHSignTypedMessageRequest.StructType]: ...
    primary_type: typing.Text
    @property
    def host_nonce_commitment(self) -> antiklepto_pb2.AntiKleptoHostNonceCommitment: ...
    def __init__(self,
        *,
        chain_id: builtins.int = ...,
        keypath: typing.Optional[typing.Iterable[builtins.int]] = ...,
        types: typing.Optional[typing.Iterable[global___ETHSignTypedMessageRequest.StructType]] = ...,
        primary_type: typing.Text = ...,
        host_nonce_commitment: typing.Optional[antiklepto_pb2.AntiKleptoHostNonceCommitment] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["host_nonce_commitment",b"host_nonce_commitment"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["chain_id",b"chain_id","host_nonce_commitment",b"host_nonce_commitment","keypath",b"keypath","primary_type",b"primary_type","types",b"types"]) -> None: ...
global___ETHSignTypedMessageRequest = ETHSignTypedMessageRequest

class ETHTypedMessageValueResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _RootObject:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _RootObjectEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ETHTypedMessageValueResponse._RootObject.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: ETHTypedMessageValueResponse._RootObject.ValueType  # 0
        DOMAIN: ETHTypedMessageValueResponse._RootObject.ValueType  # 1
        MESSAGE: ETHTypedMessageValueResponse._RootObject.ValueType  # 2
    class RootObject(_RootObject, metaclass=_RootObjectEnumTypeWrapper):
        pass

    UNKNOWN: ETHTypedMessageValueResponse.RootObject.ValueType  # 0
    DOMAIN: ETHTypedMessageValueResponse.RootObject.ValueType  # 1
    MESSAGE: ETHTypedMessageValueResponse.RootObject.ValueType  # 2

    ROOT_OBJECT_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    root_object: global___ETHTypedMessageValueResponse.RootObject.ValueType
    @property
    def path(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(self,
        *,
        root_object: global___ETHTypedMessageValueResponse.RootObject.ValueType = ...,
        path: typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["path",b"path","root_object",b"root_object"]) -> None: ...
global___ETHTypedMessageValueResponse = ETHTypedMessageValueResponse

class ETHTypedMessageValueRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.bytes
    def __init__(self,
        *,
        value: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["value",b"value"]) -> None: ...
global___ETHTypedMessageValueRequest = ETHTypedMessageValueRequest

class ETHRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PUB_FIELD_NUMBER: builtins.int
    SIGN_FIELD_NUMBER: builtins.int
    SIGN_MSG_FIELD_NUMBER: builtins.int
    ANTIKLEPTO_SIGNATURE_FIELD_NUMBER: builtins.int
    SIGN_TYPED_MSG_FIELD_NUMBER: builtins.int
    TYPED_MSG_VALUE_FIELD_NUMBER: builtins.int
    @property
    def pub(self) -> global___ETHPubRequest: ...
    @property
    def sign(self) -> global___ETHSignRequest: ...
    @property
    def sign_msg(self) -> global___ETHSignMessageRequest: ...
    @property
    def antiklepto_signature(self) -> antiklepto_pb2.AntiKleptoSignatureRequest: ...
    @property
    def sign_typed_msg(self) -> global___ETHSignTypedMessageRequest: ...
    @property
    def typed_msg_value(self) -> global___ETHTypedMessageValueRequest: ...
    def __init__(self,
        *,
        pub: typing.Optional[global___ETHPubRequest] = ...,
        sign: typing.Optional[global___ETHSignRequest] = ...,
        sign_msg: typing.Optional[global___ETHSignMessageRequest] = ...,
        antiklepto_signature: typing.Optional[antiklepto_pb2.AntiKleptoSignatureRequest] = ...,
        sign_typed_msg: typing.Optional[global___ETHSignTypedMessageRequest] = ...,
        typed_msg_value: typing.Optional[global___ETHTypedMessageValueRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["antiklepto_signature",b"antiklepto_signature","pub",b"pub","request",b"request","sign",b"sign","sign_msg",b"sign_msg","sign_typed_msg",b"sign_typed_msg","typed_msg_value",b"typed_msg_value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["antiklepto_signature",b"antiklepto_signature","pub",b"pub","request",b"request","sign",b"sign","sign_msg",b"sign_msg","sign_typed_msg",b"sign_typed_msg","typed_msg_value",b"typed_msg_value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["request",b"request"]) -> typing.Optional[typing_extensions.Literal["pub","sign","sign_msg","antiklepto_signature","sign_typed_msg","typed_msg_value"]]: ...
global___ETHRequest = ETHRequest

class ETHResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PUB_FIELD_NUMBER: builtins.int
    SIGN_FIELD_NUMBER: builtins.int
    ANTIKLEPTO_SIGNER_COMMITMENT_FIELD_NUMBER: builtins.int
    TYPED_MSG_VALUE_FIELD_NUMBER: builtins.int
    @property
    def pub(self) -> common_pb2.PubResponse: ...
    @property
    def sign(self) -> global___ETHSignResponse: ...
    @property
    def antiklepto_signer_commitment(self) -> antiklepto_pb2.AntiKleptoSignerCommitment: ...
    @property
    def typed_msg_value(self) -> global___ETHTypedMessageValueResponse: ...
    def __init__(self,
        *,
        pub: typing.Optional[common_pb2.PubResponse] = ...,
        sign: typing.Optional[global___ETHSignResponse] = ...,
        antiklepto_signer_commitment: typing.Optional[antiklepto_pb2.AntiKleptoSignerCommitment] = ...,
        typed_msg_value: typing.Optional[global___ETHTypedMessageValueResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["antiklepto_signer_commitment",b"antiklepto_signer_commitment","pub",b"pub","response",b"response","sign",b"sign","typed_msg_value",b"typed_msg_value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["antiklepto_signer_commitment",b"antiklepto_signer_commitment","pub",b"pub","response",b"response","sign",b"sign","typed_msg_value",b"typed_msg_value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["response",b"response"]) -> typing.Optional[typing_extensions.Literal["pub","sign","antiklepto_signer_commitment","typed_msg_value"]]: ...
global___ETHResponse = ETHResponse
