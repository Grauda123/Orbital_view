# gotEat

## Table of Contents
* [General Info](#general-information)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Usage](#usage)
* [Updates from last milestone](#updates)
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
- db4free (for mysql hosting)
- UptimeRobot for continuous polling.

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

#### Create an account on [db4free](https://www.db4free.net/signup.php) 

#### Create your own database credentials and create the account.
<img
  src="/img/signup_db4free.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">


#### After successful creation of the account, go to phpmyAdmin from the side navigation.
<img
  src="/img/access_phpmyAdmin.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

### The database created can be accessed from the side panel with the value from the MySQL database name in the signup.
<img
  src="/img/phpmyAdmin_db.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">


#### Create an account on [UptimeRobot](https://uptimerobot.com/signUp) 
<img
  src="/img/uptimeRobot_createAcc.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

### After log in, add a new monitor which can be found in the top left
<img
  src="/img/uptimeRobot_main.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

### Details for the new Monitor:
- For the Monitor type: select HTTP(s).
- Friendly Name: Choose any name you would like to call your Monitor.
- URL (or IP): enter your web server link. In the example below, we used the online IDE, replit.
  
  <img
  src="/img/replit_weblink.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
  
- Monitoring Interval and Monitor timeout: Default values
- Tick the alert notify checkbox. This is to notify you via email in the event when your server is down or ran into any problems.
  
  <img
  src="/img/uptimeRobot_alert.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

Overall this would be how it would look like. Click the Create Monitor button at the bottom. Now you would be able to monitor the status of the telegram bot.
<img
  src="/img/uptimeRobot_main.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">



### Import the various packages
#### configparser is used to read the config.ini file that was created
> pip install configparser
#### telethon is a library used to communicate the telegram API
> pip install telethon
#### mysqldb is used to connect to the mysql database
> pip install mysqlclient


## Usage
<!-- After completing the setup above, in the telegram search bar, type in `gotEat` or [vist](https://t.me/gotEatBot). --> 

### Starting page 
- to ensure that you are at the right bot, refer to the two pictures below.
  <table border="0">
 <tr>
    <td><b style="font-size:15px">Landing page</b></td>
    <td><b style="font-size:15px">After 'Start'</b></td>
 </tr>
 <tr>
    <td>
      <img src="/img/gotEat_start.png" alt="Alt text" title="gotEat landing page" style="display: inline-block; margin: 0 auto; max-width: 300px">

  </td> <!-- replace with sc-->
    <td> <img src="/img/gotEat_start2.png" alt="Alt text" title="After 'start'" style="display: inline-block; margin: 0 auto; max-width: 300px"> <!-- replace with sc-->
 </tr>
</table>

## `/logmeal` + food name + number of servings -> log meal eaten 
<img
  src="/img/logmeal_start.png"
  alt="Alt text"
  title="logmeal_start"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
  
### "Are you having your meal now?" 

#### if you selected `Nope` 
- select the date of entry for the meal you would like to log. Ranges -3 days from the current date.
  <img
  src="/img/logmeal_nope.png"
  alt="Alt text"
  title="logmeal_start"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

- Input the time of the meal in the HH:MM format (24- hour clock)

<table border="0">
 <tr>
    <td><b style="font-size:15px">Log time</b></td>
    <td><b style="font-size:15px">Log time confirmation</b></td>
 </tr>
 <tr>
    <td>
      <img src="/img/logmeal_nope1.png" alt="Alt text" title=“Log time” style="display: inline-block; margin: 0 auto; max-width: 300px">

</td> <!-- replace with sc-->
    <td> <img src="/img/logmeal_nope2.png" alt="Alt text" title=“Log time confirmation” style="display: inline-block; margin: 0 auto; max-width: 300px"> <!-- replace with sc-->
 </tr>
</table>

#### if you selected `Yup!` or finished inputing your time, you will be presented the next set of queries

### "Please select the type of the meal:" 
- There are four options: "Breakfast", "Lunch", "Dinner" or "Snack"
- Select one of the four options that best describe the meal you want to log
  
<img
  src="/img/logmeal_selectmeal.png"
  alt="Alt text"
  title="logmeal_start"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

- Your option is successfully recorded when you see "You have selected (option)"

### "What have you eaten today?" 
- input the meal that you are eating

  <img
  src="/img/logmeal_beefnood.png"
  alt="Alt text"
  title="logmeal_start"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

- gotEat will find the option closest to the name of meal entered
- select the option presented

### "Meal entry logged successfully!" 

  <img
  src="/img/logmeal_successful.jpg"
  alt="Alt text"
  title="logmeal_start"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

# Updates
- We have recently made significant updates to our database hosting.
- Previously, our users had to download a hosting solution, which essentially transformed their computers into hosts.
- However, we have now transitioned to an online hosting platform, enabling us to make our database available online.
- As part of this update, we have replaced XAMMP, the previous hosting tool, with PHPAdmin.
  
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

