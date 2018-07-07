Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/karimoff/py-fdl/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

py-fdl could be more useful if more documentation is added. 
Go ahead and write something to README.md.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/karimoff/py-fdl/issues.

Get Started!
------------

Ready to contribute? Here's how to set up `devon` for local development.

1. Fork the `py-fdl` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/py-fdl.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv py-fdl
    $ cd py-fdl/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass tests::

    $ pytest

   To get pytest, just pip install pytest into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "[<file_name or module_name>]]Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.md.
3. The pull request should work for Python 3.4, 3.5 and 3.6, and for PyPy. Check
   https://travis-ci.org/karimoff/py-fdl/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

    $ pytest tests/test_firebase_dynamic_links.py
