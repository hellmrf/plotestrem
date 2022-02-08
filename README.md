# Plotestrem

[![Python 3](https://img.shields.io/badge/python-3-blue?style=for-the-badge)](https://pypi.org/project/plotestrem)
[![PyPI](https://img.shields.io/pypi/v/plotestrem?style=for-the-badge)](https://pypi.org/project/plotestrem)
[![GPLv3.0](https://img.shields.io/github/license/hellmrf/plotestrem?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0.en.html)

Small Python script for rapidly fitting data in the context of experimental sciences. With Plotestrem, you can easily fit (almost) any function and get a beautiful and scalable graphic. The axes are completely LaTeX-friendly, so you can use any packages you want. It also means you can use the same font as your main document.

For now, the equation is only generated for linear and exponential fitting, which should be sufficient for many applications. Maybe in the future I'll add more support.

This code is quite old, so it's not well-written, but it works.

![Example](docs/example.png)
## Usage

You'll need Python 3 installed and a LaTeX distribution (if you don't have, you can install or use [Google Colab](#google-colaboratory)). Then install the package:
```shell
pip3 install plotestrem
```

Once you have everything set up, open [`runner.py`](./runner.py), add your data and run.

Yeah, it have no interface. Maybe one day. Who knows.

### Fitting types
You can fit the data using three builtin fitters, or provide your own function. You just need to pass `fit_type` accordingly.

- `"linear"`: linear fit, will plot a line and show the parameters for the `y = a * x + b` equation;
- `"exp"`: exponential fit, will plot the exponential function and show the parameters for the `y = a * exp(-b * x) + c` equation;
- `"none"`: no fitting. It just skips the regression. Your data will be plotted as a scatter plot;
- Lastly, you can provide a function (a lambda or just the name of an existing function, without the parenthesis) to be used in the fitting. For now, the program shows only the R² value (not the parameters) for user-defined functions, but this is an interesting feature to have in the future. Also, the function to be passed should be in the form `f(x, *fit)`, with `fit` being the coefficients. For example, a linear function would be passed as a `f(x, a, b)`.

### Google Colaboratory
You _can_ use this package without installing anything (no LaTeX, no Python, nothing) on your machine. To do this, you can use [Google Colaboratory](https://colab.research.google.com/). As Colab has only the most famous packages pre-installed (and hasn't LaTeX), you'll have to run a little code to setup the environment. Just copy the following code in a cell and run, and then use normally, as you would do in your local machine.
```
!apt install texlive-latex-extra texlive-science cm-super dvipng
!pip install plotestrem
```

I suggest using a relative path to save the file, so you can download the PDF going to Files.
You can get an working example [here](https://colab.research.google.com/drive/1wgI9LphKXKSPd4UrwDI_NfGGI6jJDIIS?usp=sharing), copy, and just edit for your needs.

Once you run the code, the graph will show up below the cell. It's a bitmap version of your graphics, but incredibly useful to see what's going on. After you have everything ok, just download the PDF file clicking on Files on Colab's left bar.
## Why _Plotestrem_?

It's how a *mineiro* (native of Minas Gerais -- Brasil) would say "Plot this thing". [Here](https://translate.google.com/?source=osdd&sl=pt&text=plota+esse+trem) you can listen a canonical speech, but it's not correct (as it's not *mineiro*). [This one](https://translate.google.com/?source=osdd&sl=pt&text=plótêss+trem) is a little better.

## Author

Developed by [Heliton Martins](https://t.me/helitonmrf).
