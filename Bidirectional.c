#include <stdio.h>

void search(int arr[], int length, int element) {
    printf("Enter your array : ");
    scanf("%d", arr[100]);
    int left = 0;
    int position = -1;
    int right = length - 1;

    for(left = 0; left <= right;){
        if(arr[left] == element) {
            position = left;
            printf("Element found in array at %dth position with %d attempts\n", position + 1, left + 1);
            break;
        }

        if(arr[right] == element) {
            position = right;
            printf("Element found in array at %dth position with %d attempts\n", position + 1, length - right);
            break;
        }

        left++;
        right++;
    }

    if (position == -1){
        printf("Not found element in array\n");
    }
}

int main() {
    int arr[] = {2,4,6,8,10,12};
    int e, length;
    
    search(arr, length, e);

    printf("Enter the element to be search : ");
    scanf("%d", &e);

    length = sizeof(arr) / sizeof(arr[0]);

    return 0;
}