class Solution {
    public:
    double myPow(double x, int n) {
        if (n == 0)
            return 1;
        if (n == -2147483648)
            return (1/x) * myPow(x, n+1);
        if (n < 0) {
            x = 1.0 / x;
            n = -n;
        }

        return (n%2==0 ? 1 : x) * myPow(x*x, n/2);
    }
};