use std::fs;

fn main() {
    let input = fs::read_to_string("./input.txt").expect("Something went wrong reading the file");
    let mut x:i32 = 0;
    let mut y:i32 = 0;
    for line in input.lines() {
        let mut split = line.split_whitespace();
        let command = split.next();
        let val:i32 = split.next().unwrap().parse().unwrap();
        match command {
            Some("forward") => x += val,
            Some("down") => y += val,
            Some("up") => y -= val,
            _ => ()
        }    
    }
    println!("{}",x*y)
}