

import java.util.Scanner;
public class Main {
 
 public static void main(String[] args) {
  int B=0, N;    
  Scanner sc = new Scanner(System.in);
  try{ B = Integer.parseInt(sc.next().trim());
   N = Integer.parseInt(sc.next().trim());
   int a;
   for (int i = 0; i < N; ++i) {
    a = Integer.parseInt(sc.next().trim());
    B = B - ((a % 2) + (a / 2));
   }}
  catch(Exception e){
   System.out.println("Invalid Input");
   System.exit(0);
  }
  if(B>0)
  System.out.println("YES");
  else
  System.out.println("NO");
 }
}


