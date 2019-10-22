using System;

namespace Loops
{
    class Program
    {
    public static void Main(string[] args)
    {
    string i;

    Console.WriteLine("Enter a int value to loop");
    i = Console.ReadLine();       

    myLoop(Convert.ToInt32(i));

    }
    static void myLoop(int x)
        {
            while(x < 10)
            {
                Console.WriteLine("Hello {0}", x);
                x++;
            }
      
        }
    }
}
