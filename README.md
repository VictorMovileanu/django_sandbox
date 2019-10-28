# How to use this repository

1. checkout branch

2. setup your env

    * (a): create a virtual environment and install the requirements from `requirements.txt`
    
          pip install -r requirements.txt
    
    * or (b): remove all previously installed packages and reinstall from `requirements.txt`
    
          pip freeze | xargs pip uninstall -y && pip install -r requirements.txt
 
3. follow further instructions in the branch specific README file 

# Prerequisites
Following tools are installed in the master branch

* `django-extensions`: e6a0daefe4c41b962e309bec699c173857230a14

# Branches

1. intercooler.js
2. `testing`: load test data with mockaroo
3. `django-oauth-toolkit`: create an oauth server
4. `accounts`: basic account views implementations