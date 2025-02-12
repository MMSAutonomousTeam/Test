// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from letters_drawing_2:msg/TurtleInfo.idl
// generated code does not contain a copyright notice

#ifndef LETTERS_DRAWING_2__MSG__DETAIL__TURTLE_INFO__STRUCT_H_
#define LETTERS_DRAWING_2__MSG__DETAIL__TURTLE_INFO__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'turtle_name'
// Member 'letter'
#include "rosidl_runtime_c/string.h"
// Member 'target_coords'
#include "geometry_msgs/msg/detail/point__struct.h"

/// Struct defined in msg/TurtleInfo in the package letters_drawing_2.
typedef struct letters_drawing_2__msg__TurtleInfo
{
  rosidl_runtime_c__String turtle_name;
  geometry_msgs__msg__Point target_coords;
  rosidl_runtime_c__String letter;
} letters_drawing_2__msg__TurtleInfo;

// Struct for a sequence of letters_drawing_2__msg__TurtleInfo.
typedef struct letters_drawing_2__msg__TurtleInfo__Sequence
{
  letters_drawing_2__msg__TurtleInfo * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} letters_drawing_2__msg__TurtleInfo__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LETTERS_DRAWING_2__MSG__DETAIL__TURTLE_INFO__STRUCT_H_
