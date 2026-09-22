#include<stdio.h>
#include<stdlib.h>//rand()
#include<time.h>//time()

int main(){
	
	int answer;
	int target;
	int t = target;
	int a = answer;
	
	srand(time(NULL));
	t = rand()%100;
	
	printf("請猜一個0～99的數字:");
	
	while(t != a){
		
		scanf("%d", &a);
		
		if(t == a){
		
		printf("恭喜你猜對了，答案是:""%d", t);
	}else if(a > t){
		printf("數字太大了!請在猜一次:");
	}else if(a < t){
		printf("數字太小了!請在猜一次:");
	}		
	}
