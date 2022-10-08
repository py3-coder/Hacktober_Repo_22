class Solution {
public:
    int totalNQueens(int n) {
        // Creating the data structure 
        vector<vector<string>>answer;
        vector<string>chessBoard(n);
        string s(n, '.');
        for(int i = 0; i < n; i++){
            chessBoard[i] = s;
        }
        puzzle(0, chessBoard, answer, n);
        return answer.size();
    }
    
    // Creating the recursive function 
    void puzzle(int currentCol, vector<string>&chessBoard, vector<vector<string>>&answer, int n){
        // Base condition, when we traverse all the cell validity
        if(currentCol == n){
            answer.push_back(chessBoard);
            return ;
        }
        for(int currentRow = 0; currentRow < n; currentRow++){
            // Checking valid cell
            if(isValid(currentRow, currentCol, chessBoard, n)){
                chessBoard[currentRow][currentCol] = 'Q';
                puzzle(currentCol + 1, chessBoard, answer, n);
                chessBoard[currentRow][currentCol] = '.';
            }
        }
    }
    
    // Checking if given cell is valid
    bool isValid(int row, int col, vector<string>&chessBoard, int n){
        // Checking up-left diagonal
        int currentRow = row;
        int currentCol = col;
        while(currentRow >= 0 && currentCol >= 0){
            if(chessBoard[currentRow][currentCol] == 'Q')
                return false;
                currentRow--;
                currentCol--;
        }
        
        // Checking whole left cell
        currentRow = row;
        currentCol = col;
        while(currentCol >= 0){
            if(chessBoard[currentRow][currentCol] == 'Q')
                return false;
                currentCol--;
        }
        
        // Checking down-left diagonal
        currentRow = row;
        currentCol = col;
        while(currentRow < n && currentCol >= 0){
            if(chessBoard[currentRow][currentCol] == 'Q')
                return false;
                currentRow++;
                currentCol--;
        }
        return true;
    }
};
