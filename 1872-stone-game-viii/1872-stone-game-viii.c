int stoneGameVIII(int* stones, int stonesSize){
    int n = stonesSize;

    for (int i = 1; i < n; i++) {
        stones[i] += stones[i - 1];
    }

    int best = stones[n - 1];

    for (int i = n - 2; i >= 1; i--) {
        int value = stones[i] - best;

        if (value > best) {
            best = value;
        }
    }

    return best;
}