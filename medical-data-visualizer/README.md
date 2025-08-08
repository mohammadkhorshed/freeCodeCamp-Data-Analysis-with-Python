# Medical Data Visualizer

This project is part of the [freeCodeCamp Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/) certification. The goal of this project is to process and visualize medical examination data to better understand the relationships and distributions of health-related features.

## 📊 Objective

The project performs data cleaning and generates two key visualizations:
1. **Categorical Plot (catplot)** — showing the distribution of various health metrics for patients with and without cardiovascular disease.
2. **Heat Map** — visualizing correlations between different health metrics after data filtering.

---

## 🗃 Dataset

The dataset used is `medical_examination.csv`, which includes patient data with the following fields:
- Age, gender, height, weight, blood pressure
- Cholesterol and glucose levels
- Lifestyle factors: smoking, alcohol intake, activity
- Cardiovascular disease indicator (`cardio`)

Make sure the dataset is placed at:
```
medical-data-visualizer/medical_examination.csv
```

---

## 🔍 Features and Steps

### ✔️ Data Preprocessing

1. **BMI Calculation**  
   Calculates Body Mass Index (BMI) and creates a new `overweight` column (`1` if BMI > 25, else `0`).

2. **Normalization**  
   Normalizes `cholesterol` and `gluc` values:
   - Values of 1 → 0 (normal)
   - Values > 1 → 1 (elevated)

3. **Data Cleaning**  
   For the heatmap, the data is filtered to remove:
   - Incorrect blood pressure entries (`ap_lo` > `ap_hi`)
   - Extreme outliers in `height` and `weight` (outside 2.5th–97.5th percentile)

---

## 📊 Visualizations

### 🟦 draw_cat_plot()

Creates a categorical plot to show the counts of features (`cholesterol`, `gluc`, `smoke`, `alco`, `active`, `overweight`) for each value (0 or 1), split by `cardio` status.

- Output: `catplot.png`
- Location: `medical-data-visualizer/catplot.png`

#### 📷 Categorical Plot Preview

![Categorical Plot](./medical-data-visualizer/catplot.png)

---

### 🟥 draw_heat_map()

Generates a heatmap of the correlation matrix from the cleaned dataset.

- Output: `heatmap.png`
- Location: `medical-data-visualizer/heatmap.png`

#### 📷 Heatmap Preview

![Heatmap](./medical-data-visualizer/heatmap.png)

---

## 📚 License

This project is part of the freeCodeCamp curriculum and is intended for educational purposes. You are free to reuse and modify it for learning.

---

## 🙋‍♂️ Author

**Mohammad Khorshed**  
GitHub: [@mohammadkhorshed](https://github.com/mohammadkhorshed)