# j2parser
Just a simple python cli for parsing jinja2 templates

# Syntax
Usage: *j2parse.py [options] TEMPLATE*

Options:

 * *-h*, *--help*            show this help message and exit

 * *-f FILE*, *--file=FILE*  Load variables from yaml file

 * *-s "VAR1=VALUE1"*, *--set="VAR1=VALUE1"*
                        Set variables for template

Values from *-s* will override values in FILE.

# Examples

`j2parse.py -f env.yaml -s 'SOMEVAR=SOMEVAL' template.j2`
