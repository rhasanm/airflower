# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/protos/strategia.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cnexus/protos/strategia.proto\x12\tstrategia\"\x1f\n\x0f\x44\x65\x63isionRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\" \n\rDecisionReply\x12\x0f\n\x07message\x18\x01 \x01(\t2W\n\x0f\x44\x65\x63isionService\x12\x44\n\x0cMakeDecision\x12\x1a.strategia.DecisionRequest\x1a\x18.strategia.DecisionReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nexus.protos.strategia_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_DECISIONREQUEST']._serialized_start=43
  _globals['_DECISIONREQUEST']._serialized_end=74
  _globals['_DECISIONREPLY']._serialized_start=76
  _globals['_DECISIONREPLY']._serialized_end=108
  _globals['_DECISIONSERVICE']._serialized_start=110
  _globals['_DECISIONSERVICE']._serialized_end=197
# @@protoc_insertion_point(module_scope)
