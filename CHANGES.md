## Unreleased

* add changelog link to `setup.cfg` so that it shows on Shopyo PyPi page

## Version 4.1.2

Released 2021-05-19

* repaced Alabaster sphinx theme with Furo
* pinned the pallet projects related dependencies to older versions as the latest release breaks the project

## Version 4.1.1

Released 2021-05-10

* Fixed `python maanage.py COMMAND` not working for any commands other than `rundebug` or `initilaise` commands as explained in #13

## Version 4.1.0

Released 2021-05-07

* refactored cli to use `Click` for individual commands. See [issue #473](https://github.com/Abdur-rahmaanJ/shopyo/issues/473) of the archived `shopyo` repo
* added `shopyo createmodule [OPTIONS] MODULENAME [BOXNAME]` cli to allow an option creating module with/without box in one command rather than doing `shopyo startbox BOXNAME` followed by `shopyo startsubapp MODUELNAME in BOXNAME`
* extend `shopyo new PROJNAME` command to `shopyo new [OPTIONS] [PROJNAME]` allowing the optional PROJNAME to create
the new project of same name as base directory name
* added `cli.py` with `shopyo new [OPTIONS] [PROJNAME]` command to allow users to add their click commands with example commands included. See [issue #474](https://github.com/Abdur-rahmaanJ/shopyo/issues/474) of the archived `shopyo` repo
* added verbose (`-v or --verbose`) option for each of the cli command to print extra information when running
any cli command
* made the printout of the cli commands to be consistent

## Version 3.9.4

Released 2021-03-17
