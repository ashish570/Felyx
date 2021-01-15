<h1> Felyx Assessment</h1>
<p align = "center">
<h1>Problem Statement</h1>
<ul><li> Data is supplied in the csv files is available in the cloud storage, for the assessment, the csv files are provided.These csv files needs to be stored in the SQL databse. </li>
<li>  Once loaded in the relational database, the data written in the relational table needs to be available through the API.</li>
<ul>
</p>

<h1 style="background-color:powderblue;"> Solution Approach : </h1>
<p >I'm considering Microsoft Azure stack services for different compute and storage.<p>
<ul><p>There can be two approached to load the csv files to relational database.
        <ul><li>using a code base like python,pyspark : Can be useful if the data is not in the form of schema provided and transformations are needed. </li>
          <li>using an ETL orchastrator, like DataFactory which can be useful in cases where raw data dump is required without transformation. It can provide significant performance improvement over code base</li>
          </ul></p>
    <p> Below are the infrastructrual components of this solution
<li>Compute : I'm using Databricks's infrastructure for ETL on pyspark and spark sql</li> 
<li> Raw Storage  : For raw layer I'm using databrick's file system(In a production scenario I'd have choosen ADLS which has a good connectivity with Azure services for ETL and building representational layer on top of the data.</li>
<li> Relational Storage : I've choosen Microsoft SQL Server on Azure for this use case , where I'm hosting my two tables for location and reservations.</li>
<li> End User accessibility : I"m making the data available to end user through a rest api endoint hosted on my local machine.</li>
</ul>
</p>

<h1 style="background-color:powderblue;align= 'Left'"> Execution Approach : </h1>
<p>
  Inside ETL folder there are there are three files :
  <ul>
    <li><b>DataFactory.json </b>: which is the orchastration for the notebook I'm using to write the loading logic.</li>
    <li><b>Felyx_ddl.sql </b>: is the ddl definition for the table I'm creating to load this data supplied in csv files.</li>
    <li><b>Felyx.ipynb </b>:I'm reading the data from csv files , providing a schema to the data and loading this data into sql server.</li>
    </ul>
    </p>
 <p>
  Inside API folder there are 4 files:
  <ul>
    <li> <b> api.py</b> : This is the main API file where my main function runs which calls internal functions which fetch data from database. </li>
    <li> <b>config.py</b> : This is where the database configurations are made.</li>
    <li> <b>db_models.py</b> : the function which connects to Database is defined here which uses SQL Alchemy library for connecting to database and fetching and returning the result </li>
    <li><b>requirements.txt</b> : this files defines which all libraries and packages one requires to run this project.</li>
    </ul>
    </p>
    
      
  



