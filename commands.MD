# Packages 
Flask,pymongo[srv],mongodb-migrations

# Migrations 

## steps
#### step - 1 - create migration folder 

## create migration file 
mongodb-migrate-create --description filename

## do mongodb migrations 
mongodb-migrate --url <use your url> --migrations

example :accept:

mongodb-migrate --url mongodb+srv://<username>:<password>@<clustername>.<#####>.mongodb.net/<dbname>?retryWrites=true&w=majority   --migrations
