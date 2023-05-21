# [Shooni](https://shooni.org)  

![shooni_logo](/frontend/app/src/assets/images/halffatbird.png)

## 1. What is Shooni?  
**tldr: a website (shooni.org) that helps college students to find their desired housing much faster and easier**  

Our objective is to simplify the housing search process by providing a centralized location to help college students to find their desired housing. Research into existing solutions from our competitors, Apartments.com, Zillow, and Facebook, shows that the market lacks a single platform that effectively centralizes all desirable aspects, leading to an inefficient and complex search process. To address this issue, we started and are continuing on building a user-friendly forum that allows students to filter their search based on their preferences with helpful features such as a two-way rating system(agency(homeowner) <-> user(renter)), a roommate search system, sublease opportunities, and a community forum.

## 2. Shooni System Overview
![system_overview](/images/sys_overview.png)


## 3. GitHub Repository Outline

Shooni  
 |  
 |__ frontend (written in Vue3 + Vite)  
 |&emsp;|__ app : frontend written in Vue3 + Vite  
 |   
 |__ backend (written in python; works with gcloud functions and firestore)  
 &emsp;|__ backend_scrape: scrapes data from housing websites and updates db on a daily basis  
 &emsp;|__ backend_fetch: fetches data from firestore and sends data to the frontend based on http(s) requests






