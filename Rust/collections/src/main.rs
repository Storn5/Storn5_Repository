fn main() {
    vectors();
    strings();
}

fn vectors() {
    let v: Vec<u32> = Vec::new();
    println!("{v:?}");
    // Vec<i32> by default, needs to be mut to push
    let mut v2 = vec![1, 2, 3];
    v2.push(5);

    let elem = v2[0]; // Panics if out of bounds
    let elem2 = &v2[1]; // &i32, Panics if out of bounds
    let elem3 = v2.get(3) // Option<&i32>, returns None if out of bounds
        .expect("Could not get element 3 of v2");
    // Can't mutate v2 because we have an immutable ref v2[1]
    // v2.push(6);
    println!("{elem} {elem2} {elem3}");
    for i in &v2 { // This iterates over immutable refs to elements of v2
        println!("{i}");
        // This also isn't allowed when iterating for the same reason
        // v2.push(3);
    }
    for i in &mut v2 { // This iterates over mut refs to elements of v2
        *i *= 23;
    }
    let popped_elem = v2.pop() // Returns Option<i32>;
        .expect("Could not pop element from v2");
    println!("Popped element: {popped_elem}");

    println!("Size of i32: {}, elements in v2: {}, size of v2: {}",
        size_of::<i32>(), v2.len(), size_of_val(&v2));
    v2.push(1);
    v2.push(1);
    v2.push(1);
    v2.push(1);
    v2.push(1);
    // Vec size doesn't change, it just holds a len, a capacity, a pointer, no actual values
    println!("Size of i32: {}, elements in v2: {}, size of v2: {}",
        size_of::<i32>(), v2.len(), size_of_val(&v2));
}

fn strings() {
    let mut s = String::with_capacity(15);
    s.push_str("123456789");
    println!("{s}");
    s = "12345".to_string(); // Turns &str slice into String
    s.push('6');
    println!("{s}");
    // Both &str slices and String store collections of UTF-8 encoded bytes
    let slice = "Раст — це легка мова! 🫠";
    let count = "Rust - is a simple lang!";
    println!("{} {}", slice.len(), count.len()); // len() represents actual bytes, not characters
    let mut s2 = String::from(slice);
    // To use + with strings, left must be owned and right must be &str or &String
    // (&String is deref coerced into &str)
    let ref_to_s2 = &s2;
    let s3 = s + ref_to_s2;
    // Can't use s, because its value was moved (we didn't reference it above but just moved the value)
    // let s4 = s + slice;

    // But we can still modify s2, because only an immutable ref to it was used before
    s2.push_str("whatever else");
    println!("{s2} {s3} {slice}"); // If we use {ref_to_s2}, then the line above won't work because this reference will be kept

    let ref_to_s3 = &s3;
    // This is better, returns String and we don't have to mess with move semantics & ownership
    let s4 = format!("{s2} {s3} {ref_to_s3}");
    println!("{s4} {s2} {s3} {ref_to_s3}");

    // Can't index string with an integer as if it was a Vec or an array
    // let first_char = s4[0];

    // Can index like this instead
    let first_char = s4.chars().nth(0);
    // Or this to get the first u8 value (part of a UTF8 char or the entire char, depending on size)
    let first_byte = s4.bytes().nth(0);

    let half_of_16_bit_char = s4.as_bytes()[0];
    println!("Half of the first character: {half_of_16_bit_char}");
    // Get the first 2 Cyrillic characters:
    let first_4_bytes = &s4[0..4];
    println!("First 4 bytes: {first_4_bytes:?}"); // This is fine, we are at a character boundary
    // Get the first 2.5 Cyrillic characters (5 bytes):
    // let first_5_bytes = &s4[0..5]; // Causes a panic! The 5th byte is not a character boundary, it's invalid

    for c in s4.chars() { // chars() returns actual characters instead of bytes
        println!("{c}");
    }
}
