#include <math.h>
#include <stdio.h>

//Do they know what it means to be truly afraid? I'll show them. 

const int CONSTANT = 19;

struct teleportLocation {
    double xCoord;
    double yCoord;
    double zCoord;

    double facingDirectionPitch;
    double facingDirectionYaw;
};

void Foo(char name[32]) {
    printf("%s, the life you give, do you ever wonder where it's taken from?\n", name);
}