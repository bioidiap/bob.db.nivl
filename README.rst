.. vim: set fileencoding=utf-8 :
.. Tiago de Freitas Pereira <tiago.pereira@idiap.ch>
.. Thu Apr 16 16:39:01 CEST 2015


.. image:: https://img.shields.io/badge/github-master-0000c0.png
   :target: https://github.com/bioidiap/bob.db.ldhf/tree/master
.. image:: https://img.shields.io/badge/original-data--files-a000a0.png
   :target: http://biolab.korea.ac.kr/database/

=======================================================
Long Distance Heterogeneous Face Database (LDHF-DB)
=======================================================

This package contains the access API and descriptions for the `Long Distance Heterogeneous Face Database (LDHF-DB) <http://biolab.korea.ac.kr/database/>`. 
The actual raw data for the database should be downloaded from the original URL. 
This package only contains the Bob accessor methods to use the DB directly from python, with the original protocol of the database.

Long Distance Heterogeneous Face Database (LDHF-DB) is for research on VIS-NIR face recognition.
It includes 100 identities faces captured in both VIS and NIR (at nighttime) in different standoffs: 1m, 60m, 100m and 150m.

This package implements the cross-disntance and cross-spectral evaluation protocol described in the paper::

  D. Kang, H. Han, A. K. Jain, and S.-W. Lee, "Nighttime Face Recognition at Large Standoff: Cross-Distance and Cross-Spectral Matching", Pattern Recognition, Vol. 47, No. 12, 2014, pp. 3750-3766.

.. note::

  This protocol consists of 10-fold cross-validation letting 90 identities for training and 10 for evaluation for each fold.
  The 1m VIS images are used for enrollment and the NIR images with different standoffs (1m, 60m, 100m and 150m) are used for probing.


You would normally not install this package unless you are maintaining it. 
What you would do instead is to tie it in at the package you need to **use** it.
There are a few ways to achieve this:

1. You can add this package as a requirement at the ``setup.py`` for your own
   `satellite package
   <https://github.com/idiap/bob/wiki/Virtual-Work-Environments-with-Buildout>`_
   or to your Buildout ``.cfg`` file, if you prefer it that way. With this
   method, this package gets automatically downloaded and installed on your
   working environment, or

2. You can manually download and install this package using commands like
   ``easy_install`` or ``pip``.

The package is available in two different distribution formats:

1. You can download it from `PyPI <http://pypi.python.org/pypi>`_, or

2. You can download it in its source form from `its git repository
   <https://github.com/bioidiap/bob.db.ldhf>`_.

You can mix and match points 1/2 and a/b above based on your requirements. Here
are some examples:

Modify your setup.py and download from PyPI
===========================================

That is the easiest. Edit your ``setup.py`` in your satellite package and add
the following entry in the ``install_requires`` section (note: ``...`` means
`whatever extra stuff you may have in-between`, don't put that on your
script)::

    install_requires=[
      ...
      "bob.db.ldhf",
    ],

Proceed normally with your ``boostrap/buildout`` steps and you should be all
set. That means you can now import the ``bob.db.cuhk_cufs`` namespace into your scripts.

Modify your buildout.cfg and download from git
==============================================

You will need to add a dependence to `mr.developer
<http://pypi.python.org/pypi/mr.developer/>`_ to be able to install from our
git repositories. Your ``buildout.cfg`` file should contain the following
lines::

  [buildout]
  ...
  extensions = mr.developer
  auto-checkout = *
  eggs = bob.db.cuhk_cufs

  [sources]
  bob.db.cuhk_cufs = git https://github.com/bioidiap/bob.db.cuhk_cufs.git
  ...
