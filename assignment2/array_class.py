"""
Array class for assignment 2
"""
import math

class Array:

    def __getitem__(self, key):
        """Returns a element at a given index using indexing.
        Args:
            key (int): the index where we went to access a value.
        Returns:
            int: an integer at a given index.
            float: a float at a given index.
            boolean: a boolean value at a given index.
            list: returns a list at a given index
        """
        return self.all_values[key]

    def __init__(self, shape, *values):
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
        if type(values[0]) != float and type(values[0]) != int and type(values[0]) != bool:
            raise TypeError("Values need to be of type int, float or bool")

        if type(shape) != tuple:
            raise TypeError("Shape needs to be a tuple")

        self.array_type = type(values[0])
        for x in values:
            if type(x) != self.array_type:
                raise ValueError("Values need to be of same type")
        
        # Check that the amount of values corresponds to the shape
        if math.prod(shape) != len(values):
            raise ValueError("Values does not fit with shape")

        self.array_flat = list(values)
        self.all_values = []
        self.shape = shape
        self.type = type(values[0])

        # Set class-variables

        # If array is 2D
        if len(shape) == 2:
            
            n,m = shape
            count = 0
            for i in range(n):
                self.all_values.append([])
                for j in range(m):
                    self.all_values[i].append(values[count])
                    count+=1

        # If array is 1D
        else:
            for i in range(math.prod(shape)):
                self.all_values.append(values[i])


    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
        return str(self.array_flat)

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """

        # check that the method supports the given arguments (check for data type and shape of array)

        if type(other) == Array and self.shape == other.shape:
            if other.array_type == int or other.array_type == float:
                new_values = [sum(x) for x in zip(self.array_flat, other.array_flat)]
                return Array(self.shape, *tuple(new_values))

            # if the array is a boolean you should return NotImplemented
            else:
                return NotImplemented
        
        elif type(other) == int or type(other) == float:
            new_values = [sum(x) for x in zip(self.array_flat, [other]*math.prod(self.shape))]
            return Array(self.shape, *tuple(new_values))

        else:
            return NotImplemented

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
        if type(other) == Array and self.shape == other.shape:
            if other.array_type == int or other.array_type == float:
                new_values = [value1-value2 for (value1,value2) in zip(self.array_flat, other.array_flat)]
                return Array(self.shape, *tuple(new_values))

            else:
                return NotImplemented
        
        elif type(other) == int or type(other) == float:
            new_values = [value1-value2 for (value1,value2) in zip(self.array_flat, [other]*math.prod(self.shape))]
            return Array(self.shape, *tuple(new_values))

        else:
            return NotImplemented

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        """
        if type(other) == Array and self.shape == other.shape:
            if other.array_type == int or other.array_type == float:
                new_values = [value2-value1 for (value1,value2) in zip(self.array_flat, other.array_flat)]
                return Array(self.shape, *tuple(new_values))

            # if the array is a boolean you should return NotImplemented
            else:
                return NotImplemented
        
        elif type(other) == int or type(other) == float:
            new_values = [value2-value1 for (value1,value2) in zip(self.array_flat, [other]*math.prod(self.shape))]
            return Array(self.shape, *tuple(new_values))

        else:
            return NotImplemented

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        if type(other) == Array and self.shape == other.shape:
            if other.array_type == int or other.array_type == float:
                new_values = [value1*value2 for (value1,value2) in zip(self.array_flat, other.array_flat)]
                return Array(self.shape, *tuple(new_values))

            else:
                return NotImplemented
        
        elif type(other) == int or type(other) == float:
            new_values = [value1*value2 for (value1,value2) in zip(self.array_flat, [other]*math.prod(self.shape))]
            return Array(self.shape, *tuple(new_values))

        else:
            return NotImplemented

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
        if type(other) == Array and self.shape == other.shape:
            if self.array_flat == other.array_flat:
                return True
            return False
        return False

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
        if type(other) != Array and type(other) != int and type(other) != float:
            return TypeError

        if type(other) == int or type(other) == float:
            new_values = [value1==value2 for (value1,value2) in zip(self.array_flat, [other]*len(self.array_flat))]
        
        if type(other) == Array and self.shape == other.shape:
            new_values = [value1 == value2 for (value1,value2) in zip(self.array_flat, other.array_flat)]
            return Array(self.shape, *tuple(new_values))
        else:
            raise ValueError("The shape of both array has to be equal")

    def min_element(self):
        """Returns the smallest value of the array.
        Only needs to work for type int and float (not boolean).
        Returns:
            float: The value of the smallest element in the array.
        """
        if self.type is int or self.type is float:
            return float(min(self.array_flat))
        else:
            raise TypeError("Array needs to consist of either integer of float values")

    def mean_element(self):
        """Returns the mean value of an array
        Only needs to work for type int and float (not boolean).
        Returns:
            float: the mean value
        """
        if self.type == int or self.type == float:
            return float(sum(self.array_flat)/len(self.array_flat))