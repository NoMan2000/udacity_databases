# Stubs for yaml.events (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class Event:
    start_mark = ...  # type: Any
    end_mark = ...  # type: Any
    def __init__(self, start_mark=..., end_mark=...) -> None: ...

class NodeEvent(Event):
    anchor = ...  # type: Any
    start_mark = ...  # type: Any
    end_mark = ...  # type: Any
    def __init__(self, anchor, start_mark=..., end_mark=...) -> None: ...

class CollectionStartEvent(NodeEvent):
    anchor = ...  # type: Any
    tag = ...  # type: Any
    implicit = ...  # type: Any
    start_mark = ...  # type: Any
    end_mark = ...  # type: Any
    flow_style = ...  # type: Any
    def __init__(self, anchor, tag, implicit, start_mark=..., end_mark=..., flow_style=...) -> None: ...

class CollectionEndEvent(Event): ...

class StreamStartEvent(Event):
    start_mark = ...  # type: Any
    end_mark = ...  # type: Any
    encoding = ...  # type: Any
    def __init__(self, start_mark=..., end_mark=..., encoding=...) -> None: ...

class StreamEndEvent(Event): ...

class DocumentStartEvent(Event):
    start_mark = ...  # type: Any
    end_mark = ...  # type: Any
    explicit = ...  # type: Any
    version = ...  # type: Any
    tags = ...  # type: Any
    def __init__(self, start_mark=..., end_mark=..., explicit=..., version=..., tags=...) -> None: ...

class DocumentEndEvent(Event):
    start_mark = ...  # type: Any
    end_mark = ...  # type: Any
    explicit = ...  # type: Any
    def __init__(self, start_mark=..., end_mark=..., explicit=...) -> None: ...

class AliasEvent(NodeEvent): ...

class ScalarEvent(NodeEvent):
    anchor = ...  # type: Any
    tag = ...  # type: Any
    implicit = ...  # type: Any
    value = ...  # type: Any
    start_mark = ...  # type: Any
    end_mark = ...  # type: Any
    style = ...  # type: Any
    def __init__(self, anchor, tag, implicit, value, start_mark=..., end_mark=..., style=...) -> None: ...

class SequenceStartEvent(CollectionStartEvent): ...
class SequenceEndEvent(CollectionEndEvent): ...
class MappingStartEvent(CollectionStartEvent): ...
class MappingEndEvent(CollectionEndEvent): ...
