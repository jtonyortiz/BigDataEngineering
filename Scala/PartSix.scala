//
//Author: James Ortiz
//File: PartSix.scala
// Description Part #6 from Assignment in Module 3
//Compile: scala PartSix.scala
import java.io.PrintWriter

object PartSix extends App{

    val filename = "example.txt"
    val res = io.Source.fromFile(filename).getLines.toArray.reverse.mkString("\n")
    println(res.reverse)

}