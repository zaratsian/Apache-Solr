echo ""
echo ""
echo "*********************************************************************************"
echo "*"
echo "*  References:"
echo "*         http://hortonworks.com/hadoop-tutorial/searching-data-solr/"
echo "*         https://cwiki.apache.org/confluence/display/solr/SolrCloud"
echo "*"
echo "*********************************************************************************"
echo ""
echo ""
echo "Loggin in as solr user..."
su solr
sleep 2
echo ""
echo ""
echo "Creating solr home directory for core1 to core N..."
sleep 2
mkdir -p ~/solr-cores/core1
#mkdir -p ~/solr-cores/core1
cp /opt/lucidworks-hdpsearch/solr/server/solr/solr.xml ~/solr-cores/core1
#cp /opt/lucidworks-hdpsearch/solr/server/solr/solr.xml ~/solr-cores/core2
echo ""
echo ""
echo "Starting SolrCloud on port 8983..."
sleep 2
/opt/lucidworks-hdpsearch/solr/bin/solr start -cloud -p 8983 -z sandbox.hortonworks.com:2181 -s ~/solr-cores/core1
echo ""
echo ""
echo "Creating solr collection, called zcollection..."
/opt/lucidworks-hdpsearch/solr/bin/solr create -c zcollection -d /opt/lucidworks-hdpsearch/solr/server/solr/configsets/data_driven_schema_configs_hdfs/conf -n zcollection -s 2 -rf 2
sleep 10
echo "SolrCloud Collection created! Running on port 8983"
echo ""
echo ""
