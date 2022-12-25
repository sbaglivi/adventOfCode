use std::fs;
fn main() {
    let content = fs::read_to_string("input.txt")
        .expect("Could not read test.txt") ;

    let lines = content.lines().map(|x| x.trim());
    let mut total_score = 0;
    for line in lines {
        let digits: Vec<i64> = line.chars().map(get_correct_digit).collect();
        let score = five_to_ten(digits);
        total_score += score;
    }
    let in_five = ten_to_five(total_score);
    println!("The total score is {}", in_five);
}

fn get_correct_digit(digit: char) -> i64 {
    match digit {
        '-' => -1,
        '=' => -2,
        _ => {
            let res = digit.to_digit(10); 
            if res.is_some() {
                i64::try_from(res.unwrap()).expect("Should have been able to convert from u64 to i64")
            } else {
                println!("Could not extract digit from {digit}");
                panic!();
            }
        }
    }
}

fn five_to_ten(digits: Vec<i64>) -> i64 {
    let mut multiplier = 1;
    let mut total = 0;
    for x in digits.iter().rev() {
        total += multiplier * x;
        multiplier *= 5;
    }
    return total
}

// fn ten_to_five(num: i64) -> &'static String {
fn ten_to_five(num: i64) -> String { let mut current = num;
    let mut s = Vec::new();
    println!("{}", current);
    loop {
        let remainder = current % 5;
        // let d = u64::try_from(remainder).expect("Should have been able to convert from i64 to u64");
        // let c = char::from_u64(d).expect("Convert u64 to char");
        // println!("{d}");
        // s.push(c);
        s.insert(0, remainder.to_string());
        current /= 5;
        if current == 0 {
            break;
        }
    }
    return s.join("")
}

fn five_to_snafu(num: String) -> String { 
    // Iterate backwards 2 chars at a time on string, if last digit in segment is > 2 then
    // trasnlate it as 5*first digit - n times 2nd digit
    let len = num.chars().count();
    for i in 0..len-1 {
        let slice = &num[i..i+2];
        if slice.chars().nth(1).unwrap() != '3' && slice.chars().nth(1).unwrap() != '4' {
            continue;
        }
    }
    num

}
/*
10 / 0
5  1 
2 0
1 1
divide by new base, save remainder as new digit
--
124030
3 > 2 -> 3*5 = 15 = (5*5)*1 - x => x = 10 / 5 = 2 => -2
last three are now 1-20 -> 1=0
4 -> 4*125 = 500 = 625 - 500= 125 / 125 = 1 (-) 
13-1=0
13-11-20 
13-1=0
3125 + 1875 = 5000 = 6250 - 1250 = 2=
3*625=1875 3125 - 625 = 2500 / 625 = 4 -> impossible no? or 3-4 = -1
2--1=0
*/