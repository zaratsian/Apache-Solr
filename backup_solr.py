

##############################################################################################################
#
#   Solr Backup Script
#
#   Reference: 
#       https://lucene.apache.org/solr/guide/6_6/making-and-restoring-backups.html#create-snapshot-api
#
##############################################################################################################


import sys,os
import requests


def solr_backup(
    solr_host      = 'localhost', 
    solr_port      = '8983',
    collection     = 'hwx_search', 
    backup_dir     = '/tmp',
    backup_name    = 'hwx_search_backup',
    include_date   = False
    ):
    
    solr_base_url = 'http://' + str(solr_host) + ':' + str(solr_port) + '/solr/' + str(collection)
    
    if include_date:
        backup_name = str(backup_name) + '_' + re.sub('[^0-9]','',str(datetime.datetime.now()))
    else:
        backup_name = str(backup_name)
    
    solr_url = solr_base_url + '/replication?command=backup&location=' + str(backup_dir) + '&name=' + str(backup_name) + '&wt=json'
    r = requests.get(solr_url)
    
    if r.status_code == 200:        
        # Get Status of Solr Backup
        #status_url = solr_base_url = "/replication?command=details&wt=json"
        #r = requests.get(status_url)
        #status_json = r.json()
        #print(status_json)
    else:
        print('[ ERROR ] Response Code: ' + str(r.status_code))


if __name__ == '__main__':
    
    solr_backup(
    solr_host    = 'localhost', 
    solr_port    = '8983',
    collection   = 'hwx_search', 
    backup_dir   = '/tmp',
    backup_name  = 'hwx_search_backup',
    include_date = False
    )


#ZEND
