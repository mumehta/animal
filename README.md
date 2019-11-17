# Animal #
* Serializes data and saves to csv and json
* Reads json using panda lib and display on console

## What it does ##
* Inputs user name, address and phone
* Stores values in dictionary
* Serializes to csv and json formats
* Reads json on web and displays on console using pandas lib

## SetUp ##
* git clone https://github.com/mumehta/animal.git
* cd animal
* virtualenv -p <path_to_python3.6> venv
* pip install -r requirements.txt
  
## Run Application ##
* animal.py --name=munish "--address=my address" --phone=432

## Results ##
* Check generated files in project root: client.csv and client.json

## Under the hood - Ci ##
The project is setup on github and makes use of github workflow. When you commit and push to remote repo, build kicks in and runs build and unit tests - pytest. 
Workflow: .github/workflows/animalapp.yml
