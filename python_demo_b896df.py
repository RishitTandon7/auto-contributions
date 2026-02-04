# --- Learning Objective ---
# This tutorial will teach you how to create a simple Python decorator
# to log function calls and their execution times. You will learn:
# 1. What decorators are and how they work in Python.
# 2. How to define and use decorators.
# 3. How to wrap other functions with decorators.
# 4. How to measure and log execution time.
# 5. How to pass arguments to decorated functions.
# 6. How to preserve function metadata (like name and docstring).
#
# Decorators are a powerful feature in Python that allow you to modify
# or enhance functions (or classes) in a clean and reusable way.
# They are often used for logging, access control, instrumentation, etc.

# Import necessary modules
import time
import functools # This module is essential for decorators!

# --- Decorator Definition ---

# We define a function that will act as our decorator.
# A decorator is essentially a function that takes another function
# as an argument, adds some functionality to it, and returns a new function.
def log_execution_time(func):
    """
    This is a decorator that logs the function name and its execution time.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The wrapped function with logging capabilities.
    """
    # functools.wraps is crucial here! It preserves the original function's
    # metadata (like __name__, __doc__, etc.). Without it, the decorated
    # function would appear to have the name and docstring of the wrapper function.
    # This makes debugging and introspection much easier.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        The wrapper function that will execute before and after the original function.
        It handles logging and timing.
        """
        # --- Logging the function call ---
        # We log that the function is about to be called.
        # Using f-strings for easy string formatting.
        print(f"INFO: Calling function: '{func.__name__}'")

        # --- Measuring Execution Time ---
        # Record the start time before the function is executed.
        start_time = time.perf_counter() # perf_counter is good for precise timing.

        # --- Executing the original function ---
        # Call the original function ('func') with its arguments (*args, **kwargs).
        # This is how the decorator "wraps" the original function.
        # We need to capture its return value to return it later.
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            # --- Handling Exceptions ---
            # If the decorated function raises an exception, we should log it
            # and then re-raise the exception so that the calling code can handle it.
            print(f"ERROR: Function '{func.__name__}' raised an exception: {e}")
            raise # Re-raise the caught exception

        # --- Measuring Execution Time (End) ---
        # Record the end time after the function has finished executing.
        end_time = time.perf_counter()

        # Calculate the duration of the function's execution.
        duration = end_time - start_time

        # --- Logging the execution time ---
        # Log that the function has completed and how long it took.
        print(f"INFO: Function '{func.__name__}' finished in {duration:.4f} seconds.")

        # --- Returning the result ---
        # Return the result that the original function produced.
        # This is important so that the decorated function behaves like the original
        # from the perspective of the code that calls it.
        return result

    # The decorator returns the wrapper function. This wrapper function
    # will replace the original function when the decorator is applied.
    return wrapper

# --- Example Usage ---

# Apply the decorator using the '@' syntax.
# This is syntactic sugar for:
# my_function_one = log_execution_time(my_function_one)
@log_execution_time
def my_function_one(a, b):
    """This is a sample function that performs addition."""
    print(f"  Inside my_function_one: Adding {a} and {b}")
    time.sleep(0.1) # Simulate some work
    return a + b

@log_execution_time
def another_function(name, greeting="Hello"):
    """A function that prints a greeting."""
    print(f"  Inside another_function: Greeting '{name}' with '{greeting}'")
    time.sleep(0.05) # Simulate some work
    return f"{greeting}, {name}!"

@log_execution_time
def function_with_error():
    """This function is designed to raise an error."""
    print("  Inside function_with_error: About to raise an error.")
    raise ValueError("Something went wrong!")

# --- Calling the decorated functions ---

print("\n--- Testing my_function_one ---")
# When we call my_function_one, the 'wrapper' function from the decorator
# will be executed. It will log the call, time the execution, call the
# original my_function_one, and then log the completion and duration.
result1 = my_function_one(5, 3)
print(f"Result of my_function_one: {result1}")

print("\n--- Testing another_function ---")
# We can pass both positional and keyword arguments to the decorated function.
result2 = another_function("Alice", greeting="Hi")
print(f"Result of another_function: {result2}")

result3 = another_function("Bob") # Using the default greeting
print(f"Result of another_function: {result3}")

print("\n--- Testing function_with_error ---")
try:
    function_with_error()
except ValueError as e:
    print(f"Successfully caught expected error: {e}")

# You can also inspect the decorated function's metadata.
# Thanks to functools.wraps, __name__ and __doc__ are preserved.
print(f"\nName of decorated my_function_one: {my_function_one.__name__}")
print(f"Docstring of decorated my_function_one: {my_function_one.__doc__}")