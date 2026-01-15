use std::{io::{self, Write}};

/// Adds 35 to x, unless x is 35, in which case returns 0
fn add_35_unless_equal(x: i32) -> i32 {
    let y = 35;
    if x == y {
        return 0;
    }
    x + y
}

/// Another function that implements adding 35 conditionally with a different syntax
fn another_add_35_unless_equal(x: i32) -> i32 {
    if x == 35 { 0 } else { x + 35 }
}

/// Creates an array of 16 numbers and lets the user choose which one to print
fn test_array(stdin: io::Stdin, stdout: &mut io::Stdout) {
    let mut array = [add_35_unless_equal(34); 16];
    if true {
        array = [another_add_35_unless_equal(34); 16];
    }

    let mut index = String::new();
    print!("Enter an index [0-15]: ");
    stdout.flush().expect("Could not flush stdout");
    stdin.read_line(&mut index).expect("Could not read user input");
    let index = index.trim().parse::<usize>().expect("Could not parse user input as usize");

    println!("The user chose element {index}, which is {}", array[index]);
}

fn main() {
    let stdin = io::stdin();
    let mut stdout = io::stdout(); // Needs to be mutable for flush to work?

    // Can't pass stdin and use it later due to borrow issues?
    test_array(io::stdin(), &mut stdout);
}
