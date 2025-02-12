// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from letters_drawing_2:msg/TurtleInfo.idl
// generated code does not contain a copyright notice
#include "letters_drawing_2/msg/detail/turtle_info__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `turtle_name`
// Member `letter`
#include "rosidl_runtime_c/string_functions.h"
// Member `target_coords`
#include "geometry_msgs/msg/detail/point__functions.h"

bool
letters_drawing_2__msg__TurtleInfo__init(letters_drawing_2__msg__TurtleInfo * msg)
{
  if (!msg) {
    return false;
  }
  // turtle_name
  if (!rosidl_runtime_c__String__init(&msg->turtle_name)) {
    letters_drawing_2__msg__TurtleInfo__fini(msg);
    return false;
  }
  // target_coords
  if (!geometry_msgs__msg__Point__init(&msg->target_coords)) {
    letters_drawing_2__msg__TurtleInfo__fini(msg);
    return false;
  }
  // letter
  if (!rosidl_runtime_c__String__init(&msg->letter)) {
    letters_drawing_2__msg__TurtleInfo__fini(msg);
    return false;
  }
  return true;
}

void
letters_drawing_2__msg__TurtleInfo__fini(letters_drawing_2__msg__TurtleInfo * msg)
{
  if (!msg) {
    return;
  }
  // turtle_name
  rosidl_runtime_c__String__fini(&msg->turtle_name);
  // target_coords
  geometry_msgs__msg__Point__fini(&msg->target_coords);
  // letter
  rosidl_runtime_c__String__fini(&msg->letter);
}

bool
letters_drawing_2__msg__TurtleInfo__are_equal(const letters_drawing_2__msg__TurtleInfo * lhs, const letters_drawing_2__msg__TurtleInfo * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // turtle_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->turtle_name), &(rhs->turtle_name)))
  {
    return false;
  }
  // target_coords
  if (!geometry_msgs__msg__Point__are_equal(
      &(lhs->target_coords), &(rhs->target_coords)))
  {
    return false;
  }
  // letter
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->letter), &(rhs->letter)))
  {
    return false;
  }
  return true;
}

bool
letters_drawing_2__msg__TurtleInfo__copy(
  const letters_drawing_2__msg__TurtleInfo * input,
  letters_drawing_2__msg__TurtleInfo * output)
{
  if (!input || !output) {
    return false;
  }
  // turtle_name
  if (!rosidl_runtime_c__String__copy(
      &(input->turtle_name), &(output->turtle_name)))
  {
    return false;
  }
  // target_coords
  if (!geometry_msgs__msg__Point__copy(
      &(input->target_coords), &(output->target_coords)))
  {
    return false;
  }
  // letter
  if (!rosidl_runtime_c__String__copy(
      &(input->letter), &(output->letter)))
  {
    return false;
  }
  return true;
}

letters_drawing_2__msg__TurtleInfo *
letters_drawing_2__msg__TurtleInfo__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  letters_drawing_2__msg__TurtleInfo * msg = (letters_drawing_2__msg__TurtleInfo *)allocator.allocate(sizeof(letters_drawing_2__msg__TurtleInfo), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(letters_drawing_2__msg__TurtleInfo));
  bool success = letters_drawing_2__msg__TurtleInfo__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
letters_drawing_2__msg__TurtleInfo__destroy(letters_drawing_2__msg__TurtleInfo * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    letters_drawing_2__msg__TurtleInfo__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
letters_drawing_2__msg__TurtleInfo__Sequence__init(letters_drawing_2__msg__TurtleInfo__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  letters_drawing_2__msg__TurtleInfo * data = NULL;

  if (size) {
    data = (letters_drawing_2__msg__TurtleInfo *)allocator.zero_allocate(size, sizeof(letters_drawing_2__msg__TurtleInfo), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = letters_drawing_2__msg__TurtleInfo__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        letters_drawing_2__msg__TurtleInfo__fini(&data[i - 1]);
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
letters_drawing_2__msg__TurtleInfo__Sequence__fini(letters_drawing_2__msg__TurtleInfo__Sequence * array)
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
      letters_drawing_2__msg__TurtleInfo__fini(&array->data[i]);
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

letters_drawing_2__msg__TurtleInfo__Sequence *
letters_drawing_2__msg__TurtleInfo__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  letters_drawing_2__msg__TurtleInfo__Sequence * array = (letters_drawing_2__msg__TurtleInfo__Sequence *)allocator.allocate(sizeof(letters_drawing_2__msg__TurtleInfo__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = letters_drawing_2__msg__TurtleInfo__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
letters_drawing_2__msg__TurtleInfo__Sequence__destroy(letters_drawing_2__msg__TurtleInfo__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    letters_drawing_2__msg__TurtleInfo__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
letters_drawing_2__msg__TurtleInfo__Sequence__are_equal(const letters_drawing_2__msg__TurtleInfo__Sequence * lhs, const letters_drawing_2__msg__TurtleInfo__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!letters_drawing_2__msg__TurtleInfo__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
letters_drawing_2__msg__TurtleInfo__Sequence__copy(
  const letters_drawing_2__msg__TurtleInfo__Sequence * input,
  letters_drawing_2__msg__TurtleInfo__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(letters_drawing_2__msg__TurtleInfo);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    letters_drawing_2__msg__TurtleInfo * data =
      (letters_drawing_2__msg__TurtleInfo *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!letters_drawing_2__msg__TurtleInfo__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          letters_drawing_2__msg__TurtleInfo__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!letters_drawing_2__msg__TurtleInfo__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
