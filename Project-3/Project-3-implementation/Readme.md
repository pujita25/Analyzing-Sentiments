## Project Abstract

Recently, people have started using online forums frequently for discussions. Along with the discussions on online forums,
trolls and spammers have become more common. It is a timeconsuming and tedious job to moderate the comments and posts on these forums, so the organizations have to rely on external people to handle them. We are trying to differentiate between negative and positive comments and tweets on Twitter, Reddit, and YouTube. To achieve this, we would get real-world data from the above mentioned platforms. We also intend to visualize Twitter, Reddit, and YouTube’s data.

## Team - Systematic_Squad

* Nagalakshmi Prasanna Pujita Bodapati, nbodapa1@binghamton.edu
* Saisuraj Aitha, saitha2@binghamton.edu
* kshamitha Gandu, kgandu1@binghamton.edu
* Mohith kumar Sopparam, msoppar1@binghamton.edu
* Anshul Upadhyay, aupadhy5@binghamton.edu

## Tech-stack

* `Python` - For Reddit Data extraction we used python to create and develop this project. [Python Website](https://www.python.org/)
* `pymongo` - For storing comments that are collected from Reddit/Subreddits we used pymongo to conenct to Mongodb client [pymongo - Documentation](https://pymongo.readthedocs.io/en/stable/)
* `flask` - Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions
* `textblob` - TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.
* `numpy` - NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices.
* `HTML` - Pure HTML used for rendering browser specific UI.
* `Bootstrap` - Used for user friendly and interactive styling.

## Datasources - data collection
* `Twitter`:
    * Using `twitter_data_analysis` function - analyzed the sentimental analysis and the polarity
* `Reddit`:
    * Using `reddit_data_analysis` function - analyzed the sentimental analysis and the polarity 
* `Youtube`:
     * Using `youtube_data_analysis` function - analyzed the sentimental analysis and the polarity 

## How to run the project?
Install Python
Install Mongodb / Mongoshell
Run server for Mongodb and run mongoshell
Create databases
    * `Twitter` - 'twitterdatabase'
    * `Youtube` - 'youtubedatabase'
    * `Reddit` -  'redditdatabase'
Create Collections
    * `Twitter` - 'twitter'
    * `Youtube` - 'youtube'
    * `Reddit` -  'redditcomments'

`For project 3 implementation run the following command`
ssh -L 5000:127.0.0.1:5000 nbodapa1@128.226.28.120
Password to enter: `MEeaaNe92`

Then to run the UI
paste the URL in the browser -  http://127.0.0.1:5000

## Special instructions for us???
The mongodb server should be running with corresponding databases and collections created.
