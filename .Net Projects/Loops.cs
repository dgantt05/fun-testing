using System;

namespace Loops {
    class Program {
        int i = 0;
        void Main(string[] args){
            while (i < 10)
            {
                Console.WriteLine("i's value is {0}", i);

                i++;
            }
        }
    }
}