function modifyArray(e) {
    const r = e.map(function(a) { 
        if (a % 2 == 0) { return 2 * a; }
        else { return 3 * a; } 
    }); return r;
}