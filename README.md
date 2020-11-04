API MSP
===============================

version number: 1.0.0
author: Felipe Maza

Overview
--------

API for MSP Tools library.
This version uses [Swagger UI](https://swagger.io/tools/swagger-ui/), and a namespace `/tools/`.

Installation / Usage
--------------------

To install use pip:

    $ python -m pip install git+https://github.com/IHCantabria/apiprocess-msp.git


Or clone the repo:

    $ git clone ssh://git@github.com/IHCantabria//apiprocess-msp.git
    $ python setup.py install
    
Example
-------

Check Api:

    http://127.0.0.1:5050/tools/check_api

Biological:

    {
        "point": {
            "lon": -13.016,
            "lat": 28.486
        },
        "specie": {
            "name": "European seabass",
            "salinity_min": 30,
            "salinity_max": 40,
            "temperature_min": 18,
            "temperature_max": 26
        },
        "dates": {
            "ini": "2015-01-01",
            "end": "2015-03-01"
        }
    }

    curl -X POST "http://127.0.0.1:5050/tools/biological" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{    \"point\": {        \"lon\": -13.016,        \"lat\": 28.486    },    \"specie\": {        \"name\": \"European seabass\",        \"salinity_min\": 30,        \"salinity_max\": 40,        \"temperature_min\": 18,        \"temperature_max\": 26    },    \"dates\": {        \"ini\": \"2015-01-01\",        \"end\": \"2015-03-01\"    }}"

Wave:

    {
        "config": {
            "hs_min": 1,
            "hs_max": 5,
            "tp_min": 5,
            "tp_max": 14,
            "cge_min": 15
        },
        "point": {
            "lon": -13.016,
            "lat": 28.486
        },
        "dates": {
            "start": "2015-01-01",
            "end": "2015-03-01"
        }
    }

    curl -X POST "http://127.0.0.1:5050/tools/wave" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{    \"config\": {        \"hs_min\": 1,        \"hs_max\": 5,        \"tp_min\": 5,        \"tp_max\": 14,        \"cge_min\": 15    },    \"point\": {        \"lon\": -13.016,        \"lat\": 28.486    },    \"dates\": {        \"start\": \"2015-01-01\",        \"end\": \"2015-03-01\"    }}"

Wind:

    {
        "config": {
            "hs_max": 5,
            "pow": 400
        },
        "point": {
            "lon": -7.229,
            "lat": 48.75895
        },
        "dates": {
            "start": "2010-02-01",
            "end": "2010-02-05"
        }
    }

    curl -X POST "http://127.0.0.1:5050/tools/wind" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{    \"config\": {        \"hs_max\": 5,        \"pow\": 400    },    \"point\": {        \"lon\": -7.229,        \"lat\": 48.75895    },    \"dates\": {        \"start\": \"2010-02-01\",        \"end\": \"2010-02-05\"    }}"

Historical:

    {
        "point": {
            "lon": -13.016,
            "lat": 28.486
        },
        "specie": {
            "name": "European seabass",
            "salinity_min": 30,
            "salinity_max": 40,
            "temperature_min": 18,
            "temperature_max": 26
        },
        "dates": {
            "ini": "2015-01-01",
            "end": "2015-03-01"
        }
    }

    curl -X POST "http://127.0.0.1:5050/tools/historical" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{    \"point\": {        \"lon\": -13.016,        \"lat\": 28.486    },    \"specie\": {        \"name\": \"European seabass\",        \"salinity_min\": 30,        \"salinity_max\": 40,        \"temperature_min\": 18,        \"temperature_max\": 26    },    \"dates\": {        \"ini\": \"2015-01-01\",        \"end\": \"2015-03-01\"    }}"
