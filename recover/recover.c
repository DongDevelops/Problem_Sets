#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Correct usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file != NULL)
    {
        int buffer[];
        int count = 0;
        while(fread(buffer, 512, 1, argv[1]))
        {
            if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
            {
                count ++;
                sprintf(filename, "%03i.jpg", count);
                FILE *img = fopen(filename, "w");
            }
        }
    }
}
