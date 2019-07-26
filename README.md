# elastic-cli

Simple elasticsearch client (Very Simple), you can use it to get logs in a range date (day or hour) for a specfic index. 

Python 3, test with Elasticsearch version 6 & 7, I use the default port for Elasticsearch.

run pip3 install elasticsearch (client library for es)

Usage sample : python escli.py --index <nom_index> --fieldname <timestamp|date> --period <hour|day>


## Installation 

# centos

```
sudo yum install python36 python36-pip
sudo pip install elasticsearch6
```
