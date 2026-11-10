public class ArrayFinder {

    public static int findElement(int[] numbers, int index) {
        if (index > numbers.length) {
            return -1;
        }

        return numbers[index];
    }

    public static void main(String[] args) {
        int[] values = {10, 20, 30, 40, 50};

        System.out.println(findElement(values, 2));
        System.out.println(findElement(values, 5));
    }
}
