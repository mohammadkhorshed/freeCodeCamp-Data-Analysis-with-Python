# Demographic Data Analyzer

This project is part of the [freeCodeCamp Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/) certification. The goal is to analyze demographic data from the U.S. Census and extract key statistical insights using **Python** and **Pandas**.

## 📈 Objective

The project analyzes a dataset of adults' demographics and returns insights such as:
- Average age of men
- Percentage of people with a Bachelor's degree
- Income distribution among education levels
- Minimum working hours and associated income stats
- Highest-earning country based on income proportion
- Most common occupation for high earners in India

## 🗂 Dataset

The dataset used is [`adult.data.csv`](https://archive.ics.uci.edu/ml/datasets/adult) from the UCI Machine Learning Repository, which contains demographic information such as:
- Age
- Education
- Occupation
- Race
- Hours-per-week
- Salary

Make sure the dataset is saved at:
```
demographic-data-analyzer/adult.data.csv
```

## 🔧 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/mohammadkhorshed/fcc-demographic-data-analyzer.git
cd fcc-demographic-data-analyzer
```

### 2. Install Requirements

```bash
pip install pandas
```

### 3. Run the Script

```bash
python main.py
```

This will:
- Print the calculated statistics
- Automatically run the unit tests to verify output correctness

## 🧪 Unit Tests

Unit tests are included in `test_module.py` and are executed automatically when running `main.py`. They validate:
- Race counts
- Age averages
- Education and income percentages
- Working hours and associated income
- Top-earning countries and occupations

To run the tests manually:

```bash
python -m unittest test_module.py
```

## 📁 File Structure

```
.
├── demographic_data_analyzer.py   # Core analysis logic
├── adult.data.csv                 # Demographic dataset (must be placed here)
├── main.py                        # Entrypoint script to run analysis and tests
├── test_module.py                 # Unit tests
└── README.md                      # Project documentation
```

## 📌 Key Functions

### `calculate_demographic_data(print_data=True)`

- Input: None (reads from CSV file)
- Output: Dictionary of computed demographic statistics
- Optional printout of results

Returned keys:
```python
{
  'race_count': Series,
  'average_age_men': float,
  'percentage_bachelors': float,
  'higher_education_rich': float,
  'lower_education_rich': float,
  'min_work_hours': int,
  'rich_percentage': float,
  'highest_earning_country': str,
  'highest_earning_country_percentage': float,
  'top_IN_occupation': str
}
```

## 📚 License

This project is provided for educational purposes as part of the freeCodeCamp curriculum. Feel free to modify and reuse it for your own learning.

## 🙋‍♂️ Author

**Mohammad Khorshed**  
GitHub: [@mohammadkhorshed](https://github.com/mohammadkhorshed)
