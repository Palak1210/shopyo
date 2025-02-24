Commandline Args
################

.. toctree::
   :titlesonly:

Various commandline args exist to ease your life.

shopyo
******

.. _shopyo usage:

*Usage*

.. code:: bash

   shopyo [OPTIONS] COMMAND [ARGS]...

CLI management for shopyo cli. For Example, to run the app
in production mode you can run

.. code:: bash

   shopyo --config=production run

.. _shopyo options:

*Options*

.. option:: --version

   Show the flask version

.. option:: --config <CONFIG NAME>

   By default config is set to "development". Other available configurations are
   "testing" and "production". For commands `createmodule`_ , `collectstatic`_
   and `new`_ this options has no affect.

clean
*****

.. _shopyo clean usage:

*Usage*

.. code:: bash

   shopyo clean [OPTIONS]

or

.. code:: bash

   manage.py clean [OPTIONS]

removes ``__pycache__``, ``migrations/``, ``shopyo.db`` files and drops
``db`` if present

.. _shopyo clean options:

*Options*

.. option:: -v, --verbose

   Show all hidden outputs in terminal

.. option:: --help

   Show the command usage/help message and exit


Initialise
**********

.. _shopyo initialise usage:

*Usage*

.. code:: bash

   shopyo initialise [OPTIONS]

or

.. code:: bash

   manage.py initialise [OPTIONS]

Creates ``db``, ``migration/``, adds default users, add settings.
This command need to be run only once before running the project

.. _shopyo initialise options:

**Options**

.. option:: -v, --verbose

   Show all hidden outputs in terminal

.. option:: --help

   Show the command usage/help message and exit

run
***

.. _shopyo run usage:

*Usage*

.. code:: bash

   shopyo run [OPTIONS]

or

.. code:: bash

   manage.py run [OPTIONS]

Run a local development server.

This server is for development purposes only. It does not provide the
stability, security, or performance of production WSGI servers.

