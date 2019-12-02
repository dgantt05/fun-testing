package app;
import java.util.Scanner;

public class Play {    
   

    public static void main(String[] args) throws Exception {
        System.out.println("Let's figure out what to play!");
        System.out.println("How many people are going to play? ");
        
        Scanner input = new Scanner(System.in);
        int number = input.nextInt();
        System.out.println("You entered " + number);
        input.close();


        if(number > 5) {
            System.out.println("Half-life 2 DM, Goldeneye, Rising Storm 2: Vietnam, NBA 2K19, Tekken, Witch it");
            System.out.println("you might need to split up into smaller groups to game");
        } else {
            if(number == 5) {
                System.out.println("League of Legends, CS:GO, Dead by Daylight in-house, Tekken, NBA 2K19, ARAM");
            } else {
                if(number == 4) {
                    System.out.println("Tekken, Dead by Daylight, NBA 2K19, Deep Rock Galactic, Monster Hunter Worlds");
                }
            } 
        } 
         if(number <= 3){
             System.out.println("Apex, Remnant: From the Ashes, Monster Hunter Worlds, Tekken, NBA 2K19, Rocket League");
         }
        
    }
}