# QuickConfigs
This Python script extracts a csv file into YAML and then pushes out the appropriate config files based on the switch 'make' var

Credit to Edelman/Lowe/Oswalt for the framework of the templating script and to Josue Rojas for the csv -> yaml conversion script. 

To customize update:
template_file1 = "access_template.j2"
template_file2 = "bb_template.j2"
yaml_parameter_file = "configdata.yml"

AND
if parameter['make'] == ("IE-4000-8T4G-E"):
if parameter['make'] == ("C9500-16X"):

IF
more template options are needed add additional
templatefile
template loader
directory creation/validation
template render


