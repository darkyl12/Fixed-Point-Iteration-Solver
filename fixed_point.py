import math

def evaluate_function(func_str, x):
    return eval(func_str)

def fixed_point_iteration(func_str, x0, tol=0.0100,max_iter=5):
    Counter = 0
    g_x0 = x0
    
    while Counter < max_iter :
        f_x0 = evaluate_function(func_str, x0)
        g_x0 = f_x0 + x0  # g(x) = f(x) + x
        
        print(f"Counter {Counter}: x0 = {x0:.4f}, f(x0) = {f_x0:.4f}, g(x0) = {g_x0:.4f}")
    
        
        if abs(f_x0) < tol:
            print(f"Converged to fixed point: {g_x0:.4f} in {Counter + 1} iterations.")
            return g_x0
        
        x0 = g_x0  # Update x0 for the next iteration
        Counter += 1

# Input function from user
func_input = input("Enter a function f(x) ")
x_initial = float(input("Enter the (x0): "))

root = fixed_point_iteration(func_input, x_initial)
print(f"Fixed point found: {root:}")