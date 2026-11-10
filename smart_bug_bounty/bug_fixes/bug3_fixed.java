public class ArrayFinderFixed {

    public static int findElement(int[] numbers, int index) {
        if (numbers == null || index < 0 || index >= numbers.length) {
            return -1;
        }

        return numbers[index];
    }

    public static void main(String[] args) {
        int[] values = {10, 20, 30, 40, 50};

        assert findElement(values, 2) == 30;
        assert findElement(values, 0) == 10;
        assert findElement(values, 5) == -1;
        assert findElement(values, -1) == -1;
        assert findElement(null, 0) == -1;

        System.out.println("All bug3 tests passed!");
    }
}
