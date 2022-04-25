
import os
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import ticker
import tikzplotlib as tpl

models = ['$DenseNet-scratch$', '$Softmax$', '$VAE_{x}+Softmax$', '$VCCA_{xy}$',
            '$VCCA_{xi}+Softmax$', '$VCCA_{xiy}$', '$VCCA_{xw}+Softmax$', '$VCCA_{xwy}$',
            '$VCCA_{xiw}+Softmax$', '$VCCA_{xiwy}$']
acc_means = [67.33, 71.67, 69.20, 70.72,
             77.02, 77.22, 75.37, 74.72, 
             77.51, 77.78]
acc_stds = [1.35, 0.28, 0.46, 0.56,
            0.51, 0.55, 0.46,  0.85, 
             0.51, 0.45]

acc_coarse_means = [75.67, 83.34, 81.24, 82.12,
                    86.46, 86.54, 86.00, 85.59, 
                    86.69, 86.88]
acc_coarse_stds = [1.15, 0.32, 0.63, 0.61, 
                    0.42, 0.51, 0.32, 0.78, 
                    0.41, 0.47]

colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:green', 
            'tab:red', 'tab:red', 'tab:purple', 'tab:purple', 
            'tab:pink', 'tab:pink',]#['b', 'g', 'r', 'r', 'c', 'c', 'm', 'm', 'y', 'y']
patterns = ['', '', '', '///', '', '///', '', '///', '', '///']

fig, ax = plt.subplots()
for i in range(len(models)):
    ax.bar(i, acc_means[i], width=0.5, color=colors[i], edgecolor='black', hatch=patterns[i], label=models[i], alpha=0.85, yerr=acc_stds[i])
ax.set_ylim(60, 80)
ax.grid(axis='y')
ax.set_ylabel('Accuracy (%)')
ax.set_xlabel('Models')
ax.set_xticklabels([])
ax.legend(ncol=1)
plt.tick_params(bottom=False)
#plt.show()
fig.tight_layout()
tpl.save('accuracy.tex',  # this is name of the file where your code will lie
    axis_width="\\figwidth",  # we want LaTeX to take care of the width
    axis_height="\\figheight",  # we want LaTeX to take care of the height
    # if the figure contains an image in the background (this one doesn't), this is where LaTeX (!) should search for the png.
    tex_relative_path_to_data="./",
    # we want the plot to look *exactly* like here (e.g. axis limits, axis ticks, etc.)
    strict=True,
)
plt.savefig('accuracy.png', format='png')
plt.close()

