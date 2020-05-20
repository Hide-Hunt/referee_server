# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/CatchEvent.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/CatchEvent.proto',
  package='ch.epfl.sdp.game.comm',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x16proto/CatchEvent.proto\x12\x15\x63h.epfl.sdp.game.comm\"0\n\nCatchEvent\x12\x12\n\npredatorID\x18\x01 \x01(\x05\x12\x0e\n\x06preyID\x18\x02 \x01(\x05\x62\x06proto3'
)




_CATCHEVENT = _descriptor.Descriptor(
  name='CatchEvent',
  full_name='ch.epfl.sdp.game.comm.CatchEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='predatorID', full_name='ch.epfl.sdp.game.comm.CatchEvent.predatorID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preyID', full_name='ch.epfl.sdp.game.comm.CatchEvent.preyID', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=49,
  serialized_end=97,
)

DESCRIPTOR.message_types_by_name['CatchEvent'] = _CATCHEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CatchEvent = _reflection.GeneratedProtocolMessageType('CatchEvent', (_message.Message,), {
  'DESCRIPTOR' : _CATCHEVENT,
  '__module__' : 'proto.CatchEvent_pb2'
  # @@protoc_insertion_point(class_scope:ch.epfl.sdp.game.comm.CatchEvent)
  })
_sym_db.RegisterMessage(CatchEvent)


# @@protoc_insertion_point(module_scope)
