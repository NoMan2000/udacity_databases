# Stubs for xmlrpclib (Python 2)

from typing import Any, AnyStr, Callable, IO, Iterable, List, Mapping, MutableMapping, Optional, Tuple, Type, TypeVar, Union
from types import InstanceType
from datetime import datetime
from time import struct_time
from httplib import HTTPConnection, HTTPResponse, HTTPSConnection
from ssl import SSLContext
from StringIO import StringIO
from gzip import GzipFile

_Unmarshaller = Any
_timeTuple = Tuple[int, int, int, int, int, int, int, int, int]
# Represents types that can be compared against a DateTime object
_dateTimeComp = Union[AnyStr, DateTime, datetime, _timeTuple]
# A "host description" used by Transport factories
_hostDesc = Union[str, Tuple[str, Mapping[Any, Any]]]

def escape(s: AnyStr, replace: Callable[[AnyStr, AnyStr, AnyStr], AnyStr] = ...) -> AnyStr: ...

MAXINT = ...  # type: int
MININT = ...  # type: int
PARSE_ERROR = ...  # type: int
SERVER_ERROR = ...  # type: int
APPLICATION_ERROR = ...  # type: int
SYSTEM_ERROR = ...  # type: int
TRANSPORT_ERROR = ...  # type: int
NOT_WELLFORMED_ERROR = ...  # type: int
UNSUPPORTED_ENCODING = ...  # type: int
INVALID_ENCODING_CHAR = ...  # type: int
INVALID_XMLRPC = ...  # type: int
METHOD_NOT_FOUND = ...  # type: int
INVALID_METHOD_PARAMS = ...  # type: int
INTERNAL_ERROR = ...  # type: int

class Error(Exception): ...

class ProtocolError(Error):
    url = ...  # type: str
    errcode = ...  # type: int
    errmsg = ...  # type: str
    headers = ...  # type: Any
    def __init__(self, url: str, errcode: int, errmsg: str, headers: Any) -> None: ...

class ResponseError(Error): ...

class Fault(Error):
    faultCode = ...  # type: Any
    faultString = ...  # type: str
    def __init__(self, faultCode: Any, faultString: str, **extra: Any) -> None: ...

boolean = ...  # type: Type[bool]
Boolean = ...  # type: Type[bool]

class DateTime:
    value = ...  # type: str
    def __init__(self, value: Union[str, unicode, datetime, float, int, _timeTuple, struct_time] = ...) -> None: ...
    def make_comparable(self, other: _dateTimeComp) -> Tuple[_dateTimeComp, _dateTimeComp]: ...
    def __lt__(self, other: _dateTimeComp) -> bool: ...
    def __le__(self, other: _dateTimeComp) -> bool: ...
    def __gt__(self, other: _dateTimeComp) -> bool: ...
    def __ge__(self, other: _dateTimeComp) -> bool: ...
    def __eq__(self, other: _dateTimeComp) -> bool: ...
    def __ne__(self, other: _dateTimeComp) -> bool: ...
    def timetuple(self) -> struct_time: ...
    def __cmp__(self, other: _dateTimeComp) -> int: ...
    def decode(self, data: Any) -> None: ...
    def encode(self, out: IO) -> None: ...

class Binary:
    data = ...  # type: str
    def __init__(self, data: Optional[str] = ...) -> None: ...
    def __cmp__(self, other: Any) -> int: ...
    def decode(self, data: str) -> None: ...
    def encode(self, out: IO) -> None: ...

WRAPPERS = ...  # type: tuple

# Still part of the public API, but see http://bugs.python.org/issue1773632
FastParser = ...  # type: None
FastUnmarshaller = ...  # type: None
FastMarshaller = ...  # type: None

# xmlrpclib.py will leave ExpatParser undefined if it can't import expat from
# xml.parsers. Because this is Python 2.7, the import will succeed.
class ExpatParser:
    def __init__(self, target: _Unmarshaller) -> None: ...
    def feed(self, data: str): ...
    def close(self): ...

# TODO: Add xmllib.XMLParser as base class
class SlowParser:
    handle_xml = ...  # type: Callable[[str, bool], None]
    unknown_starttag = ...  # type: Callable[[str, Any], None]
    handle_data = ...  # type: Callable[[str], None]
    handle_cdata = ...  # type: Callable[[str], None]
    unknown_endtag = ...  # type: Callable[[str, Callable[[Iterable[str], str], str]], None]
    def __init__(self, target: _Unmarshaller) -> None: ...

class Marshaller:
    memo = ...  # type: MutableMapping[int, Any]
    data = ...  # type: Optional[str]
    encoding = ...  # type: Optional[str]
    allow_none = ...  # type: bool
    def __init__(self, encoding: Optional[str] = ..., allow_none: bool = ...) -> None: ...
    dispatch = ...  # type: Mapping[type, Callable[[Marshaller, str, Callable[[str], None]], None]]
    def dumps(self, values: Union[Iterable[Union[None, int, bool, long, float, str, unicode, List, Tuple, Mapping, datetime, InstanceType]], Fault]) -> str: ...
    def dump_nil(self, value: None, write: Callable[[str], None]) -> None: ...
    def dump_int(self, value: int, write: Callable[[str], None]) -> None: ...
    def dump_bool(self, value: bool, write: Callable[[str], None]) -> None: ...
    def dump_long(self, value: long, write: Callable[[str], None]) -> None: ...
    def dump_double(self, value: float, write: Callable[[str], None]) -> None: ...
    def dump_string(self, value: str, write: Callable[[str], None], escape: Callable[[AnyStr, Callable[[AnyStr, AnyStr, AnyStr], AnyStr]], AnyStr] = ...) -> None: ...
    def dump_unicode(self, value: unicode, write: Callable[[str], None], escape: Callable[[AnyStr, Callable[[AnyStr, AnyStr, AnyStr], AnyStr]], AnyStr] = ...) -> None: ...
    def dump_array(self, value: Union[List, Tuple], write: Callable[[str], None]) -> None: ...
    def dump_struct(self, value: Mapping, write: Callable[[str], None], escape: Callable[[AnyStr, Callable[[AnyStr, AnyStr, AnyStr], AnyStr]], AnyStr] = ...) -> None: ...
    def dump_datetime(self, value: datetime, write: Callable[[str], None]) -> None: ...
    def dump_instance(self, value: InstanceType, write: Callable[[str], None]) -> None: ...

