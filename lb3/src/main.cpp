#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>

double comp_func(double x){
    return sinh(x)-x+1;
}

double Bisect(double left, double right, double eps, int &n){
    double e=std::abs(eps)*2.0;
    double f_left=comp_func(left), f_right=comp_func(right);
    double x=(left+right)/2.0, y;
    
    if (f_left*f_right > 0.0){
        std::cout << "Неверное задание интервала\n";
        exit(1);
    }
    
    if (eps <= 0.0){
        std::cout << "Неверное задание точности\n";
        exit(1);
    }

    n = 0;
    
    if (f_left == 0.0)
        return left;
    if (f_right == 0.0)
        return right;
    
    while ((right-left) >= e){
        x = 0.5*(right+left);
        y = comp_func(x);
        
        if (y == 0.0)
            return (x);
        
        if (y*f_left < 0.0)
            right = x;
        else{ 
            left = x;
            f_left = y; 
        }
        n++;
    }
    return x;
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

int main(){
    std::ofstream out("output.txt");

    int fix=1;
    double l=-2.0, r=-1.0;
    for (double eps=0.1; eps >= 0.000001; eps *= 0.1){
        int cnt_it;
        double ans=Bisect(l, r, eps, cnt_it);
        out << std::fixed << std::setprecision(fix) << eps << ' ' << 0.0 << ' ' << cnt_it << ' ' << ans << '\n';
        
        for (double delta=0.1; delta > 1e-9; delta *= 0.1){
            ans = Bisect(Round(l, delta), Round(r, delta), eps, cnt_it);
            out << std::fixed << std::setprecision(fix) << eps << ' ' << delta << ' ' << cnt_it << ' ' << std::fixed << std::setprecision(fix) << ans << '\n';
        }
        fix++;
    }

    out.close();
}