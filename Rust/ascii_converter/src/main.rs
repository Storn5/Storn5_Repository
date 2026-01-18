use std::time::Instant;

fn main() {
    let original_string = "Hello, woRLd! 1234";
    println!("Original: {original_string}");
    println!("Lowercase: {}", to_lowercase(original_string));
    println!("Lowercase: {}", to_lowercase_improved(original_string));
    println!("Uppercase: {}", to_uppercase(original_string));
    let digits = "23008947";
    let parsed_num = match to_u64(digits) {
        Some(num) => num,
        None => 0
    };
    let parsed_num_improved = match to_u64_improved(digits) {
        Some(num) => num,
        None => 0
    };
    println!("Original: {digits}");
    println!("Number: {parsed_num}");
    println!("Number: {parsed_num_improved}");
    println!("String: {}", to_string(parsed_num));
    println!("String: {}", to_string_improved(parsed_num));

    println!("\n-----------Time comparison-----------");
    const ITERS: u32 = 100_000;
    const STRING: &str = "Hello, woRLd! 1234\nHello, woRLd! 1234\nHello, woRLd! 1234\nHello, woRLd! 1234\nHello, woRLd! 1234\nHello, woRLd! 1234\nHello, woRLd! 1234\nHello, woRLd! 1234\nHello, woRLd! 1234\nHello, woRLd! 1234\nHello, woRLd! 1234\nHello, woRLd! 1234\nHello, woRLd! 1234\n";

    let now = Instant::now();
    for _ in 0..ITERS {
        to_lowercase(STRING);
    }
    println!("{ITERS} iterations of to_lowercase completed in {:.2?}", now.elapsed());

    let now = Instant::now();
    for _ in 0..ITERS {
        to_lowercase_improved(STRING);
    }
    println!("{ITERS} iterations of to_lowercase_improved completed in {:.2?}", now.elapsed());

    const NUM_STRING: &str = "18446744073709551614";

    let now = Instant::now();
    for _ in 0..ITERS {
        to_u64(NUM_STRING);
    }
    println!("{ITERS} iterations of to_u64 completed in {:.2?}", now.elapsed());

    let now = Instant::now();
    for _ in 0..ITERS {
        to_u64_improved(NUM_STRING);
    }
    println!("{ITERS} iterations of to_u64_improved completed in {:.2?}", now.elapsed());

    const NUM: u64 = 18446744073709551614;

    let now = Instant::now();
    for _ in 0..ITERS {
        to_string(NUM);
    }
    println!("{ITERS} iterations of to_string completed in {:.2?}", now.elapsed());

    let now = Instant::now();
    for _ in 0..ITERS {
        to_string_improved(NUM);
    }
    println!("{ITERS} iterations of to_string_improved completed in {:.2?}", now.elapsed());
}

fn to_lowercase(s: &str) -> String {
    let bytes = s.bytes();
    let mut res = String::new();

    for byte in bytes {
        // Add 32 to the char, because ASCII lowercase letters are 32 positions after uppercase
        let parsed_byte = if byte >= b'A' && byte <= b'Z' { byte | 0b0100000 } else { byte };
        res.push(parsed_byte as char);
    }
    res
}

fn to_lowercase_improved(s: &str) -> String {
    let bytes = s.bytes();
    // This removes the necessity to allocate new heap memory for the String
    // For some reason, this has much more impact in release mode than in debug mode
    let mut res = String::with_capacity(s.len());

    for byte in bytes {
        // Add 32 to the char, because ASCII lowercase letters are 32 positions after uppercase
        let parsed_byte = if byte >= b'A' && byte <= b'Z' { byte | 0b0100000 } else { byte };
        res.push(parsed_byte as char);
    }
    res
}

fn to_uppercase(s: &str) -> String {
    let bytes = s.bytes();
    let mut res = String::new();

    for byte in bytes {
        // Subtract 32 from the char, because ASCII uppercase letters are 32 positions before lowercase
        let parsed_byte = if byte >= b'a' && byte <= b'z' { byte & 0b1011111 } else { byte };
        res.push(parsed_byte as char);
    }
    res
}

const BASE_10: u64 = 10;

fn to_u64(s: &str) -> Option<u64> {
    let bytes = s.bytes();
    let len = bytes.len();
    let mut res: u64 = 0;

    for (i, byte) in bytes.enumerate() {
        if byte >= b'0' && byte <= b'9' {
            // Subtract 48 from the char, because ASCII digits start at 48
            let digit = (byte & 0b001111) as u64;
            // Multiply it by the correct power of 10, from biggest (left) to smallest (right)
            let power = (len - i - 1) as u32;
            res += BASE_10.pow(power) * digit;
        } else {
            return None;
        }
    }
    Some(res)
}

/// This modification is actually identical to the original in release mode, but much faster in debug mode
fn to_u64_improved(s: &str) -> Option<u64> {
    let bytes = s.bytes();
    let mut res: u64 = 0;

    for byte in bytes {
        if byte >= b'0' && byte <= b'9' {
            // Subtract 48 from the char, because ASCII digits start at 48
            let digit = (byte & 0b001111) as u64;
            // Multiply it by 10 ("shift" to the left), and add the next digit
            // This removes the necessity to calculate powers of 10, and adds overflow safety checks
            // If overflow occurs, these return None, and the ? operator causes the entire function to return None
            res = res.checked_mul(10)?
                .checked_add(digit)?;
        } else {
            return None;
        }
    }
    Some(res)
}

fn to_string(mut num: u64) -> String {
    // u64::MAX = 18446744073709551615, so maximum power of 10 is 19
    const MAX_POWER: u32 = 19;
    let mut first_digit_found = false;
    let mut res = String::new();

    for power in (0..=MAX_POWER).rev() {
        // Get the digit at the i-th position
        let digit = num / BASE_10.pow(power);
        // Only add it to the string if we're inside the number, of if it's not 0 (avoid leading zeros)
        if digit > 0 || first_digit_found {
            // Add 48 to the char, because ASCII digits start at 48
            res.push((0b110000 + digit as u8) as char);
            num = num % BASE_10.pow(power);
            first_digit_found = true;
        }
    }
    res
}

fn to_string_improved(mut num: u64) -> String {
    if num == 0 {
        return "0".to_string();
    }

    // Number of digits in num
    let len = num.ilog10() as usize;
    // For some reason, this has much more impact in release mode than in debug mode
    let mut res = String::with_capacity(len);

    while num > 0 {
        // Get the digit at the i-th position from the end
        let digit = (num % 10) as u8;
        // "Shift" number to the right by 1 digit, discarding the one on the right
        // This will eventually turn the number into 0, because all digits will be cut off
        num /= 10;
        // Add 48 to the char, because ASCII digits start at 48
        res.push((0b110000 | digit) as char);
    }
    // Reverse the string becaues it's in the wrong order
    res.chars().rev().collect()
}
