#include "helpers.h"
#include <math.h>

double round(double x);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtBlue = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed)/3.0);
            image[i][j].rgbtGreen = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed)/3.0);
            image[i][j].rgbtRed = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed)/3.0);
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
            image[i][j].rgbtRed = round(.393*image[i][j].rgbtRed + .769*image[i][j].rgbtGreen + .189*image[i][j].rgbtBlue);
            image[i][j].rgbtGreen = round(.349*image[i][j].rgbtRed + .686*image[i][j].rgbtGreen + .168*image[i][j].rgbtBlue);
            image[i][j].rgbtBlue = round(.272*image[i][j].rgbtRed + .534*image[i][j].rgbtGreen + .131*image[i][j].rgbtBlue);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
