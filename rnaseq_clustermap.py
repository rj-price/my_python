#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def clustermap_plot(file=None):
    
    df = pd.read_csv(sys.argv[1], sep='\t', index_col=0)

    sns.set(font_scale=1.8)
    heatmap = sns.clustermap(df, center=0, cmap="vlag", vmin=-3, vmax=3,
                   dendrogram_ratio=(.1, .2),
                   row_cluster = True, col_cluster = False,
                   cbar_pos=(.02, .32, .03, .2),
                   linewidths=.75, figsize=(30, 50))
    heatmap.ax_row_dendrogram.remove()
    heatmap.ax_col_dendrogram.set_visible(False)

    filename = sys.argv[1]
    name = filename.split('.')[0]
    heatmap.savefig(name+".png")

    exit()

if __name__ == '__main__':
    clustermap_plot(sys.argv[1])
