# generated from rosidl_generator_py/resource/_idl.py.em
# with input from roboy_info_system_msg:msg/RobotAlert.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RobotAlert(type):
    """Metaclass of message 'RobotAlert'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('roboy_info_system_msg')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'roboy_info_system_msg.msg.RobotAlert')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__robot_alert
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__robot_alert
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__robot_alert
            cls._TYPE_SUPPORT = module.type_support_msg__msg__robot_alert
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__robot_alert

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RobotAlert(metaclass=Metaclass_RobotAlert):
    """Message class 'RobotAlert'."""

    __slots__ = [
        '_alert_level',
        '_alert_message',
    ]

    _fields_and_field_types = {
        'alert_level': 'int32',
        'alert_message': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.alert_level = kwargs.get('alert_level', int())
        self.alert_message = kwargs.get('alert_message', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.alert_level != other.alert_level:
            return False
        if self.alert_message != other.alert_message:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def alert_level(self):
        """Message field 'alert_level'."""
        return self._alert_level

    @alert_level.setter
    def alert_level(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'alert_level' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'alert_level' field must be an integer in [-2147483648, 2147483647]"
        self._alert_level = value

    @builtins.property
    def alert_message(self):
        """Message field 'alert_message'."""
        return self._alert_message

    @alert_message.setter
    def alert_message(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'alert_message' field must be of type 'str'"
        self._alert_message = value
