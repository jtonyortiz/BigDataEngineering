//Author: James Ortiz
//File: PartOneToThree.scala
//Description: Contains answer to parts 1, 2, and 3 
//of assignment in Module 3
//Compile: scala PartOneToThree.scala

//Part #1: Write a class AccountInfo 
//with methods deposit and withdraw, and a read-only 
//property balance
class AccountInfo (initBal: Double){
   var balance = initBal

   def deposit(amount: Double) = {
        balance += amount;
   }

   def withdraw(amount: Double) = {
       balance -= amount;
   }

}


//Assignment Part #2:
//Write an object Conversions with methods inchestoFeet, milestoKms and
//poundsToKilos and invoke its methods from a class of your choice
case class Conversions(value: Double){
    import Conversions._
    def calcInchesToFeet: Double = inchestoFeet(value)
    def calcMilesToKms: Double = milestoKms(value)
    def calcPoundsToKilos: Double = poundsToKilos(value)
}


object Conversions{
    def inchestoFeet(inches: Double): Double = {
        inches/12.00D
    }

    def milestoKms(miles: Double): Double = {
        miles * 1.609D
    }

    def poundsToKilos(pounds: Double): Double  = {
        pounds * 0.45359237D
    }
}
//End of Assignment Part 2

//Assignment part #3:
//
//
//
class BankAccount (initBal: Double){

   var balance = initBal

   def deposit(amount: Double): Double = {
        balance += amount
        balance -= 1
        return balance
   }

   def withdraw(amount: Double): Double = {
       balance -= amount
       balance -= 1
       return balance
   }

   def getBalance(): Double = {
       return balance
   }

}

//Main Object used as a driver for other exercizes in the assignment:
object PartOneToThree extends App{

    //Testing Part 1 of Assignment:
    var a = new AccountInfo(500.00);
    //Printing intitial balance:
    println("Initial balance is $" + a.balance)

    //Depositing 300.00
    a.deposit(300.00)
    println("After depositing 300.00 the balance is now: $" + a.balance)
    
    //Widthdrawing 250.00
    a.withdraw(250.00)
    println("After withdrawing 250.00, the balance is now: $" + a.balance)

    //==== Part 1 Completed ====

    //Testing part 2 of Assignment:
    println("Part #2 of Assignment")
    var conv1 = Conversions(24.00)
    println("24 inches to feet: " + conv1.calcInchesToFeet)

    var conv2 = Conversions(500.00)
    println("500 miles into Kilometers: " + conv2.calcMilesToKms)

    var conv3 = Conversions(50.00)
    println("50 pounds to kilos: " + conv3.calcPoundsToKilos)
    //==== Part #2 Completed =====

    //Testing Part #3 of Assignment:
    println("Part #3 of Assignment")
    var ba = new BankAccount(500.00)
    println("Get current balance: " + ba.getBalance())
    println("Depositing $1700: " + ba.deposit(1700.00))
    println("Withdrawing $500: " + ba.withdraw(500.00))
    println("The Current Balance is now: $" + ba.getBalance())
    //===== Part #3 Completed =====


}