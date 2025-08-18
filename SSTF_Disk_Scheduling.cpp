#include <iostream>
#include <cmath> // for abs()
#include <algorithm> // for sort()
using namespace std;

int main() {
    int n;
    cout << "Enter number of disk requests: ";
    cin >> n;

    int requests[100];  // max 100 requests
    cout << "Enter the disk requests:\n";
    for (int i = 0; i < n; i++) {
        cin >> requests[i];
    }

    // Create a copy to sort just for display (optional)
    int sorted_requests[100];
    for (int i = 0; i < n; i++) {
        sorted_requests[i] = requests[i];
    }
    sort(sorted_requests, sorted_requests + n);

    int head;
    cout << "Enter initial head position: ";
    cin >> head;

    bool visited[100] = {false};  // to mark which requests have been processed
    int total_seek = 0;

    cout << "\nSorted Requests (for reference): ";
    for (int i = 0; i < n; i++) {
        cout << sorted_requests[i] << " ";
    }
    cout << "\n";

    cout << "Seek Sequence: ";

    // Process all disk requests one by one with original requests array (SSTF)
    for (int i = 0; i < n; i++) {
        int nearest_index = -1;

        // Find the nearest unvisited request
        for (int j = 0; j < n; j++) {
            if (!visited[j]) {
                if (nearest_index == -1 || abs(requests[j] - head) < abs(requests[nearest_index] - head)) {
                    nearest_index = j;
                }
            }
        }

        // Move head to the nearest request
        visited[nearest_index] = true;
        total_seek += abs(requests[nearest_index] - head);
        head = requests[nearest_index];

        cout << head << " ";
    }

    cout << "\nTotal Number of Seek Operations: " << n;
    cout << "\nTotal Seek Distance: " << total_seek << endl;

    return 0;
}
