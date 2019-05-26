========
Concepts
========

.. note::
   The concepts described in this section correspond to the latest release (version |release|).
   
   Model concepts and processes of older releases may differ from the current release. It is therefore
   recommended to read the release notes of older versions if you plan to use
   an older release.
   

Introduction
------------

SPHY is a spatially distributed leaky bucket type of model, and is applied on a cell-by-cell basis.
The main terrestrial hydrological processes are described in a conceptual way so that changes
in storages and fluxes can be assessed adequately over time and space. SPHY is written in the
Python programming language using the `PCRaster <http://pcraster.geo.uu.nl/>`_ 
(:cite:`Karssenberg2001`, :cite:`Karssenberg2010`, :cite:`Karssenberg2002`) dynamic modeling
framework.

SPHY is grid based and cell values represent averages over a cell. For glaciers, sub-grid variability is taken into account: a cell
can be glacier-free, partially glacierized, or completely covered by glaciers. The cell fraction not covered by glaciers consists of either land
covered with snow or land that is free of snow. Land that is free of snow can consist of vegetation, bare soil, or open water. The dynamic vegetation
module accounts for a time-varying fractional vegetation coverage, which affects processes such as interception, effective precipitation, and potential
evapotranspiration. :numref:`fig_concepts` provides a schematic overview of the SPHY modeling concepts.

.. _fig_concepts:

.. figure:: images/SPHY_concepts.*
   :alt: SPHY model concepts
   :figwidth: 70% 
   
   SPHY model concepts.

Soil layers and fluxes
----------------------

The soil column structure is similar to VIC (:cite:`Liang1994`, :cite:`Liang1996`), with two upper soil storages
and a third groundwater storage. Their corresponding drainage components are surface runoff,
lateral flow and baseflow. SPHY simulates for each cell precipitation in the form of rain or snow.
Precipitation that falls on land surfaces can be intercepted by
vegetation and evaporated in part or whole. A part of the liquid precipitation is transformed in surface runoff,
whereas the remainder infiltrates into the soil. The resulting soil moisture is subject to
evapotranspiration, depending on the soil properties and fractional vegetation cover, while the
remainder contributes to river discharge by means of lateral flow from the first soil layer, and
baseflow from the groundwater layer.

Glaciers
--------

Depending on the temperature and a criticial temperature threshold, precipitation can either fall as rain or as snow. 
The snow storage is updated with snow accumulation and/or snowmelt. Melting of glacier ice contributes to the river discharge by means of a slow and fast component,
being (i) percolation to the groundwater layer that eventually becomes baseflow, and (ii) direct runoff. 

Runoff and routing
------------------

The cell-specific runoff, which becomes available for routing, is the sum of surface runoff,
lateral flow, baseflow, snowmelt and glacier melt. If no lakes are present, then the user can choose a simple flow accumulation routing scheme:
for each cell, the accumulated amount of water that flows out of the cell into its neighboring
downstream cell is calculated. This accumulated amount is the amount of water in the cell itself
plus the amount of water in upstream cells of the cell, and is calculated using the flow direction
network. If lakes are present, then the fractional accumulation flux routing scheme is used;
depending on the actual lake storage, a fraction of that storage becomes available for routing
and is extracted from the lake, while the remaining part becomes the updated actual lake
storage. The flux available for routing is routed in the same way as in the simple flow
accumulation routing scheme.

Model input
-----------

As input, SPHY requires static data as well as dynamic data. For the static data, the most
relevant are digital elevation model (DEM), land use type, glacier cover, lakes/reservoirs and
soil characteristics. The main dynamic data consist of climate data, such as precipitation,
temperature, and reference evapotranspiration. Since SPHY is grid based, optimal use of
remote sensing data and global data sources can be made. For example, the Normalized
Difference Vegetation Index (NDVI) (:cite:`Tucker1979`, :cite:`Carlson1997a`, :cite:`Myneni1994`)
can be used to determine the leaf-area index (LAI) in order to estimate the
growth stage of land cover. For setting up the model, streamflow data are not necessary.
However, to undertake a proper calibration and validation procedure, flow data are required.
The model could also be calibrated using actual evapotranspiration, soil moisture contents,
and/or snow-covered area (SCA). An example application in which the
SPHY model has been calibrated using `MODIS <https://modis.gsfc.nasa.gov/data/dataprod/mod10.php>`_ snow cover images
can be found :ref:`here <calibration_MODIS_snow_cover>`.

Model output
------------

The SPHY model provides a wealth of output variables that can be selected based on the
preference of the user. Spatial output can be presented as maps of all the available hydrological
processes, i.e., actual evapotranspiration, runoff generation (separated by its components), and
groundwater recharge. These maps can be generated on a daily basis, but can also be
aggregated at monthly or annual time periods. Time-series can be generated for each cell in the
study area. Time-series often used are streamflow, actual evapotranspiration and recharge to
the groundwater.

Modules
-------

SPHY enables the user to turn on/off modules (processes) that are relevant/irrelevant for the
area of interest. This concept is very useful if the user is studying hydrological processes in
regions where not all hydrological processes are relevant. A user may for example be interested
in studying irrigation water requirements in central Africa. For this region, glacier and snow
melting processes are irrelevant, and can thus be switched off. The advantages of turning off
irrelevant modules are two-fold: (i) decrease model run time, and (ii) decrease the number of
required model input data.

