interface sportsperson
{
void details(int ID,String name);
}
class athlete implements sportsperson
{
int ID=18;
String name="Virat";
athlete()
{
System.out.println("Participated in common wealth game");
}
public void details(int ID,String name)
{
ID=this.ID;
name=this.name;
System.out.println("Name and ID of the athelet:"+ID+" "+name);
}
}
class hockey_player implements sportsperson
{
int ID=12;
String name="John";
hockey_player()
{
System.out.println("Numbers of goals scored :9");
}
public void details(int ID,String name)
{
ID=this.ID;
name=this.name;
System.out.println("name and ID of the hockey player:"+ID+" "+name);
}
}
public class exp5post
{
public static void main(String[] args)
{
sportsperson s;
s=new athlete();
s.details(18,"Virat");
sportsperson s1;
s1=new hockey_player();
s1.details(12,"John");
}
}