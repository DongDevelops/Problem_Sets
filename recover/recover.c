#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Correct usage: ./recover IMAGE\n");
        return 1;
    }

    int ReadFile[];
    FILE *buffer = fopen(argv[1], "r");
    if (buffer == NULL)
    {
        printf("Correct usage: ./recover IMAGE\n");
        return 1;
    }

    int count = 0;

    while(fread(buffer, 512, 1, buffer))
    {
        for(int n = 0; n < 512, n++);
        {
            if(buffer[n] == 0xff && buffer[n+1] == 0xd8 && buffer[n+2] == 0xff && (buffer[n+3] & 0xf0) == 0xe0)
            {
                sprintf(filename, "%03i.jpg", count);
                count ++;

                FILE *img = fopen("%03i.jpg", "w");
                if(img == NULL)
                {
                    return 1;
                }

                fwrite(img, 512, 1, buffer);
            }

            else if(buffer[n] == 0)
            {
                return 1;
            }

        }
    }
}
