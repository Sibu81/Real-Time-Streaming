# Databricks notebook source
df = spark.table("default.order_1018")
# Example: View the first 10 rows
df.show(10)

# Example: Aggregation (sum of amount per customer)
from pyspark.sql.functions import sum

agg_df = df.groupBy("customer_id").agg(sum("amount").alias("total_spent"))
agg_df.show()



# COMMAND ----------

from pyspark.sql.functions import to_timestamp

# Example: select orders between two dates (adjust timestamps)
df_with_timestamp = df.withColumn("ts", to_timestamp(df.timestamp))
filtered_df = df_with_timestamp.filter((df_with_timestamp.ts >= "2025-10-01") & (df_with_timestamp.ts < "2025-11-01"))
filtered_df.show()



# COMMAND ----------

from pyspark.sql.functions import to_timestamp, current_timestamp, datediff
df = df.withColumn("ts", to_timestamp(df.timestamp))
recent_df = df.filter(datediff(current_timestamp(), df.ts) <= 7)
recent_df.show()


# COMMAND ----------

from pyspark.sql.functions import hour
df = df.withColumn("order_hour", hour(to_timestamp(df.timestamp)))
orders_by_hour = df.groupBy("order_hour").count().orderBy("order_hour")
orders_by_hour.show()


# COMMAND ----------

from pyspark.sql.functions import avg
avg_order = df.groupBy("customer_id").agg(avg("amount").alias("avg_order_amount"))
avg_order.show()


# COMMAND ----------

from pyspark.sql.functions import count
order_counts = df.groupBy("customer_id").agg(count("order_id").alias("num_orders"))
order_counts.show()


# COMMAND ----------

from pyspark.sql.functions import hour, avg

df = df.withColumn("order_hour", hour(to_timestamp(df.timestamp)))
avg_order_hour = df.groupBy("order_hour").agg(avg("amount").alias("avg_order_amount")).orderBy("order_hour")
avg_order_hour.show()


# COMMAND ----------

from pyspark.sql.functions import to_date, sum

df = df.withColumn("order_date", to_date(to_timestamp(df.timestamp)))
daily_sales = df.groupBy("order_date").agg(sum("amount").alias("total_sales"))
daily_sales.orderBy("order_date").show()
