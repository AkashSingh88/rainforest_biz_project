from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from enrich_accounts.config.ConfigStore import *
from enrich_accounts.udfs.UDFs import *

def salesforce_Opportunity(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("Id", StringType(), True), StructField("IsDeleted", IntegerType(), True), StructField("AccountId", StringType(), True), StructField("IsPrivate", IntegerType(), True), StructField("Name", StringType(), True), StructField("Description", StringType(), True), StructField("StageName", StringType(), True), StructField("StageSortOrder", IntegerType(), True), StructField("Amount", IntegerType(), True), StructField("Probability", IntegerType(), True), StructField("ExpectedRevenue", IntegerType(), True), StructField("TotalOpportunityQuantity", StringType(), True), StructField("CloseDate", StringType(), True), StructField("Type", StringType(), True), StructField("NextStep", StringType(), True), StructField("LeadSource", StringType(), True), StructField("IsClosed", StringType(), True), StructField("IsWon", StringType(), True), StructField("ForecastCategory", StringType(), True), StructField("ForecastCategoryName", StringType(), True), StructField("CampaignId", StringType(), True), StructField("HasOpportunityLineItem", StringType(), True), StructField("Pricebook2Id", StringType(), True), StructField("OwnerId", StringType(), True), StructField("CreatedDate", StringType(), True), StructField("CreatedById", StringType(), True), StructField("LastModifiedDate", StringType(), True), StructField("LastModifiedById", StringType(), True), StructField("SystemModstamp", StringType(), True), StructField("LastActivityDate", StringType(), True), StructField("LastStageChangeDate", StringType(), True), StructField("FiscalYear", StringType(), True), StructField("FiscalQuarter", StringType(), True), StructField("ContactId", StringType(), True), StructField("PrimaryPartnerAccountId", StringType(), True), StructField("ContractId", StringType(), True), StructField("LastAmountChangedHistoryId", StringType(), True), StructField("LastCloseDateChangedHistoryId", StringType(), True), StructField("DeliveryInstallationStatus__c", StringType(), True), StructField("TrackingNumber__c", StringType(), True), StructField("OrderNumber__c", StringType(), True), StructField("CurrentGenerators__c", StringType(), True), StructField("MainCompetitors__c", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/FileStore/salesforce_export/Opportunity.csv")
