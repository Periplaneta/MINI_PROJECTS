'''
/////////////////////////////////////////////////////
-----------------------------------------------------
By: Isaac Obo Enimil
Mail: isaacoboenimil@gmail.com
linkedIn:linkedin.com/in/isaac-obo-enimil-2a2354223
-----------------------------------------------------
/////////////////////////////////////////////////////

----------------------------------------------------
This reversal algorithm reverses every sequence that
is passed as an argument to the function.
--------------------------------------------------
'''


# Define a reversal function.
def reversal(sequence):
    # Assigning pointers
    tail_pointer = len(sequence) - 1
    head_pointer = 0

    # Checking if the tail_pointer is greater than the head_pointer.
    while head_pointer < tail_pointer:

        # Swapping elements in the list
        sequence[head_pointer], sequence[tail_pointer] = sequence[tail_pointer], sequence[head_pointer]
       
        # changing the location of the pointers.
        tail_pointer -= 1
        head_pointer += 1

    # Returning the modified sequence.
    return sequence



