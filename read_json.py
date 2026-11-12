import json

with open("riverbend_tide_and_treetop_brandbrief.json", "r") as file:
  ad_brief = json.load(file)
  
with open("manifest.json", "r") as file:
  ad_data = json.load(file)
  ad_variants_data = ad_data["variants"]


print("Number of Ad Variants:", len(ad_variants_data))


for ad_copies in ad_variants_data:
  #print("For Ad number:", ad_copies["variant_number"], "Healine:", ad_copies["headline"], "Body:", ad_copies["body"], "CTA:", ad_copies["cta"])
  print("Headline:", ad_copies["headline"], "|", "Length:", len(ad_copies["headline"]))