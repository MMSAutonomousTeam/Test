// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from letters_drawing_2:msg/TurtleInfo.idl
// generated code does not contain a copyright notice

#ifndef LETTERS_DRAWING_2__MSG__DETAIL__TURTLE_INFO__TRAITS_HPP_
#define LETTERS_DRAWING_2__MSG__DETAIL__TURTLE_INFO__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "letters_drawing_2/msg/detail/turtle_info__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'target_coords'
#include "geometry_msgs/msg/detail/point__traits.hpp"

namespace letters_drawing_2
{

namespace msg
{

inline void to_flow_style_yaml(
  const TurtleInfo & msg,
  std::ostream & out)
{
  out << "{";
  // member: turtle_name
  {
    out << "turtle_name: ";
    rosidl_generator_traits::value_to_yaml(msg.turtle_name, out);
    out << ", ";
  }

  // member: target_coords
  {
    out << "target_coords: ";
    to_flow_style_yaml(msg.target_coords, out);
    out << ", ";
  }

  // member: letter
  {
    out << "letter: ";
    rosidl_generator_traits::value_to_yaml(msg.letter, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TurtleInfo & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: turtle_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "turtle_name: ";
    rosidl_generator_traits::value_to_yaml(msg.turtle_name, out);
    out << "\n";
  }

  // member: target_coords
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "target_coords:\n";
    to_block_style_yaml(msg.target_coords, out, indentation + 2);
  }

  // member: letter
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "letter: ";
    rosidl_generator_traits::value_to_yaml(msg.letter, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TurtleInfo & msg, bool use_flow_style = false)
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

}  // namespace letters_drawing_2

namespace rosidl_generator_traits
{

[[deprecated("use letters_drawing_2::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const letters_drawing_2::msg::TurtleInfo & msg,
  std::ostream & out, size_t indentation = 0)
{
  letters_drawing_2::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use letters_drawing_2::msg::to_yaml() instead")]]
inline std::string to_yaml(const letters_drawing_2::msg::TurtleInfo & msg)
{
  return letters_drawing_2::msg::to_yaml(msg);
}

template<>
inline const char * data_type<letters_drawing_2::msg::TurtleInfo>()
{
  return "letters_drawing_2::msg::TurtleInfo";
}

template<>
inline const char * name<letters_drawing_2::msg::TurtleInfo>()
{
  return "letters_drawing_2/msg/TurtleInfo";
}

template<>
struct has_fixed_size<letters_drawing_2::msg::TurtleInfo>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<letters_drawing_2::msg::TurtleInfo>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<letters_drawing_2::msg::TurtleInfo>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // LETTERS_DRAWING_2__MSG__DETAIL__TURTLE_INFO__TRAITS_HPP_
