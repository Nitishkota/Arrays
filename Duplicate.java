package org.example;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Duplicate {

    public static void main(String[] args) {
        Integer[] arr = {1, 1, 1, 2, 3, 3, 5};
        List<Integer> list = new ArrayList<>(Arrays.asList(arr)); // Convert to ArrayList

        Integer temp = null;

        // Iterate over a copy to avoid ConcurrentModificationException
        List<Integer> copyList = new ArrayList<>(list); // Create a copy for iteration
        for (Integer i : copyList) {
            if (i != null && i.equals(temp)) { // Use .equals() for Integer comparison, handle null
                list.remove(i); // Remove from the original list
            }
            temp = i;
        }

        System.out.println(list); 


        Integer[] resultArr = list.toArray(new Integer[0]); //important
        System.out.println(Arrays.toString(resultArr));
    }
}

