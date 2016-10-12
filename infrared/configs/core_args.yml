add_help_cmd: True
allow_abbrev: False
description: InfraRedCore Command line interface.

anchors:
    main: &MAIN
        help:
            short: h
            action: help
            default: __SUPPRESS__
            help: Show this help message and exit.
        conf_file:
            help: 'Infrared base configuration file (default: __DEFAULT__).'
            default: infrared/configs/infrared_base_config.yml
        logdir:
            help: 'Log directory (default: __DEFAULT__).'
            default: /tmp/infrared/logs
        loglevel:
            choices: [verbose, debug, info, warn, error, none]
            default: info
            help: 'Log level on console (default: __DEFAULT__).'

subparsers:
    plugin_manager:
        help: Plugin manager will assist in deploying the projects plugins.
        description: |
                   Plugin manager will provide actions which allow for
                   installation, removal, and inspection of project plugins.
        add_help: False
        formatter_class: RawTextHelpFormatter
        execute:
            module: core_args
        groups:
            - title: Common options
              options: *MAIN
            - title: Optional options
              options:
                install:
                    short: i
                    type: str
                    metavar: PLUGIN_NAME
                    help: Install given plugin.
                install_all:
                    short: a
                    type: bool
                    help: Install all core plugins from repository.
                list:
                    short: l
                    action: store_true
                    help: List all available or non-installed plugins.
                list_installed:
                    short: s
                    action: store_true
                    help: List all plugins which have been installed.
                remove:
                    short: r
                    type: str
                    help: Remove installed plugin(s).
