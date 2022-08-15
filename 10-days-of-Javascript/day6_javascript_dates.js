function getDayName(dateString) {
    var name;
    var names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    var date = new Date(dateString);
    name = names[date.getDay()];
    return name;
}