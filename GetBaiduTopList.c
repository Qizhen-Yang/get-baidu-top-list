#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argv, char *argc[])
{
	int pause;
	printf("Interval (min): ");
	scanf("%d", &pause);
	while (1)
	{
		system("GetBaiduTopList.py");
		usleep(pause * 60 * 1000000);
	}
	return 0;
}