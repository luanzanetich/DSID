# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: operations.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10operations.proto\x12\x05proto\"\x15\n\x04Long\x12\r\n\x05value\x18\x01 \x01(\x03\"\x93\x01\n\tEightLong\x12\x0f\n\x07value_1\x18\x01 \x01(\x03\x12\x0f\n\x07value_2\x18\x02 \x01(\x03\x12\x0f\n\x07value_3\x18\x03 \x01(\x03\x12\x0f\n\x07value_4\x18\x04 \x01(\x03\x12\x0f\n\x07value_5\x18\x05 \x01(\x03\x12\x0f\n\x07value_6\x18\x06 \x01(\x03\x12\x0f\n\x07value_7\x18\x07 \x01(\x03\x12\x0f\n\x07value_8\x18\x08 \x01(\x03\"\x06\n\x04Void\"\x1e\n\rStringMessage\x12\r\n\x05value\x18\x01 \x01(\t\"\x87\x01\n\x05Movie\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\r\n\x05genre\x18\x03 \x01(\t\x12\x10\n\x08\x64irector\x18\x04 \x01(\t\x12\x1c\n\x06\x61\x63tors\x18\x05 \x03(\x0b\x32\x0c.proto.Actor\x12\x10\n\x08\x64uration\x18\x06 \x01(\x05\x12\x12\n\nfoiEnviado\x18\x07 \x01(\x08\"J\n\x05\x41\x63tor\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07surname\x18\x03 \x01(\t\x12\x16\n\x0e\x63haracter_name\x18\x04 \x03(\t2:\n\x12LongMessageService\x12$\n\x08SendLong\x12\x0b.proto.Long\x1a\x0b.proto.Long2D\n\x17\x45ightLongMessageService\x12)\n\x08SendLong\x12\x10.proto.EightLong\x1a\x0b.proto.Long23\n\x0bVoidMessage\x12$\n\x08SendVoid\x12\x0b.proto.Void\x1a\x0b.proto.Void2R\n\x14StringMessageService\x12:\n\nSendString\x12\x14.proto.StringMessage\x1a\x14.proto.StringMessage\"\x00\x32>\n\x13MovieMessageService\x12\'\n\tSendMovie\x12\x0c.proto.Movie\x1a\x0c.proto.Movieb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'operations_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LONG._serialized_start=27
  _LONG._serialized_end=48
  _EIGHTLONG._serialized_start=51
  _EIGHTLONG._serialized_end=198
  _VOID._serialized_start=200
  _VOID._serialized_end=206
  _STRINGMESSAGE._serialized_start=208
  _STRINGMESSAGE._serialized_end=238
  _MOVIE._serialized_start=241
  _MOVIE._serialized_end=376
  _ACTOR._serialized_start=378
  _ACTOR._serialized_end=452
  _LONGMESSAGESERVICE._serialized_start=454
  _LONGMESSAGESERVICE._serialized_end=512
  _EIGHTLONGMESSAGESERVICE._serialized_start=514
  _EIGHTLONGMESSAGESERVICE._serialized_end=582
  _VOIDMESSAGE._serialized_start=584
  _VOIDMESSAGE._serialized_end=635
  _STRINGMESSAGESERVICE._serialized_start=637
  _STRINGMESSAGESERVICE._serialized_end=719
  _MOVIEMESSAGESERVICE._serialized_start=721
  _MOVIEMESSAGESERVICE._serialized_end=783
# @@protoc_insertion_point(module_scope)
