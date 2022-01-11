//
//Author: James Ortiz
//File: PartFive.scala
//Implementation of Part 5 of Assignment in Module 3
//Compile: scala PartFive.scala

object PartFive extends App{
    def facto(n: Int) = n match {
        //Case stmt 1: if value of n is < 1, return 1
        //Case stmt 2: if n > 1 apply reduceLeft (_ * _) function from 1 to n
        case _ if n < 1 => 1
        case _ => (1 to n).reduceLeft(_ * _)
    }
    //Displaying examples: 
    println("Calculating 0!: " + facto(0))
    println("Calculating 5! : " + facto(5))
    println("Calculating 10! :" + facto(10))

}