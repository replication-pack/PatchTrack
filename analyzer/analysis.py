import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def all_class_bar(height, plotting=False):
    """
        Bar Chart
    """
    left = [1, 2, 3, 4, 5]
    x_label = ['PA', 'PN', 'NE', 'CC','ERROR']


    plt.figure(figsize=(12,6), dpi=80)
    plt.bar(left, height, tick_label = x_label, width = 0.8, color = ["#377eb8", "#e41a1c", "#ff7f00", "#984ea3", "#a65628"])

    patch1 = mpatches.Patch(color='#377eb8', label='Patch Applied')
    patch2 = mpatches.Patch(color='#e41a1c', label='Patch Not Applied')
    patch3 = mpatches.Patch(color='#ff7f00', label='Not Existing Patch')
    patch4 = mpatches.Patch(color='#984ea3', label='Cannot Classify')
    patch5 = mpatches.Patch(color='#a65628', label='Error')
   
    plt.legend(fontsize=18, loc="upper right" ,handles = [patch1, patch2, patch3, patch4, patch5])
    
    plt.xlabel('Classifications', fontsize=20)
    plt.xticks(fontsize = 14)   
    plt.yticks(fontsize = 14) 
    
    plt.ylabel('Frequency', fontsize=20)
#     plt.savefig("Plots/"+str(pr_nr) + "_All_classes_bar"+".png", format="PNG",  dpi=80, bbox_inches='tight')
    if plotting:
        plt.show()
        