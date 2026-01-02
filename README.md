# AI Multi Genre Movie and Web Series Recommendation System
This project is an Artificial Intelligence based Movie and Web Series Recommendation System that recommends movies based only on user selected genres.
The system works using content based filtering and public ratings from a dataset. It is implemented completely in Python and works offline.


## Project Description
The purpose of this project is to help users find movies and web series that match their interests without manually searching through large collections.
The user only needs to enter one or more genres and the system recommends the top rated movies belonging to those genres.
The recommendation logic filters movies that match all the selected genres and then sorts them based on their average public rating.
This ensures that the recommendations are both relevant and high quality.



## Features
Genre based recommendation system  
Supports single and multiple genre input  
Uses real world movie dataset  
Ranks movies based on public ratings  
Simple command line interaction  
Works without internet or APIs  


## Technologies Used
Programming Language  
Python  

Libraries  
Pandas for data loading and data processing  



## Dataset Information
The dataset used in this project is a movie dataset stored in a CSV file.

Columns used from the dataset  
title represents the movie or web series name  
overview represents the description  
genres represents the genre information  
vote_average represents the public rating  
The dataset is static and used only for educational purposes.


## How the System Works

1 The dataset is loaded using Pandas  
2 Required columns are selected  
3 Missing values are handled  
4 Genre text is converted to lowercase for matching  
5 User enters one or more preferred genres  
6 Movies matching all selected genres are filtered  
7 Results are sorted by rating  
8 Top movies are displayed to the user  
9 The process repeats until the user exits  


## How to Run the Project

Step 1  
Make sure Python is installed on your system  

Step 2  
Install the required library  
pip install pandas  

Step 3  
Place the dataset file in the project folder and rename it to  
movies.csv  

Step 4  
Run the program  
python recommender.py  


## Example Usage

Enter preferred genre  
Action Sci Fi  

The system will display the top rated movies that belong to both Action and Science Fiction genres.

---

## Advantages

Easy to use  
Fast execution  
No internet required  
Accurate genre based filtering  
Suitable for academic projects and internships  


## Limitations
Does not use user behavior or history  
No real time data updates  
Recommendations depend on dataset quality  



## Future Enhancements
Adding collaborative filtering  
Using hybrid recommendation techniques  
Adding sentiment analysis on reviews  
Creating a web interface  
Including user rating input  


## Use Cases
Academic Artificial Intelligence projects  
Internship submissions  
Learning recommendation systems  
Movie content discovery  


## Author
Ajay Sukhdev Pawar  
Computer Engineering Student  
Interested in Artificial Intelligence Machine Learning and Data Science  


## License
This project is created for educational purposes and can be freely used modified and learned from.

## Description/Note
The recommendation system is designed to support future updates by modifying the movies.csv file.
New movies and web series can be added by inserting new records with correct title overview genre and rating values.
Once the dataset is updated the system will automatically consider the new data in future recommendations without requiring any changes in the program code.

The system is case sensitive while processing genre input. Therefore users must enter genre names with correct spelling and proper use of capital and small 
letters as they appear in the dataset. Incorrect spelling or mismatched letter cases may result in no recommendations being found.

This behavior ensures accurate matching between user input and dataset content and highlights the importance of consistent data formatting


