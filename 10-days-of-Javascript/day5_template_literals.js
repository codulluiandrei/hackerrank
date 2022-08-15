function sides(literals, ...expressions) {
    var area = expressions[0];
    var perimeter = expressions[1];
    var e1 = (perimeter + Math.sqrt(perimeter * perimeter  - (16 * area))) / 4;
    var e2 = (perimeter - Math.sqrt(perimeter * perimeter  - (16 * area))) / 4;
    var array = [e1, e2];
    array =  array.sort(function (a, b) { return a - b; });
    return array;
}