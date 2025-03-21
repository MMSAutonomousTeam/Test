// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from roboy_info_system_msg:msg/RobotAlert.idl
// generated code does not contain a copyright notice

#ifndef ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__STRUCT_H_
#define ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'alert_message'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/RobotAlert in the package roboy_info_system_msg.
typedef struct roboy_info_system_msg__msg__RobotAlert
{
  int32_t alert_level;
  rosidl_runtime_c__String alert_message;
} roboy_info_system_msg__msg__RobotAlert;

// Struct for a sequence of roboy_info_system_msg__msg__RobotAlert.
typedef struct roboy_info_system_msg__msg__RobotAlert__Sequence
{
  roboy_info_system_msg__msg__RobotAlert * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roboy_info_system_msg__msg__RobotAlert__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__STRUCT_H_
