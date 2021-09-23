#%%
import json
from jinja2 import Template
from rdflib import Graph
from rdflib.plugin import register, Parser
register("json-ld", Parser, "rdflib_jsonld.parser", "JsonLDParser")

LABELS = {
    "@id": "URI:",
    "skos:altLabel": "Alternative labels:",
    "skos:prefLabel": "Preferred label:",
    "skos:definition": "Definition:",
    "dcterms:creator": "Created by:",
    "dcterms:contributor": "Contributor:",
    "prov:wasDerivedFrom": "Derived from:",
    "skos:broader": "Broader terms:",
    "skos:narrower": "Narrower terms:",
    "skos:related": "Related terms:",
    "dcterms:created": "Created at:",
    "dcterms:modified": "Modified at:"
}

with open("../terms.ttl") as file:
    ttl = file.read()
    g = Graph().parse(data=ttl, format="turtle")

data = json.loads(
    g.serialize(
        indent=4,
        format="json-ld",
        context={
            "skos": "http://www.w3.org/2004/02/skos/core#",
            "dcterms": "http://purl.org/dc/terms/",
            "prov": "http://www.w3.org/ns/prov#"
        }))["@graph"]

metadata = [item for item in data if item.get("@type") != "skos:Concept"]

data = [item for item in data if item.get("@type") == "skos:Concept"]

data.sort(key = lambda x: x.get("skos:prefLabel")["@value"])

# Make sure properties which can have multiple entries are handled as arrays
for key in ["skos:related", "skos:broader", "skos:narrower", "skos:altLabel", "prov:wasDerivedFrom"]:
    for x in data:
        if x.get(key):
            x[key] = [x[key]] if not isinstance(x[key], list) else x[key]

#%%
with open ("../README.md", "r") as myfile:
    readme = myfile.read().replace("\n", "\n" + " "*8)

with open("./template.html") as f:
    tmpl = Template(f.read(), trim_blocks=True, lstrip_blocks=True)

output = tmpl.render(
    readme=readme,
    metadata=metadata,
    jsonld=data,
    labels=LABELS
)

with open("../index.html", "w") as fh:
    fh.write(output)
