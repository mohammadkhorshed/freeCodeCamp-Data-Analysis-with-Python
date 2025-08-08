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
                       var_name='variable', 
                       value_name='value')


    # 6
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()
    

    # 7
    graph =  sns.catplot(data=df_cat, kind='bar', x='variable', y='total', hue='value', col='cardio')


    # 8
    fig = graph.fig


    # 9
    fig.savefig(r'medical-data-visualizer/catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))
                 ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize= (12, 12))

    # 15

    sns.heatmap(corr, mask=mask, square=True, annot=True, linewidths=1, fmt="0.1f")

    # 16
    fig.savefig(r'medical-data-visualizer/heatmap.png')
    return fig
