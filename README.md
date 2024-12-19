# Authentication-Application

# User Registration Using API Call (Postman)
In that section, We are registering a user through postman api. When user register that time the jwt token is created or generated based on user credentials. I guide u step by step.

1. After setting the project you want to create super user. Login the admin panel and create a token for admin.
2. After creating token go to postman and paste the url of registration api and set the post method.
3. After setting the method go to the headers and add the key <b>Authentication </b> and value like <b> Token token_key </b> Without token setup you didn't get access.
4. After that go to body in and go to the raw option and select JSON and write the data <b>username, password</b> and <b>confirm password</b> in JSON Format and hit the api, You are successfully register and get <b>JWT Token</b>.
5. If you are getting <i> Authentication credentials were not provided </i> error then you have a problem in token setup.
<br>
<br>

![alt text](<Output/generate jwt token using registration.png>)