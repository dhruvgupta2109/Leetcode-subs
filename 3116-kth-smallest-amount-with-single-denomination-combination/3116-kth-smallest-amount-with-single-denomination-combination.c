long long gcdLL(long long a, long long b) {
    while (b != 0) {
        long long temp = a % b;
        a = b;
        b = temp;
    }

    return a;
}

int compareInt(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int popcountInt(int x) {
    int count = 0;

    while (x) {
        count += x & 1;
        x >>= 1;
    }

    return count;
}

int trailingBitIndex(int x) {
    int index = 0;

    while ((x & 1) == 0) {
        x >>= 1;
        index++;
    }

    return index;
}

long long countLEQ(long long x, long long* lcm, int m) {
    long long count = 0;

    for (int mask = 1; mask < m; mask++) {
        if (lcm[mask] > x) {
            continue;
        }

        if (popcountInt(mask) % 2 == 1) {
            count += x / lcm[mask];
        } else {
            count -= x / lcm[mask];
        }
    }

    return count;
}

long long findKthSmallest(int* coins, int coinsSize, int k) {
    qsort(coins, coinsSize, sizeof(int), compareInt);

    int* newCoins = (int*)malloc(coinsSize * sizeof(int));

    int newSize = 0;

    for (int i = 0; i < coinsSize; i++) {
        int x = coins[i];
        int keep = 1;

        for (int j = 0; j < newSize; j++) {
            if (x % newCoins[j] == 0) {
                keep = 0;
                break;
            }
        }

        if (keep) {
            newCoins[newSize++] = x;
        }
    }

    int m = 1 << newSize;

    long long* lcm = (long long*)malloc(m * sizeof(long long));

    for (int i = 0; i < m; i++) {
        lcm[i] = 1;
    }

    long long left = k;
    long long right = (long long)newCoins[0] * k + 1;

    for (int mask = 1; mask < m; mask++) {
        int prevMask = mask & (mask - 1);
        int bit = mask & -mask;
        int i = trailingBitIndex(bit);

        long long temp =
            lcm[prevMask] /
            gcdLL(lcm[prevMask], newCoins[i]);

        if (temp <= right / newCoins[i]) {
            lcm[mask] = temp * newCoins[i];
        } else {
            lcm[mask] = right + 1;
        }
    }

    while (left < right) {
        long long mid =
            left + (right - left) / 2;

        if (countLEQ(mid, lcm, m) >= k) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    free(newCoins);
    free(lcm);

    return left;
}