// generated from rosidl_typesupport_cpp/resource/idl__type_support.cpp.em
// with input from letters_drawing_2:msg/TurtleInfo.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "letters_drawing_2/msg/detail/turtle_info__struct.hpp"
#include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
#include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace letters_drawing_2
{

namespace msg
{

namespace rosidl_typesupport_cpp
{

typedef struct _TurtleInfo_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _TurtleInfo_type_support_ids_t;

static const _TurtleInfo_type_support_ids_t _TurtleInfo_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _TurtleInfo_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _TurtleInfo_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _TurtleInfo_type_support_symbol_names_t _TurtleInfo_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, letters_drawing_2, msg, TurtleInfo)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, letters_drawing_2, msg, TurtleInfo)),
  }
};

typedef struct _TurtleInfo_type_support_data_t
{
  void * data[2];
} _TurtleInfo_type_support_data_t;

static _TurtleInfo_type_support_data_t _TurtleInfo_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _TurtleInfo_message_typesupport_map = {
  2,
  "letters_drawing_2",
  &_TurtleInfo_message_typesupport_ids.typesupport_identifier[0],
  &_TurtleInfo_message_typesupport_symbol_names.symbol_name[0],
  &_TurtleInfo_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t TurtleInfo_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_TurtleInfo_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace msg

}  // namespace letters_drawing_2

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<letters_drawing_2::msg::TurtleInfo>()
{
  return &::letters_drawing_2::msg::rosidl_typesupport_cpp::TurtleInfo_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, letters_drawing_2, msg, TurtleInfo)() {
  return get_message_type_support_handle<letters_drawing_2::msg::TurtleInfo>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp
