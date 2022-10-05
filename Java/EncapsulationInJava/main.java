package EncapsulationInJava;

import java.util.Calendar;

/**
 * Encapsulation is defined as the wrapping up of data under a single unit.
 *
 * In Simple terms you are just putting the variables , functions , or any kind ,
 * of data members in a box(where box stands for a class ,function or an interface
 * or any kind of thing.
 *
 */


// Lets us see an example of encapsulation , then we will deep dive into the advantages of it .

// Here we have created a Gun Class
class EncapsulationGunClass {

    // It consists of properties of obejct of a gun
    // Let us take a gun AK-47



    private int noOfBullets;            // These are the some of the properties of Gun
    private int accuracy;
    private String colorOfGun;

    // Now according to the access modifier private we can't acces these variables
    // To access them we have to make getter and setter or public methods.


    // --------------------------------------------  getter and setter methods
    public int getNoOfBullets() {
        return noOfBullets;
    }

    public void setNoOfBullets(int noOfBullets) {
        this.noOfBullets = noOfBullets;
    }

    public int getAccuracy() {
        return accuracy;
    }

    public void setAccuracy(int accuracy) {
        this.accuracy = accuracy;
    }

    public String getColorOfGun() {
        return colorOfGun;
    }

    public void setColorOfGun(String colorOfGun) {
        this.colorOfGun = colorOfGun;
    }
    // -------------------------------------------- getter and setter methods end

}

// Now here you can access the private varibles only by using the public methods.
// let us try to do so.

public class main {

    public static void main(String[] args) {

        EncapsulationGunClass aK47 = new EncapsulationGunClass();  // Creation of Gun object

        // let us save some values to the varibles with the use of methods.

        aK47.setNoOfBullets(45);
        aK47.setAccuracy(94);
        aK47.setColorOfGun("brown");

        System.out.println(aK47.getNoOfBullets());
        System.out.println(aK47.getAccuracy());
        System.out.println(aK47.getColorOfGun());

        // Now as you can see you can access the variables using the objects .

        // ------------------------But you can't do the same with directly setting the varibles with form like

        // EncapsulationGunClass.setNoOfBullets(45)   ------> Gives error
        // EncapsulationGunClass.noOfBullets = 45;    ------> Gives error

    }
    /**
     *  So here as you can see all the varibles ( noOfBullets / accuracy / colorOfGun ) and the functions are inside
     *  a class EncapsulationGunClass . So the box(class) is having the varibles and functions hence can be called
     *  as encapsulation.
     */


    // Advantages of Encapsulation

    /**
     * 1> Actually Encapsulation = data hiding + abstraction
     * >> We had declared three variables which were private , means no one can access them directly .
     * To change them we have to use methods . OR by declaring them private we said that these variables will
     * only be used by the class EncapsulationGunClass , no other class can access these variables directly ,
     * thus hiding data from other class .
     *
     * Example of it --->
     */


    // this is a Person class

    class Person {

        private int yearOfBirth;
        public int ageOfPerson;

        public Person(int yearOfBirth) {
            this.yearOfBirth = yearOfBirth;

            this.ageOfPerson = Calendar.getInstance().get(Calendar.YEAR) - yearOfBirth;
        }

        public int getAge() {
            return ageOfPerson;
        }
    }

}


/*
public class main {

    public static void main(String[] args) {

    Person ram = new Person(2000);

    System.out.println("Ram's age: " + ram.getAge());

    ram.ageOfPerson = 100;  // This is not good because the Person calss is automatically giving us age but we are
                            // Also giving age which is incorrect as currently the ageOfPerson should be = 22
                            // but we gave ageOfPerson = 100

   // Thus we use the private varibles and methods so that other class can't access the variables
   // directly and hence in this example the main class can't able to change the ageOfPerson varible.
}
  after changing the person class for abstraction and data hiding it will become --


  class Person {

        private int yearOfBirth;
        private int ageOfPerson;

        public Person(int yearOfBirth) {
            this.yearOfBirth = yearOfBirth;

            this.ageOfPerson = Calendar.getInstance().get(Calendar.YEAR) - yearOfBirth;
        }

        public int getAge() {
            return ageOfPerson;
        }
    }
}

    // now no other class can access the variable ageOfPerson , hence we have hided the data , and restricted
    // the usage of it , hence applying the concept of abstraction .

 */


/**
 * Advantage 2
 * >> Code can be reused again and again hence saving time.
 *
 *  Advantage 3
 * >> It uses OOPS Programming which is a good practice from industry purpose
 */



