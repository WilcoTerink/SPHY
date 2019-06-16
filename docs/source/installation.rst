..  _installation:

============
Installation
============

.. note::

   The SPHY model requires the PCRaster dynamic modelling framework, which needs to be downloaded from:
   
   http://pcraster.geo.uu.nl/
   
   The PCRaster version required for the SPHY model may vary between each SPHY model release. It is
   therefore important to carefully read the :ref:`release notes <releases>` of the SPHY model release you intend to use. 

This page describes how you can install the SPHY model. There are three different ways of installing the model:

   1. Install via :ref:`Anaconda <installation_anaconda>`::
       
       conda install -c WilcoTerink SPHY
   
   2. Install via :ref:`pip <installation_pip>`::
   
       pip install SPHY
   
   3. Downloading the source code from the `SPHY model GitHub repository <https://github.com/WilcoTerink/SPHY>`_
   
Each of these installation methods is described in detail in the sections below. The recommended installation is the
**anaconda** method.


.. _anaconda:

Anaconda
--------

About Anaconda
^^^^^^^^^^^^^^

Anaconda is the world's most popular Python/R data science platform. The open-source Anaconda distribution is the easiest way
to perform Python/R data science and machine learning on Linux, Windows, and Mac OS X. With over 11 million users worldwide, it
is the industry standard for developing, testing, and training on a single machine, enabling individual data scientists to:

    + Quickly download 1,500+ Python/R data science packages
    + Manage libraries, dependencies, and environments with Conda
    + Develop and train machine learning and deep learning models with scikit-learn, TensorFlow, and Theano
    + Analyze data with scalability and performance with Dask, NumPy, pandas, and Numba
    + Visualize results with Matplotlib, Bokeh, Datashader, and Holoviews
    
More information about the Anaconda distribution can be found `here <https://www.anaconda.com/distribution/>`_.

Download Anaconda
^^^^^^^^^^^^^^^^^

It is strongly recommended to use the Anaconda Python distribution to install and manage all your Python packages. The reason for
this is because Anaconda checks for dependencies, installs missing dependencies or updates old depencies if required. Depending on the
SPHY model release, a different Anaconda Python distribution may be required (see :ref:`Releases <releases>`). Use one of the links below to
download the required Anaconda Python distribution:

    + `Python 2.7 version <https://repo.anaconda.com/archive/Anaconda2-2019.03-Windows-x86_64.exe>`_
    
    + `Python 3.7 version <https://repo.anaconda.com/archive/Anaconda3-2019.03-Windows-x86_64.exe>`_
    
.. _installation_anaconda:

Install SPHY using Anaconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have PCRaster and Anaconda installed you can easily install the SPHY model via the command prompt::

    conda install -c WilcoTerink SPHY
    
The command above will always install the most recent SPHY model release. Installing a specific SPHY model release can be achieved by::

    conda install -c WilcoTerink SPHY=2.1.1
    
which in this case installs SPHY model release 2.1.1.

Upgrading an already installed SPHY model distribution to the most recent release can be achieved by::

    conda update -c WilcoTerink SPHY

After you have installed the SPHY model, the SPHY model package resides under::

    PATH-TO-YOUR-ANACONDA-INSTALLATION\Lib\site-packages\SPHY
    

.. _pip:

pip
---

About pip
^^^^^^^^^

pip is the package installer for Python. You can use pip to install packages from the `Python Package Index <https://pypi.org/>`_ and other indexes.
In contrast to Anaconda, which comes with a complete Python installation, pip itself does not contain a Python installation. Therefore,
it is required to have a Python distribution already installed before you can use pip. See the link below for more information on how-to install pip:

    https://pip.pypa.io/en/stable/installing/

.. _installation_pip:

Install SPHY using pip
^^^^^^^^^^^^^^^^^^^^^^

Once you have PCRaster and pip installed you can easily install the SPHY model via the command prompt::

    pip install SPHY
    
The command above will always install the most recent SPHY model release. Installing a specific SPHY model release can be achieved by::

    pip install SPHY==2.1.1
    
which in this case installs SPHY model release 2.1.1.

Upgrading an already installed SPHY model distribution to the most recent release can be achieved by::

    pip install SPHY --upgrade
    
After you have installed the SPHY model, the SPHY model package resides under::

    PATH-TO-PYTHON-INSTALLATION\Lib\site-packages\SPHY


.. _installation_github:

Download from GitHub repository
-------------------------------

Alternatively, you can download the SPHY model from my GitHub repository: 

    https://github.com/WilcoTerink/SPHY/releases

You can download the release you want, and extract the contents to a folder on your hard drive.
The SPHY model can then be run from inside this folder.

Installation by this method, however, is not recommended because it does not check for the dependencies that are required to run the model, whereas the :ref:`Anaconda <anaconda>` and :ref:`pip <pip>`
installation methods do.









