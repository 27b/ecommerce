# Flask CMS/Ecommerce

## Information
This project is an "Ecommerce/CMS" using Flask.
This is a learning project and not is recommended for production.

## Working
For now, the ecommerce not work.
**[25-11-2021]**
+ Admin and ecommerce routes
+ Admin forms for orders and manage products
+ Payment method
+ Thinking in how to create a Cart for Anonymous users

## TODOS
New features in the future.
+ Add backups system with Google Drive or AWS S3
+ manage.py for create admin and "apps" 

## Points
+ The structure of the project it's inspired in Django.
+ Exceptions: tools (dir), user and settings.
+ If it's necessary, use CDN in /<app_name>/templates/base.html
+ For now, the project don't use SPA Framework, use turbolinks.

## Default apps:
+ admin
+ ecommerce (you can clone this)

## Tools
All tools were developed in-house, they may have bugs.
+ file-handler: Work with files from forms, this tool save files in disk.
+ logger: Add logs in information.logs
+ transactions: Create your Payment method how as a class and add in ecommerce.transaction
+ verification-email: Create a array in memory for validation and secret key to send of emails.
