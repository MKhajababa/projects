#include<stdio.h>
#include<stdlib.h>
int G[10][10],visited[10],n;
void DFS(int t);
int main()
{
	int i,j;
	printf("\n Enter the vertices:");
	scanf("%d",&n);
	printf("\n Enter the values \n");
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
			scanf("%d",&G[i][j]);
	}
	printf("\n The matrics \n");
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		printf("%d ",G[i][j]);
		printf("\n");
		
	}
	for(i=0;i<n;i++)
	visited[i] = 0;
	DFS(0);
}
void DFS(int t)
{
	int j;
	printf("\n%d",t);
	visited[t] = 1;
	for(j=0;j<n;j++)
	{
		if(!visited[j]&&G[t][j] == 1)
		DFS(j);
	}
}
