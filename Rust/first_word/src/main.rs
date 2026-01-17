// WARNING: this takes ownership of s
fn first_word_original_string(s: String) -> String {
    let bytes = s.as_bytes();
    let mut new_s = String::new();

    for &byte in bytes {
        if byte == b' ' {
            break;
        }
        new_s.push(byte as char);
    }
    new_s
}

// This doesn't take ownership of s, but gives ownership of a new String
fn first_word_string(s: &String) -> String {
    let bytes = s.as_bytes();
    let mut word = String::new();

    for &byte in bytes {
        if byte == b' ' { break; }
        word.push(byte as char);
    }

    word
}

// This doesn't take or give ownership, only passes around refs (slices)
fn first_word_slice(s: &String) -> Option<&str> {
    let bytes = s.as_bytes();

    for (i, &byte) in bytes.iter().enumerate() {
        if byte == b' ' {
            return Some(&s[..i]);
        }
    }
    None
}

// This is even better because it works on any string slice
fn first_word_slice_from_slice(s: &str) -> Option<&str> {
    let bytes = s.as_bytes();

    for (i, &byte) in bytes.iter().enumerate() {
        if byte == b' ' {
            return Some(&s[..i]);
        }
    }
    None
}

fn main() {
    let mut phrase = String::from("These are some words!");
    // NOT POSSIBLE - we are moving the ownership to the function, so can't borrow it later
    // let new_string = first_word_original_string(phrase);
    let string = first_word_string(&phrase);
    let slice = match first_word_slice(&phrase) {
        Some(s) => s,
        None => ""
    };
    // ALSO NOT POSSIBLE - we are already have some immutable refs, so can't use the mutable ref now
    // let new_string = first_word_original_string(phrase);
    // ALSO NOT POSSIBLE
    // phrase.clear();

    // &String and .as_str() are compatible? Type coercion?
    let a = &phrase;
    let b = phrase.as_str();
    if a == b {
        println!("Equal!");
    }
    // You can either pass &phrase or phrase.as_str() ? Type coercion?
    let slice_from_slice = match first_word_slice_from_slice(&phrase) {
        Some(s) => s,
        None => ""
    };

    // Array shenanigans
    let array = [1, 2, 3, 4, 5];
    let array_slice = &array[1..];
    let new_slice = &[2, 3, 4, 5];
    if array_slice == new_slice {
        println!("Also equal!");
    }

    println!("{phrase} {string} {slice} {slice_from_slice}");
}
