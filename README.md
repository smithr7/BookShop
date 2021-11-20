# BookShop Project

The BookShop Project is an online shop for buying books. It encompasses common favourite and newly released literature for reading. The website component itself is designed to allow users to shop around for whatever book they want. 

## What is included in this github?

The core components of this git-hub include the webpages, python FLASK script to action the website. Additional content include cascading style sheets and image content within the static file located under src. Please note the cascading style sheets is run under the FLASK script and not directly into the HTML as referenced. The images also are run through a reference within the database system.

## Executing script

Please use the terminal bash in either codio or on the website to pull this repository. Upon pulling the repository, locate the 5001CEM_Software_Engineering/bin/ and execute the BookShop.py as shown for codio and bash terminal:

```
export FLASK_APP=BookShop
flask run (--host=0.0.0.0)
```
Proceed to use the local machine url or server box info to load the login page. Please see information on accessing this below:

```
Local machine url: http://127.0.0.1/
Codio server box: https://metal-bagel-80.codio-box.uk
```

## Website layout

Book Shop website layout operates by the following hierarchy:

```
- Login Page
-   Home Page
-     Books Page
-       Check out
-         Payment
-     About us
-     Contact us    
```
Indentation in this situation demonstrates child elements of a parent element be them webpages or modals (functions of the webpages). 
