public class SudokuSolver {

    public static void main(String[] args) {
        int[][] board = {
                { 3, 0, 6, 5, 0, 8, 4, 0, 0 },
                { 5, 2, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 8, 7, 0, 0, 0, 0, 3, 1 },
                { 0, 0, 3, 0, 1, 0, 0, 8, 0 },
                { 9, 0, 0, 8, 6, 3, 0, 0, 5 },
                { 0, 5, 0, 0, 9, 0, 6, 0, 0 },
                { 1, 3, 0, 0, 0, 0, 2, 5, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 7, 4 },
                { 0, 0, 5, 2, 0, 6, 3, 0, 0 }
        };

        if (solve(board)) {
            display(board);
        } else {
            System.out.println("cannot solve sudoku!!");
        }
    }

    static boolean solve(int[][] board) {
        int n = board.length;
        int row = -1;
        int col = -1;

        boolean isLeft = true;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // iterate in sudoku and check if you find 0 then just stop.
                if (board[i][j] == 0) {
                    row = i;
                    col = j;
                    isLeft = false;
                    break;
                }
            }
            // if isleft false then break
            if (isLeft == false) {
                break;
            }
        }

        if (isLeft) {
            return true; // sudoku solved
        }
        // so we need to put a number at row and col to solve a sudoku at where 0 is
        for (int number = 1; number < 10; number++) {
            // check that putting number at perticular row and col is safe or not
            if (isSafe(board, row, col, number)) {
                // if safe then put the number and then
                board[row][col] = number;

                // go for next recursive call if we can solve sudoku from there or not
                if (solve(board)) {
                    // found the answer
                    return true;
                } else {
                    // if we are not able to solve the sudoku we just use backtracking
                    // backtrack
                    board[row][col] = 0;
                }
            }
        }

        // if true is not returned then just return false that sudoku cannot be solved
        return false;
    }

    static boolean isSafe(int[][] board, int row, int col, int number) {
        // for checking if number exist in row or not
        for (int i = 0; i < board.length; i++) {
            if (board[row][i] == number) {
                return false;
            }
        }

        // for checking if number exist in column or not
        for (int i = 0; i < board.length; i++) {
            if (board[i][col] == number) {
                return false;
            }
        }

        // for checking if number exist in internal [ sqrt(N) X sqrt(N) ] matrix
        int sqrt = (int) Math.sqrt(board.length);
        int rowStart = row - row % sqrt;
        int colStart = col - col % sqrt;

        for (int i = rowStart; i < rowStart + sqrt; i++) {
            for (int j = colStart; j < colStart + sqrt; j++) {
                if (board[i][j] == number) {
                    return false;
                }
            }
        }

        return true;
    }

    static void display(int[][] board) {
        // printing the 2-D array.
        for (int[] is : board) {
            for (int is2 : is) {
                System.out.print(is2 + " ");
            }
            System.out.println();
        }
    }
}
