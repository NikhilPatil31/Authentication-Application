# Authentication-Application

# User Registration Using API Call (Postman)
In that section, We are registering a user through postman api. When user register that time the jwt token is created or generated based on user credentials. I guide u step by step.

1. After setting the project you want to create super user. Login the admin panel and create a token for admin.
2. After creating token go to postman and paste the url of registration api and set the post method.
3. After setting the method go to the headers and add the key <b>Authentication </b> and value <b> Token token_key </b> ex.(Token 96df3e12925550abc0676b7a3abc666ca5a358ae) Without token setup you didn't get access.
4. After that go to body section and select raw option and select JSON and write the data <b>username, password</b> and <b>confirm password</b> in JSON Format and hit the api, You are successfully register and get <b>JWT Token</b>.
5. If you are getting <i> Authentication credentials were not provided </i> error then you have a problem in token setup.
<br>
Example.
<br>
<br>

![alt text](<Output/generate jwt token using registration.png>)

<br><br>

# Fetch Data Using Authorization
In that section, We are trying to access the data from server using api. If user registered then the user can access the data.

1. After setting the project you want to create super user. Login the admin panel and create a token for admin.
2. After creating token go to postman and paste the url of data fetching api and set the GET method.
3. After setting the method there is two options to access the data using <b>Token Authentication or JWT Authentication</b>. 
    1. If you try to access using <b>Token Authentication</b> go to the headers and add the key <b>Authentication </b> and value <b> Token token_key </b> ex.(Token 96df3e12925550abc0676b7a3abc666ca5a358ae) Without token setup you didn't get access.
    2. If you try to access using <b>JWT Token Authentication</b> go to the Authorization and select Bearer Token and pass the access key in given field.

4. After that hit the api if you registered then you got data otherwise you get error.
5. If you are getting <i> Authentication credentials were not provided </i> error then you have a problem in token setup.
<br>
Example.
<br>
<br>

![alt text](<Output/getDataUsing token.png>)

<br><br>

# Code to generate a JWT Token Based on given data
In that section, we are trying to generate a JWT Token Based on User Details like Firstname, Lastname and Age.
<br>

1. After setting the project you want to create super user. Login the admin panel and create a token for admin.
2. After creating token go to postman and paste the url of generate jwt token api and set the post method.
3. After setting the method we don't need to add a token to access api so we bypass that.
4. After that go to params section and write the data <b>Firstname, Lastname</b> and <b>Age</b> in key value and hit the api, You are successfully get generated <b>JWT Token</b>.
<br>
Example.
<br>
<br>

![alt text](<Output/generate token using given data.png>)

<br>
<br>
