// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from roboy_info_system_msg:msg/RobotAlert.idl
// generated code does not contain a copyright notice

#ifndef ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "roboy_info_system_msg/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "roboy_info_system_msg/msg/detail/robot_alert__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace roboy_info_system_msg
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_roboy_info_system_msg
cdr_serialize(
  const roboy_info_system_msg::msg::RobotAlert & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_roboy_info_system_msg
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  roboy_info_system_msg::msg::RobotAlert & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_roboy_info_system_msg
get_serialized_size(
  const roboy_info_system_msg::msg::RobotAlert & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_roboy_info_system_msg
max_serialized_size_RobotAlert(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace roboy_info_system_msg

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_roboy_info_system_msg
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, roboy_info_system_msg, msg, RobotAlert)();

#ifdef __cplusplus
}
#endif

#endif  // ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
