package org.example;
import java.util.Arrays;

public class Reverse {

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6};
        int[] temp = new int[arr.length]; // Create a new array of the same size

        // Print original array
        System.out.println("Original array: " + Arrays.toString(arr));

        // Iterate through the original array in reverse order
        for (int i = arr.length - 1; i >= 0; i--) {
            // Store the element from the original array into the temporary array
            temp[arr.length - 1 - i] = arr[i];
        }

        // Copy the reversed elements from temp back into arr
        for(int i = 0; i < arr.length; i++){
            arr[i] = temp[i];
        }

        // Print reversed array
        System.out.println("Reversed array: " + Arrays.toString(arr));
    }
}



