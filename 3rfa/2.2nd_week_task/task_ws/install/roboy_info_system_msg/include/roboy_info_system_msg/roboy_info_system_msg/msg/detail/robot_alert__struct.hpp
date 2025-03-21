// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from roboy_info_system_msg:msg/RobotAlert.idl
// generated code does not contain a copyright notice

#ifndef ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__STRUCT_HPP_
#define ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__roboy_info_system_msg__msg__RobotAlert __attribute__((deprecated))
#else
# define DEPRECATED__roboy_info_system_msg__msg__RobotAlert __declspec(deprecated)
#endif

namespace roboy_info_system_msg
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RobotAlert_
{
  using Type = RobotAlert_<ContainerAllocator>;

  explicit RobotAlert_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->alert_level = 0l;
      this->alert_message = "";
    }
  }

  explicit RobotAlert_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : alert_message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->alert_level = 0l;
      this->alert_message = "";
    }
  }

  // field types and members
  using _alert_level_type =
    int32_t;
  _alert_level_type alert_level;
  using _alert_message_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _alert_message_type alert_message;

  // setters for named parameter idiom
  Type & set__alert_level(
    const int32_t & _arg)
  {
    this->alert_level = _arg;
    return *this;
  }
  Type & set__alert_message(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->alert_message = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    roboy_info_system_msg::msg::RobotAlert_<ContainerAllocator> *;
  using ConstRawPtr =
    const roboy_info_system_msg::msg::RobotAlert_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<roboy_info_system_msg::msg::RobotAlert_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<roboy_info_system_msg::msg::RobotAlert_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      roboy_info_system_msg::msg::RobotAlert_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<roboy_info_system_msg::msg::RobotAlert_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      roboy_info_system_msg::msg::RobotAlert_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<roboy_info_system_msg::msg::RobotAlert_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<roboy_info_system_msg::msg::RobotAlert_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<roboy_info_system_msg::msg::RobotAlert_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__roboy_info_system_msg__msg__RobotAlert
    std::shared_ptr<roboy_info_system_msg::msg::RobotAlert_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__roboy_info_system_msg__msg__RobotAlert
    std::shared_ptr<roboy_info_system_msg::msg::RobotAlert_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotAlert_ & other) const
  {
    if (this->alert_level != other.alert_level) {
      return false;
    }
    if (this->alert_message != other.alert_message) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotAlert_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotAlert_

// alias to use template instance with default allocator
using RobotAlert =
  roboy_info_system_msg::msg::RobotAlert_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace roboy_info_system_msg

#endif  // ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__STRUCT_HPP_
