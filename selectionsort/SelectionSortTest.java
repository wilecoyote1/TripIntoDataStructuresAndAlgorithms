/*
 *
 * préalable, télécharger la librairie junit
 * se placer à la racine du projet et lancer la commande
 * mvn clean dependency:copy-dependencies si vous avez maven
 * ou alors vous télécharger la librairie junit dans le répertoire lib
 *
 * pour exécuter ce test, lancer la commande
 * javac -cp .:../../../../lib/junit-4.12.jar SelectionSortTest.java
 * java -cp .:../../../../lib/junit-4.12.jar:../../../../lib/hamcrest-core-1.3.jar org.junit.runner.JUnitCore SelectionSortTest
 */
import java.util.Arrays;
import java.util.Random;
import org.junit.Assert;
import org.junit.Test;

public class SelectionSortTest {

  private static final int VALEUR_MAX = 1000;
  private static final int NOMBRE_ELEMENTS_ALEATOIRE = 100000;

  @Test
  public void testTableauSimpleOK() {
    int[] tableauTest = {5, 3, 2, 2, 1, 9, 10};
    int[] tableauTestFinal = {1, 2, 2, 3, 5, 9, 10};

    SelectionSort.sort(tableauTest);
    Assert.assertArrayEquals(tableauTestFinal, tableauTest);
  }

  @Test
  public void testTableauSimpleNOK() {
    int[] tableauTest = {5, 3, 2, 2, 1, 9, 10};
    int[] tableauTestFinal = {10, 2, 2, 3, 5, 9, 1};

    SelectionSort.sort(tableauTest);
    Assert.assertFalse(Arrays.equals(tableauTestFinal, tableauTest));
  }

  @Test
  public void testGrandTableau() {
    int[] tableauTest = creationTableauAleatoire(NOMBRE_ELEMENTS_ALEATOIRE, VALEUR_MAX);
    int[] tableauTestCopy = Arrays.copyOf(tableauTest, tableauTest.length);

    Arrays.sort(tableauTest);
    SelectionSort.sort(tableauTestCopy);
    Assert.assertArrayEquals(tableauTest, tableauTestCopy);
  }

  /** */
  private static int[] creationTableauAleatoire(int n, int valeur_max) {
    int[] tableau = new int[n];
    Random random = new Random();

    for (int i = 0; i < n; i++) {
      tableau[i] = random.nextInt(valeur_max);
    }
    return tableau;
  }
}
