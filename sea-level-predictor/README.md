# 🌊 Sea Level Predictor

This project analyzes historical sea level data to visualize trends and predict future sea level rise using linear regression.

## 📌 Project Overview
The script:
1. Reads historical sea level data from **EPA's sea level dataset**.
2. Creates a scatter plot of the data points.
3. Draws two lines of best fit:
   - **1880–2013**: Uses all available data.
   - **2000–2013**: Focuses on recent trends.
4. Predicts sea level rise up to the year **2050**.
5. Saves the plot as `sea_level_plot.png`.

## How It Works
- **Step 1:** Load data using pandas.
- **Step 2:** Plot the original data points with matplotlib.
- **Step 3:** Perform linear regression with scipy.stats.linregress on both datasets.
- **Step 4:** Plot both regression lines to visualize trends.
- **Step 5:** Save the final graph for review.

## 📊 Example Output
![Sea Level Plot](sea-level-predictor/sea_level_plot.png)

## 🛠️ Requirements
- Python 3.x
- Pandas
- Matplotlib
- SciPy

## 📂 Data Source
Data provided by the [Environmental Protection Agency (EPA)](https://www.epa.gov/).

## 📈 Predictions
The two regression lines allow comparison between long-term and recent trends, offering insights into acceleration or deceleration in sea level rise.

**Author:** Mohammad Khorshed Alam