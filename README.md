xdiag_magic_extension
=====================

This is an [IPython](http://ipython.readthedocs.io/)/[Jupyter](http://jupyter.org/) ([notebook](http://jupyter-notebook-beginner-guide.readthedocs.io/)) extension,
providing [custom magics](http://ipython.readthedocs.io/en/stable/config/custommagics.html)
for [blockdiag](http://blockdiag.com/), and is inspired by
[this gist](https://gist.github.com/douzepouze/48fcae6f45e685ceb9db).

__Warning__: consider this code to be _alpha_-quality. No tests, just a proof-of-concept. You have been warned.

Usage
-----

activate your virtualenv, then

    git clone ... && cd ...
    pip install -r requirements.txt
    pip install -e .

in your Jupyter notebook:

    %load_ext xdiag_magic
    %xdiag_output_format svg
    %%blockdiag
    {
        A -> B -> C
    }
