use std::{time::Instant, collections::HashMap};

fn test_fib(n: u32, counter: &mut u32) -> u32 {
    *counter += 1;
    if n <= 1 { n } else {
        test_fib(n-1, counter) + test_fib(n-2, counter)
    }
}

fn test_fib_memoized(n: u32, counter: &mut u32) -> u32 {
    let mut memoized_fib_ns: HashMap<u32, u32> = HashMap::new();

    // memoized_fib_ns has to be mut because we're inserting things
    fn test_fib_memoized_inner(n: u32, memoized_fib_ns: &mut HashMap<u32, u32>, counter: &mut u32) -> u32 {
        *counter += 1;
        if n <= 1 { n }
        else {
            // Have to pass a reference into .get() ?
            match memoized_fib_ns.get(&n) {
                Some(res) => *res, // Have to dereference res because it's a reference?
                None => {
                    let res = test_fib_memoized_inner(n-2, memoized_fib_ns, counter) +
                        test_fib_memoized_inner(n-1, memoized_fib_ns, counter);
                    memoized_fib_ns.insert(n, res);
                    res
                }
            }
        }
    }

    test_fib_memoized_inner(n, &mut memoized_fib_ns, counter)
}


fn main() {
    let mut now = Instant::now();
    let mut counter: u32 = 0;
    let fib_40 = test_fib(40, &mut counter);
    println!("The 40th Fibonacci number is {fib_40} (calculated in {:.2?} in {counter} calls)", now.elapsed());

    now = Instant::now();
    counter = 0;
    let fib_40_memoized = test_fib_memoized(40, &mut counter);
    println!("The 40th memoized Fibonacci number is {fib_40_memoized} (calculated in {:.2?} in {counter} calls)", now.elapsed());
}
