# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: signal_fx_protocol_buffers.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
# @@protoc_insertion_point(imports)


DESCRIPTOR = _descriptor.FileDescriptor(
    name='signal_fx_protocol_buffers.proto',
    package='com.signalfx.metrics.protobuf',
    serialized_pb='\n signal_fx_protocol_buffers.proto\x12\x1d\x63om.signalfx.metrics.protobuf\"@\n\x05\x44\x61tum\x12\x10\n\x08strValue\x18\x01 \x01(\t\x12\x13\n\x0b\x64oubleValue\x18\x02 \x01(\x01\x12\x10\n\x08intValue\x18\x03 \x01(\x03\"\'\n\tDimension\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xf0\x01\n\tDataPoint\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0e\n\x06metric\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x33\n\x05value\x18\x04 \x01(\x0b\x32$.com.signalfx.metrics.protobuf.Datum\x12=\n\nmetricType\x18\x05 \x01(\x0e\x32).com.signalfx.metrics.protobuf.MetricType\x12<\n\ndimensions\x18\x06 \x03(\x0b\x32(.com.signalfx.metrics.protobuf.Dimension\"V\n\x16\x44\x61taPointUploadMessage\x12<\n\ndatapoints\x18\x01 \x03(\x0b\x32(.com.signalfx.metrics.protobuf.DataPoint\"T\n\nPointValue\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x33\n\x05value\x18\x04 \x01(\x0b\x32$.com.signalfx.metrics.protobuf.Datum\"T\n\x08Property\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b\x32,.com.signalfx.metrics.protobuf.PropertyValue\"[\n\rPropertyValue\x12\x10\n\x08strValue\x18\x01 \x01(\t\x12\x13\n\x0b\x64oubleValue\x18\x02 \x01(\x01\x12\x10\n\x08intValue\x18\x03 \x01(\x03\x12\x11\n\tboolValue\x18\x04 \x01(\x08\"\xe8\x01\n\x05\x45vent\x12\x11\n\teventType\x18\x01 \x02(\t\x12<\n\ndimensions\x18\x02 \x03(\x0b\x32(.com.signalfx.metrics.protobuf.Dimension\x12;\n\nproperties\x18\x03 \x03(\x0b\x32\'.com.signalfx.metrics.protobuf.Property\x12>\n\x08\x63\x61tegory\x18\x04 \x01(\x0e\x32,.com.signalfx.metrics.protobuf.EventCategory\x12\x11\n\ttimestamp\x18\x05 \x01(\x03\"J\n\x12\x45ventUploadMessage\x12\x34\n\x06\x65vents\x18\x01 \x03(\x0b\x32$.com.signalfx.metrics.protobuf.Event*F\n\nMetricType\x12\t\n\x05GAUGE\x10\x00\x12\x0b\n\x07\x43OUNTER\x10\x01\x12\x08\n\x04\x45NUM\x10\x02\x12\x16\n\x12\x43UMULATIVE_COUNTER\x10\x03*\x82\x01\n\rEventCategory\x12\x12\n\x0cUSER_DEFINED\x10\xc0\x84=\x12\x0b\n\x05\x41LERT\x10\xa0\x8d\x06\x12\x0b\n\x05\x41UDIT\x10\xc0\x9a\x0c\x12\t\n\x03JOB\x10\xe0\xa7\x12\x12\x0e\n\x08\x43OLLECTD\x10\x80\xb5\x18\x12\x17\n\x11SERVICE_DISCOVERY\x10\xa0\xc2\x1e\x12\x0f\n\tEXCEPTION\x10\xe0\xdc*')

_METRICTYPE = _descriptor.EnumDescriptor(
    name='MetricType',
    full_name='com.signalfx.metrics.protobuf.MetricType',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='GAUGE', index=0, number=0,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='COUNTER', index=1, number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ENUM', index=2, number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CUMULATIVE_COUNTER', index=3, number=3,
            options=None,
            type=None),
        ],
    containing_type=None,
    options=None,
    serialized_start=1081,
    serialized_end=1151,
)

MetricType = enum_type_wrapper.EnumTypeWrapper(_METRICTYPE)
_EVENTCATEGORY = _descriptor.EnumDescriptor(
    name='EventCategory',
    full_name='com.signalfx.metrics.protobuf.EventCategory',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='USER_DEFINED', index=0, number=1000000,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ALERT', index=1, number=100000,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='AUDIT', index=2, number=200000,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='JOB', index=3, number=300000,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='COLLECTD', index=4, number=400000,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='SERVICE_DISCOVERY', index=5, number=500000,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='EXCEPTION', index=6, number=700000,
            options=None,
            type=None),
        ],
    containing_type=None,
    options=None,
    serialized_start=1154,
    serialized_end=1284,
)

