# psycovid-beta-version
# Data analysis
- Name of the project: Psycovid
- Description: A project based on the Psychological impact of the COVID-19 pandemic, that uses Machine Learning technics to predict emotions based on personality aspects. This project makes also possible to implement recommendation systems suggesting best activities for each User after answering a few questions.
- Data Source: https://osf.io/cjxua/ COVIDiSTRESS_global_survey_May_30_2020_final_cleaned_file.csv (rows = 125306, columns = 153)
- Type of analysis:

Please document the project the better you can.

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for psycovid in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/psycovid`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "psycovid"
git remote add origin git@github.com:{group}/psycovid.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
psycovid-run
```

# Install

Go to `https://github.com/{group}/psycovid` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/psycovid.git
cd psycovid
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
psycovid-run
```
