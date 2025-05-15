package org.example;

public class Maximum {


        public static void main(String[] args) {

            int[] arr = {1,2,3,4,5};
            int temp = 0;
            for (int i=0; i<arr.length; i++){
                if (temp<arr[i]){
                    temp=arr[i];
                }
                else{
                    continue;
                }

            }
            System.out.println(temp);
//            System.out.println(temp);

        }
}
