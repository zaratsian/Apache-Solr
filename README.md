<h3>Apache Solr</h3>

<br>Install Oracle JDK 8
<br><code>sudo apt-get install oracle-java8-installer</code>

<br>Install Solr - Lucidworks HDP Search
<br>https://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.4.2/bk_hdp_search/content/ch_hdp-search-install.html
<br>
<code>
cd /etc/apt/sources.list.d
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B9733A7A07513CAD
sudo wget http://public-repo-1.hortonworks.com/HDP-SOLR-2.3-100/repos/ubuntu14/hdp-solr.list
sudo apt-get update
sudo apt-get install lucidworks-hdpsearch
</code>

Modify ownership to solr
<br><code>sudo chown -R solr:solr /opt/lucidworks-hdpsearch/solr</code>
