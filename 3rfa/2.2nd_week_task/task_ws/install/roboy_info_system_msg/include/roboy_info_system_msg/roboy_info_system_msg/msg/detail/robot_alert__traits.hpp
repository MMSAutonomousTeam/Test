// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from roboy_info_system_msg:msg/RobotAlert.idl
// generated code does not contain a copyright notice

#ifndef ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__TRAITS_HPP_
#define ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "roboy_info_system_msg/msg/detail/robot_alert__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace roboy_info_system_msg
{

namespace msg
{

inline void to_flow_style_yaml(
  const RobotAlert & msg,
  std::ostream & out)
{
  out << "{";
  // member: alert_level
  {
    out << "alert_level: ";
    rosidl_generator_traits::value_to_yaml(msg.alert_level, out);
    out << ", ";
  }

  // member: alert_message
  {
    out << "alert_message: ";
    rosidl_generator_traits::value_to_yaml(msg.alert_message, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotAlert & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: alert_level
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "alert_level: ";
    rosidl_generator_traits::value_to_yaml(msg.alert_level, out);
    out << "\n";
  }

  // member: alert_message
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "alert_message: ";
    rosidl_generator_traits::value_to_yaml(msg.alert_message, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotAlert & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace roboy_info_system_msg

namespace rosidl_generator_traits
{

[[deprecated("use roboy_info_system_msg::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const roboy_info_system_msg::msg::RobotAlert & msg,
  std::ostream & out, size_t indentation = 0)
{
  roboy_info_system_msg::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use roboy_info_system_msg::msg::to_yaml() instead")]]
inline std::string to_yaml(const roboy_info_system_msg::msg::RobotAlert & msg)
{
  return roboy_info_system_msg::msg::to_yaml(msg);
}

template<>
inline const char * data_type<roboy_info_system_msg::msg::RobotAlert>()
{
  return "roboy_info_system_msg::msg::RobotAlert";
}

template<>
inline const char * name<roboy_info_system_msg::msg::RobotAlert>()
{
  return "roboy_info_system_msg/msg/RobotAlert";
}

template<>
struct has_fixed_size<roboy_info_system_msg::msg::RobotAlert>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<roboy_info_system_msg::msg::RobotAlert>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<roboy_info_system_msg::msg::RobotAlert>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__TRAITS_HPP_
