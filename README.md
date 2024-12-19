# Authentication-Application

# User Registration Using API Call (Postman)
In that section, We are registering a user through postman api. When user register that time the jwt token is created or generated based on user credentials. I guide u step by step.

1. After setting the project you want to create super user. Login the admin panel and create a token for admin.
2. After creating token go to postman and paste the url of registration api and set the post method.
3. After setting the method go to the headers and add the key <b>Authentication </b> and value <b> Token token_key </b> ex.(Token 96df3e12925550abc0676b7a3abc666ca5a358ae) Without token setup you didn't get access.
4. After that go to body section and select raw option and select JSON and write the data <b>username, password</b> and <b>confirm password</b> in JSON Format and hit the api, You are successfully register and get <b>JWT Token</b>.
5. If you are getting <i> Authentication credentials were not provided </i> error then you have a problem in token setup.
Example.
<br>
<br>

![alt text](<Output/generate jwt token using registration.png>)

# Fetch Data Using Authorization
In that section, We are trying to access the data from server using api. If user registered then the user can access the data.

1. After setting the project you want to create super user. Login the admin panel and create a token for admin.
2. After creating token go to postman and paste the url of data fetching api and set the GET method.
3. After setting the method there is two options to access the data using Token Authentication or JWT Authentication. 
    1. If you have simple Token go to the headers and add the key <b>Authentication </b> and value <b> Token token_key </b> ex.(Token 96df3e12925550abc0676b7a3abc666ca5a358ae) Without token setup you didn't get access.
    2. If you have JWT Token the go to the Authorization and select Bearer Token and pass the access key in given field.

4. After that hit the api if you registered then you got data otherwise you get error.
5. If you are getting <i> Authentication credentials were not provided </i> error then you have a problem in token setup.

Example.

![alt text](<Output/getDataUsing token.png>)