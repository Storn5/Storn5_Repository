use std::{fs::File, io::ErrorKind};

fn main() {
    let f = match File::open("doesnt-exist.wtf") {
        Ok(res) => res,
        Err(open_error) => match open_error.kind() {
            ErrorKind::NotFound => {
                eprintln!("The file was not found: {open_error:?}");
                match File::create("doesnt-exist.wtf") {
                    Ok(res) => res,
                    Err(create_error) => {
                        panic!("There was an error creating the file: {create_error:?}");
                    }
                }
            },
            _ => {
                panic!("File exists, but cannot be opened: {open_error:?}");
            }
        }
    };

    // Instead of match, we can use .unwrap_ methods
    let res: i32 = Err(10).unwrap_or_default();

    // unwrap() just panics if there's an error, otherwise returns the contents of the Result
    let f2 = File::open("doesnt-exist.wtf").unwrap();

    // expect() lets us put a custom message
    // let f3 = File::open("doesnt-exist.2").expect("Could not open the file doesnt-exist.2");

    let f3 = File::open("doesnt-exist.3").unwrap_or_else(|error| {
        match error.kind() {
            ErrorKind::NotFound => {
                File::create("doesnt-exist.3").unwrap_or_else(|error2| {
                    panic!("Error creating file: {error2:?}");
                })
            },
            _ => {
                panic!("Cannot open existing file: {error:?}")
            }
        }
    });

    // We can also check if the result is Ok without match
    let res: Result<i32, &str> = Err("test");
    if res.is_err() {
        eprintln!("res is an error! {res:?}");
    }
}

fn panic() {
    // With RUST_BACKTRACE=1 or full this shows a trace with src file paths
    // With RUST_BACKTRACE=1 or full in --release mode, this shows a trace without paths
    panic!("Hello world panic");
}

fn panic_with_memory_access() {
    let v = vec![1, 2, 3, 4, 5];
    v[69];
}
