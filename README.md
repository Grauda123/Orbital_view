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

## Technologies Used
- python 3.11
- mysql
- db4free (for mysql hosting)
- UptimeRobot for continuous polling.

# Updates
- We have made significant updates to our database hosting.
- Previously, our users had to download a hosting solution, which essentially transformed their own computers into servers. Our database was also local for each user.
- Currently, we have now transitioned to an online hosting platform. Our database is also available online.
- As part of this update, we have replaced XAMMP, the previous hosting tool, with PHPAdmin.
- Improved the functions for easier user interation
- For example:
  - custom calender
  - inline keyboards to minimise user activity.
  - Searching for possible food when user input what they ate.

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
#### python telegram 
> pip install python-telegram-bot
#### mysql module to run mysql statements
> pip install mysql-connector-python

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

#### if the user input does not match with the database, the user can enter their own meal name. 

  <img
  src="/img/nofood.png"
  alt="Alt text"
  title="logmeal_start"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
  
### "Meal entry logged successfully!" 

  <img
  src="/img/logmeal_successful.jpg"
  alt="Alt text"
  title="logmeal_start"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

## /cancel
- this feature allows user to cancel during the middle of their queries, restarting their entry
  <img
  src="/img/cancel.png"
  alt="Alt text"
  title="logmeal_start"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

- user can go back to the start and log their meal


# Testing cases 
  <img
  src="/img/testcase_time.png"
  alt="Alt text"
  title="logmeal_start"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

## To do 

1. Improve on the search of possible food.
2. Fix set reminders feature.
  - user can set meal reminders and reminder to take a break.
  - This is optional to the user. 
4. Fix recommendation for users.
5. Add the option to view and delete records for users.
6. Fix invalid time
7. send telegram stickers
8. user statistics
   - download a summary of what the user has eaten during a predefined interval from the database.

## Acknowledgements

- This project was inspired by our everyday busy life in NUS and our unhealthy eating habits
- This project was based [many](#https://www.youtube.com/watch?v=jkSI-floXs8) [tutorials](https://www.youtube.com/watch?v=EzFq8WnO1Gw).
- Many thanks to our advisor 

