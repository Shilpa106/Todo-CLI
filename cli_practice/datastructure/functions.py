def distance_travelled(t, u=0, g=9.81):
    """
    Function distance_travelled calculates the distance travelled by an object
    with initial speed u, in a time interval of t, where acceleration due to gravity is g
    input: t (time taken), u (initial speed) g (acceleration due to gravity)
    output: distance travelled
    Example: 
        >>> distance_travelled(1.0)
            4.905
    """
    d=u*t+0.5*g*t**2
    return d
print(distance_travelled(2.0))
print(distance_travelled(2.0, u=1.0))
print(distance_travelled(2.0,g=9.7))
print(distance_travelled(g=9.7,t=2.0))

# scope inside a function is different than the one outside it
# inside function scope ,you can access the outer scope variables but can not change them

def set_name(input_name):
    name = input_name
    print(f"Name inside the function:{name}")

set_name("Shilpi")

def add_char_to_list(char, lst=[]):
    lst.append(char)
    return lst
add_char_to_list('s')
add_char_to_list('h')
add_char_to_list('i')
add_char_to_list('l')
add_char_to_list('p')
# print(''.join(add_char_to_list('r')))
print(add_char_to_list('i'))
