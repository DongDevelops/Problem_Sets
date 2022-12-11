// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    node* word = malloc(sizeof(node));
    while(scanf(word))
    {
        if(int i = 0; i < N; i++)
        {
            table[i] = word[0] % 26;
        }
    }

    return toupper(word[0]) - 'A';
}

int word_count = 0;
char* load_words = NULL;

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO

    load_words = fopen(dictionary, "r");
    if(load_words == NULL)
    {
        return false;
    }

    while(fread(&load_words, sizeof(char), 1, dictionary));
    {
        if(load_words == NUL)
        {
            word_count ++;
        }

    }

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    if(file == NULL)
    {
        return 0;
    }
    size = word_count;
    return size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
