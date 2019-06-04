.. rt files content and synthax can be tested http://rst.ninjs.org/#

**Solution**:
-------------

========================
Test-Valsys Instructions
========================

The solution chosen is an API in which endpoint 'accounts' will render the last account and it's value from a list of accounts used as parameters that have been saved in a dictionary. 
A CLI could also have been used by providing the parameters using the curl function but that was just a personal choice

===========
Quick Start
===========

1. Clone the repository:

.. code-block:: console

    $ git clone https://github.com/sbenou/test_valsys


Activate the virtual environment called valsys-env:

.. code-block:: console

    - linux, mac, ubuntu
    $ source valsys-env/bin/activate
    - windows:
    $ valsys-env\Scripts\activate

========================
Install the dependencies
========================

.. code-block:: console

    - $ pip install -r requirements.txt
    or
    - $ python setup.py install

This will download the necessary dependencies and install them.

run the app:

.. code-block:: console

    - linux, mac, ubuntu
    $ export FLASK-APP=app.py flask run
    - Windows
    $ set FLASK-APP=app.py flask run

run the tests available in the directory *tests*:
I have not completed them due to the workload I currently have but can be completed once I have some more spare time definitely but I have 
committed to look at quite a few scenarios

.. code-block:: console

    $ python accounts-test.py


=============
How to use it
=============
1. From app.py, change the accounts stored in the dictionary containing all parameters
2. Go to the /accounts endpoint in your browser to see the result.

============
Improvements
============

1. Instead of storing the parameters in a dictionary they can be stored in a json file which is the most probable way these would be provided.
2. Also with regards to the views, Jinja layout template could have been used to extends the base html on both the index.html and accounts.html
