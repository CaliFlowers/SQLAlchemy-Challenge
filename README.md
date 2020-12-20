# SQLAlchemy-Challenge
I hve already covered the pros and cons of using Object Relation Mapping (ORM) libraries in a different repository(https://github.com/CaliFlowers/sql-challenge/blob/main/README.md). This mini=project is a full demonstration of why ORM exists; and how it can be useful. While I have already covered weather analysis using Python in a previous mini=project. (https://github.com/CaliFlowers/Python_APIChallenge), this mini=project approaches a more focused geographic location to do a similar analysis; but using SQL Alchemy. 
## WHY SQLALCHEMY?
It might be baffling to some people why an otherwised experienced Python or SQL programmer might want to indulge the headache of performing SQL queries in Python. However, one can also not ignore the value of data normalization and the many benefits of using relational databases. As baffling as it might seem, many people who possess large quantities of datahave to store their data in Relational Databases. 

## API SERVICES
Application Program Interfaces are ab excellent method for sharing and retrieving data. However, one notices a problem in that lare datasets work best when stored in relational databases; while API services typically tend to be designed with Python in mind. So how can an SQL database effectively interface with a Python=based query?

One obvious answer is an ORM, which allows a Python API to query information from a database probiding certain conditions are met. 

## DATA PRODUCTS
For companies like Google, direct access to consumer data is a major product offered to customers. At the same time, web-based services have to pair back=end databases ewith front-end consumer interfaces. Since Javascript is the common programming language for front-end interfaces, another kind of ORM would be required to access a relational database. This, in a nutshell is why ORMs are important. 

## HAWAII WEATHER ANALYSIS
For the Python portion of this exercise, asqlite file joins two tables, one for measurements, and another for stations. In order to demonstrate how an ORM query would work, an analysis using SQLAlchemy is conducted to retrieve data with appropriate filters, store them in a pandas dataframe, perform desired analyses, and visualize the outputs. Basically, SQL Alchemy does most of the work of Data Preparation and Aggregation; while Python works with aalysis and visualization; as might be asked of a web application.  
In this example, SQL Alchemy is used to inspect the structure of a sample mini-database, to determine its contents, then to use that information to make a few sample queries that retrieve data from the sample database accordng to specified parameters as might be done in a typical request for information. In addition, more queries are used to aggregate the data in the database, to zero in on a specific weather station, then to make further queries based on date. 

## FLASK
Flask is a Python librry used for front-end programming. Flask can be used to make a web interface, in this case for an API service. The Flask portion of this examplerepeats many of the ORM queries performed on Jupyter notebook in an App.py file. This shows how an ORM might translate into a web application. Flask facilitates the client-server interaction between the database and the requesting client making the query. A query made through a Flask app will behave differently than an ORM query made in Jupyter notebook as Flask behaves like a serverthat processes queries externally while Jupyter notebook is still able to obtain more direct access to the database it is interacting with.
