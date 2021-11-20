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
The back-end functionality for loading associated data into the template bookCatalog.html which will be called whenever a user clicks on a particular book from any webpage

- 5001CEM_Software_Engineering/src/booksCatalog.py<br/>
Template with all books including search parameters for the user to select books under specific filters. Without any filters the entire database log from which any books added by the administrators have added.

- 5001CEM_Software_Engineering/src/indexScript.py<br/>
Main home page of the book shop website. All other operations/functionality are achievable through the main webpage. It also includes static webpages such as about us.

Website Components repository path:

- 5001CEM_Software_Engineering/web/templates/bookCatalog.html<br/>
Template for all books within the database including filters to enable a user to browse. Search functionality has not been added in yet as it has yet to be constructed on the back-end.

- 5001CEM_Software_Engineering/web/templates/bookPreview.html<br/>
Basic template structure for loading all database information into concerning a specific book chosen. It comprises of mainly data passed from the back-end to the front-end and structured.

- 5001CEM_Software_Engineering/web/templates/CheckOut.html<br/>
Enables the user to check-out the books that they have currently in their basket. It will serve to take payments as well and feedback information to the back-end to make the necessary changes to the stock.

- 5001CEM_Software_Engineering/web/templates/CompleteOrder.html<br/>
pending...

- 5001CEM_Software_Engineering/web/templates/index.html<br/>
Main home page from which the user is re-directed to after registering or logging in. Here it serves as the nexus with navigation to get access to other static and dynamic areas of the website.

- 5001CEM_Software_Engineering/web/templates/LoginCredentials.html<br/>
Re-direction page which is issued when entering the website. All access and entry is based between this and the register page. Please note that basic security responses have been added as per the FLASK back-end script.

- 5001CEM_Software_Engineering/web/templates/Register.html<br/>
Direction to from the login page if an account does not exist for the user. It collects all necessary information for logging in and some additional contact information so as to complete contact us form. Also serves to help will billing information and postage with books.

- 5001CEM_Software_Engineering/web/templates/StockManagement.html<br/>
Administrative webpage for reviewing the stock and products currently listed within the system. Here the administrator can control the books added, and removed.

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

![image](https://user-images.githubusercontent.com/23194490/142739467-f415ef49-e5c6-4920-8169-7c5aea35c324.png)


Indentation in this situation demonstrates child elements of a parent element be them webpages or modals (functions of the webpages). Siblings have the same bullet point symbols so as to distinguish them across the structure. Note that the Login Page and Register have been listed as siblings. The registration page will inherit all tiered structure as the login page. They have been seperated to prevent duplicating the tree.
