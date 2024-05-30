# Project-Number-1-2

Project 1 and 2 are within the github repo
Since I had created virtual environment 
python -m venv new_env
source new_env/bin/activate

Installed tensorflow with
pip install tensorflow

Installed nltk with 
Pip install nltk

Installed chatbot module with 
Pip install chatterbot


Installed keras and numpy
pip install keras numpy


Project 1 can be run with python Project_1.py

Project 2 uses intents.json so to pick up the best possible responses from training data with sqlitedb to store the testing data which is using neural network algorithm

To run project 2 first run command python admissionbot.py to create the chatbot.h5 model and then run python Project_1

words.pkl and classes.pkl contain the vocabulary and class labels that the model was trained on.
Chatbot.h5  is the pre-trained Keras model file.



ISSUES I FACED DURING THE PROCESS OF CODING THE PROJECT

I initally ran into issues trying to make the python interpreter work in VS Code but since keras couldn’t be recognized because of a problem with path at the system level i had to create a virtual environment
While I tried to code I tried using enough resources on the web to learn how to use chatterbot and ended up with issues on installation 
After installation I used resources to know how training data will be stored which i handled with the idea of creating intents.json
I was having a hard time trying to brainstorm every possible user inputs to generate the best possible response 
I was not able to understand how to train my model and so I researched on the process using various responses possible then realised that words.pkl and classes.pkl and Chatbot.h5 should be properly linked.

