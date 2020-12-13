# Healnaut
A Chatbot for Health related Queries

## Problem Statement
Siemen's Healthineer's Challenge, Statement 3

## Solution
As the pandemic started, the people always found themselves reluctant to go to hospitals for small problems but hence had lots of queries and worries in mind. So, here we are with Healnaut, a medical assistant chatbot to answer all your queries.

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
  
## Challenges Faced


