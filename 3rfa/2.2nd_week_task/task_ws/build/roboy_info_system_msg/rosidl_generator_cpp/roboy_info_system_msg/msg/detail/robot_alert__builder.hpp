// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roboy_info_system_msg:msg/RobotAlert.idl
// generated code does not contain a copyright notice

#ifndef ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__BUILDER_HPP_
#define ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roboy_info_system_msg/msg/detail/robot_alert__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roboy_info_system_msg
{

namespace msg
{

namespace builder
{

class Init_RobotAlert_alert_message
{
public:
  explicit Init_RobotAlert_alert_message(::roboy_info_system_msg::msg::RobotAlert & msg)
  : msg_(msg)
  {}
  ::roboy_info_system_msg::msg::RobotAlert alert_message(::roboy_info_system_msg::msg::RobotAlert::_alert_message_type arg)
  {
    msg_.alert_message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roboy_info_system_msg::msg::RobotAlert msg_;
};

class Init_RobotAlert_alert_level
{
public:
  Init_RobotAlert_alert_level()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotAlert_alert_message alert_level(::roboy_info_system_msg::msg::RobotAlert::_alert_level_type arg)
  {
    msg_.alert_level = std::move(arg);
    return Init_RobotAlert_alert_message(msg_);
  }

private:
  ::roboy_info_system_msg::msg::RobotAlert msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::roboy_info_system_msg::msg::RobotAlert>()
{
  return roboy_info_system_msg::msg::builder::Init_RobotAlert_alert_level();
}

}  // namespace roboy_info_system_msg

#endif  // ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__BUILDER_HPP_
