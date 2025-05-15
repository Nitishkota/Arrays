package org.example;

public class target {
    public static void main(String[] args){

        int[] arr = {1,2,3,4,5,6};

        int tar = 5;

        for (int i = 0; i<arr.length; i++){
            if (arr[i]==tar){
                System.out.println(true);
                break;
            }
            else {
                continue;
            }
        }
    }
}
