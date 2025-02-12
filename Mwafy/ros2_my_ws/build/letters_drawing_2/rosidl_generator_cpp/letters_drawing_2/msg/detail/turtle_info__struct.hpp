// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from letters_drawing_2:msg/TurtleInfo.idl
// generated code does not contain a copyright notice

#ifndef LETTERS_DRAWING_2__MSG__DETAIL__TURTLE_INFO__STRUCT_HPP_
#define LETTERS_DRAWING_2__MSG__DETAIL__TURTLE_INFO__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'target_coords'
#include "geometry_msgs/msg/detail/point__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__letters_drawing_2__msg__TurtleInfo __attribute__((deprecated))
#else
# define DEPRECATED__letters_drawing_2__msg__TurtleInfo __declspec(deprecated)
#endif

namespace letters_drawing_2
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TurtleInfo_
{
  using Type = TurtleInfo_<ContainerAllocator>;

  explicit TurtleInfo_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : target_coords(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->turtle_name = "";
      this->letter = "";
    }
  }

  explicit TurtleInfo_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : turtle_name(_alloc),
    target_coords(_alloc, _init),
    letter(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->turtle_name = "";
      this->letter = "";
    }
  }

  // field types and members
  using _turtle_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _turtle_name_type turtle_name;
  using _target_coords_type =
    geometry_msgs::msg::Point_<ContainerAllocator>;
  _target_coords_type target_coords;
  using _letter_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _letter_type letter;

  // setters for named parameter idiom
  Type & set__turtle_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->turtle_name = _arg;
    return *this;
  }
  Type & set__target_coords(
    const geometry_msgs::msg::Point_<ContainerAllocator> & _arg)
  {
    this->target_coords = _arg;
    return *this;
  }
  Type & set__letter(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->letter = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    letters_drawing_2::msg::TurtleInfo_<ContainerAllocator> *;
  using ConstRawPtr =
    const letters_drawing_2::msg::TurtleInfo_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<letters_drawing_2::msg::TurtleInfo_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<letters_drawing_2::msg::TurtleInfo_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      letters_drawing_2::msg::TurtleInfo_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<letters_drawing_2::msg::TurtleInfo_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      letters_drawing_2::msg::TurtleInfo_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<letters_drawing_2::msg::TurtleInfo_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<letters_drawing_2::msg::TurtleInfo_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<letters_drawing_2::msg::TurtleInfo_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__letters_drawing_2__msg__TurtleInfo
    std::shared_ptr<letters_drawing_2::msg::TurtleInfo_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__letters_drawing_2__msg__TurtleInfo
    std::shared_ptr<letters_drawing_2::msg::TurtleInfo_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TurtleInfo_ & other) const
  {
    if (this->turtle_name != other.turtle_name) {
      return false;
    }
    if (this->target_coords != other.target_coords) {
      return false;
    }
    if (this->letter != other.letter) {
      return false;
    }
    return true;
  }
  bool operator!=(const TurtleInfo_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TurtleInfo_

// alias to use template instance with default allocator
using TurtleInfo =
  letters_drawing_2::msg::TurtleInfo_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace letters_drawing_2

#endif  // LETTERS_DRAWING_2__MSG__DETAIL__TURTLE_INFO__STRUCT_HPP_
