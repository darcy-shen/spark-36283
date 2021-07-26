import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.types import ArrayType, DoubleType, UserDefinedType, Row, StructType, StructField

class ExamplePointUDT(UserDefinedType):
    """
    User-defined type (UDT) for ExamplePoint.
    """

    @classmethod
    def sqlType(self):
        return ArrayType(DoubleType(), False)

    @classmethod
    def module(cls):
        return 'pyspark.sql.tests'

    @classmethod
    def scalaUDT(cls):
        return 'org.apache.spark.sql.test.ExamplePointUDT'

    def serialize(self, obj):
        return [obj.x, obj.y]

    def deserialize(self, datum):
        return ExamplePoint(datum[0], datum[1])


class ExamplePoint:
    """
    An example class to demonstrate UDT in Scala, Java, and Python.
    """

    __UDT__ = ExamplePointUDT()

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "ExamplePoint(%s,%s)" % (self.x, self.y)

    def __str__(self):
        return "(%s,%s)" % (self.x, self.y)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
            other.x == self.x and other.y == self.y

spark = SparkSession.builder.getOrCreate()
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "false")
pdf = pd.DataFrame({'point': pd.Series([ExamplePoint(1.0, 1.0), ExamplePoint(2.0, 2.0)])})
schema = StructType([StructField('point', ExamplePointUDT(), False)])
df = spark.createDataFrame(pdf, schema)
df.show()

