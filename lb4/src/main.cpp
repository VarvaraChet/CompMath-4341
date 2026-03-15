#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>

using namespace std;


double Round(double x, double delta) {
    if (delta <= 1E-9) {
        cout << "Неверное задание точности округления\n";
        exit(1);
    }

    if (x > 0.0)
        return delta * (long) ((x / delta) + 0.5);
    else
        return delta * (long) ((x / delta) - 0.5);
}

double F(double x) {
    return x * x - 5.0 * sin(x);
}

double F_rounded(double x, double delta) {
    if (delta == 0) return F(x);
    return Round(F(x), delta);
}

double horda(double left, double right, double eps, double delta, int &N) {
    double fLeft = F_rounded(left, delta);
    double fRight = F_rounded(right, delta);
    double X, Y;

    if (fLeft * fRight > 0.0) {
        cout << "Неверное задание интервала\n";
        exit(1);
    }
    if (eps <= 0.0) {
        cout << "Неверное задание точности\n";
        exit(1);
    }

    N = 0;
    if (fLeft == 0.0) return left;
    if (fRight == 0.0) return right;

    do {
        X = left - (right - left) * fLeft / (fRight - fLeft);
        Y = F_rounded(X, delta);
        if (Y == 0.0) return (X);
        if (Y * fLeft < 0.0) {
            right = X;
            fRight = Y;
        }
        else {
            left = X;
            fLeft = Y;
        }
        N++;
    } while (fabs(Y) >= eps);

    return (X);

}

int main() {
    ofstream out("output.txt");
    if (!out) {
        cout << "Не удалось открыть файл output.txt\n";
        return 1;
    }

    double left = 2.0;
    double right = 2.5;

    out << setprecision(6);

    double eps_values[] = {1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6};
    double delta_values[] = {1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 0};

    for (double eps : eps_values) {
        int N;

        for (double delta : delta_values) {
            double root = horda(left, right, eps, delta, N);
            out << fixed << "Eps: " << eps
                << " Delta: " << delta
                << " N: " << N
                << " Root: " << root << '\n';
        }
    }

    out.close();
    return 0;
}