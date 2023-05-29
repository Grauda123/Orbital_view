# gotEat

## Table of Contents
* [General Info](#general-information)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Usage](#usage)
* [To do](#to-do)
* [Acknowledgements](#acknowledgements)



## General Information
Is there someone u know who always skips meals because they are too preoccupied with their work? Do you have a friend that always asks you what to eat during lunch?
The objective of this project is to develop a Telegram bot that assists individuals in building and maintaining healthy eating habits. 
Our project aims to address the common dilemma of deciding what to have for lunch by providing personalized meal recommendations and guidance and also the challenge of diet procrastination and meal skipping.
We chose to create a telegram bot because of the ease of use and accessibility, where users do not need to download another application.

### Motivation
I have bad eating habits. As a student, I tend to be so occupied with my assignments, tutorials and classes that I will skip meals or even forget them. When my friend sees me, she will always ask "u got eat?". Unfortunately, skipping meals is also quite a common occurrence in this busy Singapore. I hope to use this opportunity to help fellow meal forgotters and myself to build a healthy eating habit, along with the added extension of this application to build a healthier lifestyle. 

### User stories
- As a user, I would like to keep track of what I eat and set diet goals 
- As the system, I would praise those who complete their goals, encourage those who did not meet their goals.
- As the system, I would like to generate summary statistics.
- As the system, I would recommend food schedules.
- As a user, I would like to be reminded when to eat, drink water (as notifications).
- As a user, I would like to receive recommendations for exercise plans. 

## Features
List the ready features here:
- Log meal
- Edit meal
- Delete meal 

## Technologies Used
- python 3.11
- mysql
- Xampp (for hosting)


## Setup

<!--- Proceed to describe how to install / setup one's local environment / get started with the project. -->
#### Creating the telegram bot: In telegram chat, search for BotFather and choose the one with the tick.
<img
  src="/img/search_botfather.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
  
#### Create the telegram bot with the /newbot command and name the telegram bot.
<img
  src="/img/createbot.jpg"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

Here are the steps to follow before starting `gotEat`:

#### Download [XAMMP](https://www.apachefriends.org/download.html) 

#### Select accordingly to your operating system (ver. 8.2.4) 

<table border="0">
 <tr>
    <td><b style="font-size:15px">MacOS</b></td>
    <td><b style="font-size:15px">Windows</b></td>
 </tr>
 <tr>
    <td>
      <img src="/img/xampp_mac.png" alt="Alt text" title="Optional title" style="display: inline-block; margin: 0 auto; max-width: 300px">

</td> <!-- replace with sc-->
    <td> <img src="/img/xampp_win.png" alt="Alt text" title="Optional title" style="display: inline-block; margin: 0 auto; max-width: 300px"> <!-- replace with sc-->
 </tr>
</table>

#### When you have successfully downloaded, doublic click it and run. 

<img
  src="/img/mac-installer.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

### For macOS, you may face some error, follow these steps: 

- give permission to open XAMMP by clicking 'open'

<img
  src="/img/xampp_open.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">


- if 'open' is not shown at first, go to 'System Preferences' -> 'Security & Privacy' -> 'General' -> 'Click the lock to make changes' -> allow XAMMP download -> 'open'

<img
  src="/img/xampp_adv.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">


#### At setup page, proceed with 'next' 
<img
  src="/img/xampp_setup.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

#### Followed by 'Finish'
<img
  src="/img/xampp_finish.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

 #### After downloading, keep XAMMP running 
 <img
  src="/img/xampp_finish2.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
 
 #### In XAMMP, go to 'Manage Servers'
<img
  src="/img/xampp_manageServers.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
  
#### 'Start' servers Apache and MYSQL 
<img
  src="/img/xampp_start.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

### For windows: 
#### Start both the Apache Module and Mysql module
<img
  src="/img/start.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
  

#### Click Config button for the Apache module and select *phpMyAdmin(config.inc.php)*
<img
  src="/img/apache_config.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

#### This image shows an example of the *phpMyAdmin(config.inc.php)*. The *$cfg['Servers'][$i]['user']* and *$cfg['Servers'][$i]['password']* field shows the username and password for authentication to mysql database.
<img
  src="/img/config.inic.php.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

#### Create a folder and inside this folder create *config.ini* file ,*main.py* file and an empty sessions folder
<img
  src="/img/folder_requirements.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

#### Edit the *config.ini* file to 
- add in the api_id, api_hash which can be found with this link(#https://my.telegram.org/auth)
- Add in the bot token which can be found from BotFather
(click on the API token button to retrieve the bot token)
<img
  src="/img/botfather.jpg"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
  
- hostname = 127.0.0.1 (change the ip address if you are hosting online)
- username = *$cfg['Servers'][$i]['user']* field from the *phpMyAdmin(config.inc.php)* file.
- password = *$cfg['Servers'][$i]['password']* field from the *phpMyAdmin(config.inc.php)* file.
- database = give it any name

### Import the various packages
#### configparser is used to read the config.ini file that was created
> pip install configparser
#### telethon is a library used to communicate the telegram API
> pip install telethon
#### mysqldb is used to connect to the mysql database
> pip install mysqlclient


## Usage
<!-- After completing the setup above, in the telegram search bar, type in `gotEat` or [vist](https://t.me/gotEatBot). -->

- `/log_meal` + food name + number of servings -> log meal eaten 
<img
  src="/img/log_meal.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
  
- `/view_logs` -> returns meal ID, food name, number of servings, date logged.

- `/update_logs` + meal_id + meal_no + meal -> to change meal log
<img
  src="/img/update_log.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">


- `/delete_log` + meal_id -> remove meal log

  <img
  src="/img/delete_log.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
  
## To do

1. Meal recommendations with calories
   - recommends the user a different type of food everytime.
2. option to set reminders
   - user can set meal reminders and reminder to take a break.
   - This is optional to the user. 
3. user statistics
   - download a summary of what the user has eaten during a predefined interval from the database.
4. excercise recommendation
   - recommend different excercies based on which the user would like to target.
5. send telegram stickers

## Acknowledgements

- This project was inspired by our everyday busy life in NUS and our unhealthy eating habits
- This project was based [many](#https://www.youtube.com/watch?v=jkSI-floXs8) [tutorials](https://www.youtube.com/watch?v=EzFq8WnO1Gw).
- Many thanks to our advisor 

