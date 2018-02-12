<h3>Apache Solr</h3>
<br>Install Oracle JDK 8
<br><code>sudo apt-get install oracle-java8-installer</code>
<br>
<br>Install Solr - Lucidworks HDP Search
<br>https://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.4.2/bk_hdp_search/content/ch_hdp-search-install.html
<code>
cd /etc/apt/sources.list.d
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B9733A7A07513CAD
sudo wget http://public-repo-1.hortonworks.com/HDP-SOLR-2.3-100/repos/ubuntu14/hdp-solr.list
sudo apt-get update
sudo apt-get install lucidworks-hdpsearch
</code>
<br>Modify ownership to solr
<br><code>sudo chown -R solr:solr /opt/lucidworks-hdpsearch/solr</code>
<br>
<br>Install Zookeeper
<br><code>sudo apt-get install zookeeperd</code>
<br>
<br>Start in SolrCloud mode (use -c or -cloud):
<br><code>./bin/solr start -c -z <zkhost:zkport> -p 8983</code>
<br>
<br>Stop:
<br><code>./bin/solr stop</code>
<br>
<br>Create Collection:
<br><code>./bin/solr create -c collection_name -d data_driven_schema_configs -s 1 -rf 1 -p 8983</code>
<br>-c indicates the name
<br>-d is the config directory (located at ./solr/server/solr/configsets)
<br>-s is the number of shards
<br>-rf is the replication factor
<br>-p is the port at which Solr is running
<br>
<br>Delete Collection:
<br><code>./bin/solr delete -c collection_name</code>
<br>
<br>Indexing Data:
<br><code>./bin/post -c <collection_name> -params "separator=%7C" -type text/csv /clinicaltrials.txt</code>
<br><code>./bin/post -c <collection_name> /opt/data/my_pdf_documents/*.pdf</code>
<br>
<br>
<br>References:
<br><a href="https://blogs.apache.org/nifi/entry/indexing_tweets_with_nifi_and">Indexing with NiFi and Solr</a>
<br><a href="http://yonik.com/solr-tutorial/">Solr Tutorial - Dynamic Fields</a>
<br><a href="https://hub.docker.com/_/solr/">Solr DockerHub</a>
<br><a href="https://lucidworks.com/blog/2015/08/17/securing-solr-basic-auth-permission-rules/">Solr Basic Authentication</a>
<br><a href="https://community.hortonworks.com/articles/15159/securing-solr-collections-with-ranger-kerberos.html">Securing Solr Collections with Ranger and Kerberos</a>
<br>
<code>
qt – Query handler for the request. Standard query handler is used if not specified.
q – It is used to specify the query event.
fq – Used to specify filter queries.
sort – Used to sort the results in ascending or descending order.
start, rows – start specifies the staring number of the result set. By default it is zero. rows specify the number of records to return.
fl – Used to return selective fields.
wt – Specifies the response format. Default is XML.
indent – Setting to true makes the response more readable.
debugQuery – Setting the parameter to true gives the debugging information as part of response.
dismax –  To specify the dismax parser.
edismax – To specify the edismax parser.
facet – Setting to true enables the faceting.
spatial – Used for geospatial searches.
spellcheck – Setting to true help in searching similar terms.
</code>
