//Author: James Ortiz
//File: PartFour.scala
//Answer to part of of assignment in Module #3
//Compile: scala PartFour.scala

//Driver for PartFour
object PartFour extends App {
    val a = Array(20, 12, 6, 15, 2, 9)
    //Applying reduceLeft functionality to the array:
    val maxVal = a.reduceLeft(_ max _)
    println("The maximum value of [20, 12, 6, 15, 2, 9]")
    println(" is " + maxVal)
}

