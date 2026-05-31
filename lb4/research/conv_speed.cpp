#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>

double comp_func(double x){
    return sinh(x)-x+1;
}

double Round(double x, double delta){
    if (delta <= 1e-9){
        std::cout << "Неверное задание точности округления\n";
        exit(1);
    }
    
    if (x > 0.0) 
        return (delta*(long((x/delta)+0.5)));
    else
        return (delta*(long((x/delta)-0.5)));
}

void Horda(double left, double right, double eps, double ans){
    std::ofstream out("conv.txt");

    double f_left=comp_func(left), f_right=comp_func(right);
    double x, y;

    if (f_left*f_right > 0.0){
        std::cout << "Неверное задание интервала\n";
        exit(1);
    }
    if (eps <= 0.0){
        std::cout << "Неверное задание точности\n";
        exit(1);
    }

    if (f_left == 0.0)
        return;
    if (f_right == 0.0)
        return;
    
    double prev=0;
    int n=0;
    do{
        x = left-(right-left)*f_left/(f_right-f_left);
        y = comp_func(x);

        if (prev != 0.0)
            out << std::fixed << std::setprecision(6) << n << " " << Round(fabs(x-ans), eps)/prev << '\n';
        prev = Round(fabs(x-ans), eps);
        
        if (y == 0.0)
            return;

        if (y*f_left < 0.0){
            right = x;
            f_right = y;
        }
        else{
            left = x;
            f_left = y;
        }

        n++;

    } while (fabs(y) >= eps);

    out.close();
}

int main(){
    double eps=0.000001, l=-2.0, r=-1.0;
    double ans=-1.729117;
    
    Horda(l, r, eps, ans);
}