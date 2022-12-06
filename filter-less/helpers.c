#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float average = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed)/3.0;
            int avg = round(average);
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtRed = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float originalRed = image[i][j].rgbtRed;
            float originalGreen = image[i][j].rgbtGreen;
            float originalBlue = image[i][j].rgbtBlue;

            int sepiaRed = round(0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue);
            int sepiaGreen = round(0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue);
            int sepiaBlue = round(0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue);

            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width/2; j++)
        {
            int tempRed = image[i][j].rgbtRed;
            int tempGreen = image[i][j].rgbtGreen;
            int tempBlue = image[i][j].rgbtBlue;
            image[i][j].rgbtRed = image[i][width-(j+1)].rgbtRed;
            image[i][j].rgbtGreen = image[i][width-(j+1)].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width-(j+1)].rgbtBlue;
            image[i][width-(j+1)].rgbtRed = tempRed;
            image[i][width-(j+1)].rgbtGreen = tempGreen;
            image[i][width-(j+1)].rgbtBlue = tempBlue;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int copy[i][j].rgbtRed = image[i][j].rgbtRed;
            int copy[i][j].rgbtGreen = image[i][j].rgbtGreen;
            int copy[i][j].rgbtBlue = image[i][j].rgbtBlue;

            int sumRed = 0;
            int sumGreen = 0;
            int sumBlue = 0;
            int count = 0;

            for (int k = -1; k < 2; k++)
            {
                for (int h = -1; h < 2; h++)
                {
                    if (i + k < 0 || i + k == height || j + h < 0 || )
                }
            }
        }
    }



    for (int i = -1; i < 2; i++)
    {
        for (int j = -1; j < 2; j++)
        {
            copy[i][j].rgbtRed
            copy[i][j].rgbtGreen
            copy[i][j].rgbtBlue

            // copy[i-1] [1]
        }
    }
    return;
}

