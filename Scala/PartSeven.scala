//
//Author: James Ortiz
//File: PartSeven.scala
//Description: Part #7 of assignment in Module 3
//Compile: scala PartSeven.scala

//Driver program for part seven
object PartSeven extends App{
    
    var filename = "example2.txt"
    //One line solution by split and filtering of words greater than 10 characters:
    io.Source.fromFile(filename).mkString.split("\\W+").filter(_.length > 10).foreach(println(_))

}