# generated from rosidl_generator_py/resource/_idl.py.em
# with input from letters_drawing_2:msg/TurtleInfo.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_TurtleInfo(type):
    """Metaclass of message 'TurtleInfo'."""

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
            module = import_type_support('letters_drawing_2')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'letters_drawing_2.msg.TurtleInfo')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__turtle_info
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__turtle_info
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__turtle_info
            cls._TYPE_SUPPORT = module.type_support_msg__msg__turtle_info
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__turtle_info

            from geometry_msgs.msg import Point
            if Point.__class__._TYPE_SUPPORT is None:
                Point.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TurtleInfo(metaclass=Metaclass_TurtleInfo):
    """Message class 'TurtleInfo'."""

    __slots__ = [
        '_turtle_name',
        '_target_coords',
        '_letter',
    ]

    _fields_and_field_types = {
        'turtle_name': 'string',
        'target_coords': 'geometry_msgs/Point',
        'letter': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.turtle_name = kwargs.get('turtle_name', str())
        from geometry_msgs.msg import Point
        self.target_coords = kwargs.get('target_coords', Point())
        self.letter = kwargs.get('letter', str())

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
        if self.turtle_name != other.turtle_name:
            return False
        if self.target_coords != other.target_coords:
            return False
        if self.letter != other.letter:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def turtle_name(self):
        """Message field 'turtle_name'."""
        return self._turtle_name

    @turtle_name.setter
    def turtle_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'turtle_name' field must be of type 'str'"
        self._turtle_name = value

    @builtins.property
    def target_coords(self):
        """Message field 'target_coords'."""
        return self._target_coords

    @target_coords.setter
    def target_coords(self, value):
        if __debug__:
            from geometry_msgs.msg import Point
            assert \
                isinstance(value, Point), \
                "The 'target_coords' field must be a sub message of type 'Point'"
        self._target_coords = value

    @builtins.property
    def letter(self):
        """Message field 'letter'."""
        return self._letter

    @letter.setter
    def letter(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'letter' field must be of type 'str'"
        self._letter = value
