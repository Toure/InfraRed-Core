import clg

from infrared.cli import core
from infrared.configs import yaml_list
from infrared.configs import yaml_merge

# Merge all spec file which were installed.
combined_conf = yaml_merge(yaml_list())

# Collect all functions which will correspond to the cli args.
clg.TYPES.update({function_name: function
                  for function_name, function in vars(core).items()
                  if not function_name.startswith('_')})


def main():
    cmd = clg.CommandLine(combined_conf)
    return cmd.parse()

if __name__ == '__main__':
    import sys
    sys.exit(main())
