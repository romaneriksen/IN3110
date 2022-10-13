"""
Array class for assignment 2
"""

from xmlrpc.client import boolean
import math


class Array:

    index = 0
    all_values = []

    
    def values_print():
        for x in Array.all_values:
            print(x)

    def __getitem__(self, key):
        """Returns a element at a given index using indexing.

        Args:
            key (int): the index where we went to access a value.

        Returns:
            int: an integer at a given index
            float: a float at a given index
            boolean: a boolean value at a given index
        """
        if key in range(len(self.all_values[self.index])):
            current_array = Array.all_values[self.index]
            return current_array[key]


    def __init__(self, shape, *values):

        # array_dimension = len(tuple)
        self.size = math.prod(shape) 
        # Checks if shape is of correct type
        if type(shape) != tuple:
            raise TypeError("shape must be of type tuple")
        
        # Checks if number of values fits with the shape of the array
        if shape[0] != len(values):
            raise ValueError("number of values need to fit with the shape of array")

        for value in values:
            first_type = type(values[0])

            # Checks if the values are the correct type
            if type(value) != int and type(value) != float and type(value) != bool:
                print(type(value))
                raise TypeError("values must be of type int, float or boolean")
            
            # Checks if all the values are the same type
            if type(value) != first_type:
                raise ValueError("all values need to be of same type")

        self.index = Array.index
        Array.index += 1      

        self.type = type(values[0])

        array_elements = values
        Array.all_values.append(array_elements)

            

        """Initialize an array of 1-dimensionality. Elements can only be of type:

        - int
        - float
        - bool

        Make sure the values and shape are of the correct type.

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).

        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either int, float or boolean.

        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """

        # Check if the values are of valid types

        # Check that the amount of values corresponds to the shape

        # Set class-variables

        pass

    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.

        """
        return str(Array.all_values[self.index])
        pass

    

    def __add__(self, other):
        
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        new_values = 0 # Variable to store the new values
        return_array = 0 # variable to store return Array

        if type(self) != Array:
            return NotImplemented
        
        elif type(other) is bool:
            return NotImplemented

        # If other is Array
        elif type(self) is Array and type(other) is Array:
            if self.shape is other.shape:
                if self.type is int or self.type is float:
                    if other.type is int or other.type is float:
                        new_values = [sum(x) for x in zip(Array.all_values[self.index], Array.all_values[other.index])]
                        my_tuple = tuple(new_values) # Turns the new values into a tuple
                        return_array = Array(self.shape, *my_tuple) # the '*' operand passes tuple as arguments to the Array constructor
                        return return_array
                    else:
                        return NotImplemented
                else:
                    return NotImplemented
            else:
                return NotImplemented
        
        # If other is either int or float
        elif type(self) is Array and type(other) is int or float:
            if self.type is int or self.type is float:
                new_values = [sum(x) for x in zip(Array.all_values[self.index], [other]*self.size)]
                my_tuple = tuple(new_values) # Turns the new values into a tuple
                return_array = Array(self.shape, *my_tuple) # the '*' operand passes tuple as arguments to the Array constructor
                return return_array
            else:
                return NotImplemented

        else:
            return NotImplemented

            
        # if the array is a boolean you should return NotImplemented


    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """

        new_values = 0 # Variable to store the new values
        return_array = 0 # variable to store return Array

        if type(self) != Array:
            return NotImplemented
        
        elif type(other) is bool:
            return NotImplemented

        # If other is Array
        elif type(self) is Array and type(other) is Array:
            if self.shape is other.shape:
                if self.type is int or self.type is float:
                    if other.type is int or other.type is float:
                        new_values = [value1-value2 for (value1, value2) in zip(Array.all_values[self.index], Array.all_values[other.index])]
                        my_tuple = tuple(new_values) # Turns the new values into a tuple
                        return_array = Array(self.shape, *my_tuple) # the '*' operand passes tuple as arguments to the Array constructor
                        return return_array
                    else:
                        return NotImplemented
                else:
                    return NotImplemented
            else:
                return NotImplemented
        
        # If other is either int or float
        elif type(self) is Array and type(other) is int or float:
            if self.type is int or self.type is float:
                new_values = [value1-value2 for (value1, value2) in zip(Array.all_values[self.index], [other]*self.size)]
                my_tuple = tuple(new_values) # Turns the new values into a tuple
                return_array = Array(self.shape, *my_tuple) # the '*' operand passes tuple as arguments to the Array constructor
                return return_array
            else:
                return NotImplemented

        else:
            return NotImplemented

        pass

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """

        new_values = 0 # Variable to store the new values
        return_array = 0 # variable to store return Array

        if type(self) != Array:
            return NotImplemented
        
        elif type(other) is bool:
            return NotImplemented

        # If other is Array
        elif type(self) is Array and type(other) is Array:
            if self.shape is other.shape:
                if self.type is int or self.type is float:
                    if other.type is int or other.type is float:
                        new_values = [value2-value1 for (value1, value2) in zip(Array.all_values[self.index], Array.all_values[other.index])]
                        my_tuple = tuple(new_values) # Turns the new values into a tuple
                        return_array = Array(self.shape, *my_tuple) # the '*' operand passes tuple as arguments to the Array constructor
                        return return_array
                    else:
                        return NotImplemented
                else:
                    return NotImplemented
            else:
                return NotImplemented
        
        # If other is either int or float
        elif type(self) is Array and type(other) is int or float:
            if self.type is int or self.type is float:
                new_values = [value2-value1 for (value1, value2) in zip(Array.all_values[self.index], [other]*self.size)]
                my_tuple = tuple(new_values) # Turns the new values into a tuple
                return_array = Array(self.shape, *my_tuple) # the '*' operand passes tuple as arguments to the Array constructor
                return return_array
            else:
                return NotImplemented

        else:
            return NotImplemented

        pass

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """

        new_values = 0 # Variable to store the new values
        return_array = 0 # variable to store return Array

        if type(self) != Array:
            return NotImplemented
        
        elif type(other) is bool:
            return NotImplemented

        # If other is Array
        elif type(self) is Array and type(other) is Array:
            if self.shape is other.shape:
                if self.type is int or self.type is float:
                    if other.type is int or other.type is float:
                        new_values = [value1*value2 for (value1, value2) in zip(Array.all_values[self.index], Array.all_values[other.index])]
                        my_tuple = tuple(new_values) # Turns the new values into a tuple
                        return_array = Array(self.shape, *my_tuple) # the '*' operand passes tuple as arguments to the Array constructor
                        return return_array
                    else:
                        return NotImplemented
                else:
                    return NotImplemented
            else:
                return NotImplemented
        
        # If other is either int or float
        elif type(self) is Array and type(other) is int or float:
            if self.type is int or self.type is float:
                new_values = [value1*value2 for (value1, value2) in zip(Array.all_values[self.index], [other]*self.size)]
                my_tuple = tuple(new_values) # Turns the new values into a tuple
                return_array = Array(self.shape, *my_tuple) # the '*' operand passes tuple as arguments to the Array constructor
                return return_array
            else:
                return NotImplemented

        else:
            return NotImplemented

        pass

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        # Hint: this solution/logic applies for all r-methods
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """
        
        print(Array.all_values[self.index])
        print(type(Array.all_values[other.index]))
        if type(other) is Array:    
            if self.shape is other.shape:
                if Array.all_values[self.index] == Array.all_values[other.index]:
                    return True
                else:
                    return False
            else:
                return False
        else: 
            return False
        
        
        pass

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.

        """
        new_values = 0 # Variable to store the new values
        return_array = 0 # variable to store return Array

        if type(other) != Array and type(other) != int and type(other) != float:
            return TypeError

        elif type(other) == Array: 
            if self.shape == other.shape:
                new_values = [value1 == value2 for (value1, value2) in zip(Array.all_values[self.index], Array.all_values[other.index])]
                my_tuple = tuple(new_values) # Turns the new values into a tuple
                return_array = Array(self.shape, *my_tuple) # the '*' operand passes tuple as arguments to the Array constructor
                return return_array
            else:
                raise ValueError("The array shapes need to be of the same size")
        
        else:
            return TypeError

        pass

    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """
        if self.type is int or self.type is float:
            return float(min(Array.all_values[self.index]))
        
        else:
            raise TypeError("Array needs to consist of either integer of float values")

        pass

    def mean_element(self):
        """Returns the mean value of an array

        Only needs to work for type int and float (not boolean).

        Returns:
            float: the mean value
        """
        if self.type is int or self.type is float:
            return float(sum(Array.all_values[self.index])/self.size)
        
        else:
            raise TypeError("Array needs to consist of either integer of float values")


        pass
