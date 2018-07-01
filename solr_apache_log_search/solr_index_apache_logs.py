
################################################################################################################
#
#   Solr Example - Parse Apache Logs and write to Solr
#
################################################################################################################
#
#   Create Collection 
#   /opt/lucidworks-hdpsearch/solr/bin/solr create -c hwx_search -s 1 -rf 1 -p 8983
#
#   Delete Collection
#   /opt/lucidworks-hdpsearch/solr/bin/solr delete -c hwx_search
#
#   Solr Documentation:
#   Solr 5.5 - http://archive.apache.org/dist/lucene/solr/ref-guide/apache-solr-ref-guide-5.5.pdf
#   Solr 7.4 - http://lucene.apache.org/solr/guide/7_4/uploading-data-with-index-handlers.html
#
################################################################################################################
#
#   Banana UI:  http://localhost:8983/solr/banana/index.html#/dashboard
#   Github:     https://github.com/lucidworks/banana
#
################################################################################################################

import sys,re
import datetime,time
import requests

################################################################################################################
#
#   Functions
#
################################################################################################################

def solr_delete_record(collection_name, id_to_delete):
    solr_url = 'http://localhost:8983/solr/' + str(collection_name) + '/update?commit=true'
    headers  = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(solr_url, headers=headers, json={ "delete":id_to_delete })
    return response


def solr_add_json_record(collection_name, json_payload):
    solr_url = 'http://localhost:8983/solr/' + str(collection_name) + '/update?commit=true'
    headers  = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(solr_url, headers=headers, json=json_payload)
    return response


def load_apache_logs(filepath):
    '''
    Example Apache Log (one line):
    '83.149.9.216 - - [17/May/2015:10:05:03 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1" 200 203023 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"'
    '''
    # Get Apache Log Data
    # wget https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/apache_logs/apache_logs -O /tmp/apache.log
    file  = open(filepath, 'r')
    data  = file.read()
    file.close()
    lines = data.split('\n')
    return lines


def parse_apache_log(apache_log):
    '''
    Example Apache Log:
    '83.149.9.216 - - [17/May/2015:10:05:03 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1" 200 203023 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"'
    '''
    # Apache Regex / Pattern
    apache_regex = '([0-9\.]+) - - \[(.*?)\] \"(.*?)\" ([0-9]+) ([0-9]+) \"(.*?)\" \"(.*?)\"'
    parsed_log  = re.match(apache_regex, apache_log).groups()
    return parsed_log


################################################################################################################
#
#   Main
#
################################################################################################################

if __name__ == "__main__":
    
    filepath        = '/tmp/apache.log'
    collection_name = 'hwx_search'
    
    # Get Apache Logs
    lines = load_apache_logs(filepath)
    
    for i,apache_log in enumerate(lines):
        
        try:
            # Parse Apache Log log
            parsed_log  = parse_apache_log(apache_log)
            parsed_json = [
                {
                    "id": datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f"),
                    "remote_host":          parsed_log[0],
                    "datetimestamp":        datetime.datetime.strptime(parsed_log[1].split()[0], '%d/%b/%Y:%H:%M:%S').strftime('%Y-%m-%dT%H:%M:%S.000Z'),
                    "request_type":         parsed_log[2].split()[0],
                    "request_url":          parsed_log[2].split()[1],
                    "request_protocol":     parsed_log[2].split()[2],
                    "request_status_code":  parsed_log[3],
                    "payload_bytes":        parsed_log[4],
                    "referer":              parsed_log[5],
                    "user_agent":           parsed_log[6]
                }
            ]
            
            r = solr_add_json_record(collection_name, parsed_json)
            
            if (i % 1000)==0 and r.status_code==200:  # Print status update every 1000 records
                print('[ INFO ] Processed ' + str(i) + ' apache logs')
            elif (r.status_code!=200):
                print('[ WARNING ] Passed on record number ' + str(i) + ' with status code: ' + str(r.status_code))
        
        except:
            print('[ WARNING ] Passed on record >> ' + str(apache_log))


# ZEND
