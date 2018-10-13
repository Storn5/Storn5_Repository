/**
 * helpers.c
 *
 * Computer Science 50
 * Problem Set 3
 *
 * Helper functions for Problem Set 3.
 */

#include <cs50.h>

#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    int start = 0, end = n-1, middle = (end+start+1)/2;
    while (start <= end) {
        if (values[middle] == value)
            return true;
        if (values[middle] < value)
            start = middle + 1;
        else
            end = middle - 1;
        middle = (end+start+1)/2;
    }
    return false;
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    int temp, counter = 1;
    while (counter > 0) {
        counter = 0;
        for (int i = 0; i < n-1; i ++) {
            if (values[i] > values[i+1]) {
                temp = values[i];
                values[i] = values[i+1];
                values[i+1] = temp;
                counter ++;
            }
        }
    }
    return;
}