EventCategory = enum_type_wrapper.EnumTypeWrapper(_EVENTCATEGORY)
GAUGE = 0
COUNTER = 1
ENUM = 2
CUMULATIVE_COUNTER = 3
USER_DEFINED = 1000000
ALERT = 100000
AUDIT = 200000
JOB = 300000
COLLECTD = 400000
SERVICE_DISCOVERY = 500000
EXCEPTION = 700000


_DATUM = _descriptor.Descriptor(
    name='Datum',
    full_name='com.signalfx.metrics.protobuf.Datum',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='strValue', full_name='com.signalfx.metrics.protobuf.Datum.strValue', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=str("", "utf-8"),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='doubleValue', full_name='com.signalfx.metrics.protobuf.Datum.doubleValue', index=1,
            number=2, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='intValue', full_name='com.signalfx.metrics.protobuf.Datum.intValue', index=2,
            number=3, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        ],
    extensions=[
        ],
    nested_types=[],
    enum_types=[
        ],
    options=None,
    is_extendable=False,
    extension_ranges=[],
    serialized_start=67,
    serialized_end=131,
)


_DIMENSION = _descriptor.Descriptor(
    name='Dimension',
    full_name='com.signalfx.metrics.protobuf.Dimension',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='com.signalfx.metrics.protobuf.Dimension.key', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=str("", "utf-8"),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='value', full_name='com.signalfx.metrics.protobuf.Dimension.value', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=str("", "utf-8"),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        ],
    extensions=[
        ],
    nested_types=[],
    enum_types=[
        ],
    options=None,
    is_extendable=False,
    extension_ranges=[],
    serialized_start=133,
    serialized_end=172,
)


_DATAPOINT = _descriptor.Descriptor(
    name='DataPoint',
    full_name='com.signalfx.metrics.protobuf.DataPoint',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='source', full_name='com.signalfx.metrics.protobuf.DataPoint.source', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=str("", "utf-8"),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='metric', full_name='com.signalfx.metrics.protobuf.DataPoint.metric', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=str("", "utf-8"),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='timestamp', full_name='com.signalfx.metrics.protobuf.DataPoint.timestamp', index=2,
            number=3, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='value', full_name='com.signalfx.metrics.protobuf.DataPoint.value', index=3,
            number=4, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='metricType', full_name='com.signalfx.metrics.protobuf.DataPoint.metricType', index=4,
            number=5, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='dimensions', full_name='com.signalfx.metrics.protobuf.DataPoint.dimensions', index=5,
            number=6, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        ],
    extensions=[
        ],
    nested_types=[],
    enum_types=[
        ],
    options=None,
    is_extendable=False,
    extension_ranges=[],
    serialized_start=175,
    serialized_end=415,
)


_DATAPOINTUPLOADMESSAGE = _descriptor.Descriptor(
    name='DataPointUploadMessage',
    full_name='com.signalfx.metrics.protobuf.DataPointUploadMessage',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='datapoints', full_name='com.signalfx.metrics.protobuf.DataPointUploadMessage.datapoints', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        ],
    extensions=[
        ],
    nested_types=[],
    enum_types=[
        ],
    options=None,
    is_extendable=False,
    extension_ranges=[],
    serialized_start=417,
    serialized_end=503,
)


_POINTVALUE = _descriptor.Descriptor(
    name='PointValue',
    full_name='com.signalfx.metrics.protobuf.PointValue',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='timestamp', full_name='com.signalfx.metrics.protobuf.PointValue.timestamp', index=0,
            number=3, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='value', full_name='com.signalfx.metrics.protobuf.PointValue.value', index=1,
            number=4, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        ],
    extensions=[
        ],
    nested_types=[],
    enum_types=[
        ],
    options=None,
    is_extendable=False,
    extension_ranges=[],
    serialized_start=505,
    serialized_end=589,
)


_PROPERTY = _descriptor.Descriptor(
    name='Property',
    full_name='com.signalfx.metrics.protobuf.Property',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='com.signalfx.metrics.protobuf.Property.key', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=str("", "utf-8"),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='value', full_name='com.signalfx.metrics.protobuf.Property.value', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        ],
    extensions=[
        ],
    nested_types=[],
    enum_types=[
        ],
    options=None,
    is_extendable=False,
    extension_ranges=[],
    serialized_start=591,
    serialized_end=675,
)


_PROPERTYVALUE = _descriptor.Descriptor(
    name='PropertyValue',
    full_name='com.signalfx.metrics.protobuf.PropertyValue',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='strValue', full_name='com.signalfx.metrics.protobuf.PropertyValue.strValue', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=str("", "utf-8"),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='doubleValue', full_name='com.signalfx.metrics.protobuf.PropertyValue.doubleValue', index=1,
            number=2, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='intValue', full_name='com.signalfx.metrics.protobuf.PropertyValue.intValue', index=2,
            number=3, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='boolValue', full_name='com.signalfx.metrics.protobuf.PropertyValue.boolValue', index=3,
            number=4, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        ],
    extensions=[
        ],
    nested_types=[],
    enum_types=[
        ],
    options=None,
    is_extendable=False,
    extension_ranges=[],
    serialized_start=677,
    serialized_end=768,
)


