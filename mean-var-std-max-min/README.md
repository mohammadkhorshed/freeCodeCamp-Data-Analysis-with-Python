# Mean-Variance-Standard Deviation Calculator

This is a Python project developed for [freeCodeCamp's Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/) course. The project implements a function that calculates various statistical measures (mean, variance, standard deviation, max, min, and sum) for a given 3×3 matrix derived from a 9-element list.

## 📊 What It Does

The function `calculate()` takes a list of **exactly nine numbers**, reshapes it into a 3x3 NumPy array, and returns a dictionary containing the following statistics:

- **Mean**
- **Variance**
- **Standard Deviation**
- **Maximum**
- **Minimum**
- **Sum**

For each of these measures, results are provided in three formats:
- Across columns (axis 0)
- Across rows (axis 1)
- Flattened (entire matrix)

---

## 🧮 Example

```python
>>> calculate([0,1,2,3,4,5,6,7,8])
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [...],
  ...
}
```