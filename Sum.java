package org.example;

public class Sum {

    public static void main(String[] args){

        int[] arr = {1,2,3,4,5,6};
        int temp = 0;

        for (int i=0; i<arr.length; i++){
            temp = temp + arr[i];
        }
        System.out.println(temp);

    }

}
