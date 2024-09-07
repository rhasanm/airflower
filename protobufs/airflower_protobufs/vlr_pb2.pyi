from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VLRThresholdRequest(_message.Message):
    __slots__ = ("strategy",)
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    strategy: str
    def __init__(self, strategy: _Optional[str] = ...) -> None: ...

class VLRThresholdResponse(_message.Message):
    __slots__ = ("threshold",)
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    threshold: int
    def __init__(self, threshold: _Optional[int] = ...) -> None: ...
