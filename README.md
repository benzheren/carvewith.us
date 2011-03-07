# carvewith.us

A project for ski & snowboard lovers.

## Development
### Local Environment Setup
Assume that you are using Mac OS X Snow Leopard (this means you will have python and related tools installed):

0. Install virtualenv and install [virtualenvwrapper](http://www.doughellmann.com/docs/virtualenvwrapper/). Use virtualenvwrapper tool to create virtual enviroment for Pyramid.
1. Install Pyramid framework by following [this](http://docs.pylonsproject.org/projects/pyramid/1.0/narr/install.html#installing-pyramid-on-a-unix-system).
2. Install Mysql Community Server 5.1 64-bit from [here](http://dev.mysql.com/downloads/mysql/5.1.html). Make sure that you install 64-bit, not 32-bit.
3. Install MySQL-python library with pip or easy_install.

### Database
1. In your local mysql database, create a user:carvewithus with password:5mad_cows. Create a database called carvewithus and grant correct privileges of this database to carvewithus user.

## Open Questions
* What's the relationship between our users? Friends or followers? (Follower case, this guy is awsome and I  like to follow him when he goes to snowboarding)
* Other than ski/snowboard, do we need any other preference/interests to catch?

## Existing Features
1. facebook integeration
2. trip page with admin feature to invite or approve ppl
3. picture upload
4. email notification
5. trip filtering
6. Upcoming/Newly Created trips
7. user roles: organizer, others
8. simple planning between spots, trip and users, a trust system(if u cancel too late, ur credit get destroyed). Extra people get suggestion to rent a car or bus (first come first server based). 

## Feature Pipeline
1. Lodging affiliate
2. Money management
3. Personal car info
4. Coming/New trips near you with push notification
5. Twitter integration
6. Search Trips instead of filtering: Solr
7. Autocomplete
8. messaging system
9. private trips
10. trip feedback
11. repeat the same trip, same group of ppl
