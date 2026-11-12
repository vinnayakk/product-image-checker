import csv
import json

with open("riverbend_tide_and_treetop_brandbrief.json", "r") as file:
  ad_brief = json.load(file)

with open("results.csv", "r") as file:
  ad_data = csv.DictReader(file)
  all_data = list(ad_data)

#print(all_data)
for headline_data in all_data:
  print("Headline:", headline_data["headline"], "|", "Length:", len(headline_data["headline"]))