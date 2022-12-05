#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Correct usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *f = fopen(argv[1], "r");
    fread(buffer, 512, 1, argv[1]);
}
