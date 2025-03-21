// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from roboy_info_system_msg:msg/RobotAlert.idl
// generated code does not contain a copyright notice

#ifndef ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__FUNCTIONS_H_
#define ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "roboy_info_system_msg/msg/rosidl_generator_c__visibility_control.h"

#include "roboy_info_system_msg/msg/detail/robot_alert__struct.h"

/// Initialize msg/RobotAlert message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * roboy_info_system_msg__msg__RobotAlert
 * )) before or use
 * roboy_info_system_msg__msg__RobotAlert__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_roboy_info_system_msg
bool
roboy_info_system_msg__msg__RobotAlert__init(roboy_info_system_msg__msg__RobotAlert * msg);

/// Finalize msg/RobotAlert message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_roboy_info_system_msg
void
roboy_info_system_msg__msg__RobotAlert__fini(roboy_info_system_msg__msg__RobotAlert * msg);

/// Create msg/RobotAlert message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * roboy_info_system_msg__msg__RobotAlert__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_roboy_info_system_msg
roboy_info_system_msg__msg__RobotAlert *
roboy_info_system_msg__msg__RobotAlert__create();

/// Destroy msg/RobotAlert message.
/**
 * It calls
 * roboy_info_system_msg__msg__RobotAlert__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_roboy_info_system_msg
void
roboy_info_system_msg__msg__RobotAlert__destroy(roboy_info_system_msg__msg__RobotAlert * msg);

/// Check for msg/RobotAlert message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_roboy_info_system_msg
bool
roboy_info_system_msg__msg__RobotAlert__are_equal(const roboy_info_system_msg__msg__RobotAlert * lhs, const roboy_info_system_msg__msg__RobotAlert * rhs);

/// Copy a msg/RobotAlert message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_roboy_info_system_msg
bool
roboy_info_system_msg__msg__RobotAlert__copy(
  const roboy_info_system_msg__msg__RobotAlert * input,
  roboy_info_system_msg__msg__RobotAlert * output);

/// Initialize array of msg/RobotAlert messages.
/**
 * It allocates the memory for the number of elements and calls
 * roboy_info_system_msg__msg__RobotAlert__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_roboy_info_system_msg
bool
roboy_info_system_msg__msg__RobotAlert__Sequence__init(roboy_info_system_msg__msg__RobotAlert__Sequence * array, size_t size);

/// Finalize array of msg/RobotAlert messages.
/**
 * It calls
 * roboy_info_system_msg__msg__RobotAlert__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_roboy_info_system_msg
void
roboy_info_system_msg__msg__RobotAlert__Sequence__fini(roboy_info_system_msg__msg__RobotAlert__Sequence * array);

/// Create array of msg/RobotAlert messages.
/**
 * It allocates the memory for the array and calls
 * roboy_info_system_msg__msg__RobotAlert__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_roboy_info_system_msg
roboy_info_system_msg__msg__RobotAlert__Sequence *
roboy_info_system_msg__msg__RobotAlert__Sequence__create(size_t size);

/// Destroy array of msg/RobotAlert messages.
/**
 * It calls
 * roboy_info_system_msg__msg__RobotAlert__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_roboy_info_system_msg
void
roboy_info_system_msg__msg__RobotAlert__Sequence__destroy(roboy_info_system_msg__msg__RobotAlert__Sequence * array);

/// Check for msg/RobotAlert message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_roboy_info_system_msg
bool
roboy_info_system_msg__msg__RobotAlert__Sequence__are_equal(const roboy_info_system_msg__msg__RobotAlert__Sequence * lhs, const roboy_info_system_msg__msg__RobotAlert__Sequence * rhs);

/// Copy an array of msg/RobotAlert messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_roboy_info_system_msg
bool
roboy_info_system_msg__msg__RobotAlert__Sequence__copy(
  const roboy_info_system_msg__msg__RobotAlert__Sequence * input,
  roboy_info_system_msg__msg__RobotAlert__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // ROBOY_INFO_SYSTEM_MSG__MSG__DETAIL__ROBOT_ALERT__FUNCTIONS_H_
