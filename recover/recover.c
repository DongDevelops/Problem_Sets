#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Correct usage: ./recover IMAGE\n");
        return 1 ;
    }


    FILE *buffer = fopen(argv[1], "r");
    int *rFile = malloc(sizeof(argv[1]));
    if (buffer == NULL)
    {
        printf("Correct usage: ./recover IMAGE\n");
        return 1;
    }

    int count = 0;

    while(fread(rFile, 512, 1, buffer))
    {
        for(int n = 0; n < 512; n++)
        {
            if(rFile[n] == 0xff && rFile[n+1] == 0xd8 && rFile[n+2] == 0xff && (rFile[n+3] & 0xf0) == 0xe0)
            {
                sprintf(rFile, "%03i.jpg", count);
                count ++;
                continue;
                FILE *img = fopen("%03i.jpg", "w");
                if(img == NULL)
                {
                    return 1;
                }

                fwrite(, 512, 1, img);
            }

            else if(rFile[n] == 0)
            {
                return 1;
            }
        }
        free(rFile);
    }
}
