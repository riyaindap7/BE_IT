import java.util.Scanner;

abstract class Shape{
    double len;
    double breadth;
    double radius;
    double side;
    public abstract double RectangleArea(double len,double breadth);
    public abstract  double SquareArea(double side);
    public abstract  double CircleArea(double area);
}
class Area extends Shape{
    public double RectangleArea(double len,double breadth){
        return  len*breadth;
    }
     public double SquareArea(double side){
        return side*side;
     }
     public double CircleArea(double radius){
         return Math.PI * radius * radius;

     }
}
public class Cppl241 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Area rt = new Area();
        Area cr  =new Area();
        Area sq = new Area();
        System.out.println("Enter the Length of the Rectangle:");
        rt.len = sc.nextDouble();
        System.out.println("Enter the Breadth of the Rectangle:");
        rt.breadth = sc.nextDouble();
        System.out.println("Enter the Side of the Square:");
        sq.side = sc.nextDouble();
        System.out.println("Enter the Radius of the Circle:");
        cr.radius = sc.nextDouble();
        System.out.println("The area of the Rectangle is "+rt.RectangleArea(rt.len,rt.breadth));
        System.out.println("The area of the Square is "+sq.SquareArea(sq.side));
        System.out.println("The area of the Circle is "+cr.CircleArea(cr.radius));

    }
}
