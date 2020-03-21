
import java.util.Scanner;

public class C_goldbach {
    
    public static void main(String args[]){


        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        int count = 0;
        int curr = num;

        //System.out.println(is_prime(23));

        while (curr > 2){
             curr = max_prime_diff(curr);
             //System.out.println(curr);
            count++;
        }
        
        System.out.print(count);
        sc.close();
    }

    
    public static boolean is_prime(int n){
        if (n==1){
            return false;
        }
        int i =2;
        while (i*i <= n){
            if (n % i == 0){
                return false;
            }
            i++;
        }
        return true;
    }
    
    public static int max_prime_diff(int n){
        if (n==4){
            return 0;
        }
        for (int i =3; i <= n; i=i+2){
            if (is_prime(i)){
                if (is_prime(n-i)){
                    int out = n-i-i;
                    return out;
                    
                }
            }
        }
        return -1;
    }
    


}
