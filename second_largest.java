package org.example;

public class second_largest {

    public static void main(String[] args){

        int max = 0;
        int sec_max = 0;

        int[] arr = {1,2,3,7,5,6};
        for (int i=0; i<arr.length; i++){
            if(max<arr[i]){
                max = arr[i];
            }

        }
        System.out.println(max);

        for (int j =0; j<arr.length; j++){
            if (arr[j] > sec_max && arr[j] < max){
                sec_max = arr[j];
            }


        }
        System.out.println("Second max is");
        System.out.println(sec_max);
    }
}
