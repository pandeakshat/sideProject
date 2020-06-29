import java.util.Scanner;
import java.util.*;

public class rockpaperscissor
{

final static int ROCK = 1, SCISSOR = 2, PAPER = 3;

    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        System.out.println("Rock Paper Scissor \n (1) - Rock, \n (2) - Scissors, \n (3) - Paper \n ");
        
          int[][] p= new int[4][4];
        

        for(int i=0; i<4; i++)
        { for( int j=0; j<4; j++)
        {
            p[i][j]=0;
        }
        }

        String[] pl = new String[4];

        for(int n=0; n<10; n++)
        {
        int[] player= new int[4];
        

        for(int i=0; i<4; i++)
        {
            player[i] = getMove();
            if(player[i]==1)
                pl[i]="ROCKS";
            else if (player[i]==2)
                pl[i]="SCISS";
            else
                pl[i]="PAPER";
        }
        

        System.out.print("\t _____________________________________________________________________________________________________\n");
        System.out.print("\t | Player 1 \t\t | Player 2 \t\t | Player 3 \t\t | Player 4 \t\t| \n");
        System.out.print("\t | Choice:" + pl[0]);
        System.out.print("\t\t | Choice:" + pl[1]);
        System.out.print("\t\t | Choice:" + pl[2]);
        System.out.print("\t\t | Choice:" + pl[3]);
        System.out.print(" \t| \n");
        System.out.print("\t _____________________________________________________________________________________________________\n");

        
        System.out.print("\t _________________________________________________________________________________________________________________________________________________\n");
        System.out.print("\t | Totals \t\t |       \t\t| Against \t\t\t\t\t \t\t\t\t    \t\t | \n");
                System.out.print("\t _________________________________________________________________________________________________________________________________________________\n");

        System.out.print("\t |        \t\t |       \t\t| Player 1 \t\t | Player 2 \t\t | Player 3 \t\t | Player 4 \t\t | \n");
                System.out.print("\t _________________________________________________________________________________________________________________________________________________\n");

       

        for(int i=0; i<4; i++)
            {   int a = i+1;
                System.out.print("\t | Player wins \t\t | Player " + a +" \t\t|");
                for(int j=0; j<4; j++)
                    {

                         if (i==j)
                         {
                            System.out.print("\t\t  - \t |");
                         }

                        else {
                                        switch (player[i]){
                                        case 1:
                                        if (player[j] == 2)
                                        {    p[i][j] += 1;
                                            System.out.print("\t\t " + p[i][j] +" \t |");
                                        }
                                        else
                                            System.out.print("\t\t " + p[i][j] +" \t |");
                                        break;
                                        case 2:
                                        if (player[j] == 3)
                                         {     p[i][j] += 1;
                                            System.out.print("\t\t " + p[i][j]+" \t |");
                                         }
                                        else
                                            System.out.print("\t\t " + p[i][j] +" \t |");
                                        break;
                                        case 3:
                                        if (player[j] == 1)
                                        {       p[i][j] += 1;
                                            System.out.print("\t\t " + p[i][j] +" \t |");
                                        }
                                        else
                                            System.out.print("\t\t " + p[i][j] +" \t |");
                                        break;
                              }
        }
    }
    System.out.print("\n");
                    }
        System.out.print("\t _________________________________________________________________________________________________________________________________________________\n");

            }
        
}

     public static int getMove()
    {
        Random random = new Random();
        int input = random.nextInt(3)+1;
        return input;   
    }
}    