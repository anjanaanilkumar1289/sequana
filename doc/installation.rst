.. _installation:

Installation
##########################################

If you are a developer, you would want to install **Sequana** from source.
There are lots of dependencies that require compilation and may be time
consuming. We therefore recommend the **Anaconda** solution. Sequana is indeed
available on **bioconda** for python 3.7.3 (and below). Note, however, that
releases of Sequana are also available on Pypi so you could also use **pip**. 

If you just want to test **Sequana** or **Sequanix** or one of the Sequana
standalone, we also provide **Singularity** containers. This is a great 
solution for reproducibility as well. Containers are
available on https://singularity-hub.org/collections/114/. 

.. topic:: Design choice

    Since version 0.8.0, we decided to move the pipelines outside of the main 
    sequana library. This choice was made to face the increase of pipelines
    available in the Sequana project. Indeed, each pipeline comes with its own
    dependencies, which are not neccesseraly Python. The full installation of
    Sequana started to be cumbersome even for experienced users. We dealt with this
    issue using bioconda. Yet, even with such solutions it started to be
    difficult to manage easy installation. So, as usual, divide and conquer:
    each pipeline has now its own life cycle outside of Sequana. For example,
    the variant calling pipeline is hosted on
    https://github.com/sequana/variant_calling. This way, you can install
    Sequana quite easily using pip, or bioconda, or virtual environment as shown
    here below.


Latest recommended installation method
======================================

Sequana is maintained under Python 3.6 (March 2020) and is known to work under
Python 3.7.3 and **under**, not beyond due to PyQt library not yet available
(bug-free) beyond Python 3.7.3.

Lots of dependencies have been dropped in version 0.8.0 so that you could simply
use pip to install Sequana and we can also provide biocontainer or BioConda. 

First you should create a virtual environment so as to not interfer with your own environment. 
We will use conda for that::

    conda create --name sequana_env python=3.7.3
    source activate sequana_env

.. warning:: we strongly recommend to use Python version 3.7.3 or below so that 
   you can beneficiate from Sequanix interface. 

pip installation
----------------

::

    pip install sequana==0.8.2
    pip install packaging   # for v0.8.0 only, fixed in later versions

This will install the dependencies such as Pandas, Numpy, etc. It will take about
5-10 minutes to install this version.

.. note:: If you want to use Sequanix, which rely on PyQt5, please install PyQt5 using conda::

        conda install -c anaconda qt pyqt>5

    Using pip may lead to compatibility issues with your underlying Qt library,
    which must be available to install PyQt

bioconda installation
-----------------------

::

    conda install sequana==0.8.2

.. note:: see below for more information about bioconda installation (e.g., how to set
   up the channels)

pipelines
----------
Whatever is the installation method you choose, you can now install a specific pipeline as follows::

    pip install sequana_rnaseq

The dependencies of this pipeline must be dealt with by the developer or users.


Other solutions (not always up-to-date)
========================================

#. Singularity (tested with version 2.4.2; see below for installation) . Strictly speaking, there is no compilation. This method is for testing and production. It downloads an image / container that is ready-to-use (here the latest available release)::

      singularity pull --name sequana.img shub://sequana/sequana

   and can be used as follows (for example)::

      singularity exec sequana.img sequanix --help

   See :ref:`Singularity <singularity_details>` section to install a specific release and more details.

#. Bioconda. **Sequana** is available on conda/bioconda as a pre-compiled package::

       conda install sequana

