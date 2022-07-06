from plotestrem import plotestrem
import numpy as np

from random import random

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([2 * xi + (random() - 0.5) for xi in x])  # y = 2x + noise

fit_type = "linear"  # "linear", "exp", "none" or a lambda function to be fitted

# Define the labels for the plot. LaTeX input is allowed.
xlabel = r'$ C_f / \si{\gram\per\liter} $'
ylabel = r"$ \ln x $"

LaTeX_preamble = r"\usepackage{amsmath}\usepackage{stix}\usepackage[version=4]{mhchem}\usepackage{siunitx}"

decimal_places = 3  # Default:5
scientific_notation = False

# Set the path to save the figure.
# path = "~/Documents/graph.pdf"
path = "/tmp/a.pdf"

open_after_completed = True
plotestrem(x, y, fit_type=fit_type, xlabel=xlabel, ylabel=ylabel, LaTeX_preamble=LaTeX_preamble, decimal_places=decimal_places,
           scientific_notation=scientific_notation, path=path, open_after_completed=open_after_completed, decimal_marker=".",
           file_format="pdf", table_header=None)
