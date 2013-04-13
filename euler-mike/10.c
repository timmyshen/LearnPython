#include <stdio.h>
#include <string.h>

unsigned long map[300000];
unsigned long unit_size;
unsigned long max = 2000000;

void set(unsigned long num)
{
    map[num / unit_size] |= (1 << (num % unit_size));
}

int check(unsigned long num)
{
    return map[num / unit_size] & (1 << (num % unit_size));
}

int main() 
{
    memset(map, 0, sizeof(map));
    unit_size = sizeof(unsigned long);

    unsigned long long sum = 0;
    unsigned long i;
    for (i = 2; i <= max; i++) {
        if (!check(i)) {
            sum += i;
            printf("%lu\n", i);
            unsigned long j;
            for (j = i; j <= max; j += i) {
                set(j);  
            }
        }
    }
    printf("sum = %llu\n", sum);
    return 0;
}