class Unmarshaller:
    def append(self, object: Any) -> None: ...
    def __init__(self, use_datetime: bool = ...) -> None: ...
    def close(self) -> tuple: ...
    def getmethodname(self) -> Optional[str]: ...
    def xml(self, encoding: str, standalone: bool) -> None: ...
    def start(self, tag: str, attrs: Any) -> None: ...
    def data(self, text: str) -> None: ...
    def end(self, tag: str, join: Callable[[Iterable[str], str], str] = ...) -> None: ...
    def end_dispatch(self, tag: str, data: str) -> None: ...
    dispatch = ...  # type: Mapping[str, Callable[[Unmarshaller, str], None]]
    def end_nil(self, data: str): ...
    def end_boolean(self, data: str) -> None: ...
    def end_int(self, data: str) -> None: ...
    def end_double(self, data: str) -> None: ...
    def end_string(self, data: str) -> None: ...
    def end_array(self, data: str) -> None: ...
    def end_struct(self, data: str) -> None: ...
    def end_base64(self, data: str) -> None: ...
    def end_dateTime(self, data: str) -> None: ...
    def end_value(self, data: str) -> None: ...
    def end_params(self, data: str) -> None: ...
    def end_fault(self, data: str) -> None: ...
    def end_methodName(self, data: str) -> None: ...

class _MultiCallMethod:
    def __init__(self, call_list: List[Tuple[str, tuple]], name: str) -> None: ...
class MultiCallIterator:
    def __init__(self, results: List) -> None: ...

class MultiCall:
    def __init__(self, server: ServerProxy) -> None: ...
    def __getattr__(self, name: str) -> _MultiCallMethod: ...
    def __call__(self) -> MultiCallIterator: ...

def getparser(use_datetime: bool = ...) -> Tuple[Union[ExpatParser, SlowParser], Unmarshaller]: ...
def dumps(params: Union[tuple, Fault], methodname: Optional[str] = ..., methodresponse: Optional[bool] = ..., encoding: Optional[str] = ..., allow_none: bool = ...) -> str: ...
def loads(data: str, use_datetime: bool = ...) -> Tuple[tuple, Optional[str]]: ...

def gzip_encode(data: str) -> str: ...
def gzip_decode(data: str, max_decode: int = ...) -> str: ...

class GzipDecodedResponse(GzipFile):
    stringio = ...  # type: StringIO
    def __init__(self, response: HTTPResponse) -> None: ...
    def close(self): ...

class _Method:
    def __init__(self, send: Callable[[str, tuple], Any], name: str) -> None: ...
    def __getattr__(self, name: str) -> _Method: ...
    def __call__(self, *args: Any) -> Any: ...

class Transport:
    user_agent = ...  # type: str
    accept_gzip_encoding = ...  # type: bool
    encode_threshold = ...  # type: Optional[int]
    def __init__(self, use_datetime: bool = ...) -> None: ...
    def request(self, host: _hostDesc, handler: str, request_body: str, verbose: bool = ...) -> tuple: ...
    verbose = ...  # type: bool
    def single_request(self, host: _hostDesc, handler: str, request_body: str, verbose: bool = ...) -> tuple: ...
    def getparser(self) -> Tuple[Union[ExpatParser, SlowParser], Unmarshaller]: ...
    def get_host_info(self, host: _hostDesc) -> Tuple[str, Optional[List[Tuple[str, str]]], Optional[Mapping[Any, Any]]]: ...
    def make_connection(self, host: _hostDesc) -> HTTPConnection: ...
    def close(self) -> None: ...
    def send_request(self, connection: HTTPConnection, handler: str, request_body: str) -> None: ...
    def send_host(self, connection: HTTPConnection, host: str) -> None: ...
    def send_user_agent(self, connection: HTTPConnection) -> None: ...
    def send_content(self, connection: HTTPConnection, request_body: str) -> None: ...
    def parse_response(self, response: HTTPResponse) -> tuple: ...

class SafeTransport(Transport):
    def __init__(self, use_datetime: bool = ..., context: Optional[SSLContext] = ...) -> None: ...
    def make_connection(self, host: _hostDesc) -> HTTPSConnection: ...

class ServerProxy:
    def __init__(self, uri: str, transport: Optional[Transport] = ..., encoding: Optional[str] = ..., verbose: bool = ..., allow_none: bool = ..., use_datetime: bool = ..., context: Optional[SSLContext] = ...) -> None: ...
    def __getattr__(self, name: str) -> _Method: ...
    def __call__(self, attr: str) -> Optional[Transport]: ...

Server = ServerProxy
