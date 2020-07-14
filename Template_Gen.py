#!/usr/bin/env python3

import jinja2
import sys
import os
import yaml
from jinja2 import Environment, FileSystemLoader

os.system("csv2yml.py 1")

template_file1 = "access_template.j2"
template_file2 = "bb_template.j2"
yaml_parameter_file = "configdata.yml"
access_sx_output_directory = "access_sx_output"
bb_sx_output_directory = "bb_sx_output"

# Parse the contents from the YAML files
print("Read YAML parameter file...")
config_parameters = yaml.full_load(open(yaml_parameter_file))

# Load Jinja2 Templates
print("Create Jinja2 environment...")
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."),
                         trim_blocks=True,
                         lstrip_blocks=True)
template1 = env.get_template(template_file1)
template2 = env.get_template(template_file2)

# Directory Validation
if os.path.exists(access_sx_output_directory):
		print("Validated access switch output directory location...")
if os.path.exists(bb_sx_output_directory):
		print("Validated backbone switch output directory location...")

# If it doesn't create it.
if not os.path.exists(access_sx_output_directory):
		print("Create access switch config output directory...")
		os.mkdir(access_sx_output_directory)

if not os.path.exists(bb_sx_output_directory):
		print("Create backbone switch config output directory...")
		os.mkdir(bb_sx_output_directory)
		

#### Template Rendering
print("Creating templates...")
for parameter in config_parameters:
		if parameter['make'] == ("IE-4000-8T4G-E"):
			result = template1.render(parameter)
			f = open(os.path.join(access_sx_output_directory, parameter['hostname'] + ".config"), "w")
			f.write(result)
			f.close()
			print("Configuration '%s' created..." % (parameter['hostname'] + ".config"))
		if parameter['make'] == ("C9500-16X"):
			result = template2.render(parameter)
			f = open(os.path.join(bb_sx_output_directory, parameter['hostname'] + ".config"), "w")
			f.write(result)
			f.close()
			print("Configuration '%s' created..." % (parameter['hostname'] + ".config"))
print("DONE")
