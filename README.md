# login-page-with-excel
Creating a login interface and saving information in excel sheet

This project contains 3 different files:
  1. login_excel.py
  
     Reading data from an excel sheet containg username (column 1) and password (column 2). It is kind of a login interface 
     which verfies correct credentials and then prits out that the user has logined successfully.
     At the end of this code, I have imported a file which saves username and password, if you dont want it then you can just
     delete that part (20 to 28).
     
  2. login_info.py
     
     Taking in data from user and then saving the username and password in a excel sheet, just like a database. At the end of this
     code, I have imported a file which will then ask you to login with the username and password you just created, you can certainly
     take out that part(40 to 42)  if you would like to.
     
  3. login_info_otp.py (Code verification by sending an email)
     
     This whole code is very similar to the second one but the only difference is that over here you have to provide an email instead
     of username and then an email would be sent to you with a code which you will have to provide to successfully create your account.
     This is just like an email verification code.

Prerequisite:
  1. A excel sheet with cell A1 = USERNAME and cell B1 = PASSWORD
  2. Downloading libraries such as openpyxl and pandas
  
Additional Information :
  1. In login_info_otp.py, I have used local environment variable which contains the information regarding my email and password, I used it so that I don't
     have to write my credentials. I will attach a link which contains information about creating environment variables.
  2. Environment Variables (Windows):  https://www.youtube.com/watch?v=IolxqkL7cD8
     Environment Variables (Mac and linux):  https://www.youtube.com/watch?v=5iWhQWVXosU&t=78s
  3. Sending an email with python: https://www.youtube.com/watch?v=JRCJ6RtE3xU&t=1522s
  4. Automating excel with python : https://www.youtube.com/watch?v=7YS6YDQKFh0&t=549s
     
