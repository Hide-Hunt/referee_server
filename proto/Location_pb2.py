# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/Location.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/Location.proto',
  package='ch.epfl.sdp.game.comm',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x14proto/Location.proto\x12\x15\x63h.epfl.sdp.game.comm\"/\n\x08Location\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x62\x06proto3'
)




_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='ch.epfl.sdp.game.comm.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='ch.epfl.sdp.game.comm.Location.latitude', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='ch.epfl.sdp.game.comm.Location.longitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'proto.Location_pb2'
  # @@protoc_insertion_point(class_scope:ch.epfl.sdp.game.comm.Location)
  })
_sym_db.RegisterMessage(Location)


# @@protoc_insertion_point(module_scope)
