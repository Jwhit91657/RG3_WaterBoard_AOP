#!/usr/bin/env python3

import arcpy

MAP_NAME = "Map"

project = arcpy.mp.ArcGISProject('current')

map_exists = False
for _map in project.listMaps():
    if _map.name == MAP_NAME:
        map_exists = True

if not map_exists:
    print("[+] Calgem Map doesn't exist. Creating a new one.")
    the_map = project.createMap(MAP_NAME)
    
else:
    print("[+] Calgem Map exists. Using current map.")
    the_map = [map for map in project.listMaps() if map.name == MAP_NAME][0]

service_urls = {
    "wells": "https://gis.conservation.ca.gov/server/rest/services/WellSTAR/Wells/MapServer",
    "facilities": "https://gis.conservation.ca.gov/server/rest/services/WellSTAR/Facilities/MapServer",
    "districts": "https://gis.conservation.ca.gov/server/rest/services/CalGEM/CalGEM_Districts/MapServer",
    "aquifer_exemptions": "https://gis.conservation.ca.gov/server/rest/services/CalGEM/Post_Primacy_Aquifer_Exemptions/MapServer",
    "primacy_exemptions": "https://gis.conservation.ca.gov/server/rest/services/CalGEM/Primacy_Aquifer_Exemptions/MapServer",
    "places": "https://gis.conservation.ca.gov/server/rest/services/CalGEM/Places/MapServer",
    "places_county": "https://gis.conservation.ca.gov/server/rest/services/CalGEM/Places_County/MapServer",
    "admin_boundaries": "https://gis.conservation.ca.gov/server/rest/services/CalGEM/Admin_Bounds/MapServer",
    "base_plss": "https://gis.conservation.ca.gov/server/rest/services/Base/Base_PLSS/MapServer",
    "base_counties": "https://gis.conservation.ca.gov/server/rest/services/Base/Base_Counties/MapServer",
    "base_cities": "https://gis.conservation.ca.gov/server/rest/services/Base/Base_BOECities/MapServer",
    "ugs": "https://gis.conservation.ca.gov/server/rest/services/WellSTAR/UGS/MapServer",
    "fault_zones": "https://gis.conservation.ca.gov/server/rest/services/CGS_Earthquake_Hazard_Zones/SHP_Fault_Zones/MapServer",
    "liquefaction_zones": "https://gis.conservation.ca.gov/server/rest/services/CGS_Earthquake_Hazard_Zones/SHP_Liquefaction_Zones/MapServer",
    "zone_info": "https://gis.conservation.ca.gov/server/rest/services/CGS_Earthquake_Hazard_Zones/SHP_ZoneInfo/MapServer"
}

print(f"[+] Adding {len(service_urls)} new map servers to the {MAP_NAME} map.")

for service, url in service_urls.items():
    print(f"[+] Adding layer to map: {service} | From URL: {url}.")
    the_map.addDataFromPath(url)

print("[+] Saving Project..")
project.save()

print("[+] Done.")
