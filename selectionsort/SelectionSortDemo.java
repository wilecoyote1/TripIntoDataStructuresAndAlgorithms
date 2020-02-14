/*
* Copyright (C) 2018 Olivier Lemoigne
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
* http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*
* Date : 31 juillet 2018
*
* utilisation: javac TriSelectionDemo.java
*              java TriSelectionDemo


*/
import java.util.Arrays;
import java.util.Random;

public final class SelectionSortDemo {

  private static final int VALEUR_MAX = 1000;
  private static final int NOMBRE_ELEMENTS_ALEATOIRE = 10;

  private SelectionSortDemo() {}

  public static void main(String[] args) {

    int[] tableauTest = {5, 3, 2, 2, 1, 9, 10};
    System.out.println("tri par sélection d'un tableau de " + tableauTest.length + " éléments");
    System.out.println("tableau avant tri");
    System.out.println(Arrays.toString(tableauTest));
    System.out.println("tableau après tri");
    SelectionSort.sort(tableauTest);
    System.out.println(Arrays.toString(tableauTest));

    int[] tableauAleatoire = createRandomArray(NOMBRE_ELEMENTS_ALEATOIRE, VALEUR_MAX);
    System.out.println(
        "tri par sélection d'un tableau de " + tableauAleatoire.length + " éléments");
    System.out.println("tableau avant tri");
    System.out.println(Arrays.toString(tableauAleatoire));
    SelectionSort.sort(tableauAleatoire);
    System.out.println("tableau après tri");
    System.out.println(Arrays.toString(tableauAleatoire));
  }

  private static int[] createRandomArray(int n, int valeur_max) {
    int[] tableau = new int[n];
    Random random = new Random();

    for (int i = 0; i < n; i++) {
      tableau[i] = random.nextInt(valeur_max);
    }
    return tableau;
  }
}