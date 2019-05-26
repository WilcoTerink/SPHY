===============
Running a model
===============

This section describes how you can run the SPHY model. How-to run the model depends on the way you have installed
the SPHY model:

    1. Installation via :ref:`Anaconda <installation_anaconda>` or :ref:`pip <installation_pip>`
    
    2. Installation using the download from the :ref:`GitHub repository <installation_github>`
    
See ONE of the sections below for how-to run your SPHY model depending on the chosen installation method.


Running the model with an Anaconda or pip installation
------------------------------------------------------

If you have installed the SPHY model via Anaconda or pip, then you can run the SPHY model from any location
on your PC; i.e. you do not need to refer to the physical address where the SPHY model source code resides.
This is an advantage, because you do not need to copy all the model's source code files everytime you start
a new project.

The steps that are needed to run the model are:

  1. Create a folder somewhere on your hard drive, e.g. ``c:\my_model``
  
  2. After you have installed the model via Anaconda or pip, the ``SPHY_config.cfg`` configuration template can be found under:
  
     ``PATH-TO-YOUR-PYTHON-INSTALLATION\Lib\site-packages\SPHY\SPHY_config.cfg``
     
     Copy ``SPHY_config.cfg`` to the folder you created under step 1
     
     
  3. You can edit the ``SPHY_config.cfg`` and set all the variables in this configuration file
  
  4. After you have edited and saved ``SPHY_config.cfg``, you can run the model by::

         python -m SPHY.main -i c:\my_model\SPHY_config.cfg   


Running the model with the GitHub download installation
-------------------------------------------------------

If you have downloaded the source code from the `SPHY model GitHub repository <https://github.com/WilcoTerink/SPHY>`_, then you always
need to work from the folder where you have extracted the model's source code files; i.e. every time you start a new project you
have to copy the source code files to the new project folder.

The steps that are needed to run the model are:

  1. Create a folder somewhere on your hard drive, e.g. ``c:\my_model``
  
  2. Copy all the model source code files to the folder created under step 1
  
  3. You can edit the ``SPHY_config.cfg`` and set all the variables in this configuration file
  
  4. Save the ``SPHY_config.cfg`` file
  
  5. You can now run the model via:: 
  
         python c:\my_model\sphy.py -i c:\my_model\SPHY_config.cfg
         


    

