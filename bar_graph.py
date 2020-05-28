"""
This script plots Vertical Bar Graph and Horizontal Bar Graph.
    
Reference:
    Stack Overflow
"""

import numpy as np
import matplotlib.pyplot as plt

save_path = r'C:\Users\Desktop\img_'

print("\nEnter '0' to plot Vertical Bar Graph\nEnter '1' to plot Horizontal Bar Graph")
mode = int(input("\nEnter the (0 or 1): "))

if mode == 0:
    N = 5
    ind = np.arange(N)  
    width = 0.13        # width of the bars
    
    fig = plt.figure(figsize=(8, 5)) # width, height
    ax = fig.add_subplot(111)
    
    Dataset_1 = [1285, 1759, 312, 608, 1036]
    red_bar = ax.bar(ind, Dataset_1, width, color='r')
    
    Dataset_2 = [1464, 697, 1025, 555, 1804]
    blue_bar = ax.bar(ind+width, Dataset_2, width, color='b')
    
    Dataset_3 = [1321, 1549, 557, 662, 911]
    green_bar = ax.bar(ind+width+width, Dataset_3, width, color='g')
    
    ax.set_xlabel('Age')
    ax.set_ylabel('Number of People')
    ax.set_xticks(ind+width)
    ax.set_xticklabels(('>= 30', '>= 50', '>=70 ', '>= 80', '>= 90'))
    plt.title('City Population Division', fontsize=14)
    ax.legend((red_bar[0], blue_bar[0], green_bar[0]), ('Dataset_1', 'Dataset_2', 
              'Dataset_3'), loc = 9, prop={'size': 14})
    
    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            v = str(round(h, 2))
            ax.text(rect.get_x()+rect.get_width()/2., 1.0*h, v,
                    ha='center', va='bottom')
    
    autolabel(red_bar)
    autolabel(blue_bar)
    autolabel(green_bar)
    
    plt.show()
    save_path = save_path +'vertical_bar_graph.png'
    plt.savefig(save_path, bbox_inches='tight')
    
else:
    N = 5
    ind = np.arange(N) 
    height = 0.13        # height of the bars
    
    fig = plt.figure(figsize=(8, 5)) # width, height
    
    ax = fig.add_subplot(111)
    
    Dataset_1 = [1285, 1759, 312, 608, 1036]
    red_bar = ax.barh(ind+height+height, Dataset_1, height, color='r')
    
    Dataset_2 = [1464, 697, 1025, 555, 1804]
    blue_bar = ax.barh(ind+height, Dataset_2, height, color='b')
    
    Dataset_3 = [1321, 1549, 557, 662, 911]
    green_bar = ax.barh(ind, Dataset_3, height, color='g')
    
    ax.set_xlabel('Number of People')
    ax.set_ylabel('Age')
    ax.set_yticks(ind+height)
    ax.set_yticklabels(('>= 30', '>= 50', '>=70 ', '>= 80', '>= 90'))
    plt.title('City Population Division', fontsize=14)
    ax.legend((red_bar[0], blue_bar[0], green_bar[0]), ('Dataset_1', 'Dataset_2', 
              'Dataset_3'), loc = 4, prop={'size': 14})
    
    def autolabel(rects):
        for rect in rects:
            w = rect.get_width()
            v = str(round(w, 2))
            ax.text(1.0*w, rect.get_y()+rect.get_height()/2, v,
                    ha='left', va= 'center')
    
    autolabel(red_bar)
    autolabel(blue_bar)
    autolabel(green_bar)
    
    plt.show()
    save_path = save_path +'horizontal_bar_graph.png'
    plt.savefig(save_path, bbox_inches='tight')
