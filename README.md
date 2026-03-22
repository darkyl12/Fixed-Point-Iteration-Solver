# 📌 Fixed Point Iteration Solver

This project implements the **Fixed Point Iteration Method** in Python to approximate the root of a function.

---

## 📖 About the Method

The Fixed Point Iteration method solves equations of the form:

g(x) = x

In this implementation, we use:

g(x) = f(x) + x

The algorithm repeatedly updates the value of x until the result converges within a given tolerance.

---

## ⚙️ How It Works

1. Start with an initial guess (x₀)
2. Compute:
   - f(x₀)
   - g(x₀) = f(x₀) + x₀
3. Update x₀ → g(x₀)
4. Repeat until:
   - |f(x₀)| < tolerance  
   OR  
   - Maximum iterations reached

---

## ▶️ How to Run

1. Run the script:
```bash
python main.py
```

2. Enter:
- A function f(x)
- Initial guess (x₀)

---

## 🧪 Example

### Input:
```
Enter a function f(x): (3 - x)/2
Enter the (x0): 1
```

### Output:
```
Counter 0: x0 = 1.0000, f(x0) = 1.0000, g(x0) = 2.0000
Counter 1: x0 = 2.0000, f(x0) = 0.5000, g(x0) = 2.5000
Counter 2: x0 = 2.5000, f(x0) = 0.2500, g(x0) = 2.7500
Counter 3: x0 = 2.7500, f(x0) = 0.1250, g(x0) = 2.8750
Counter 4: x0 = 2.8750, f(x0) = 0.0625, g(x0) = 2.9375
```

---

## ⚠️ Notes

- Not all functions converge.
- The choice of function and initial guess is very important.
- The method works best when the function is well-behaved near the root.

---

## 💡 Tips

- Try different initial values (x₀) to see how it affects convergence.
- Use simple functions for better stability.
- Avoid functions that diverge or oscillate.

---

## 🚀 Future Improvements

- Add plotting of iterations
- Add convergence visualization
- Improve input safety instead of using `eval`
- Display error at each iteration

---

## 👨‍💻 Author
BY yousef lotfy
Created as a numerical methods project using Python.
