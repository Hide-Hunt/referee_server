# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/Game.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto import GameEvent_pb2 as proto_dot_GameEvent__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/Game.proto',
  package='ch.epfl.sdp.game.comm',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10proto/Game.proto\x12\x15\x63h.epfl.sdp.game.comm\x1a\x15proto/GameEvent.proto\"\xc3\x01\n\x04Game\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64minID\x18\x03 \x01(\t\x12\x17\n\x0fstart_timestamp\x18\x04 \x01(\x07\x12\x15\n\rend_timestamp\x18\x05 \x01(\x07\x12.\n\x07players\x18\n \x03(\x0b\x32\x1d.ch.epfl.sdp.game.comm.Player\x12\x30\n\x06\x65vents\x18\x0b \x03(\x0b\x32 .ch.epfl.sdp.game.comm.GameEvent\"E\n\x06Player\x12\n\n\x02id\x18\x01 \x01(\x05\x12/\n\x07\x66\x61\x63tion\x18\x02 \x01(\x0e\x32\x1e.ch.epfl.sdp.game.comm.Faction*!\n\x07\x46\x61\x63tion\x12\x08\n\x04PREY\x10\x00\x12\x0c\n\x08PREDATOR\x10\x01\x62\x06proto3'
  ,
  dependencies=[proto_dot_GameEvent__pb2.DESCRIPTOR,])

_FACTION = _descriptor.EnumDescriptor(
  name='Faction',
  full_name='ch.epfl.sdp.game.comm.Faction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PREY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREDATOR', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=335,
  serialized_end=368,
)
_sym_db.RegisterEnumDescriptor(_FACTION)

Faction = enum_type_wrapper.EnumTypeWrapper(_FACTION)
PREY = 0
PREDATOR = 1



_GAME = _descriptor.Descriptor(
  name='Game',
  full_name='ch.epfl.sdp.game.comm.Game',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ch.epfl.sdp.game.comm.Game.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ch.epfl.sdp.game.comm.Game.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adminID', full_name='ch.epfl.sdp.game.comm.Game.adminID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='ch.epfl.sdp.game.comm.Game.start_timestamp', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_timestamp', full_name='ch.epfl.sdp.game.comm.Game.end_timestamp', index=4,
      number=5, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='players', full_name='ch.epfl.sdp.game.comm.Game.players', index=5,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events', full_name='ch.epfl.sdp.game.comm.Game.events', index=6,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=67,
  serialized_end=262,
)


_PLAYER = _descriptor.Descriptor(
  name='Player',
  full_name='ch.epfl.sdp.game.comm.Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ch.epfl.sdp.game.comm.Player.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='faction', full_name='ch.epfl.sdp.game.comm.Player.faction', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=264,
  serialized_end=333,
)

_GAME.fields_by_name['players'].message_type = _PLAYER
_GAME.fields_by_name['events'].message_type = proto_dot_GameEvent__pb2._GAMEEVENT
_PLAYER.fields_by_name['faction'].enum_type = _FACTION
DESCRIPTOR.message_types_by_name['Game'] = _GAME
DESCRIPTOR.message_types_by_name['Player'] = _PLAYER
DESCRIPTOR.enum_types_by_name['Faction'] = _FACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Game = _reflection.GeneratedProtocolMessageType('Game', (_message.Message,), {
  'DESCRIPTOR' : _GAME,
  '__module__' : 'proto.Game_pb2'
  # @@protoc_insertion_point(class_scope:ch.epfl.sdp.game.comm.Game)
  })
_sym_db.RegisterMessage(Game)

Player = _reflection.GeneratedProtocolMessageType('Player', (_message.Message,), {
  'DESCRIPTOR' : _PLAYER,
  '__module__' : 'proto.Game_pb2'
  # @@protoc_insertion_point(class_scope:ch.epfl.sdp.game.comm.Player)
  })
_sym_db.RegisterMessage(Player)


# @@protoc_insertion_point(module_scope)
