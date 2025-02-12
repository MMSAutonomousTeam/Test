// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from letters_drawing_2:msg/TurtleInfo.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "letters_drawing_2/msg/detail/turtle_info__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace letters_drawing_2
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void TurtleInfo_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) letters_drawing_2::msg::TurtleInfo(_init);
}

void TurtleInfo_fini_function(void * message_memory)
{
  auto typed_message = static_cast<letters_drawing_2::msg::TurtleInfo *>(message_memory);
  typed_message->~TurtleInfo();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember TurtleInfo_message_member_array[3] = {
  {
    "turtle_name",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(letters_drawing_2::msg::TurtleInfo, turtle_name),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "target_coords",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<geometry_msgs::msg::Point>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(letters_drawing_2::msg::TurtleInfo, target_coords),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "letter",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(letters_drawing_2::msg::TurtleInfo, letter),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers TurtleInfo_message_members = {
  "letters_drawing_2::msg",  // message namespace
  "TurtleInfo",  // message name
  3,  // number of fields
  sizeof(letters_drawing_2::msg::TurtleInfo),
  TurtleInfo_message_member_array,  // message members
  TurtleInfo_init_function,  // function to initialize message memory (memory has to be allocated)
  TurtleInfo_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t TurtleInfo_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &TurtleInfo_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace letters_drawing_2


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<letters_drawing_2::msg::TurtleInfo>()
{
  return &::letters_drawing_2::msg::rosidl_typesupport_introspection_cpp::TurtleInfo_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, letters_drawing_2, msg, TurtleInfo)() {
  return &::letters_drawing_2::msg::rosidl_typesupport_introspection_cpp::TurtleInfo_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
