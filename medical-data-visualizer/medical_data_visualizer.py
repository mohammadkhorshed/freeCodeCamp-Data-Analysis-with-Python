import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv(r'medical-data-visualizer/medical_examination.csv')

# 2
ibm = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (ibm > 25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars=['cardio'], 
                       value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
                       var_name='Metric', 
                       value_name='Value')


    # 6
    df_cat = None
    

    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
