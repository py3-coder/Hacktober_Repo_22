package com.qyu4x.qq.algorithm;

import java.util.Arrays;

public class InsertionSort {
    public static void main(String[] args) {
        testInsertionSortV1();
    }

    public static Integer[] insertionSortV1(Integer[] array) {

        for (var i = 1; i < array.length; i++) {
            Integer key = array[i];
            var j = i-1;

            while (j >= 0 && array[j] > key) {
                array[j+1] = array[j];
                j = j-1;
            }

            array[j+1] = key;
        }

        return array;
    }

    public static void testInsertionSortV1() {

        Integer[] something = {10, 8, 4, 6, 1, 2};
        var result = insertionSortV1(something);

        System.out.println(Arrays.toString(something));
    }

}