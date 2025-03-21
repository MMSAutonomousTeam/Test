// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from roboy_info_system_msg:msg/RobotAlert.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "roboy_info_system_msg/msg/detail/robot_alert__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace roboy_info_system_msg
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void RobotAlert_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) roboy_info_system_msg::msg::RobotAlert(_init);
}

void RobotAlert_fini_function(void * message_memory)
{
  auto typed_message = static_cast<roboy_info_system_msg::msg::RobotAlert *>(message_memory);
  typed_message->~RobotAlert();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember RobotAlert_message_member_array[2] = {
  {
    "alert_level",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roboy_info_system_msg::msg::RobotAlert, alert_level),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "alert_message",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roboy_info_system_msg::msg::RobotAlert, alert_message),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers RobotAlert_message_members = {
  "roboy_info_system_msg::msg",  // message namespace
  "RobotAlert",  // message name
  2,  // number of fields
  sizeof(roboy_info_system_msg::msg::RobotAlert),
  RobotAlert_message_member_array,  // message members
  RobotAlert_init_function,  // function to initialize message memory (memory has to be allocated)
  RobotAlert_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t RobotAlert_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &RobotAlert_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace roboy_info_system_msg


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<roboy_info_system_msg::msg::RobotAlert>()
{
  return &::roboy_info_system_msg::msg::rosidl_typesupport_introspection_cpp::RobotAlert_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, roboy_info_system_msg, msg, RobotAlert)() {
  return &::roboy_info_system_msg::msg::rosidl_typesupport_introspection_cpp::RobotAlert_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
