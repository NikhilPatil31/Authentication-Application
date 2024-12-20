# Authentication-Application
<br>
# User Registration Using API Call (Postman)
<br>
In that section, We are registering a user through postman api. When user register that time the jwt token is created or generated based on user credentials. I guide you step by step.
<br>
1. After setting the project you need to create super user. Login the admin panel and create a token for admin.
2. After creating token go to postman and paste the url of registration api and set the post method.
3. After setting the method go to the headers and add the key <b>Authentication </b> and value <b> Token token_key </b> ex.(Token 96df3e12925550abc0676b7a3abc666ca5a358ae) Without token setup you didn't get access.
4. After that go to body section and select raw option and select JSON Type and write the data <b>username, password</b> and <b>confirm password</b> in JSON Format and hit the api, You are successfully register and get <b>JWT Token</b>.
5. If you are getting <i><b> Authentication credentials were not provided </b></i> error then you have a problem in token setup.
<br>
Example.
<br>
<br>

![alt text](<Output/generate jwt token using registration.png>)

<br><br>

# Fetch Data Using Authentication(Token Authentication/ JWT Token Authentication)
<br>
In that section, We are trying to access the data from server using api. If user registered then the user can access the data.
<br>
1. After setting the project you need to create super user. Login the admin panel and create a token for admin.
2. After creating token go to postman and paste the url of data fetching api (studentsapi/) and set the GET method.
3. After setting the method there is two options to access the data using <b>Token Authentication or JWT Authentication</b>. 
    1. If you try to access using <b>Token Authentication</b> go to the headers and add the key <b>Authentication </b> and value <b> Token token_key </b> ex.(Token 96df3e12925550abc0676b7a3abc666ca5a358ae) Without token setup you didn't get access.
    2. If you try to access using <b>JWT Token Authentication</b> go to the Authorization and select Bearer Token and pass the access key in given field.

4. After that hit the api if you registered then you get data otherwise you get error.
5. If you are getting <i><b> Authentication credentials were not provided </b></i> error then you have a problem in token setup.
<br>
Example.
<br>
<br>

![alt text](<Output/getDataUsing token.png>)

<br><br>

# Generate a JWT Token Based on given data
<br>
In that section, we are trying to generate a JWT Token Based on User Details like Firstname, Lastname and Age.
<br>

1. After setting the project you need to create super user. Login the admin panel and create a token for admin.
2. After creating token go to postman and paste the url of generate jwt token api(generate-token/) and set the POST method.
3. After setting the method you don't need to add a token to access api so we bypass that.
4. After that go to params section and write the data <b>Firstname, Lastname</b> and <b>Age</b> in key value and hit the api, You are successfully get generated <b>JWT Token</b>.
<br>
Example.
<br>
<br>

![alt text](<Output/generate token using given data.png>)

<br>
<br>

# Refresh JWT Token
<br>
In that section, We are trying to refresh the JWT Token. JWT provides method to refresh the expired JWT Token. Which helps to work fluintly.
<br>
1. After completing User registration using api call (postman) we get a two tokens Refresh Token and Access Token. Access Token used to accessing the data. Access token is expired after some time then we call the method which helps to generate new access token or refresh the access token.
2. When Access token expired goto postman and paste the url of refresh token api(api/token/) and select POST method.
3. After that goto body section and select raw option and select JSON Type and write the <b>username, password</b> in JSON Format and hit the api, You are successfully get refreshed <b>JWT Token</b>.
<br>
Example.
<br>
<br>

![alt text](<Output/refresh jwt token.png>)

<br><br>

# Get or Create Token Using API Call
<br>
In that section, We try to generate a Token using API Call. We are creating a Token for a user who is not have any token.
<br>
1. After setting django project you need to create super user. After that if you don't create a token for admin so don't worry we can generate the token either login admin panel or using API Call. But you want the another user token to generate the admin token.
2. So do User registration using api call(postman) then you got JWT Token.
3. After that go to postman and paste the url of login api(login/) and select POST method.
4. After that go to the Authorization and select Bearer Token and pass the access key in given field.
5. Then goto the body section and select raw option and select JSON Type and write the <b>username, password</b> in JSON Format and hit the api, You are successfully get newly created Token or get existed Token.

<br>
Example.
<br><br>

![alt text](<Output/get or create token.png>)

<br><br>