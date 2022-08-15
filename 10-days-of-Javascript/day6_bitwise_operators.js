function getMaxLessThanK(n, k) {
    let maxim = 0;
    let curr = -1;
    for (let i = 1; i < k; i++) {
        for (let j = i + 1; j <= n; j++) {
            curr = i & j;
            if (curr < k && curr > maxim)  {
                maxim = curr;
            }
        }
    } return maxim;
}