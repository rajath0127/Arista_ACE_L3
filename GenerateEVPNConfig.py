import pandas as pd
from jinja2 import Environment, FileSystemLoader
import yaml
import glob
import os

leafs = []
spines = []

# Load all YAML files from leafs/ folder
for file in glob.glob("leafs/*.yml"):
    with open(file) as f:
        data = yaml.safe_load(f)
        leafs.append(data)

for file in glob.glob("spines/*.yml"):
    with open(file) as f:
        data = yaml.safe_load(f)
        spines.append(data)

print(leafs[0])

env = Environment(loader=FileSystemLoader("templates"))
leaf_template = env.get_template("leaf_template.j2")
spine_template = env.get_template("spine_template.j2")

# Render config
for leaf in leafs:
    config = leaf_template.render(**leaf, spines=spines)
    filename = f"configs/{leaf['hostname']}_config.cfg"
    with open(filename, "w") as f:
        f.write(config)
    
for spine in spines:
    config = spine_template.render(**spine, leafs=leafs)
    filename = f"configs/{spine['hostname']}_config.cfg"
    with open(filename, "w") as f:
        f.write(config)