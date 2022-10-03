package OOPS.Inheritence;
// acquiring prprs from parent class to child class this featues enables is a relation and denoted with an arrow head
//line example
     ///   person 
// Student         //Employee 

public class BoxConstructor {

        double l;
        double w;
        double h;

        BoxConstructor(){

            this.l =1;
            this.w =2;
            this.h =3;        
        
        }

        BoxConstructor(double side){

           this.l=side;
           this.w=side;
           this.h=side;

        }

        BoxConstructor(double l, double h, double w)
        {
            this.l=l;
            this.w=w;
            this.h=h;

        }

        public void info(){

            System.out.println("running");
        }

       
  
}
