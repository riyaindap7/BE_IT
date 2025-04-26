abstract class Animal{ 
    abstract void sound();
     abstract void animalType();
    void action(){
        System.out.println("running");
    }
}

class Dog extends Animal{
    void sound(){
        System.out.println("barking");
    }
    void animalType(){
        System.out.println("I am dog");
    }
}


public class AbstractTest
{
public static void main(String[] args)
{
System.out.println("Hello world");
Dog d=new Dog();
d.sound();
d.action();
d.animalType();
}
}
