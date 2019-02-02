/*
CW : Clock wise
CCW

CCW(ax, ay, bx, by, cx, cy) = (ax*by + bx*cy + cx*ay) - (ay*bx + by*cx + cy*ax)
*/

#include<iostream>

using namespace std;

struct Point
{
    int x;
    int y;
}

typedef struct Point;

Point points[3];

int ccw(Point p1, Point p2, Point p3)
{
    int temp = p1.x * p2.y + p2.x * p3.y + p3.x * p
}

int main()
{
    
}