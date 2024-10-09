import java.util.Arrays;

class quicksort{
    static int[] array={4, 2, 8, 7, 1, 5, 3, 6};
    public static void main(String[] args) throws InterruptedException {
        System.out.println("Bem vindo ao algoritmo de QuickSort!\n");
        System.out.println("Array antes do quicksort= "+ Arrays.toString(array));
        QuickSort(array, 0, array.length-1);
        System.out.println("Array depois do quicksort= "+ Arrays.toString(array));
    }

    public static void QuickSort(int[] a, int comeco, int fim){
        int pivo = a[comeco];
        int esquerda = comeco;
        int direita = fim;

        while (esquerda<=direita) {
            while(array[esquerda] < pivo) esquerda++;
            while(array[direita] > pivo) direita--;

            if (esquerda<=direita){
                int temp = array[esquerda];
                array[esquerda] = array[direita];
                array[direita] = temp;
                esquerda++;
                direita--;
            }

        }
        if (comeco < direita) {
            QuickSort(array, comeco, direita);
        }
        if (esquerda < fim) {
            QuickSort(array, esquerda, fim);
        }
    }
}