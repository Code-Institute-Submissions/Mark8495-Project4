# **Table Of Contents**

# **Introduction**
This project is my 4th project in the 5 project course for Code Institute.

This was an idea I had in mind when I began to plan the project. I wanted to create a great website where users could upload and share their recipes that they considered divine.
I followed the Django Blog Tutorial from Code Institute course. I found going over the blog project great in building my confidence in working with Django.

The main requirement of this project was to build a Full Stack site based on business logic used to control a centrally-owned dataset. This required me as the developer to set up an authentication and provide role-based access to the site's data.

The Site is a great community platform where they can share their favourite dishes, they can also comment and give suggestions to other peoples recipes.


# **UX**
## **User Stories**
### **Users**
1. As a User I can look through a paginated list of recipes.
2. As a User I can click and see a users' recipes so that the User can expand their cooking knowledge
3. As a User I can upload my recipe so I can share it with other users
4. As a User I can upload images with my recipes so other users can see what the recipe will make
5. As a User I can see the comments and number of likes so that I can keep up with people's opinion about the post
6. As a User I can sign in and out of the my account safely and securely
7. As a User I can comment on posts so that I can interact with other Users
8. As a User I can see my login status so that I know if they are logged in or not
9. As a User I can like and unlike posts so I can intereact with the content
10. As a User I can create, read, update and delete posts so I can manage the content I create

### **Admin**
1. As an Admin I can filter, search and delete posts so that I can manage my website content.
2. As an Admin I can control what comments stay on posts so that I can filter out objectionable comments.

#### **Site Aims**

My main aim for the project was to create a site where the users could share their recipes with ease, as well as interact with other people interested in cooking. I wanted to create a community where people interested in cooking or learning to cook.

A user could also use the site to store their recipes for their own use in the future.

The website focuses on the following target audiences:

- **Demographic:**
    - Food loving people
    - People looking for more recipes to expand their food knowledge
    - Cooking enthusiasts

The website needs to enable the user to:
- Browse recipes
- Create and set up their account
- Create and upload their recipes
- Like and comment on a recipe

The website needs to enable the admin to:
- Approve recipe uploads and comments
- Filter through recipes, comments, and users to ease control of the site

#### **Scope**
A scope was defined to identify what needed to be done to align features with the strategy previously defined. Due to the imbalance of scores above, there will be some trade-offs. The was broken into these categories:

- **Content Requirements**
    
    - The UX *must* address these:
        - A comprehensive list of recipes.
        - A comprehensive set of instructions with ingredients to follow.
        - A list of all comments made on a recipe.
    - The UX *should* accommodate these:
        - Easy navigation of the site.
        - Ability to comment and like recipes.

### **Structure**
I

#### **Database Schema**
Here is the database schema for my intial plan for my database tables:

#### **Skeleton**

### **Design**

#### **Typography**
#### **Colour Scheme**
#### **Imagery**

# **Features** 
## **Design Features**
Each page of the website features a consistent responsive navigational system:

## **Exisiting Features**

## **Features to Implement in the future**
- A profile page for all users where all their recipes and favorites are shown on one page.

## **Issues and Bugs**

## **Testing**
### **User Stories**

### **Manual Testing**

#### **Common Elements Testing**

#### **Page Testing**

### **Automated Testing**
The [W3C Markup Validator](https://validator.w3.org/ "Link to M£C Markup Validator Site") service was used to validate the `HTML` and `CSS` code used. The [PEP8 Python Validator](http://pep8online.com/ "Link to the PEP8 Python Validator Site") was used to validate the `Python` code used.

- HTML pages - Code Validation - all HTML pages clear.

- CSS Stylesheet - CSS tested with no errors.


#### **User Testing** 
I asked fellow users on slack to test out my project and listened to any problems they had with the site.

I also asked my family to test it on several different devices and browsers and changed anything that they found wrong with the site.

#### **Browser Validation**
I tested my project on both chrome and safari.
## **Technologies Used**
### Main Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")

### Additional Languages Used
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to Python Wiki")
     - Used to implement Django functionality, including building models, forms, and views for the app.

### Frameworks, Libraries & Programs Used
- [Django](https://www.djangoproject.com/ "Link to Django Project website")
    - Django was used to build the models, forms, and views of the app, and was the backbone of this project.
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/ "Link to Bootstrap page")
     - Bootstrap was used to implement the responsiveness of the site, using bootstrap classes.
- [Cloudinary](https://cloudinary.com/ "Link to Cloudinary page")
     - Cloudinary was used as free cloud storage for images uploaded to the site through the recipe forms.
- [Summernote](https://summernote.org "Link to Summernote page")
     - Summernote was used to allow users to add styling when adding a recipe to the site. This is particularly useful for using bullet points for ingredients or numbering the steps for the recipe.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/ "Link to the Crispy Forms documentation")
    - Crispy Forms was used to style the add and edit recipe forms, allowing more than one field to occupy a line on the form.
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")
    - Google fonts were used to import the fonts "Poppins" and "Dancing Script" into the style.css file. These fonts were used throughout the project.
- [Font Awesome](https://fontawesome.com/ "Link to FontAwesome")
     - Font Awesome was used on all pages throughout the website to import icons (e.g. social media icons) for UX purposes.
- [Git](https://git-scm.com/ "Link to Git homepage")
     - Git was used for version control by utilizing the GitPod terminal to commit to Git and push to GitHub.
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project after pushing
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
     - Am I Responsive was used to see responsive design throughout the process and to generate mockup imagery to be used.
## **Deploymemt**

This project was developed using a [GitPod](https://gitpod.io/ "Link to GitPod") workspace. The code was committed to [Git](https://git-scm.com/ "Link to Git") and pushed to [GitHub](https://github.com/ "Link to GitHub") using the terminal.

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Attach the Postgres database:
    - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

3. Prepare the environment and settings.py file:
    - In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    - In your GitPod workspace, create an env.py file in the main directory. 
    - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    - Add the SECRET_KEY value to the Config Vars in Heroku.
    - Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    - Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
    - In settings.py add the following sections:
        - Cloudinary to the INSTALLED_APPS list
        - STATICFILE_STORAGE
        - STATICFILES_DIRS
        - STATIC_ROOT
        - MEDIA_URL
        - DEFAULT_FILE_STORAGE
        - TEMPLATES_DIR
        - Update DIRS in TEMPLATES with TEMPLATES_DIR
        - Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

4. Store Static and Media files in Cloudinary and Deploy to Heroku:
    - Create three directories in the main directory; media, storage, and templates.
    - Create a file named "Procfile" in the main directory and add the following:
        - web: gunicorn project-name.WSGI
    - Log in to Heroku using the terminal Heroku login -i.
    - Then run the following command: **heroku git:remote -a your_app_name_here** and replace your_app_name_here with the name of your Heroku app. This will link the app to your Gitpod terminal.
    - After linking your app to your workspace, you can then deploy new versions of the app by running the command **git push heroku main** and your app will be deployed to Heroku.
    