The reloader and debugger are enabled by default if ``FLASK_ENV=development```
or ``FLASK_DEBUG=1``.

.. note::

   This is wrapper around the ``flask run`` command

.. _shopyo run options:


*Options*

.. option:: -h, --host <host>

   The interface to bind to.

.. option:: -p, --port <port>

   The port to bind to.

.. option:: --cert <PATH>

   Specify a certificate file to use HTTPS.

.. option:: --key <FILE>

   The key file to use when specifying a certificate.

.. option:: --reload / --no-reload

   Enable or disable the reloader. By default the reloader is active if debug is enabled.

.. option:: --debugger / --no-debugger

   Enable or disable the debugger. By default the debugger is active if debug is enabled.

.. option:: --eager-loading / --lazy-loader

   Enable or disable eager loading. By default eager loading is enabled if the reloader is disabled.

.. option:: --with-threads / --without-threads

   Enable or disable multithreading.

.. option:: --extra-files PATH

   Extra files that trigger a reload on change. Multiple paths are separated by ';'.

.. option:: --help

   Show the command usage/help message and exit


rundebug
********

.. _shopyo rundebug usage:

*Usage*

.. code:: bash

   shopyo rundebug [OPTIONS]

or

.. code:: bash

   manage.py rundebug [OPTIONS]

Run a local development server.

same as ``app.run(debug=True)``

runserver
*********

.. _shopyo runserver usage:

*Usage*

.. code:: bash

   shopyo runserver [OPTIONS]

or

.. code:: bash

   manage.py runserver [OPTIONS]

Run a local development server.

same as ``app.run(debug=False)``

createmodule
************

.. _shopyo createmodule usage:

*Usage*

.. code:: bash

   shopyo createmodule [OPTIONS] MODULENAME [BOXNAME]

or

.. code:: bash

   manage.py createmodule [OPTIONS] MODULENAME [BOXNAME]

create a module ``MODULENAME`` inside ``modules/``. If ``BOXNAME`` is
provided, create the module inside ``modules/BOXNAME.``

If box ``BOXNAME`` does not exist, it is created.

If ``MODULENAME`` already exists, an error is thrown and command is terminated.

.. code:: bash

   shopyo createmodule dumpling # modules/dumpling
   shopyo createmodule box__plate/dumpling # modules/box__plate/dumpling


startbox
********

*Usage*

.. code:: bash

   shopyo startbox [OPTIONS] BOXNAME [BOXNAME]

or

.. code:: bash

   shopyo startbox [OPTIONS] BOXNAME [BOXNAME]

Creates an empty box

.. code:: bash

   shopyo startbox api # modules/box__api



collectstatic
*************

.. _shopyo collectstatic usage:

*Usage*

.. code:: bash

   shopyo collectstatic [OPTIONS] [SRC]

or

.. code:: bash

   manage.py collectstatic [OPTIONS] [SRC]

Copies ``static/`` in ``modules/`` or ``modules/SRC`` into ``/static/modules/``

.. code:: bash

   .
   └── modules/
      └── box__default/
            ├── auth/
            │   └── static
            └── appadmin/
               └── static

For the modules structure shown above:

   to collect static in only one module, run either of two commands:

   .. code:: bash

      $ shopyo collectstatic box__default/auth
      $ shopyo collectstatic modules/box__default/auth

   to collect static in all modules inside a box, run either of two commands below:

   .. code:: bash

      $ shopyo collectstatic box__default
      $ shopyo collectstatic modules/box__default

   to collect static in all modules run either of the two commands below:

   .. code:: bash

      $ shopyo collectstatic
      $ shopyo collectstatic modules

.. _shopyo collectstatic options:

*Options*

.. option:: -v, --verbose

   Show all hidden outputs in terminal

.. option:: --help

   Show the command usage/help message and exit

.. _shopyo collectstatic arguments:

*Arguments*

.. object:: SRC

   | `Optional argument`
   | the module path relative to ``modules/`` where ``static/`` exists.

new
***

.. _shopyo new usage:

*Usage*

.. code:: bash

   shopyo new [OPTIONS] [PROJNAME]

Creates a new shopyo project.

By default it will create the project(folder) of same name as the parent
folder. If ``PROJNAME`` is provided ``shopyo new somename``, it will create ``PROJNAME/PROJNAME``
under parent folder

For Example, say your current working directory is ``/path/to/blog``. Assuming you have
created a virtual environment ``env`` and activated it, and installed ``shopyo``.
Apart from env folder, your cwd should be empty. Then after running:

.. code:: bash

   shopyo new

the following blog project is created

.. code:: bash

   .
   └── blog
      ├── env
      ├── blog
      │   ├── docs
      │   ├── modules
      │   │   └── ...
      │   ├── __init__.py
      │   ├── sphinx_source
      │   │   └── ...
      │   ├── static
      │   │   └── ...
      │   ├── tests
      │   │   └── ...
      │   ├── .test.prod.env
      │   ├── __init__.py
      │   ├── app.py
      │   ├── cli.py
      │   ├── config.py
      │   ├── config_demo.json
      │   ├── conftest.py
      │   ├── init.py
      │   ├── manage.py
      │   └── wsgi.py
      ├── .gitignore
      ├── dev_requirements.txt
      ├── MANIFEST.in
      ├── pytest.ini
      ├── README.md
      ├── requirements.txt
      ├── setup.py
      └── tox.ini

Some files are omitted above but the general structure is as shown above. Now
you can initialise your project by running:

.. code:: bash

   path/to/blog/blog$ shopyo initialise

and run the project as:

.. code:: bash

   path/to/blog/blog$ shopyo run


You now have a complete Flask based blog application

.. _shopyo new options:

*Options*

.. option:: -v, --verbose

   Show all hidden outputs in terminal

.. option:: --help

   Show the command usage/help message and exit

.. _shopyo new arguments:

*Arguments*

.. object:: PROJNAME

   | `Optional argument`
   | if provided, creates the new project folder PROJNAME/PROJNAME inside cwd


db
**

.. _shopyo db usage:

*Usage*

.. code:: bash

   shopyo db [OPTIONS]

or

.. code:: bash

   manage.py db [OPTIONS]

db migrate and db upgrate are used to migrate the db

.. note::

   This is wrapper around the ``flask db``  of flask-migrate


routes
******

.. _shopyo routes usage:

*Usage*

.. code:: bash

   shopyo routes

or

.. code:: bash

   manage.py routes

Shows all routes and methods

.. note::

   This is wrapper around the ``flask routes``  command
