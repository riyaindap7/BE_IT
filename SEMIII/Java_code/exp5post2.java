abstract class shape
{
abstract void draw();
}
class rectangle extends shape
{
private int width;
private int height;
rectangle(int width, int height)
{
this.width=width;
this.height=height;
}
void draw()
{
System.out.println("Drawing a rectangle with width "+width+" and height"+height);
}
}
class circle extends shape
{
private int radius;
circle(int radius)
{
this.radius=radius;
}
void draw()
{
System.out.println("Drawing a circle with radius "+radius);
}
}
public class exp5post2
{
public static void main(String[] args)
{
rectangle rec=new rectangle(5,2);
circle c=new circle(8);
rec.draw();
c.draw();
}
}
