#1. Launch browser
#2. Navigate to url 'http://automationexercise.com'
#3. Verify that home page is visible successfully
#4. Click on 'Signup / Login' button
#5. Verify 'New User Signup!' is visible
#6. Enter name and already registered email address
#7. Click 'Signup' button
#8. Verify error 'Email Address already exist!' is visible

#import libraries
#set playwright as proper browser
#set page
#browser = p.chromium.launch(headless=False)
        #page = browser.new_page()
#launch browser
#goto.page
#use previous code to create account then to logout
#expect to have title
#Locate signup /login button (link) and click
#expect text new user signup!
#locate text slotes (type[input] or data-qa) and fill
#locate button (role?class?) signup and click
#expect text email address already exist to be visible