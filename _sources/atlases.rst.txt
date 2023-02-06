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

.. dropdown::           Harvard-Oxford

    .. dropdown::           deterministic version

        .. raw:: html
            :file: _static/HarvardOxford_deterministic_viewer.html
    
        .. grid:: 2
            :outline:

            .. grid-item-card::

                .. dropdown:: Function

                    .. code-block:: python
                    
                        from bids_atlas.datasets import get_HarvardOxford
                        AAL_atlas = get_HarvardOxford(type='dseg', threshold='25')

            .. grid-item-card::

                .. dropdown:: Meta-data

                    .. code-block:: json
                    
                        {
                            "Name": "Harvard-Oxford parcellations from FSL - deterministic version",
                            "Description": "Harvard-Oxford parcellations from FSL",
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

    .. dropdown::           probabilistic version

        .. raw:: html
            :file: _static/HarvardOxford_deterministic_viewer.html
    
        .. grid:: 2
            :outline:

            .. grid-item-card::

                .. dropdown:: Function

                    .. code-block:: python
                    
                        from bids_atlas.datasets import get_HarvardOxford
                        AAL_atlas = get_HarvardOxford(type='pseg')

            .. grid-item-card::

                .. dropdown:: Meta-data

                    .. code-block:: json
                    
                        {
                            "Name": "Harvard-Oxford parcellations from FSL - probabilistic version",
                            "Description": "Harvard-Oxford parcellations from FSL",
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

.. dropdown::           Talairach 

    .. dropdown::           Gyrus level

        .. raw:: html
            :file: _static/Talairach_gyrus_viewer.html
    
        .. grid:: 2
            :outline:

            .. grid-item-card::

                .. dropdown:: Function

                    .. code-block:: python
                    
                        from bids_atlas.datasets import get_talairach
                        AAL_atlas = get_HarvardOxford(level='gyrus')

            .. grid-item-card::

                .. dropdown:: Meta-data

                    .. code-block:: json
                    
                        {
                            "Name": "Talairach Deterministic atlas",
                            "Description": "PLEASE ADD",
                            "BIDSVersion": "PLEASE ADD",
                            "Curators": "PLEASE ADD",
                            "HowToAcknowledge": "PLEASE ADD",
                            "SourceDatasetsURLs": "PLEASE ADD",
                            "License": "Unknown",
                            "Funding": "PLEASE ADD",
                            "ReferencesAndLinks": ["https://onlinelibrary.wiley.com/doi/abs/10.1002/1097-0193%28200007%2910%3A3%3C120%3A%3AAID-HBM30%3E3.0.CO%3B2-8",
                                                "https://onlinelibrary.wiley.com/doi/abs/10.1002/%28SICI%291097-0193%281997%295%3A4%3C238%3A%3AAID-HBM6%3E3.0.CO%3B2-4"],
                            "Species": "Homo sapiens",
                            "DerivedFrom": "PLEASE ADD",
                            "LevelType": "PLEASE ADD",
                            "SpecialReference": "PLEASE ADD"
                        }

    .. dropdown::           Hemisphere level

        .. raw:: html
            :file: _static/Talairach_hemisphere_viewer.html
    
        .. grid:: 2
            :outline:

            .. grid-item-card::

                .. dropdown:: Function

                    .. code-block:: python
                    
                        from bids_atlas.datasets import get_talairach
                        AAL_atlas = get_HarvardOxford(level='hemisphere')

            .. grid-item-card::

                .. dropdown:: Meta-data

                    .. code-block:: json
                    
                        {
                            "Name": "Talairach Deterministic atlas",
                            "Description": "PLEASE ADD",
                            "BIDSVersion": "PLEASE ADD",
                            "Curators": "PLEASE ADD",
                            "HowToAcknowledge": "PLEASE ADD",
                            "SourceDatasetsURLs": "PLEASE ADD",
                            "License": "Unknown",
                            "Funding": "PLEASE ADD",
                            "ReferencesAndLinks": ["https://onlinelibrary.wiley.com/doi/abs/10.1002/1097-0193%28200007%2910%3A3%3C120%3A%3AAID-HBM30%3E3.0.CO%3B2-8",
                                                "https://onlinelibrary.wiley.com/doi/abs/10.1002/%28SICI%291097-0193%281997%295%3A4%3C238%3A%3AAID-HBM6%3E3.0.CO%3B2-4"],
                            "Species": "Homo sapiens",
                            "DerivedFrom": "PLEASE ADD",
                            "LevelType": "PLEASE ADD",
                            "SpecialReference": "PLEASE ADD"
                        }

    .. dropdown::           Lobe level

        .. raw:: html
            :file: _static/Talairach_lobe_viewer.html
    
        .. grid:: 2
            :outline:

            .. grid-item-card::

                .. dropdown:: Function

                    .. code-block:: python
                    
                        from bids_atlas.datasets import get_talairach
                        AAL_atlas = get_HarvardOxford(level='lobe')

            .. grid-item-card::

                .. dropdown:: Meta-data

                    .. code-block:: json
                    
                        {
                            "Name": "Talairach Deterministic atlas",
                            "Description": "PLEASE ADD",
                            "BIDSVersion": "PLEASE ADD",
                            "Curators": "PLEASE ADD",
                            "HowToAcknowledge": "PLEASE ADD",
                            "SourceDatasetsURLs": "PLEASE ADD",
                            "License": "Unknown",
                            "Funding": "PLEASE ADD",
                            "ReferencesAndLinks": ["https://onlinelibrary.wiley.com/doi/abs/10.1002/1097-0193%28200007%2910%3A3%3C120%3A%3AAID-HBM30%3E3.0.CO%3B2-8",
                                                "https://onlinelibrary.wiley.com/doi/abs/10.1002/%28SICI%291097-0193%281997%295%3A4%3C238%3A%3AAID-HBM6%3E3.0.CO%3B2-4"],
                            "Species": "Homo sapiens",
                            "DerivedFrom": "PLEASE ADD",
                            "LevelType": "PLEASE ADD",
                            "SpecialReference": "PLEASE ADD"
                        }

    .. dropdown::           Tissue level

        .. raw:: html
            :file: _static/Talairach_tissue_viewer.html
    
        .. grid:: 2
            :outline:

            .. grid-item-card::

                .. dropdown:: Function

                    .. code-block:: python
                    
                        from bids_atlas.datasets import get_talairach
                        AAL_atlas = get_HarvardOxford(level='tissue')

            .. grid-item-card::

                .. dropdown:: Meta-data

                    .. code-block:: json
                    
                        {
                            "Name": "Talairach Deterministic atlas",
                            "Description": "PLEASE ADD",
                            "BIDSVersion": "PLEASE ADD",
                            "Curators": "PLEASE ADD",
                            "HowToAcknowledge": "PLEASE ADD",
                            "SourceDatasetsURLs": "PLEASE ADD",
                            "License": "Unknown",
                            "Funding": "PLEASE ADD",
                            "ReferencesAndLinks": ["https://onlinelibrary.wiley.com/doi/abs/10.1002/1097-0193%28200007%2910%3A3%3C120%3A%3AAID-HBM30%3E3.0.CO%3B2-8",
                                                "https://onlinelibrary.wiley.com/doi/abs/10.1002/%28SICI%291097-0193%281997%295%3A4%3C238%3A%3AAID-HBM6%3E3.0.CO%3B2-4"],
                            "Species": "Homo sapiens",
                            "DerivedFrom": "PLEASE ADD",
                            "LevelType": "PLEASE ADD",
                            "SpecialReference": "PLEASE ADD"
                        }

    .. dropdown::           BA level

        .. raw:: html
            :file: _static/Talairach_ba_viewer.html
    
        .. grid:: 2
            :outline:

            .. grid-item-card::

                .. dropdown:: Function

                    .. code-block:: python
                    
                        from bids_atlas.datasets import get_talairach
                        AAL_atlas = get_HarvardOxford(level='gyrus')

            .. grid-item-card::

                .. dropdown:: Meta-data

                    .. code-block:: json
                    
                        {
                            "Name": "Talairach Deterministic atlas",
                            "Description": "PLEASE ADD",
                            "BIDSVersion": "PLEASE ADD",
                            "Curators": "PLEASE ADD",
                            "HowToAcknowledge": "PLEASE ADD",
                            "SourceDatasetsURLs": "PLEASE ADD",
                            "License": "Unknown",
                            "Funding": "PLEASE ADD",
                            "ReferencesAndLinks": ["https://onlinelibrary.wiley.com/doi/abs/10.1002/1097-0193%28200007%2910%3A3%3C120%3A%3AAID-HBM30%3E3.0.CO%3B2-8",
                                                "https://onlinelibrary.wiley.com/doi/abs/10.1002/%28SICI%291097-0193%281997%295%3A4%3C238%3A%3AAID-HBM6%3E3.0.CO%3B2-4"],
                            "Species": "Homo sapiens",
                            "DerivedFrom": "PLEASE ADD",
                            "LevelType": "PLEASE ADD",
                            "SpecialReference": "PLEASE ADD"
                        }                    