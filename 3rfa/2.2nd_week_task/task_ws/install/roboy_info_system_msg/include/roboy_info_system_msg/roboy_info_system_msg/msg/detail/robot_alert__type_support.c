// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from roboy_info_system_msg:msg/RobotAlert.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "roboy_info_system_msg/msg/detail/robot_alert__rosidl_typesupport_introspection_c.h"
#include "roboy_info_system_msg/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "roboy_info_system_msg/msg/detail/robot_alert__functions.h"
#include "roboy_info_system_msg/msg/detail/robot_alert__struct.h"


// Include directives for member types
// Member `alert_message`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void roboy_info_system_msg__msg__RobotAlert__rosidl_typesupport_introspection_c__RobotAlert_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  roboy_info_system_msg__msg__RobotAlert__init(message_memory);
}

void roboy_info_system_msg__msg__RobotAlert__rosidl_typesupport_introspection_c__RobotAlert_fini_function(void * message_memory)
{
  roboy_info_system_msg__msg__RobotAlert__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember roboy_info_system_msg__msg__RobotAlert__rosidl_typesupport_introspection_c__RobotAlert_message_member_array[2] = {
  {
    "alert_level",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roboy_info_system_msg__msg__RobotAlert, alert_level),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "alert_message",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roboy_info_system_msg__msg__RobotAlert, alert_message),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers roboy_info_system_msg__msg__RobotAlert__rosidl_typesupport_introspection_c__RobotAlert_message_members = {
  "roboy_info_system_msg__msg",  // message namespace
  "RobotAlert",  // message name
  2,  // number of fields
  sizeof(roboy_info_system_msg__msg__RobotAlert),
  roboy_info_system_msg__msg__RobotAlert__rosidl_typesupport_introspection_c__RobotAlert_message_member_array,  // message members
  roboy_info_system_msg__msg__RobotAlert__rosidl_typesupport_introspection_c__RobotAlert_init_function,  // function to initialize message memory (memory has to be allocated)
  roboy_info_system_msg__msg__RobotAlert__rosidl_typesupport_introspection_c__RobotAlert_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t roboy_info_system_msg__msg__RobotAlert__rosidl_typesupport_introspection_c__RobotAlert_message_type_support_handle = {
  0,
  &roboy_info_system_msg__msg__RobotAlert__rosidl_typesupport_introspection_c__RobotAlert_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_roboy_info_system_msg
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, roboy_info_system_msg, msg, RobotAlert)() {
  if (!roboy_info_system_msg__msg__RobotAlert__rosidl_typesupport_introspection_c__RobotAlert_message_type_support_handle.typesupport_identifier) {
    roboy_info_system_msg__msg__RobotAlert__rosidl_typesupport_introspection_c__RobotAlert_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &roboy_info_system_msg__msg__RobotAlert__rosidl_typesupport_introspection_c__RobotAlert_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
