use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    // File hosts must exist in current path before this produces output
    if let Ok(lines) = read_lines("./1input.txt") {
        // Consumes the iterator, returns an (Optional) String
        let nums: Vec<_> = lines.map(|line| line.unwrap().parse::<i32>().unwrap()).collect();
        // Inefficient, but the corpus is small...
        for x in &nums {
            for y in &nums {
                for z in &nums {
                    if x + y + z == 2020 {
                        println!("{}", x * y * z)
                    }
                }
            }
        }
    }
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}