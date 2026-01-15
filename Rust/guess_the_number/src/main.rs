use std::{cmp::Ordering, io::{self, Write}};
use rand::Rng;

fn main() {
    let stdin = io::stdin();
    let mut stdout = io::stdout(); // Needs to be mutable for flush to work?
    let expected = rand::thread_rng()
        .gen_range(1..=10);

    // Labeled loop (useful to disambiguate 2 loops within each other)
    let did_user_quit: bool = 'main_game_loop: loop {
        // Allow user to keep guessing until they quit or enter a valid number
        let guess: i32 = loop {
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
                        // Break out of the outer loop using the label
                        // and set did_user_quit to true
                        break 'main_game_loop true;
                    } else {
                        continue;
                    }
                },
            };
            break guess;
        };

        println!("You entered {guess}");

        match guess.cmp(&expected) {
            Ordering::Less => println!("Try higher!"),
            Ordering::Equal => {
                println!("YES!!!! YOU'VE GOT IT!!11!");
                // The user won, so set did_user_quit to false
                break false;
            },
            Ordering::Greater => println!("Try lower!"),
        }
    };

    println!("Thanks for playing.");
    // If the user quit manually, they didn't win
    if did_user_quit {
        println!("Better luck next time!");
    }
}
