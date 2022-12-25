use std::fs;
fn main() {
    let content = fs::read_to_string("test.txt")
        .expect("Could not read test.txt") ;

    let lines = content.lines().map(|x| x.trim());
    let mut total_score = 0;
    for line in lines {
        let digits: Vec<i32> = line.chars().map(get_correct_digit).collect();
        let score = five_to_ten(digits);
        total_score += score;
    }
    let in_five = ten_to_five(total_score);
    println!("The total score is {}", in_five);
}

fn get_correct_digit(digit: char) -> i32 {
    match digit {
        '-' => -1,
        '=' => -2,
        _ => {
            let res = digit.to_digit(10); 
            if res.is_some() {
                i32::try_from(res.unwrap()).expect("Should have been able to convert from u32 to i32")
            } else {
                println!("Could not extract digit from {digit}");
                panic!();
            }
        }
    }
}

fn five_to_ten(digits: Vec<i32>) -> i32 {
    let mut multiplier = 1;
    let mut total = 0;
    for x in digits.iter().rev() {
        total += multiplier * x;
        multiplier *= 5;
    }
    return total
}

fn ten_to_five(num: i32) -> &'static String {
    let mut current = num;
    let mut s = String::new();
    while current / 5 != 0 {
        let d = u32::try_from(num % 5).expect("Should have been able to convert from i32 to u32");
        s.push(char::from_u32(d).expect("Should have been able to convert from u32 to char"));
        current /= 5;
    }
    &s
}