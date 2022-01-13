import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.SparkContext._
 
object ScalaWordCount {
 def main(args: Array[String]) {
 val logFile = "hdfs://nameservice1/user/edureka_292003/SparkScala/sample.txt"
 val sparkConf = new SparkConf().setAppName("Spark Word Count")
 val sc = new SparkContext(sparkConf)
 val file = sc.textFile(logFile)
 val counts = file.flatMap(_.split(" ")).map(word => (word, 1)).reduceByKey(_ + _) 
 counts.saveAsTextFile("hdfs://nameservice1/user/edureka_292003/SparkScala/output.txt")
 }
}