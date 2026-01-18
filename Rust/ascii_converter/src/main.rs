fn main() {
    let original_string = "Hello, woRLd! 1234";
    println!("Original: {original_string}");
    println!("Lowercase: {}", to_lowercase(original_string));
    println!("Uppercase: {}", to_uppercase(original_string));
    let digits = "238947";
    let parsed_num = match to_u64(digits) {
        Some(num) => num,
        None => 0
    };
    println!("Original: {digits}");
    println!("Number: {parsed_num}");
    println!("String: {}", to_string(parsed_num));
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

fn to_string(mut num: u64) -> String {
    // u64::MAX = 18446744073709551615, so maximum power of 10 is 19
    const MAX_POWER: u32 = 19;
    let first_digit_found = false;
    let mut res = String::new();

    for power in (0..=MAX_POWER).rev() {
        // Get the digit at the i-th position
        let digit = num / BASE_10.pow(power);
        // Only add it to the string if we're inside the number, of if it's not 0 (avoid leading zeros)
        if digit > 0 || first_digit_found {
            res.push((0b110000 + digit as u8) as char);
            num = num % BASE_10.pow(power);
        }
    }
    res
}
