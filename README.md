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

Initially, I ran into significant issues trying to get the Python interpreter to work correctly in VS Code. The main problem was that Keras couldn’t be recognized due to a path problem at the system level. This led to various import errors and prevented me from running any of my scripts. After some research, I realized the best solution was to create a virtual environment. Setting up the virtual environment helped isolate the project dependencies, ensuring that Keras and other libraries were correctly recognized.

While trying to implement the chatbot, I faced numerous issues with the installation of Chatterbot. The installation process was not straightforward, and I encountered compatibility issues with various dependencies. I spent a considerable amount of time on forums and documentation sites trying to troubleshoot these issues. Eventually, I managed to install Chatterbot, but this initial hurdle significantly delayed my progress.

Once Chatterbot was installed, I needed to create training data for the chatbot. I used various resources to understand how to structure the training data and decided to use a JSON file (intents.json). This file would contain different user intents and corresponding responses. Developing this file was challenging because I had to think through and brainstorm every possible user input to generate the most accurate and helpful responses. It was a time-consuming process trying to anticipate the wide range of questions users might ask.

One of the biggest challenges was understanding how to train the chatbot model effectively. Despite using several tutorials and resources, I found it difficult to grasp the training process fully. The documentation often assumed a higher level of prior knowledge, which was frustrating. After extensive research, I learned about the importance of properly linking words.pkl, classes.pkl, and chatbot.h5. These files are crucial for the chatbot to understand and classify user inputs correctly. Ensuring these files were correctly generated and linked involved a lot of trial and error, and it took several iterations to get the model to function as expected.

After training the model, integrating and testing the chatbot in a real-world scenario posed its own set of challenges. I had to deal with unexpected bugs and errors that weren’t apparent during the development phase. Debugging these issues required a lot of patience and meticulous checking of the entire codebase to ensure everything was working as intended. I researched on the process using various responses possible then realised that words.pkl and classes.pkl and Chatbot.h5 should be properly linked.
