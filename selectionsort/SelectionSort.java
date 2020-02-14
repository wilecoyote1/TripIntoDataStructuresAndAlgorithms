/** @author: <a href="mailto:lemoigne.olivier@gmail.com">Olivier Lemoigne</a> */
public final class SelectionSort {

  // to not instantiate class
  private SelectionSort() {}

  /**
   * Sorts the specified array into ascending numerical order.
   *
   * @param the array to be sort implementation note : the sorting algorithm is a selection sort.
   *     This algorithm offers O(n2) performance
   */
  public static void sort(int... array) {

    for (int i = 0; i < array.length - 1; i++) {
      int smallestIndex = i;

      // find the smallest index
      for (int j = i + 1; j < array.length; j++) {
        if (array[j] < array[smallestIndex]) {
          smallestIndex = j;
        }
      }
      // swap the current index with the smallest index
      swap(array, i, smallestIndex);
    }
  }

  /*
   * swap value from index i to index j
   */
  private static void swap(int[] array, int i, int j) {
    int tmp = array[i];
    array[i] = array[j];
    array[j] = tmp;
  }
}