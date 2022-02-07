import os
from typing import Union, Callable
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import rcParams
from matplotlib import pyplot as plt

from .utils import open_external


def __process_table_header(header) -> str:
    if type(header) == str:
        # Try to detect the separator
        parts = header.split('&')
        if len(parts) == 3:
            return header

        parts = header.split(',')
        if len(parts) == 3:
            return " & ".join(parts)
    elif type(header) == list:
        return " & ".join(header)
    # Fallback
    return "Param & Value & Error"


def __process_fit_type(fit_type: Union[str, Callable]) -> Callable:
    """Get a fit type and return the processed thing 

    Args:
        fit_type (Any): "linear", "exp" or a function to be fitted.
    """
    def lin_func(x, a, b):
        return a * x + b

    def exp_func(x, a, b, c):
        return a * np.exp(-b * x) + c

    if fit_type == "linear":
        return lin_func
    elif fit_type == "exp":
        return exp_func
    elif callable(fit_type):
        return fit_type
    elif fit_type == "none":
        return lambda x: None
    else:
        raise Exception(
            "fit_type should be \"linear\", \"exp\", or a function.")

def R2(x: Union[list, np.ndarray], y: Union[list, np.ndarray], f: Callable, *fit) -> float:
    residuals = y - f(x, *fit)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r_squared = 1.0 - (ss_res / ss_tot)
    return r_squared

def plotestrem(x,
               y,
               fit_type: Union[str, Callable] = "linear",
               xlabel: str = "",
               ylabel: str = "",
               LaTeX_preamble: str = "",
               decimal_places: int = 5,
               scientific_notation: bool = False,
               path: str = None,
               open_after_completed: bool = False,
               table_header: Union[str, list, None] = None):
    table_header = __process_table_header(table_header)

    rcParams['mathtext.fontset'] = 'cm'
    rcParams["font.family"] = "serif"
    # rcParams['font.family'] = 'STIXGeneral'
    #rcParams['font.family'] = 'fourier'
    rcParams["savefig.format"] = 'pdf'
    rcParams["text.usetex"] = True
    rcParams["text.latex.preamble"] = r'\usepackage{siunitx}' + LaTeX_preamble


    if str(fit_type).lower() != "none":
        # ------- #
        # Fitting #
        # ------- #
        func = __process_fit_type(fit_type)
        # Fit and get uncertainty
        fit, __cov = curve_fit(func, x, y)
        uncert = np.sqrt(__cov.diagonal())

        r_squared = R2(x, y, func, *fit)

        # print(fit, __cov, uncert, r_squared)

        x_pred = np.linspace(min(x), max(x), 100)

    # -------- #
    # Plotting #
    # -------- #
    if str(fit_type).lower() != "none":
        plt.plot(x_pred, func(x_pred, *fit), color="black", linewidth=0.7)
    plt.plot(x.ravel(), y, 'o', color="navy")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if fit_type == "linear":
        par = [fit[0], uncert[0], fit[1],
               uncert[1]]
        if scientific_notation == True:
            p = [
                "\\num{" + "{:.{}e}".format(x, decimal_places) + "}" for x in par]
        else:
            p = [
                "\\num{" + "{:.{}f}".format(x, decimal_places) + "}" for x in par]
        p.append("\\num{" + "{:.4f}".format(r_squared) + "}")
        p = list(map(lambda x: x if x != r"\num{inf}" else r"$\infty$", p))
        params_overlay = ""
        param_table = r'\begin{tabular}{ccc}$ y = ax + b $ & & \\ && \\ \hline ' + table_header + r' \\ \hline $ a $ & ' + \
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
        param_table = r'\begin{tabular}{ccc} \multicolumn{3}{l}{$ y = a \cdot e^{-bx} + c $} \\ && \\ \hline ' + table_header + r' \\ \hline $ a $ & ' + \
            p[0] + r' & ' + p[1] + r' \\ $ b $ & ' + p[2] + r' & ' + p[3] + \
            r'\\ $ c $ & ' + p[4] + r' & ' + p[5] +\
            r' \\ $R^2$ & ' + p[6] + r' & \\ \hline \end{tabular}'
        # plt.text(min(x)-0.03, max(y), param_table,
        #          va="top", ha="left", multialignment="left")
        plt.text(min(x), max(y), param_table,
                 va="top", ha="left", multialignment="left")

    elif str(fit_type).lower() != "none":
        r2 = "\\num{" + "{:.4f}".format(r_squared) + "}"
        param_table = r'\begin{tabular}{ccc} \hline ' + table_header + r' \\ \hline' + \
            r'$R^2$ & ' + r2 + r' & \\ \hline \end{tabular}'
        plt.text(min(x), max(y), param_table, va="top", ha="left", multialignment="left")

    if os.path.isdir(str(path)):
        path = os.path.join(path, "graph.pdf")
    if os.path.isdir(os.path.dirname(str(path))):
        path = path
    else:
        path = "graph.pdf"

    # path = path if os.path.isdir(os.path.dirname(path)) else "graph.pdf"
    plt.savefig(path, format="pdf", bbox_inches='tight')

    if open_after_completed:
        # os.system(f"xdg-open \"{path}\"")
        open_external(path)