_EVENT = _descriptor.Descriptor(
    name='Event',
    full_name='com.signalfx.metrics.protobuf.Event',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='eventType', full_name='com.signalfx.metrics.protobuf.Event.eventType', index=0,
            number=1, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=str("", "utf-8"),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='dimensions', full_name='com.signalfx.metrics.protobuf.Event.dimensions', index=1,
            number=2, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='properties', full_name='com.signalfx.metrics.protobuf.Event.properties', index=2,
            number=3, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='category', full_name='com.signalfx.metrics.protobuf.Event.category', index=3,
            number=4, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=1000000,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='timestamp', full_name='com.signalfx.metrics.protobuf.Event.timestamp', index=4,
            number=5, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        ],
    extensions=[
        ],
    nested_types=[],
    enum_types=[
        ],
    options=None,
    is_extendable=False,
    extension_ranges=[],
    serialized_start=771,
    serialized_end=1003,
)


_EVENTUPLOADMESSAGE = _descriptor.Descriptor(
    name='EventUploadMessage',
    full_name='com.signalfx.metrics.protobuf.EventUploadMessage',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='events', full_name='com.signalfx.metrics.protobuf.EventUploadMessage.events', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        ],
    extensions=[
        ],
    nested_types=[],
    enum_types=[
        ],
    options=None,
    is_extendable=False,
    extension_ranges=[],
    serialized_start=1005,
    serialized_end=1079,
)

_DATAPOINT.fields_by_name['value'].message_type = _DATUM
_DATAPOINT.fields_by_name['metricType'].enum_type = _METRICTYPE
_DATAPOINT.fields_by_name['dimensions'].message_type = _DIMENSION
_DATAPOINTUPLOADMESSAGE.fields_by_name['datapoints'].message_type = _DATAPOINT
_POINTVALUE.fields_by_name['value'].message_type = _DATUM
_PROPERTY.fields_by_name['value'].message_type = _PROPERTYVALUE
_EVENT.fields_by_name['dimensions'].message_type = _DIMENSION
_EVENT.fields_by_name['properties'].message_type = _PROPERTY
_EVENT.fields_by_name['category'].enum_type = _EVENTCATEGORY
_EVENTUPLOADMESSAGE.fields_by_name['events'].message_type = _EVENT
DESCRIPTOR.message_types_by_name['Datum'] = _DATUM
DESCRIPTOR.message_types_by_name['Dimension'] = _DIMENSION
DESCRIPTOR.message_types_by_name['DataPoint'] = _DATAPOINT
DESCRIPTOR.message_types_by_name[
    'DataPointUploadMessage'] = _DATAPOINTUPLOADMESSAGE
DESCRIPTOR.message_types_by_name['PointValue'] = _POINTVALUE
DESCRIPTOR.message_types_by_name['Property'] = _PROPERTY
DESCRIPTOR.message_types_by_name['PropertyValue'] = _PROPERTYVALUE
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['EventUploadMessage'] = _EVENTUPLOADMESSAGE


class Datum(_message.Message, metaclass=_reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _DATUM

    # @@protoc_insertion_point(class_scope:com.signalfx.metrics.protobuf.Datum)


class Dimension(_message.Message, metaclass=_reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _DIMENSION

    # @@protoc_insertion_point(class_scope:com.signalfx.metrics.protobuf.Dimension)


class DataPoint(_message.Message, metaclass=_reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _DATAPOINT

    # @@protoc_insertion_point(class_scope:com.signalfx.metrics.protobuf.DataPoint)


class DataPointUploadMessage(_message.Message, metaclass=_reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _DATAPOINTUPLOADMESSAGE

    # @@protoc_insertion_point(class_scope:com.signalfx.metrics.protobuf.DataPointUploadMessage)


class PointValue(_message.Message, metaclass=_reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _POINTVALUE

    # @@protoc_insertion_point(class_scope:com.signalfx.metrics.protobuf.PointValue)


class Property(_message.Message, metaclass=_reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PROPERTY

    # @@protoc_insertion_point(class_scope:com.signalfx.metrics.protobuf.Property)


class PropertyValue(_message.Message, metaclass=_reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PROPERTYVALUE

    # @@protoc_insertion_point(class_scope:com.signalfx.metrics.protobuf.PropertyValue)


class Event(_message.Message, metaclass=_reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _EVENT

    # @@protoc_insertion_point(class_scope:com.signalfx.metrics.protobuf.Event)


class EventUploadMessage(_message.Message, metaclass=_reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _EVENTUPLOADMESSAGE

    # @@protoc_insertion_point(class_scope:com.signalfx.metrics.protobuf.EventUploadMessage)


# @@protoc_insertion_point(module_scope)
