# Plotestrem

![Python 3](https://img.shields.io/badge/python-3-blue?style=for-the-badge)
![GPLv3.0](https://img.shields.io/github/license/hellmrf/plotestrem?style=for-the-badge)

Small Python script for rapidly fitting data in the context of experimental science. With Plotestrem, you can easily fit (almost) any function and get a beautiful and scalable graph. The axis are completely LaTeX-friendly, so you can use any packages you want. It also means you can use the same font as your main document.

For now, the equation is only generated for linear and exponential fitting, which should be sufficient for many application. Maybe in the future I'll add more support.

This code is quite old, so it's not well-written, but it works.

![Example](docs/example.png)
## Usage

You'll need Python 3 installed and a LaTeX distribution. Then install the package:
```shell
pip install git+https://github.com/hellmrf/plotestrem.git
```

Once you have everything set up, open [`runner.py`](./runner.py), add your data and run.

Yeah, it have no interface. Maybe one day. Who knows.

## Why _Plotestrem_?

It's how a *mineiro* (native of Minas Gerais -- Brasil) would say "Plot this thing". [Here](https://translate.google.com/?source=osdd&sl=pt&text=plota+esse+trem) you can listen a canonical speech, but it's not correct (as it's not *mineiro*).

## Author

Developed by [Heliton Martins](https://t.me/helitonmrf).
