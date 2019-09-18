#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int FILE_LENGTH;

typedef struct movie {
    char name[20];
    char director[30];
    char country[10];
    int income;
} movie;

void createMovies(FILE *fp) {
    fseek(fp, 0, SEEK_SET);
    movie newMovie;
    for (int i = 0; i < FILE_LENGTH; i ++) {
        scanf("%s %s %s %d", newMovie.name, newMovie.director, newMovie.country, &newMovie.income);
        fwrite(&newMovie, sizeof(movie), 1, fp);
    }
}

void printMovies(FILE *fp) {
    fseek(fp, 0, SEEK_SET);
    movie newMovie;
    printf("\nMOVIES\n");
    for (int i = 0; i < FILE_LENGTH; i ++) {
        fread(&newMovie, sizeof(movie), 1, fp);
        printf("Name: %s\tDirector: %s\tCountry: %s\tIncome: %d\n", newMovie.name, newMovie.director, newMovie.country, newMovie.income);
    }
}

void deleteLast(FILE *fp) {
    FILE_LENGTH --;
}

void insertMovie(FILE *fp, char *lastName) {
    FILE_LENGTH ++;
    movie newMovie;
    fseek(fp, -3 * sizeof(movie), SEEK_END);
    for (int i = FILE_LENGTH; i > 0; i --) {
        fread(&newMovie, sizeof(movie), 1, fp);
        if (strcmp(newMovie.name, lastName) == 0) {
            printf("Insert movie: ");
            scanf("%s %s %s %d", newMovie.name, newMovie.director, newMovie.country, &newMovie.income);
            fwrite(&newMovie, sizeof(movie), 1, fp);
            break;
        }
        fwrite(&newMovie, sizeof(movie), 1, fp);
        fseek(fp, -3 * sizeof(movie), SEEK_CUR);
    }
}

int main() {
    FILE *fp = fopen("movies.txt", "w+b");
    if (fp == NULL) {
        perror("\nError opening the file.\n");
        exit(0);
    }
    printf("Number of movies: ");
    scanf("%d", &FILE_LENGTH);
    createMovies(fp);
    int action, quit = 0;
    char lastName[20];
    while(!quit) {
        printf("Select Action:\n1. Print\n2. Delete last movie\n3. Insert new movie\nAction: ");
        scanf("%d", &action);
        switch(action) {
            case 1: printMovies(fp);
            break;
            case 2: deleteLast(fp);
            break;
            case 3: printf("Movie to insert after: ");
            scanf("%s", lastName);
            insertMovie(fp, lastName);
            break;
            default: quit = 1;
            break;
        }
    }
    fclose(fp);
}
/*Transformers Michael_Bay USA 710
Shrek Andrew_Adamson USA 484
Titanic James_Cameron USA 2187
Inception Christopher_Nolan UK 828
Avatar James_Cameron UK 2788*/