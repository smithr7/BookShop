# BookShop Project

The BookShop Project is an online shop for buying books. It encompasses common favourite and newly released literature for reading. The website component itself is designed to allow users to shop around for whatever book they want. 

## What is included in this github?

The core components of this git-hub include the webpages, python FLASK script to action the website. Additional content include cascading style sheets and image content within the static file located under src. Please note the cascading style sheets is run under the FLASK script and not directly into the HTML as referenced. The images also are run through a reference within the database system.

FLASK Components repository path:

- 5001CEM_Software_Engineering/src/CalculateStockLevels.py<br/>
Administrative control for issuing re-stocking of books and changing of quantities. It also includes the ability to remove and add products

- 5001CEM_Software_Engineering/src/CreditCardProcess.py<br/>
User credit card payment system which captures the data and immediately deletes it upon receiving the data.

- 5001CEM_Software_Engineering/src/LoginCredentials.py<br/>
The main web-page back-end functionality which operates to enable a login and redirects the user when the correct credentials are placed in. Functionality also includes basic security to stop bypassing into the system.

- 5001CEM_Software_Engineering/src/bookInformation.py<br/>
Template for loading database information into it. All the information will be loaded into the associate fields, and inherited functionality with adding to the shopping cart session. Multiple quantities can be ordered on this webpage as well.

- 5001CEM_Software_Engineering/src/booksCatalog.py<br/>
Template with all books including search parameters for the user to select books under specific filters. Without any filters the entire database log from which any books added by the administrators have added.

- 5001CEM_Software_Engineering/src/indexScript.py<br/>
Main home page of the book shop website. All other operations/functionality are achievable through the main webpage. It also includes static webpages such as about us.

Website Components repository path:


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

Book Shop website is a interconnection of back-end and front-end components. The front-end webpages have been constructed with interconnections. Please find the front-end webpages and their connections in this tiered hierarchy:
```
- Login Page
-  ▪ Home Page
-    ▫ Books Page
-      ○ Check out
-        ● Payment
-  ▪ About us
-  ▪ Contact us
- Register
```
Indentation in this situation demonstrates child elements of a parent element be them webpages or modals (functions of the webpages). Siblings have the same bullet point symbols so as to distinguish them across the structure. Note that the Login Page and Register have been listed as siblings. The registration page will inherit all tiered structure as the login page. They have been seperated to prevent duplicating the tree.
