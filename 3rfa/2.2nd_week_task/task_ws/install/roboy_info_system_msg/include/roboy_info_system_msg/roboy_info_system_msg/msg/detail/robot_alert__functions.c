// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from roboy_info_system_msg:msg/RobotAlert.idl
// generated code does not contain a copyright notice
#include "roboy_info_system_msg/msg/detail/robot_alert__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `alert_message`
#include "rosidl_runtime_c/string_functions.h"

bool
roboy_info_system_msg__msg__RobotAlert__init(roboy_info_system_msg__msg__RobotAlert * msg)
{
  if (!msg) {
    return false;
  }
  // alert_level
  // alert_message
  if (!rosidl_runtime_c__String__init(&msg->alert_message)) {
    roboy_info_system_msg__msg__RobotAlert__fini(msg);
    return false;
  }
  return true;
}

void
roboy_info_system_msg__msg__RobotAlert__fini(roboy_info_system_msg__msg__RobotAlert * msg)
{
  if (!msg) {
    return;
  }
  // alert_level
  // alert_message
  rosidl_runtime_c__String__fini(&msg->alert_message);
}

bool
roboy_info_system_msg__msg__RobotAlert__are_equal(const roboy_info_system_msg__msg__RobotAlert * lhs, const roboy_info_system_msg__msg__RobotAlert * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // alert_level
  if (lhs->alert_level != rhs->alert_level) {
    return false;
  }
  // alert_message
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->alert_message), &(rhs->alert_message)))
  {
    return false;
  }
  return true;
}

bool
roboy_info_system_msg__msg__RobotAlert__copy(
  const roboy_info_system_msg__msg__RobotAlert * input,
  roboy_info_system_msg__msg__RobotAlert * output)
{
  if (!input || !output) {
    return false;
  }
  // alert_level
  output->alert_level = input->alert_level;
  // alert_message
  if (!rosidl_runtime_c__String__copy(
      &(input->alert_message), &(output->alert_message)))
  {
    return false;
  }
  return true;
}

roboy_info_system_msg__msg__RobotAlert *
roboy_info_system_msg__msg__RobotAlert__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roboy_info_system_msg__msg__RobotAlert * msg = (roboy_info_system_msg__msg__RobotAlert *)allocator.allocate(sizeof(roboy_info_system_msg__msg__RobotAlert), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roboy_info_system_msg__msg__RobotAlert));
  bool success = roboy_info_system_msg__msg__RobotAlert__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roboy_info_system_msg__msg__RobotAlert__destroy(roboy_info_system_msg__msg__RobotAlert * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roboy_info_system_msg__msg__RobotAlert__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roboy_info_system_msg__msg__RobotAlert__Sequence__init(roboy_info_system_msg__msg__RobotAlert__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roboy_info_system_msg__msg__RobotAlert * data = NULL;

  if (size) {
    data = (roboy_info_system_msg__msg__RobotAlert *)allocator.zero_allocate(size, sizeof(roboy_info_system_msg__msg__RobotAlert), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roboy_info_system_msg__msg__RobotAlert__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roboy_info_system_msg__msg__RobotAlert__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
roboy_info_system_msg__msg__RobotAlert__Sequence__fini(roboy_info_system_msg__msg__RobotAlert__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      roboy_info_system_msg__msg__RobotAlert__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

roboy_info_system_msg__msg__RobotAlert__Sequence *
roboy_info_system_msg__msg__RobotAlert__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roboy_info_system_msg__msg__RobotAlert__Sequence * array = (roboy_info_system_msg__msg__RobotAlert__Sequence *)allocator.allocate(sizeof(roboy_info_system_msg__msg__RobotAlert__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roboy_info_system_msg__msg__RobotAlert__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roboy_info_system_msg__msg__RobotAlert__Sequence__destroy(roboy_info_system_msg__msg__RobotAlert__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roboy_info_system_msg__msg__RobotAlert__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roboy_info_system_msg__msg__RobotAlert__Sequence__are_equal(const roboy_info_system_msg__msg__RobotAlert__Sequence * lhs, const roboy_info_system_msg__msg__RobotAlert__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roboy_info_system_msg__msg__RobotAlert__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roboy_info_system_msg__msg__RobotAlert__Sequence__copy(
  const roboy_info_system_msg__msg__RobotAlert__Sequence * input,
  roboy_info_system_msg__msg__RobotAlert__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roboy_info_system_msg__msg__RobotAlert);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roboy_info_system_msg__msg__RobotAlert * data =
      (roboy_info_system_msg__msg__RobotAlert *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roboy_info_system_msg__msg__RobotAlert__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roboy_info_system_msg__msg__RobotAlert__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roboy_info_system_msg__msg__RobotAlert__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
