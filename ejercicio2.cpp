# include <iostream>

using std::cout;
using std::endl;

void rk4();


float func(float x, float y){
  return -y;
}

void rk4(){

float h = 0.1; float z = 0; float x = 0; float y = 1; float N = 10/h;
float k1; float k2; float k3; float k4;

int n; int i;


	for (int i=0; i<N; i++){


		cout << x << " " << y << " " << z << endl;

		k1= func(x,y);
    		k2= func(x+h/2, y+h*k1/2);
    		k3= func(x+h/2, y+h*k2/2);
    		k4= func(x+h, y+h*k3);
		z = z+(h/6)*(k1+k2+k3+k4);

		y = y+(h/6)*(k1+k2+k3+k4);

		x = x+h;
}
}

int main(){
rk4();

}
