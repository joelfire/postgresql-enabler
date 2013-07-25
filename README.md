==========================================================================
PostgreSQL 9.2.4 Server Enabler Guide
==========================================================================
Introduction
--------------------------------------
A Silver Fabric Enabler allows an external application or application platform, 
such as a J2EE application server to run in a TIBCO Silver Fabric software 
environment.  This document describes what is involved in developing a reasonably 
full-featured PostgreSQL enabler using Python.

Requirements
------------
* Silver Fabric 5.x 
* Java 7 SDK
* Maven 3.0
* Linux x64

Installation
--------------------------------------
The PostgreSQL Server Enabler consists of an Enabler Runtime Grid Library and a Distribution 
Grid Library. The Enabler Runtime contains information specific to a Silver Fabric 
version that is used to integrate the Enabler, and the Distribution contains a binary 
distribution of PostgreSQL used for the Enabler. Installation of the MySQL Server 
Enabler involves copying these Grid Libraries to the 
SF_HOME/webapps/livecluster/deploy/resources/gridlib directory on the Silver Fabric Broker. 


Creating and Installing the Grid Libraries
------------------------------------------
* Download the PostgreSQL binary archive from http://www.enterprisedb.com/products-services-training/pgbindownload.
* Create a pom.properties file, and set the location of your archive and your Broker installation. See the commnets in the pom.xml file for more information.
* On the command line, type 'mvn install -Ddist'. This will build the libraries and install them to the Broker.
* Go to the Silver Fabric Broker's console, select Stacks>Enablers, and click Global Actions>Update Deployment Files. The Enabler should now be in the list.
       
*****************************************************************************
NOTE: as of now, only 64-bit linux is supported. 
******************************************************************************


Runtime Context Variables
--------------------------------------
Below are some notable Runtime Context Variables associated with this Enabler.
Take a look at the container.xml file in the src/main/resources/runtime/ subdirectory

 APP_DATA_DIR - path where the database files are located; 
  			NOTE: for persistence across engine hosts, it is recommended you
                 specify a network-mounted directory for this variable.
                 Changing this will also affect other variables (e.g, CAPTURE_INCLUDES)              

 RUNAS_USER - The user the server will run-as. Will be created on the host if it does not exist.
 
 LISTEN_ADDRESSES - Addresses on which to listen. * means all.
 
 PORT - port where this database listens for connections.

 MAX_CONNECTIONS - the maximum allowed connections to the server.

 
