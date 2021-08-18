import os
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import rcParams
from matplotlib import pyplot as plt

from utils import open_external

def plotestrem(x, y, fit="linear", xlabel="", ylabel="", LaTeX_preamble="", decimal_places=5, scientific_notation=False, path=None, open_after_completed=False):
    # ------- #
    # Fitting #
    # ------- #

    # Function to be fitted
    def lin_func(x, a, b):
        return a * x + b

    def exp_func(x, a, b, c):
        return a * np.exp(-b * x) + c

    if fit_type == "linear":
        func = lin_func
    elif fit_type == "exp":
        func = exp_func
    elif callable(fit_type):
        func = fit_type
    else:
        raise Exception(
            "fit_type should be \"linear\", \"exp\", or a function.")

    # Fit and get uncertainty
    fit, __cov = curve_fit(func, x, y)
    uncert = np.sqrt(__cov.diagonal())

    # Compute R²
    residuals = y - func(x, *fit)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r_squared = 1 - (ss_res / ss_tot)

    # print(fit, __cov, uncert, r_squared)
    # -------- #
    # Plotting #
    # -------- #

    rcParams['mathtext.fontset'] = 'cm'
    # rcParams["font.family"] = "serif"
    rcParams['font.family'] = 'STIXGeneral'
    #rcParams['font.family'] = 'fourier'
    rcParams["savefig.format"] = 'pdf'
    rcParams["text.usetex"] = True
    rcParams["text.latex.preamble"] = r'\usepackage{siunitx}' + LaTeX_preamble

    x_pred = np.linspace(min(x), max(x), 100)

    plt.plot(x_pred, func(x_pred, *fit), color="black", linewidth=0.7)
    plt.plot(x.ravel(), y, 'o', color="navy")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if fit_type == "linear":
        par = [fit[0], uncert[0], fit[1],
               uncert[1]]
        if scientific_notation == True:
            p = ["\\num{" + "{:.{}e}".format(x, decimal_places) + "}" for x in par]
        else:
            p = ["\\num{" + "{:.{}f}".format(x, decimal_places) + "}" for x in par]
        p.append("\\num{" + "{:.4f}".format(r_squared) + "}")
        p = list(map(lambda x: x if x != r"\num{inf}" else r"$\infty$", p))
        params_overlay = ""
        param_table = r'\begin{tabular}{ccc}$ y = ax + b $ & & \\ && \\ \hline Param & Valor & Erro \\ \hline $ a $ & ' + \
            p[0] + r' & ' + p[1] + r' \\ $ b $ & ' + p[2] + r' & ' + p[3] + \
            r' \\ $R^2$ & ' + p[4] + r' & \\ \hline \end{tabular}'
        if fit[0] > 0.0:  # choose if table will be on the left or on the right
            plt.text(min(x), max(y), param_table, va="top",
                     ha="left", multialignment="left")
        else:
            plt.text(max(x), max(y), param_table, va="top",
                     ha="right", multialignment="left")
    elif fit_type == "exp":
        par = [fit[0], uncert[0], fit[1],
               uncert[1], fit[2],
               uncert[2]]
        if scientific_notation == True:
            p = ["\\num{" + "{:.{}e}".format(x, decimal_places) + "}" for x in par]
        else:
            p = ["\\num{" + "{:.{}f}".format(x, decimal_places) + "}" for x in par]
        p.append("\\num{" + "{:.4f}".format(r_squared) + "}")
        p = list(map(lambda x: x if x != r"\num{inf}" else r"$\infty$", p))
        params_overlay = ""
        param_table = r'\begin{tabular}{ccc} \multicolumn{3}{l}{$ y = a \cdot e^{-bx} + c $} \\ && \\ \hline Param & Valor & Erro \\ \hline $ a $ & ' + \
            p[0] + r' & ' + p[1] + r' \\ $ b $ & ' + p[2] + r' & ' + p[3] + \
            r'\\ $ c $ & ' + p[4] + r' & ' + p[5] +\
            r' \\ $R^2$ & ' + p[6] + r' & \\ \hline \end{tabular}'

        # plt.text(min(x)-0.03, max(y), param_table,
        #          va="top", ha="left", multialignment="left")
        plt.text(min(x), max(y), param_table,
                 va="top", ha="left", multialignment="left")

    if os.path.isdir(path):
        path = os.path.join(path, "graph.pdf")
    if os.path.isdir(os.path.dirname(path)):
        path = path
    else:
        path = "graph.pdf"

    # path = path if os.path.isdir(os.path.dirname(path)) else "graph.pdf"
    plt.savefig(path, format="pdf", bbox_inches='tight')

    if open_after_completed:
        # os.system(f"xdg-open \"{path}\"")
        open_external(path)


if __name__ == '__main__':
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([2 * xi + (random() - 0.5) for xi in x]) # y = 2x + noise

    fit_type = "linear"  # "linear", "exp", or a lambda function to be fitted

    # Define the labels for the plot. LaTeX input is allowed.
    xlabel = r'$ \ln\left(C_f / \si{\gram\per\liter}\right) $'
    ylabel = r"$ \ln x $"

    LaTeX_preamble = r"\usepackage{amsmath}\usepackage{stix}\usepackage[version=4]{mhchem}\usepackage{siunitx}"

    decimal_places = 3  # Default:5
    scientific_notation = False

    # Set the path to save the figure.
    path = "~/Documents/graph.pdf"
    open_after_completed = True
    plotestrem(x, y, fit=fit_type, xlabel=xlabel, ylabel=ylabel, LaTeX_preamble=LaTeX_preamble, decimal_places=decimal_places,
               scientific_notation=scientific_notation, path=path, open_after_completed=open_after_completed)
