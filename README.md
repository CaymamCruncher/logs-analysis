# Logs Analysis
## Project Description

### Requirements

To start the program you will require Vagrant, Virtual box and the
NewsData.sql file. Their links are listed below.
Vagrant: [Vagrant](https://www.vagrantup.com/)
VirtualBox: [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
NewsData: [NewsData.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

### Starting It Up

To start the project you must first cd into the directory containing
your virtual machine. From there run vagrant up and wait for the files
to install. Once the files are finished run vagrant ssh and you will be
inside your virtual machine now. Cd into the /vagrant directory and then
cd into the project directory. Once in the correct directory you will have
to run `psql -d news -f newsdata.sql` and wait for it to finish. Once that
is finished you can run `python3 News.py` to start the program

### Code Output

The code will return the answers to three questions by retrieving data
from the NewsData.sql file. The three questions are as follows
* What are the three most popular articles of all time
* Who are the most popular authors of all time
* On which days did more than 1% of requests lead to an error

##### Special thanks to fellow students and mentors in Udacity's classroom for their help
