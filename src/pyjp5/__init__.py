"""JSON5 parser and serializer for Python."""

from .core import JsonValue, JSON5DecodeError, JSON5EncodeError
from .decoder import Json5Decoder, load, loads
from .encoder import JSON5Encoder, dump, dumps

__all__ = [
    "JsonValue",
    "JSON5DecodeError",
    "JSON5EncodeError",
    "Json5Decoder",
    "load",
    "loads",
    "JSON5Encoder",
    "dumps",
    "dump",
]
