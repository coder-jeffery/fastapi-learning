class pythonlesson:

# python闭包 

    def outer_function(self, x):
        def inner_function( y):
            return x + y
        return inner_function


tools  = pythonlesson()
add_ten  = tools.outer_function(10)
print(add_ten(5))



