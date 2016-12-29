This folder contains 
1. nltk data files(corpora,taggers,tokenizers) which will be needed for compiling the code and using it in code.
2. main code of bot is in messenger_bot.py 
3. Credentials contaian 'VERIFY_TOKEN' and 'PAGE_ACCESS_TOKEN'
   'VERIFY_TOKEN' will be decided by us. And same will be put on facebook for developer application webhook.
   we will get 'PAGE_ACCESS_TOKEN' token from app page on facebook for developer.
4. chatterbotapi.py has code which will cocnnect to one of pretrained AI bot for generic purpose conversation.
   Available pretrained bots : CLEVERBOT, JABBERWACKY, PANDORABOTS
   we can use any one of them, we need to have get one bot from their sites. 
   code is self-explainotory.
5. example.py has a code which sends post request to web-service. we give json and get back json containing top 5 results
   for given skill as query. This is  just to get to know about what does json output file has. what are different fields
   and their fields.
6. Procfile : this file must be present in heroku git. This file tells which file to execute at starting
7. requirements.txt : this file should  contaian names and versions of different modules, packages required for main code.
   In this case, I have written all neccessary names and versions of different packages which I have to import in messenger_bot.py
8. runtime.txt : this file contains the python version which will be used.

############################################################
The main theme of this project is to build a facebook chatbot which will be used by candidates for getting information
about different jobs available according to input skills.

We have written the code for building a converesation with the user. 
Whenever the user say something out of conversation reply will be given by pandorabot. 
I have created an account on pandorabot.com and I got an ID for one bot which i can use for this purpose.

1. Important thing other than writing the code is deployment.
2. For using this code for fb messenger, we first need to have an webapp and that too secured web address for it
   according facebook policy. They won't accept web app if webaddress is not secured.
3. For getting secured web link for our app, we have deployed our code on heroku's server.
4. Heroku provides us the infrastructure where we can deploy our code. And importantly it will provide secured
   web app link. 
############################################################

Procedure : 

1. First make account on heroku website.
2. install Heroku CLI and also git 
3. push all these files in heroku git 
4. That will build and app on heroku and we will get an and secured webapp link.
5. Use that link in facebook for developers.

###########################################################

Reference:https://www.youtube.com/watch?v=iyoAbwR70Ns&t=837s