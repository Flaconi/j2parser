#!/usr/bin/env python

import os
import jinja2
import yaml
from optparse import OptionParser


def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
      loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)


usage = "usage: %prog [options] TEMPLATE"
parser = OptionParser(usage=usage)
parser.add_option("-f", "--file",
                  dest="file",
                  help="Load variables from yaml file",
                  metavar="FILE")
parser.add_option("-s", "--set",
                  action="append",
                  dest="environment",
                  help="Set variables for template",
                  metavar="\"VAR1=VALUE1\"")

(options, args) = parser.parse_args()
if len(args) != 1:
    parser.error("Filename is missing")
tpl_file = args[0]

environment = {}

if options.file:
    with open(options.file, 'r') as stream:
        try:
            environment = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)

if options.environment:
    for e in options.environment:
        (var, value) = e.split('=')
        environment[var] = value

result = render(tpl_file, environment)

print(result)
