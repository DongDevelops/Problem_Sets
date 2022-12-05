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
        int *buffer[];
        int count = 0;
        while(fread(buffer, 512, 1, argv[1]))
        {
            for(int n = 0; n < 512, n++);
            {
                if(buffer[n] == 0xff && buffer[n+1] == 0xd8 && buffer[n+2] == 0xff && (buffer[n+3] & 0xf0) == 0xe0)
                {
                    sprintf(filename, "%03i.jpg", count);
                    count ++;

                    FILE *img = fopen(filename, "w");
                    fwrite(%03i.jpg, 512, 1, )
                }
            }
        }
    }
}
