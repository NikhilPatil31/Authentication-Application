# Authentication-Application

# User Registration Using API Call (Postman)
In that section, We are registering a user through postman api. When user register that time the jwt token is created or generated based on user credentials. I guide u step by step.

1. After setting the project you want to create super user. Login the admin panel and create a token for admin.
2. After creating token go to postman and paste the url and set the post method.
3. After setting the method go to the headers and add the key <b>Authentication </b> and value like <b> Token token_key </b>.
4. After that go to body in that go to the raw option and select json and write the data <b>username, password</b> and <b>confirm password</b> and hit the api, You are successfully register and get <b>JWT Token</b>.
 
![alt text](<Output/generate jwt token using registration.png>)