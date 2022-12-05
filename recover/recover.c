#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Correct usage: ./recover 'the name of a forensic image'\n");
        return 1;
    }
}