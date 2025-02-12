// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from letters_drawing_2:msg/TurtleInfo.idl
// generated code does not contain a copyright notice

#ifndef LETTERS_DRAWING_2__MSG__DETAIL__TURTLE_INFO__BUILDER_HPP_
#define LETTERS_DRAWING_2__MSG__DETAIL__TURTLE_INFO__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "letters_drawing_2/msg/detail/turtle_info__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace letters_drawing_2
{

namespace msg
{

namespace builder
{

class Init_TurtleInfo_letter
{
public:
  explicit Init_TurtleInfo_letter(::letters_drawing_2::msg::TurtleInfo & msg)
  : msg_(msg)
  {}
  ::letters_drawing_2::msg::TurtleInfo letter(::letters_drawing_2::msg::TurtleInfo::_letter_type arg)
  {
    msg_.letter = std::move(arg);
    return std::move(msg_);
  }

private:
  ::letters_drawing_2::msg::TurtleInfo msg_;
};

class Init_TurtleInfo_target_coords
{
public:
  explicit Init_TurtleInfo_target_coords(::letters_drawing_2::msg::TurtleInfo & msg)
  : msg_(msg)
  {}
  Init_TurtleInfo_letter target_coords(::letters_drawing_2::msg::TurtleInfo::_target_coords_type arg)
  {
    msg_.target_coords = std::move(arg);
    return Init_TurtleInfo_letter(msg_);
  }

private:
  ::letters_drawing_2::msg::TurtleInfo msg_;
};

class Init_TurtleInfo_turtle_name
{
public:
  Init_TurtleInfo_turtle_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TurtleInfo_target_coords turtle_name(::letters_drawing_2::msg::TurtleInfo::_turtle_name_type arg)
  {
    msg_.turtle_name = std::move(arg);
    return Init_TurtleInfo_target_coords(msg_);
  }

private:
  ::letters_drawing_2::msg::TurtleInfo msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::letters_drawing_2::msg::TurtleInfo>()
{
  return letters_drawing_2::msg::builder::Init_TurtleInfo_turtle_name();
}

}  // namespace letters_drawing_2

#endif  // LETTERS_DRAWING_2__MSG__DETAIL__TURTLE_INFO__BUILDER_HPP_
