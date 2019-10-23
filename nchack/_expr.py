
from ._cleanup import cleanup
from ._runthis import run_this
import sys


def fix_expr(expr):
    """Function to fix expressions that use locals"""

    expr = ''.join((' {} '.format(el) if el in '=><+-/*^()' else el for el in expr))
    expr_split = expr.split(" ")
    new_expr = ""

    for x in expr_split:
        if x.startswith("@"):
            # We need to first check the local variable supplied is a numeric
            if (isinstance(eval("sys.modules['__main__']." + x.replace("@", "")), (int, float))) == False:
                raise ValueError(x +  " is not numeric!")
            new_expr +=  str(eval("sys.modules['__main__']." + x.replace("@", "")))
        else:
            new_expr +=  x
    return new_expr

def expression(self, operations = None, method = "expr", cores = 1):
    """Method to modify a netcdf file using expr"""

    if type(operations) is not dict:
        raise ValueError("No expression was provided")

    # first,we need to convert the operations dictionary to a cdo expression 

    expr = []

    for key,value in operations.items():
        expr.append(key + "=" + fix_expr(value))
        
    expr = ";".join(expr)
    expr = expr.replace(" ", "" )
    expr = '"' + expr + '"'


    cdo_command = "cdo -" + method + "," + expr
    run_this(cdo_command, self, output = "ensemble", cores = cores)
    
    cleanup(keep = self.current)    


def transmute(self, operations = None, cores = 1):
    """
    Create new variables using mathematical expressions, and drop original variables 

    Parameters
    -------------
    operations : dict 
        operations to apply. The keys are the new variables to generate. The values are the mathematical operations to carry out. 
    cores: int
        Number of cores to use if files are processed in parallel. Defaults to non-parallel operation 

    Returns
    -------------
    nchack.NCData
        Reduced tracker with the new variables
    """
    return expression(self, operations = operations, method = "expr", cores = cores)


def mutate(self, operations = None, cores = 1):
    """
    Create new variables using mathematical expressions, and keep original variables 

    Parameters
    -------------
    operations : dict 
        operations to apply. The keys are the new variables to generate. The values are the mathematical operations to carry out. 
    cores: int
        Number of cores to use if files are processed in parallel. Defaults to non-parallel operation 

    Returns
    -------------
    nchack.NCData
        Reduced tracker with the new variables
    """
    return expression(self, operations = operations, method = "aexpr", cores = cores)



