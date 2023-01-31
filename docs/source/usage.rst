.. _usage:

==========
Usage
==========



Execution and the BIDS format
=============================

The general usage of ``bids_atlas`` is rather straightforward as it only requires the user to 
run the `download function` for the `atlas` they want to use and indicate the `respective space` and `resolution`.
The exact command to run ``bids_atlas`` depends on the Installation method and user. Regarding the latter ``bids_atlas`` 
can either be used as a ``command line tool`` or directly within ``python``.

Here's a very conceptual example of running ``bids_atlas`` via ``CLI``: ::

    bids_atlas path/ atlas_name optional_arguments

and here from within ``python``: ::

    from bids_atlas.datasets import atlas_download_function
    path_to_atlas = atlas_download_function(path=download_path, optional_arguments)

Below, we will focus on the ``CLI`` version. Thus, if you are interested in using ``bids_atlas`` directly within ``python``,
please check the `Examples <../../>`_.

Command-Line Arguments
======================
.. argparse::
  :ref: bids_atlas.bids_atlas_cli.get_parser
  :prog: bids_atlas
  :nodefault:
  :nodefaultconst:

Example Call(s)
---------------

Below you'll find two examples calls that hopefully help
you to familiarize yourself with ``bids_atlas`` and its options.

Example 1
~~~~~~~~~

.. code-block:: bash

    bids_atlas \
    /home/user/
    AAL

Here's what's in this call:

- The 1st positional argument is the directory the user wants to store the atlas in (``/home/user``)
- The 2nd positional argument specifies which atlas should be downloaded.
  Here we choose the ``AAL`` atlas.

As we didn't specify the ``target_space`` and ``--resolution`` arguments, the ``atlas`` will be provided 
in the default specification which are ``MNI152NLin6Asym` regarding the ``space`` and ``2mm`` regarding the resolution. 

Example 2
~~~~~~~~~

.. code-block:: bash

    bids_atlas \
    /home/user/ \
    Schaefer100 \
    --resolution 1 

Here's what's in this call:

- The 1st positional argument is the directory the user wants to store the atlas in (``/home/user``)
- The 2nd positional argument specifies which atlas should be downloaded.
  Here we choose the ``Schaefer100`` atlas.
- The 3rd positional argument specifies the resolution the atlas should be provided in. Here ``1mm``.  


Support and communication
=========================

The documentation of this project is found here: https://peerherholz.github.io/bids_atlas.

All bugs, concerns and enhancement requests for this software can be submitted here:
https://github.com/peerherholz/bids_atlas/issues.

If you have a problem or would like to ask a question about how to use ``bids_atlas``,
please submit a question to `NeuroStars.org <http://neurostars.org/tags/bids_atlas>`_ with an ``bids_atlas`` tag.
NeuroStars.org is a platform similar to StackOverflow but dedicated to neuroinformatics.

All previous ``bids_atlas`` questions are available here:
http://neurostars.org/tags/bids_atlas/

Not running on a local machine? - Data transfer
===============================================

Please contact you local system administrator regarding
possible and favourable transfer options (e.g., `rsync <https://rsync.samba.org/>`_
or `FileZilla <https://filezilla-project.org/>`_).

A very comprehensive approach would be `Datalad
<http://www.datalad.org/>`_, which will handle data transfers with the
appropriate settings and commands.
Datalad also performs version control over your data.