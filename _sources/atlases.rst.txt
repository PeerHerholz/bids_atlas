=======
Atlases
=======

``bids_atlas`` comes with support of a large collection of commonly used publicly available ``atlases``.
In the following you can find a respective list, indicating the atlas, the function to download it and its metadata.

.. dropdown::           AAL 

    .. raw:: html
        :file: _static/AAL_viewer.html
   
   .. grid:: 2
    :outline:

    .. grid-item-card::

        .. dropdown:: Function

            .. code-block:: python

                from bids_atlas.datasets import get_AAL
                AAL_atlas = get_AAL()

    .. grid-item-card::

        .. dropdown:: Meta-data

            .. code-block:: json
            
                {
                    "Name": "Automated Anatomical Labeling Atlas - SPM12 version",
                    "Description": "PLEASE ADD",
                    "BIDSVersion": "PLEASE ADD",
                    "Curators": "PLEASE ADD",
                    "HowToAcknowledge": "PLEASE ADD",
                    "SourceDatasetsURLs": "PLEASE ADD",
                    "License": "PLEASE ADD",
                    "Funding": "PLEASE ADD",
                    "ReferencesAndLinks": "PLEASE ADD",
                    "Species": "PLEASE ADD",
                    "DerivedFrom": "PLEASE ADD",
                    "LevelType": "PLEASE ADD",
                    "SpecialReference": "PLEASE ADD"    
                }

.. dropdown::           Destrieux 

    .. raw:: html
        :file: _static/Destrieux_viewer.html
   
   .. grid:: 2
    :outline:

    .. grid-item-card::

        .. dropdown:: Function

            .. code-block:: python
            
                from bids_atlas.datasets import get_Destrieux
                AAL_atlas = get_Destrieux()

    .. grid-item-card::

        .. dropdown:: Meta-data

            .. code-block:: json
            
                {
                    "Name": "Destrieux cortical deterministic atlas - 2009 version",
                    "Description": "Automatic parcellation of human cortical gyri and sulci using standard anatomical nomenclature",
                    "BIDSVersion": "PLEASE ADD",
                    "Curators": "PLEASE ADD",
                    "HowToAcknowledge": "PLEASE ADD",
                    "SourceDatasetsURLs": "PLEASE ADD",
                    "License": "PLEASE ADD", 
                    "Funding": "PLEASE ADD",
                    "ReferencesAndLinks": ["https://doi.org/10.1093/cercor/bhg087", 
                                        "https://doi.org/10.1016/j.neuroimage.2010.06.010"
                                        ],
                    "Species": "Human",
                    "DerivedFrom": "PLEASE ADD",
                    "LevelType": "PLEASE ADD",
                    "SpecialReference": "PLEASE ADD"
                }
