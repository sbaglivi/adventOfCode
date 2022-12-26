use std::fs;
use regex::Regex;

fn main() {
    let line_example = "Sensor at x=2, y=18: closest beacon is at x=-2, y=15";
    let re = Regex::new(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)").unwrap();
    let result = re.captures(line_example).unwrap();
    // let result = re.captures_iter(line_example);
    if let None = result.get(0) {
        panic!("Found no match in string");
    }
    let (sensor_x, sensor_y) = (result.get(1).unwrap().as_str(), result.get(2).unwrap().as_str());
    let (beacon_x, beacon_y) = (result.get(3).unwrap().as_str(), result.get(4).unwrap().as_str());
    println!("There is a sensor at ({}, {})", sensor_x, sensor_y);
    println!("There is a beacon at ({}, {})", beacon_x, beacon_y);

    // let content = fs::read_to_string("test.txt")
    //     .expect("Could not read test.txt");
    // let lines = content.lines().map(|x| x.trim());
    // for line in lines {

    // }
}
