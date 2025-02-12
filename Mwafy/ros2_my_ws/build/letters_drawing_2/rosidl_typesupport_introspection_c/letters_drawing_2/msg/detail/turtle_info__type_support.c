// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from letters_drawing_2:msg/TurtleInfo.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "letters_drawing_2/msg/detail/turtle_info__rosidl_typesupport_introspection_c.h"
#include "letters_drawing_2/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "letters_drawing_2/msg/detail/turtle_info__functions.h"
#include "letters_drawing_2/msg/detail/turtle_info__struct.h"


// Include directives for member types
// Member `turtle_name`
// Member `letter`
#include "rosidl_runtime_c/string_functions.h"
// Member `target_coords`
#include "geometry_msgs/msg/point.h"
// Member `target_coords`
#include "geometry_msgs/msg/detail/point__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void letters_drawing_2__msg__TurtleInfo__rosidl_typesupport_introspection_c__TurtleInfo_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  letters_drawing_2__msg__TurtleInfo__init(message_memory);
}

void letters_drawing_2__msg__TurtleInfo__rosidl_typesupport_introspection_c__TurtleInfo_fini_function(void * message_memory)
{
  letters_drawing_2__msg__TurtleInfo__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember letters_drawing_2__msg__TurtleInfo__rosidl_typesupport_introspection_c__TurtleInfo_message_member_array[3] = {
  {
    "turtle_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(letters_drawing_2__msg__TurtleInfo, turtle_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "target_coords",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(letters_drawing_2__msg__TurtleInfo, target_coords),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "letter",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(letters_drawing_2__msg__TurtleInfo, letter),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers letters_drawing_2__msg__TurtleInfo__rosidl_typesupport_introspection_c__TurtleInfo_message_members = {
  "letters_drawing_2__msg",  // message namespace
  "TurtleInfo",  // message name
  3,  // number of fields
  sizeof(letters_drawing_2__msg__TurtleInfo),
  letters_drawing_2__msg__TurtleInfo__rosidl_typesupport_introspection_c__TurtleInfo_message_member_array,  // message members
  letters_drawing_2__msg__TurtleInfo__rosidl_typesupport_introspection_c__TurtleInfo_init_function,  // function to initialize message memory (memory has to be allocated)
  letters_drawing_2__msg__TurtleInfo__rosidl_typesupport_introspection_c__TurtleInfo_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t letters_drawing_2__msg__TurtleInfo__rosidl_typesupport_introspection_c__TurtleInfo_message_type_support_handle = {
  0,
  &letters_drawing_2__msg__TurtleInfo__rosidl_typesupport_introspection_c__TurtleInfo_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_letters_drawing_2
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, letters_drawing_2, msg, TurtleInfo)() {
  letters_drawing_2__msg__TurtleInfo__rosidl_typesupport_introspection_c__TurtleInfo_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Point)();
  if (!letters_drawing_2__msg__TurtleInfo__rosidl_typesupport_introspection_c__TurtleInfo_message_type_support_handle.typesupport_identifier) {
    letters_drawing_2__msg__TurtleInfo__rosidl_typesupport_introspection_c__TurtleInfo_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &letters_drawing_2__msg__TurtleInfo__rosidl_typesupport_introspection_c__TurtleInfo_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
