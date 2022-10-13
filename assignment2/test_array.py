"""
Tests for our array class
"""

from array_class import Array

# 1D tests (Task 4)
array1d = Array((6,),1,2,3,4,5,6)
array1d_float = Array((6,),1.0,2.0,3.0,4.0,5.0,6.0)
array1d_bool = Array((6,), True, True, False, True, False, False)

array2d = Array((3,3),1,2,3,4,5,6,7,8,9)
array2d_float = Array((3,3),1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0)
array2d_bool = Array((3,3),True,True,False,False,False,True,False,True,True)


def test_str_1d():
    a = str(array1d)
    assert a == '[1, 2, 3, 4, 5, 6]'


def test_add_1d():
    assert array1d+array1d == Array((6,),2,4,6,8,10,12)
    assert array1d_float+array1d_float == Array((6,),2.0,4.0,6.0,8.0,10.0,12.0)
    assert array1d + array1d_float ==  Array((6,),2.0,4.0,6.0,8.0,10.0,12.0)

    assert array1d+10 == Array((6,),11,12,13,14,15,16)
    assert 100+array1d == Array((6,),101,102,103,104,105,106)
    
    assert array1d+10.5 == Array((6,),11.5,12.5,13.5,14.5,15.5,16.5)
    assert 10.5+array1d == Array((6,),11.5,12.5,13.5,14.5,15.5,16.5)


def test_sub_1d():
    assert array1d-array1d == Array((6,),0,0,0,0,0,0)
    assert array1d_float-array1d_float == Array((6,),0.0,0.0,0.0,0.0,0.0,0.0)
    assert array1d - array1d_float ==  Array((6,),0.0,0.0,0.0,0.0,0.0,0.0)

    assert array1d-10 == Array((6,),-9,-8,-7,-6,-5,-4)
    assert 100-array1d == Array((6,),99,98,97,96,95,94)
    
    assert array1d-10.5 == Array((6,),-9.5,-8.5,-7.5,-6.5,-5.5,-4.5)
    assert 10.5-array1d == Array((6,),9.5,8.5,7.5,6.5,5.5,4.5)
    

def test_mul_1d():
    assert array1d*array1d == Array((6,),1,4,9,16,25,36)
    assert array1d_float*array1d_float == Array((6,),1.0,4.0,9.0,16.0,25.0,36.0)
    assert array1d*array1d_float ==  Array((6,),1.0,4.0,9.0,16.0,25.0,36.0)

    assert array1d*10 == Array((6,),10,20,30,40,50,60)
    assert 100*array1d == Array((6,),100,200,300,400,500,600)
    
    assert array1d*10.5 == Array((6,),10.5,21.0,31.5,42.0,52.5,63.0)
    assert 10.5*array1d == Array((6,),10.5,21.0,31.5,42.0,52.5,63.0)


def test_eq_1d():
    assert array1d == Array((6,),1,2,3,4,5,6)
    assert array1d_float == Array((6,),1.0,2.0,3.0,4.0,5.0,6.0)
    assert array1d_bool == Array((6,), True, True, False, True, False, False)


def test_same_1d():
    assert array1d.is_equal(Array((6,),1,2,3,4,5,6)) == Array((6,),True,True,True,True,True,True)
    assert array1d.is_equal(Array((6,),0,0,0,0,0,0)) == Array((6,),False,False,False,False,False,False)
    assert array1d_float.is_equal(Array((6,),1.0,3.0,10.0,4.0,5.0,100.0)) == Array((6,),True,False,False,True,True,False)
    
def test_smallest_1d():
    assert array1d.min_element() == 1
    assert array1d_float.min_element() == 1.0


def test_mean_1d():
    assert array1d.mean_element() == 3.5
    assert array1d_float.mean_element() == 3.5


# 2D tests (Task 6)


def test_add_2d():
    assert array2d + array2d == Array((3,3),2,4,6,8,10,12,14,16,18)


def test_mult_2d():
    assert array2d_float*array2d_float == Array((3,3),1.0, 4.0, 9.0, 16.0, 25.0, 36.0, 49.0, 64.0, 81.0)
    assert array2d_float*2 == Array((3,3),2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0)


def test_same_2d():
    assert array2d.is_equal(array2d_float) == Array((3,3),True,True,True,True,True,True,True,True,True)
    assert array2d_bool.is_equal(array2d) == Array((3,3),True,False,False,False,False,False,False,False,False)


def test_mean_2d():
    assert array2d.mean_element() == 5


if __name__ == "__main__":
    """
    Note: Write "pytest" in terminal in the same folder as this file is in to run all tests
    (or run them manually by running this file).
    Make sure to have pytest installed (pip install pytest, or install anaconda).
    """

    # Task 4: 1d tests
    test_str_1d()
    test_add_1d()
    test_sub_1d()
    test_mul_1d()
    test_eq_1d()
    test_mean_1d()
    test_same_1d()
    test_smallest_1d()

    # Task 6: 2d tests
    test_add_2d()
    test_mult_2d()
    test_same_2d()
    test_mean_2d()
