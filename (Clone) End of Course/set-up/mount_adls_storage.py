# Databricks notebook source
# MAGIC %md 
# MAGIC storage_account_name = "formula1dl"
# MAGIC client_id            = dbutils.secrets.get(scope="formula1-scope", key="databricks-app-client-id")
# MAGIC tenant_id            = dbutils.secrets.get(scope="formula1-scope", key="databricks-app-tenant-id")
# MAGIC client_secret        = dbutils.secrets.get(scope="formula1-scope", key="databricks-app-client-secret")
# MAGIC

# COMMAND ----------

storage_account_name = "blob8806"
mnt_account_name="formula1dl"
client_id = "ee832bea-56db-4061-b45e-2568ff0d8666"
tenant_id = "ababd49d-4f1f-42b0-9033-2ad9ec2e07da"
client_secret = "_3z8Q~5CsGHks9.vI3g0vN3IsrzXQMRPGsT6_aax"

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": f"{client_id}",
           "fs.azure.account.oauth2.client.secret": f"{client_secret}",
           "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}

# COMMAND ----------

def mount_adls(container_name):
  dbutils.fs.mount(
    source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
    mount_point = f"/mnt/{mnt_account_name}/{container_name}",
    extra_configs = configs)

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

mount_adls("raw")

# COMMAND ----------

mount_adls("processed")

# COMMAND ----------

mount_adls("presentation")

# COMMAND ----------

mount_adls("demo")

# COMMAND ----------

# dbutils.fs.unmount("/mnt/formula1dl/presentation")

# COMMAND ----------

dbutils.fs.ls("/mnt/formula1dl/raw")

# COMMAND ----------

dbutils.fs.ls("/mnt/formula1dl/processed")

# COMMAND ----------

dbutils.fs.ls("/mnt/formula1dl/presentation")

# COMMAND ----------

dbutils.fs.ls("/mnt/formula1dl/demo")

# COMMAND ----------


