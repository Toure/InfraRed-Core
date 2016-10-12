import clg

from infrared.cli import core_args
from infrared.configs import yaml_conf

ordered_dict = yaml_conf("infrared/configs/core_args.yml")


clg.TYPES.update({function_name: function
                  for function_name, function in vars(core_args).items()
                  if not function_name.startswith('_')}
                 )


def main():
    cmd = clg.CommandLine(ordered_dict)
    return cmd.parse()

if __name__ == '__main__':
    import sys
    sys.exit(main())
