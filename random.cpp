#include <iostream>
#include <cstdlib>
#include <time.h>
using namespace std;

int main() {
  const int n=50;
  int m[n];
  srand(static_cast<unsigned int>(time(0)));
  for (int i=0; i<n; i++) {
      m[i] = rand()%10+1;
      cout << m[i] << " ";
     
  }
}
