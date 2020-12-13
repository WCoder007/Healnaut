# Healnaut

A Chatbot for Health related Queries

## Problem Statement

Siemen's Healthineer's Challenge, Statement 3

## Solution

As the pandemic started, the people always found themselves reluctant to go to hospitals for small problems but hence had lots of queries and worries in mind. So, here we are with Healnaut, a medical assistant chatbot to answer your queries.

## Technology Stack Used

* Python
* RASA
* Doc2Vec Model
* nltk
* Pandas
* urllib.request
* Beautiful Soup (BS4)
* VS Code

## Methodology

  1. Using urllib.requests and Beautiful Soup (BS4), data was scraped from [WebMD](http://WebMD.com), [Icliniq](https://www.icliniq.com/en_IN/) and [Question Doctors](https://questiondoctors.com/blog/page/1)
  2. A model was made using the scraped data using Doc2Vec Model
  3. Model was intergrated to the chatbot using RASA FrameWork
  
## Model Training
* Doc2vec word embedding model was used to vectorize our questions (Ref: Doc2Vec is a Google product released in 2018 and can be use in python or R)
* To train the model, data was scrapped via beautifulsoup. 
* Only the topic and body text was fetched
* The data was then cleaned  with the help of python nltk kit.
* The model was trained on about 4 GB pure text.
* For choosing the model hyperparameters cosine similarity was chosen on the benchmark sentences and the best ones were picked.

Note: The nobility of the model is training the model on the reliable healthcare resources.
  
## Challenges Faced
* Working with people from 3 different timezones
* Finding reliable data sources
* Doc2Vec Training was a challenge on its own
* We were new to RASA Framework and had to learn pretty much from scratch


