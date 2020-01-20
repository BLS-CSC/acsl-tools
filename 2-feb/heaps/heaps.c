#include <math.h>
#include <stdio.h>
#include <SDL2/SDL.h>
#include <SDL2/SDL_ttf.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

#define BUFSIZE 16

#define SPACING 20
#define CIRCLE_DETAIL 12
#define CIRCLE_R 10
#define FONT_SIZE 12
#define WIDTH 512
#define HEIGHT 512


typedef struct node {
    int value;
    struct node *left, *right;
} node;

typedef struct glyph {
    SDL_Texture *tex;
    int advance;
}

glyph digits[10];

void read_input(int **list, int *size) {
    *size = 4 * sizeof(int);
    *list = malloc(*size);

    int status;
    int i = 0;

    do {
        if (i >= *size) {
            *size *= 2;
            *list = realloc(*list, *size);
        }

        status = scanf("%i", (*list) + i);

        i++;
    } while (status != EOF);

    *size = i - 1;
}

node *create_tree(int *list, int listSize, TTF_Font *font) {
    node *nodes = malloc(listSize * sizeof(node));
    SDL_Color black = {0, 0, 0}

    for (int i = 0; i < listSize; i++) {
        nodes[i].value = list[listSize];

        if (2 * i + 1 < listSize) {
            // A left child exists
            nodes[i].left = nodes + 2 * i + 1;
        } else {
            nodes[i].left = NULL;
        }

        if (2 * i + 2 < listSize) {
            // A right child exists
            nodes[i].right = nodes + 2 * i + 2;
        } else {
            nodes[i].right = NULL;
        }
    }

    return nodes;
}

node *read_tree() {
    int *input;
    int size;
    read_input(&input, &size);

    for (int i = 0; i < size; ++i) {
        printf("%i\n", input[i]);
    }

    node *head = create_tree(input, size);

    free(input);

    return head;
}

void init_digits(SDL_Renderer *renderer) {
    // Init TTF

    if (TTF_Init()) {
        printf("Unable to init TTF. Erorr: %s\n", TTF_GetError());
    }
    font = TTF_OpenFont("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONT_SIZE);

    SDL_Color black = { 0, 0, 0 };

    for (int i = 0; i < 10; i++) {
        SDL_Surface *surf = TTF_RenderGlyphSolid(font, '0' + i, black);
        glyphs[i].tex = SDL_CreateTextureFromSurface(renderer, surf);
        SDL_FreeSurface(surf);

        SDL_GlyphMetrics(font, '0' + i, NULL, NULL, NULL, NULL, &gylphs[i].advance);
    }

    TTF_Quit();

}

void draw_circle(SDL_Renderer *renderer, int x, int y, int radius) {
    for (int i = 0; i < CIRCLE_DETAIL; i++) {
        float a1 = 2 * i * M_PI / CIRCLE_DETAIL;
        float a2 = 2 * (i + 2) * M_PI / CIRCLE_DETAIL;
        SDL_RenderDrawLine(renderer,
                x + radius * cos(a1), y + radius * sin(a1),
                x + radius * cos(a2), y + radius * sin(a2));
    }
}

void draw_number(int num, SDL_Renderer *renderer, int x, int y) {
    char digits[BUFSIZE];
    snprintf(digits, BUFSIZE, "%i", num);

    char *digit = digits;
    while (*digit) {
        glyph g = glyphs[*digit - '0'];

        renderer.
    }
}

void draw_node(node node, SDL_Renderer *renderer, int x, int y, TTF_Font *font) {
    draw_circle(renderer, x, y, CIRCLE_R);
    

    if (node.left) {
        draw_node(*node.left, renderer, x - SPACING, y + SPACING, font);
    }

    if (node.right) {
        draw_node(*node.right, renderer, x + SPACING, y + SPACING, font);
    }
}

int main(int argc, char *argv) {
    node *head = read_tree();

    SDL_Window *window;
    SDL_Renderer *renderer;
    TTF_Font *font;

    // Init SDL

    if (SDL_Init(SDL_INIT_VIDEO)) {
        printf("Unable to init SDL. Error: %s\n", SDL_GetError());
        return 1;
    }

    window = SDL_CreateWindow("Heap Sort Demonstration",
            SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
            WIDTH, HEIGHT, 0);

    if (!window) {
        printf("Could not create window. Error: %s\n", SDL_GetError());
    }
    
    renderer = SDL_CreateRenderer(window, -1, 0);
    if (!renderer) {
        printf("Could not create SDL Renderer. Error: %s\n", SDL_GetError());
    }
    
    init_digits(renderer);
    
    // Begin drawing

    SDL_SetRenderDrawColor(renderer, 255, 255, 255, SDL_ALPHA_OPAQUE);
    SDL_RenderClear(renderer);

    SDL_SetRenderDrawColor(renderer, 0, 0, 0, SDL_ALPHA_OPAQUE);
    draw_node(*head, renderer, WIDTH/2, SPACING, font);

    SDL_RenderPresent(renderer);

    // Cleanup

    SDL_Delay(2000);

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    free(head);

    return 0;
}
