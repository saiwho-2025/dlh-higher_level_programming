#!/usr/bin/env python3
"""this module serialize objects using pickle module"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """Initialize the CustomObject with name, age, and student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the specified format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to a file using pickle."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, IOError) as e:
            print(f"Error writing to file: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load an instance of CustomObject from a file."""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)

                # Check if the loaded object is actually
                # an instance of CustomObject
                if isinstance(obj, cls):
                    return obj
                return None
        except (FileNotFoundError, pickle.UnpicklingError,
                EOFError, AttributeError):
            # Handles non-existent, malformed, or empty files
            return None
        except Exception as e:
            # Catch-all for unexpected OS errors
            return None


# Example usage for testing:
if __name__ == "__main__":
    # Create object
    original_obj = CustomObject("John", 25, True)

    # Serialize
    original_obj.serialize("data.pkl")

    # Deserialize
    new_obj = CustomObject.deserialize("data.pkl")

    if new_obj:
        new_obj.display()
