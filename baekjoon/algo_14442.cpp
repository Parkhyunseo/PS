#include <iostream>
#include <stdio.h>
#include <queue>
#include <algorithm>
#include <string.h>

using namespace std;

int N, M, K;

int dp[1001][1001][11];
char map[1001][1001];

int dx[] = { 0,1,-1,0 };
int dy[] = { 1,0,0,-1 };

struct Position {
	int x, y, k;
	Position(int x, int y, int k) : x(x), y(y), k(k) {}
};

int main()
{
	scanf("%d %d %d", &N, &M, &K);
	for (int i = 0; i < N; ++i)
		scanf("%s", map[i]);

	queue<Position> q;
	q.push(Position(0, 0, 0));
	
	memset(dp, 0x3f, sizeof(dp));
	dp[0][0][0] = 1;
	
	while (!q.empty()) 
	{
		Position here = q.front();
		q.pop();
		for (int i = 0; i < 4; ++i) {
			int nx, ny; 
			nx = here.x + dx[i];
			ny = here.y + dy[i];
			
			int nk = here.k + map[nx][ny] - '0';
			int nd = dp[here.x][here.y][here.k] + 1;
			
			if (nx < 0 || N <= nx || ny < 0 || M <= ny) 
			    continue;
			
			if (nk <= K && dp[nx][ny][nk] > nd) 
			{
				dp[nx][ny][nk] = nd;
				q.push(Position(nx, ny, nk));
			}
		}
	}

	int result = 1e9;
	for (int i = 0; i <= K; ++i) 
	    result = min(result, dp[N - 1][M - 1][i]);
	
	if (result == 1e9)
	    result = -1;
	
	printf("%d", result);

	return 0;
}