
#include <iostream>	


#include <complex>
using namespace std;


int main ()
{	

std::complex<double> mycomplex (3.0, 4.0);


cout << "The absolute value of " << mycomplex << " is: ";
cout << abs(mycomplex) << endl;
	

cout << "The argument of " << mycomplex << " is: ";
cout << arg(mycomplex) << endl;

return 0;
}
