# SPARK 36283

https://issues.apache.org/jira/browse/SPARK-36283

## `python bug.py`
```
+----------+
|     point|
+----------+
|(0.0, 0.0)|
|(0.0, 0.0)|
+----------+
```

## `python bug2.py`
```
Traceback (most recent call last):
  File "bug2.py", line 54, in <module>
    df = spark.createDataFrame(pdf, schema)
  File "/Users/da/.pyenv/versions/spark-36283/lib/python3.8/site-packages/pyspark/sql/session.py", line 673, in createDataFrame
    return super(SparkSession, self).createDataFrame(
  File "/Users/da/.pyenv/versions/spark-36283/lib/python3.8/site-packages/pyspark/sql/pandas/conversion.py", line 300, in createDataFrame
    return self._create_dataframe(data, schema, samplingRatio, verifySchema)
  File "/Users/da/.pyenv/versions/spark-36283/lib/python3.8/site-packages/pyspark/sql/session.py", line 700, in _create_dataframe
    rdd, schema = self._createFromLocal(map(prepare, data), schema)
  File "/Users/da/.pyenv/versions/spark-36283/lib/python3.8/site-packages/pyspark/sql/session.py", line 509, in _createFromLocal
    data = list(data)
  File "/Users/da/.pyenv/versions/spark-36283/lib/python3.8/site-packages/pyspark/sql/session.py", line 682, in prepare
    verify_func(obj)
  File "/Users/da/.pyenv/versions/spark-36283/lib/python3.8/site-packages/pyspark/sql/types.py", line 1409, in verify
    verify_value(obj)
  File "/Users/da/.pyenv/versions/spark-36283/lib/python3.8/site-packages/pyspark/sql/types.py", line 1390, in verify_struct
    verifier(v)
  File "/Users/da/.pyenv/versions/spark-36283/lib/python3.8/site-packages/pyspark/sql/types.py", line 1409, in verify
    verify_value(obj)
  File "/Users/da/.pyenv/versions/spark-36283/lib/python3.8/site-packages/pyspark/sql/types.py", line 1304, in verify_udf
    verifier(dataType.toInternal(obj))
  File "/Users/da/.pyenv/versions/spark-36283/lib/python3.8/site-packages/pyspark/sql/types.py", line 1409, in verify
    verify_value(obj)
  File "/Users/da/.pyenv/versions/spark-36283/lib/python3.8/site-packages/pyspark/sql/types.py", line 1354, in verify_array
    element_verifier(i)
  File "/Users/da/.pyenv/versions/spark-36283/lib/python3.8/site-packages/pyspark/sql/types.py", line 1409, in verify
    verify_value(obj)
  File "/Users/da/.pyenv/versions/spark-36283/lib/python3.8/site-packages/pyspark/sql/types.py", line 1403, in verify_default
    verify_acceptable_types(obj)
  File "/Users/da/.pyenv/versions/spark-36283/lib/python3.8/site-packages/pyspark/sql/types.py", line 1291, in verify_acceptable_types
    raise TypeError(new_msg("%s can not accept object %r in type %s"
TypeError: element in array field point: DoubleType can not accept object 1 in type <class 'int'>
```

## `python bug_fixed.py`
```
+----------+
|     point|
+----------+
|(1.0, 1.0)|
|(2.0, 2.0)|
+----------+
```
