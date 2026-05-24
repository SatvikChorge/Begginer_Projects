#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *link;
};

int main() {
    struct node *head = NULL;
    head = (struct node *)malloc(sizeof(struct node));
    head -> data = 96;
    head -> link = NULL;

    printf(" %d\n %d\n %d\n %p\n %p\n %p\n", head -> data, head, head -> link, head -> data, head, head -> link);

    return 0;
}