use std::{fs::File, io::{self, ErrorKind, Read}, error::Error};

fn panic() {
    // With RUST_BACKTRACE=1 or full this shows a trace with src file paths
    // With RUST_BACKTRACE=1 or full in --release mode, this shows a trace without paths
    panic!("Hello world panic");
}

fn panic_with_memory_access() {
    let v = vec![1, 2, 3, 4, 5];
    v[69];
}

// main normally returns () but can also return a Result like this
fn main() -> Result<(), Box<dyn Error>> {
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

    let f4 = read_file("doesnt-exist.4");
    if f4.is_err() {
        eprintln!("Could not read file! {f4:?}");
    }
    let f4 = read_file_alternative("doesnt-exist.4");
    if f4.is_err() {
        eprintln!("Could not read file! {f4:?}");
    }

    // We can also check if the result is Ok without match
    let res: Result<i32, &str> = Err("test");
    if res.is_err() {
        eprintln!("res is an error! {res:?}");
    }

    // This is possible because main can return an Error
    let f5 = File::open("doesnt-exist.5")?;

    // But now we have to do this at the end of main to return a valid Result
    Ok(())
}

/// These methods are already implemented by std::fs::read_to_string()
fn read_file(filename: &str) -> Result<String, io::Error> {
    let mut file = match File::open(filename) {
        Ok(f) => f,
        Err(e) => return Err(e)
    };

    let mut contents = String::new();
    match file.read_to_string(&mut contents) {
        Ok(_) => Ok(contents),
        Err(e) => Err(e)
    }
}

/// This is the same thing but using the ? syntax
/// For Result<>, the ? immediately stops the function and returns the Err contents if there's an error
/// For Option<>, the ? immediately stops the function and returns None if there's None
/// Otherwise, ? returns the contents of the value (either Ok() contents or Some() contents)
fn read_file_alternative(filename: &str) -> Result<String, io::Error> {
    let mut file = File::open(filename)?;

    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    // You can also do File::open()?.read_to_string()?; in one line

    // You can use ? with Option<> too, but not when our function retuns a Result<>
    // This has the wrong returns type
    // let line_1_last_char = contents.lines().next()?.chars().last();

    Ok(contents)
}
