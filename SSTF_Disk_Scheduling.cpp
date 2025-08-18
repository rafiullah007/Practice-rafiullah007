#include <iostream>
#include <cmath>
#include <algorithm> 
using namespace std;

int main() {
    int n;
    cout << "Enter number of disk requests: ";
    cin >> n;

    int a[100];  
    cout << "Enter the disk requests:\n";
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // Create a copy to sort just for display (optional)
    int sort_a[100];
    for (int i = 0; i < n; i++) {
        sort_a[i] = a[i];
    }
    sort(sort_a, sort_a + n);

    int head;
    cout << "Enter initial head position: ";
    cin >> head;

    bool visited[100] = {false};  // to mark which requests have been processed
    int total_seek = 0;

    cout << "\nSorted Requests : ";
    for (int i = 0; i < n; i++) {
        cout << sort_a[i] << " ";
    }
    cout << "\n";

    cout << "Seek Sequence: ";

    // Process all disk requests one by one with original requests array (SSTF)
    for (int i = 0; i < n; i++) {
        int nearest_index = -1;

        // Find the nearest unvisited request
        for (int j = 0; j < n; j++) {
            if (!visited[j]) {
                if (nearest_index == -1 || abs(a[j] - head) < abs(a[nearest_index] - head)) {
                    nearest_index = j;
                }
            }
        }

        // Move head to the nearest request
        visited[nearest_index] = true;
        total_seek += abs(a[nearest_index] - head);
        head = a[nearest_index];

        cout << head << " ";
    }

    cout << "\nTotal Number of Seek Operations: " << n;
    cout << "\nAbsolute Distance: " << total_seek << endl;

    return 0;
}
