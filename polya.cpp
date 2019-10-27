#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int n;
	cin>>n;
	int a[100]={0};
	for(int i=0;i<n;i++){
		int b;
		cin>>b;
		a[b-1]++;
	}
	cout<< max_element(a);
	return 0;
}