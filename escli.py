from datetime import datetime, timedelta
from elasticsearch import Elasticsearch
import sys, getopt

def usage():
    print ("\nThis is the usage function\n")
    print ('Usage: '+sys.argv[0]+' --index <nom_index> --fieldname <timestamp|date> --period <hour|day>')

def es_search(index_name, field_name, search_date):
    
    es = Elasticsearch()
    request = []
    print('Search Date : ', search_date.strftime("%Y-%m-%dT%H:%M:%S"))
    req_head = {'index': index_name}
    req_body = {'query':{'range':{field_name:{'gte': search_date.strftime("%Y-%m-%dT%H:%M:%S") }}}}
    request.extend([req_head, req_body])
    resp = es.msearch(body = request)
    print(resp)



if __name__ == '__main__': 
   
    try:
        options, remainder = getopt.gnu_getopt(sys.argv[1:], 'i:f:p', ['index=','fieldname=', 'period='])
        

        if len(sys.argv) <= 1:
            print(usage())
            sys.exit(2)
            
        print('OPTIONS   :', options)
        for opt, arg in options:
            if opt in ('-o', '--index'):
                index_name = arg
            elif opt in ('-f', '--fieldname'):
                fieldname = arg
            elif opt in ('-p', '--period'):
                period_eval = arg
                if period_eval == 'hour':
                    search_date = datetime.now() - timedelta(hours=1)
                elif period_eval == 'day':
                    search_date = datetime.now() - timedelta(days=1)
                
        print('INDEX   :', index_name)
        print('PERIOD    :', period_eval)
        print('FIELDNAME :', fieldname)
        print('Search Date : ', search_date)
        es_search(index_name, fieldname, search_date)

        
    except getopt.GetoptError as e:
        print(e)
        usage()
        sys.exit(2)

  
