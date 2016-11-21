<h3>Apache Solr</h3>
<br>Install Oracle JDK 8
<br>```sudo apt-get install oracle-java8-installer```
<br>
<br>Install Solr - Lucidworks HDP Search
<br>https://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.4.2/bk_hdp_search/content/ch_hdp-search-install.html
```
cd /etc/apt/sources.list.d
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B9733A7A07513CAD
sudo wget http://public-repo-1.hortonworks.com/HDP-SOLR-2.3-100/repos/ubuntu14/hdp-solr.list
sudo apt-get update
sudo apt-get install lucidworks-hdpsearch
```
<br>Modify ownership to solr
<br>```sudo chown -R solr:solr /opt/lucidworks-hdpsearch/solr```
<br>
<br>Install Zookeeper
<br>```sudo apt-get install zookeeperd```
<br>
<br>References:
<br><a href="https://blogs.apache.org/nifi/entry/indexing_tweets_with_nifi_and">Indexing with NiFi and Solr</a>
<br><a href="http://yonik.com/solr-tutorial/">Solr Tutorial - Dynamic Fields</a>
