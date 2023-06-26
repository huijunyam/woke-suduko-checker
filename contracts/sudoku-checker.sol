// SPDX-License-Identifier: MIT
pragma solidity ^0.8.16;

contract SudukoChecker {
    function check(uint256[9][9] memory board) external pure returns (bool) {
        uint256[][] memory rows = new uint256[][](9);
        uint256[][] memory cols = new uint[][](9);
        uint256[][] memory boxes = new uint[][](9);
        for (uint i; i < 9; i++) {
            rows[i] = new uint256[](9);
            cols[i] = new uint256[](9);
            boxes[i] = new uint256[](9);
        }

        for (uint256 i = 0; i < 9; i++) {
            for (uint256 j = 0; j < 9; j++) {
                if (board[i][j] < 1 || board[i][j] > 9) {
                    return false;
                }
                if (rows[i][board[i][j] - 1] == 1) {
                    return false;
                }
                rows[i][board[i][j] - 1] = 1;

                if (cols[j][board[i][j] - 1] == 1) {
                    return false;
                }
                cols[j][board[i][j] - 1] = 1;

                uint256 idx = (i / 3) * 3 + (j / 3);
                if (boxes[idx][board[i][j] - 1] == 1) {
                    return false;
                }
                boxes[idx][board[i][j] - 1] = 1;
            }
        }
        return true;
    }
}
