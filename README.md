# CancerModels-notification-service
This service currently checks if there are new models in PDXNet data portal.

## Schedule
This service checks for new models 1st day of each month at 9:00 am.

## Current implementation
Uses JAX endpoint with PDXNet model list and a copy of list of PDXNet models in the CancerModels.org platform.

## To do:
    - Capture model information from CancerModels.org API directly.
    - Curl/wget PDXNet clinical files directly from the PDXNet portal.
    - Add functionality for HCMI and CMP data updates.
    - Implement upload service for the new data changes to git. 