#. From source. If you prefer to install everything yourself, the source code is available on
   github (http://github.com/sequana/sequana) and releases are posted on Pypi::

        pip install sequana

These three methods are detailled hereafter.

.. _installation_conda:


From bioconda 
==============

If you have not installed **Sequana**, be aware that many dependencies need to 
be compiled (i.e., time consumming and requires proper C compilator).
Besides, many pipelines rely on third-party software such as BWA or samtools that are not
Python libraries. We therefore recommend to use **conda** that provides pre-compiled 
software for you.

Install conda executable
----------------------------

In practice, we do use `Anaconda <https://conda.readthedocs.io/>`_ . We recommend to
install **conda** executable via the manual installer (`download <https//continuum.io/downloads>`_). 
You may have the choice between Python 2 and 3. We recommend to choose a Python version 3.

Add bioconda channels
------------------------

When you want to install a new package, you have to use this type of syntax::

    conda install ipython

where **ipython** is the package you wish to install. Note that by default,
**conda** looks on the official Anaconda website (channel). However, there are
many channels available. We will use the **bioconda** channel. To use it, type
these commands (once for all)::

    conda config --add channels r
    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda

.. warning:: **it is important to add them in this order**, as mentionned on bioconda webpage
    (https://bioconda.github.io/).

If you have already set the channels, please check that the order is correct.
With the following command::

    conda config --get channels

You should see::

    --add channels 'r'   # lowest priority
    --add channels 'defaults'
    --add channels 'conda-forge'
    --add channels 'bioconda'   # highest priority

Create an environement
-------------------------

Once **conda** is installed and the channels set, open a new shell.
Although this is not required strictly speaking, we would
recommend to create an environment dedicated to Sequana. This environment can
later be removed without affecting your system or conda installation. A
**conda** environment is nothing else than a directory and can be created as
follows::

    conda create --name sequana_env python=3.7.3

Then, since you may have several environments, you must activate the **sequana**
environment itself (each time you open a new shell)::

    source activate sequana_env


Installation
-------------------

Sequana is on `bioconda <https://bioconda.github.io/>`_. You can follow these `instructions <http://bioconda.github.io/recipes/sequana/README.html>`_ or type::

    conda install sequana



From Pypi website (released source code)
==========================================
If you do not want to use **conda**, we provide releases on the Python Package Index website (pip tool)::

    pip install sequana
    pip install PyQt5


.. warning:: we do not support this methods but it should work. The main
    issues being that you will need to install the dependencies yourself. See
    hereafter for some of the tool used by the pipelines


From GitHub Source code
===========================

Finally, if you are a developer and wish to use the latest code, you 
can install **sequana** from source::

    conda create --name sequana python=3.7.3
    source activate sequana
    git clone git@github.com:sequana/sequana.git
    cd sequana
    python setup.py install

    # to use sequanix interface:
    conda install -c anaconda qt pyqt>5

    # to perform testing and documentation:
    pip install -r requirements_dev.txt


This should install most of the required dependencies. However, you may need to
install more packages depending on the pipeline used (related to Qt for
instance).

.. _singularity_details:

Singularity
============
.. warning:: this is now up-to-date. Come back later or contribute to this
   section.

We provide Singularity images on https://singularity-hub.org/collections/114/ .
They contain Sequana standalones and some of the pipelines dependencies
as well as Sequanix. Note, however, that Sequanix relies on PyQt (graphical
environment) and would work for Linux users only for the time being. The main
reason being that under Mac and windows a virtualbox is used by Singularity
preventing a X connection. 

First, install singularity (http://singularity.lbl.gov/). You must use at least
version 3.5. We suggest users to look at the l=singularity installation page
itself to install the tool.
 
Once done, you can either build an image yourself or download a Sequana image. 
For instance, for the latest master version::

    singularity pull --name sequana.img shub://sequana/sequana:latest

or for the release 0.6.3::

    singularity pull --name sequana_0_6_3.img shub://sequana/sequana:0_6_3

The term latest in Singularity Hub will pull, across all of your branches and
tags, the most recent image, so if you come back in a year and get the latest (or ommit tha tag), you may not get the same container ! So, it is best using a specific tag. 

Do not interrupt the download (1.5Go). Once downloaded,
you can use, for instance, the sequana_coverage executable::

    singularity exec sequana.img sequana_coverage --help

or sequanix::

    singularity exec sequana.img sequanix

Would you miss a dependency, just enter into the singularity container and install the missing dependencies. You will need writable permission::

    sudo singularity shell -w sequana.img

Then, inside the container, install or fix the problem and type exit to save the
container.

.. note:: you may need to install squashfs-tools (e.g. yum install squashfs-tools )


.. .. include:: ../docker/README.rst






