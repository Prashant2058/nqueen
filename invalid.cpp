-#include <iostream>
#include <vector>
#include <set>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <algorithm>

using namespace std;

// Mark all invalid positions attacked by a queen at (i, j)
set<pair<int, int>> invalid_points(int n, int i, int j) {
    set<pair<int, int>> points;

    for (int x = 0; x < n; ++x) {
        points.insert({x, j});          // Same column
        points.insert({i, x});          // Same row

        int d1 = i + j - x;
        if (d1 >= 0 && d1 < n) points.insert({x, d1});

        int d2 = x - i + j;
        if (d2 >= 0 && d2 < n) points.insert({x, d2});
    }

    points.erase({i, j});
    return points;
}

// Las Vegas algorithm to place queens randomly
pair<vector<vector<int>>, int> las_vegas(int n) {
    bool success = false;
    int attempts = 0;
    vector<vector<int>> board;

    while (!success) {
        attempts++;
        board = vector<vector<int>>(n, vector<int>(n, 1));
        vector<int> valid_positions(n * n);
        for (int i = 0; i < n * n; ++i) valid_positions[i] = i;

        for (int i = 0; i < n; ++i) {
            if (valid_positions.empty()) break;

            int rand_index = rand() % valid_positions.size();
            int q_pos = valid_positions[rand_index];
            valid_positions.erase(valid_positions.begin() + rand_index);

            int x = q_pos / n;
            int y = q_pos % n;

            set<pair<int, int>> invalid = invalid_points(n, x, y);

            for (auto [p, q] : invalid) {
                board[p][q] = 0;
                int index = n * p + q;

                auto it = find(valid_positions.begin(), valid_positions.end(), index);
                if (it != valid_positions.end()) valid_positions.erase(it);
            }

            if (valid_positions.empty()) {
                if (i >= n - 1) success = true;
                break;
            }
        }
    }

    return {board, attempts};
}

int main() {
    srand(time(0));  // Seed for randomness

    ofstream file("lv_avg.csv", ios::app);
    if (file.tellp() == 0) file << "n,Avg_Attempt\n";  // Write header if file is empty

    for (int n = 24; n < 50; ++n) {
        vector<int> attempts_list;

        for (int i = 0; i < 4000; ++i) {
            auto [result, attempts] = las_vegas(n);
            attempts_list.push_back(attempts);
            cout << "n = " << n << ", run " << i + 1 << endl;
        }

        long long total = 0;
        for (int val : attempts_list) total += val;

        int avg = total / attempts_list.size();
        file << n << "," << avg << "\n";
    }

    file.close();
    return 0;
}
