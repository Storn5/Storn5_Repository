use std::{cmp::Ordering, io, io::Write};
use rand::Rng;

fn main() {
    let stdin = io::stdin();
    let mut stdout = io::stdout(); // Needs to be mutable for flush to work?
    let expected = rand::thread_rng()
        .gen_range(1..=10);

    loop {
        print!("Enter your guess (or \"quit\"): ");
        // Need to flush after print! because the terminal doesn't show it immediately
        stdout.flush()
            .expect("Could not flush stdout");

        let mut guess = String::new();
        stdin.read_line(&mut guess)
            .expect("User did not provide a valid input");

        let guess = match guess.trim().parse::<i32>() {
            Ok(res) => res,
            Err(_) => {
                if guess.trim() == "quit" {
                    break;
                } else {
                    continue;
                }
            },
        };

        println!("You entered {guess}");

        match guess.cmp(&expected) {
            Ordering::Less => println!("Try higher!"),
            Ordering::Equal => {
                println!("YES!!!! YOU'VE GOT IT!!11!");
                break;
            },
            Ordering::Greater => println!("Try lower!"),
        }
    }

    println!("Thanks for playing.");
}
