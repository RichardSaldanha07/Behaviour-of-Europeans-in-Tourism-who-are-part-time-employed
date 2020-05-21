# Data-Intensive-Architecture
A project implementation of Hadoop Map Reduce using Java and Python Programming Language
Kindly Read the document for proceeding with the execution of codes

           Note: 
There are 5 folders made which are as follows
1. Java Codes 
2. Python Codes, 
3. Datasets-used, 
4. Filesusedforcorrelation, 
5. Processed-Datasets 
2.	The code folders consist of two sub folders 1. Java Codes consisting of java files(class,jar,.java), csv files, file format files and .pem file
 ready-mainreasonforparttime.csv, ready-participationintourismforpersonalpurpose.csv, part-r-00000, _SUCCESS, richardsaldanha.pem and 2. Python Codes.
3.	The two python files correlation and datacleaning are in Python Codes folder are made available in ipynb and .py file extension. You can run the ipynb and .py file in Anaconda Navigator using Jupiter Note Book. 
4.	The java files (class,jar,.java) are made available which can be executed in the java environment.
5.	Dataset folder consist of two csv files used mainreasonforparttime.csv, participationintourismforpersonalpurposes.csv for analysis
6.	Processed-Datasets consist of dataset after data cleaning and transformation stage
ready-mainreasonforparttime.csv, ready-participationintourismforpersonalpurpose.csv, ready_mainreasonforparttime.csv, ready_participationintourismforpersonalpurpose.csv.
7.	Filesusedforcorrelation folder consist of part-r-00000 and correlation.csv file

Steps to Perform Hadoop MapReduce Reduce Side Join
1.	Connect to Amazon EC2 instance by opening an SSH client or connecting using a PUTTY and locate the .pem file on your local machine and connect it using its public DNS ssh -i "richardsaldanha.pem" ubuntu@ec2-52-214-202-124.eu-west-1.compute.amazonaws.com
2.	 Login to hadoop user by the following command su - hduser with password as Hadoop.
3.	Make sure that all the environmental variables have been initialized correctly
env | grep HADOOP
env | grep JAVA
4.	Create a directory mkdir diaProjectrichard and give all access to it by chmod 777 diaProjectrichard.
5.	Next, In a separate window, open a terminal in your local machine and navigate to the directory where the csv files are present and transfer it to the environment using the below command sftp -i "richardsaldanha.pem" ubuntu@ec2-52-214-202-124.eu-west-1.compute.amazonaws.com cd /home/hduser/diaProjectrichard 
put ready-mainreasonforparttime.csv put ready-participationintourismforpersonalpurpose.csv
bye
6.	Now once you have your two csv files we then copy them from local file system to hdfs
cd /home/hduser/diaProjectrichard
hdfs dfs -mkdir /user/hduser/ProjectMRJoin-in
hdfs dfs -copyFromLocal */ user/hduser/ProjectMRJoin-in
hdfs dfs -ls /user/hduser/ProjectMRJoin-in
7.	In the next step, we will create a java file using either vim editor or nano command in which we will perform Reduce-side join on our two CSV files 
ready-mainreasonforparttime.csv  and ready-participationintourismforpersonalpurpose.csv, where we will create two mapper class, which are ParttimeMapper and TourismMapper which will hold the key which is country\_period  a primary key in one dataset and a foreign key in another dataset along with the values which are columns value\_in\_percent in both CSV files. In the Reducer class, we will perform the operation to count the total number of occurrences,totalparttime and totaltourism for that particular key which is our country\_period
8.	we compile using the command hadoop com.sun.tools.javac.Main DiaProjectMRJoin.java , after successfully compilation we generate a jar file by using the command  jar cf DiaProjectMRJoin.jar*.class
9.	We then run the hadoop task  using the command hadoop jar DiaProjectMRJoin.jar DiaProjectMRJoin ProjectMRJoin-in/ready-mainreasonforparttime.csv ProjectMRJoin-in/ready-participationintourismforpersonalpurpose.csv outDiaProjectMRJoin
10.	 if there are errors we then check for the errors in the diaProjectMRJoin.java file and solve the errors.
11.	 Once errors are solved we check the output director on HDFS by navigating to the directory hdfs dfs -ls /user/hduser/outDiaProjectMRJoin
12.	On successful execution a file by the name part-r-00000 would be created so we navigate to the file by the command  cd ~/diaProjectrichard hdfs dfs -get /user/hduser/outDiaProjectMRJoin/part-r-00000
13.	To inspect the output we make use of the more part-r-00000 command or by cd ~/diaProjectrichard hdfs dfs cat /user/hduser/outDiaProjectMRJoin/part-r-00000.
14.	Take the part-r-00000 file from the Hadoop ecosystem into the local machine by
sftp -i "richardsaldanha.pem" ubuntu@ec2-52-214-202-124.eu-west-1.compute.amazonaws.com
cd /home/hduser/diaProjectrichard
get part-r-00000
15.	Convert it to Excel and perform Pearson Coefficient of correlation in Python.




