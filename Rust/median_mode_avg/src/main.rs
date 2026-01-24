use std::{collections::HashMap, time::Instant};

fn main() {
    let mut nums = Vec::from([1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10]);
    let mode_val = mode(&nums).expect("Couldn't get mode");
    let mode_val_loop = mode_loop(&nums).expect("Couldn't get mode with loop");
    let median_val = median(&mut nums).expect("Couldn't get median");
    let mean_val = mean(&nums).expect("Couldn't get mean");
    // Should be     5,                                    3,                  2.7142857142857144
    println!("Mode: {mode_val} ({mode_val_loop}), Median: {median_val}, Mean: {mean_val}");

    nums = Vec::from([]);
    let mode_val = mode(&nums).unwrap_or(69);
    let mode_val_loop = mode_loop(&nums).unwrap_or(69);
    let median_val = median(&mut nums).unwrap_or(69);
    let mean_val = mean(&nums).unwrap_or(69.0);
    // Should be     69,                                   69,                 69
    println!("Mode: {mode_val} ({mode_val_loop}), Median: {median_val}, Mean: {mean_val}");

    time_mode();
    time_mode_loop();
    time_median();
    time_median_mergesort();
    time_median_insertionsort();
    time_median_mergeinsertionsort();
}

fn time_mode() {
    let nums = Vec::from([1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10]);
    let now = Instant::now();
    for _ in 0..10_000 {
        let a = mode(&nums).unwrap();
        print!("{a}\r");
    }
    println!("\rMode 1 time: {:.2?}", now.elapsed());
}

fn time_mode_loop() {
    let nums = Vec::from([1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10]);
    let now = Instant::now();
    for _ in 0..10_000 {
        let a = mode_loop(&nums).unwrap();
        print!("{a}\r");
    }
    println!("\rMode 2 time: {:.2?}", now.elapsed());
}

fn time_median() {
    let mut nums = Vec::from([1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10]);
    let now = Instant::now();
    for _ in 0..10_000 {
        let a = median(&mut nums).unwrap();
        print!("{a}\r");
    }
    println!("\rMedian sort() time: {:.2?}", now.elapsed());
}

fn time_median_mergesort() {
    let mut nums = Vec::from([1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10]);
    let now = Instant::now();
    for _ in 0..10_000 {
        let a = median_mergesort(&mut nums).unwrap();
        print!("{a}\r");
    }
    println!("\rMedian merge sort time: {:.2?}", now.elapsed());
}

fn time_median_insertionsort() {
    let mut nums = Vec::from([1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10]);
    let now = Instant::now();
    for _ in 0..10_000 {
        let a = median_insertionsort(&mut nums).unwrap();
        print!("{a}\r");
    }
    println!("\rMedian insertion sort time: {:.2?}", now.elapsed());
}

fn time_median_mergeinsertionsort() {
    let mut nums = Vec::from([1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10, 1, 2, 3, 2, 5, -2, -1, 3, -1, 5, 5, 9, -3, 10]);
    let now = Instant::now();
    for _ in 0..10_000 {
        let a = median_mergeinsertionsort(&mut nums).unwrap();
        print!("{a}\r");
    }
    println!("\rMedian merge & insertion sort time: {:.2?}", now.elapsed());
}

/// Returns most common number, if numbers are empty returns None 
fn mode(nums: &[i32]) -> Option<i32> {
    if nums.len() == 0 {
        return None;
    }

    let mut map: HashMap<i32, u32> = HashMap::new();
    for i in nums {
        let i_occurences = map.entry(*i).or_default();
        *i_occurences += 1;
    }

    match map.iter().max_by(|first, second| first.1.cmp(&second.1)) {
        Some((&key, &_)) => Some(key),
        None => None
    }
}

/// Alternative implementation with a loop to find max map value
fn mode_loop(nums: &[i32]) -> Option<i32> {
    if nums.len() == 0 {
        return None;
    }

    let mut map: HashMap<i32, u32> = HashMap::new();
    for i in nums {
        let i_occurences = map.entry(*i).or_default();
        *i_occurences += 1;
    }

    let mut max: u32 = 0;
    let mut max_num: i32 = 0;
    for (key, value) in map {
        if value >= max {
            max = value;
            max_num = key;
        }
    }

    Some(max_num)
}

fn median(nums: &mut [i32]) -> Option<i32> {
    let len = nums.len();
    if len == 0 {
        return None;
    }

    nums.sort();
    Some(nums[len / 2])
}

fn median_mergesort(mut nums: &mut [i32]) -> Option<i32> {
    let len = nums.len();
    if len == 0 {
        return None;
    }

    merge_sort(&mut nums);
    Some(nums[len / 2])
}

fn median_insertionsort(mut nums: &mut [i32]) -> Option<i32> {
    let len = nums.len();
    if len == 0 {
        return None;
    }

    insertion_sort(&mut nums);
    Some(nums[len / 2])
}

fn median_mergeinsertionsort(mut nums: &mut [i32]) -> Option<i32> {
    let len = nums.len();
    if len == 0 {
        return None;
    }

    merge_and_insertion_sort(&mut nums);
    Some(nums[len / 2])
}

fn merge_sort(nums: &mut [i32]) {
    let len = nums.len();
    if len <= 1 {
        return;
    }

    // Can't do this because you can't have 2 mut references to nums
    // let left =  &mut nums[..len/2];
    // let right = &mut nums[len/2..];
    let (mut left, mut right) = nums.split_at_mut(len/2);
    let left_len = left.len();
    let right_len = right.len();
    merge_sort(&mut left);
    merge_sort(&mut right);

    let mut new_nums: Vec<i32> = Vec::with_capacity(len);
    let (mut left_index, mut right_index): (usize, usize) = (0, 0);
    while left_index < left_len || right_index < right_len {
        // I'm adding the leftover elements inside this loop, because doing .extend_from_slice() after the loop was slower
        if left_index == left_len {
            new_nums.push(right[right_index]);
            right_index += 1;
        } else if right_index == right_len {
            new_nums.push(left[left_index]);
            left_index += 1;
        } else {
            if left[left_index] < right[right_index] {
                new_nums.push(left[left_index]);
                left_index += 1;
            } else {
                new_nums.push(right[right_index]);
                right_index += 1;
            }
        }
    }

    // But copy_from_slice is faster than manually assigning the elements of nums
    nums.copy_from_slice(&new_nums);
}

fn insertion_sort(nums: &mut [i32]) {
    let mut i: usize = 1;
    while i < nums.len() {
        let mut j = i;
        let val_to_compare = nums[i];
        while j > 0 && val_to_compare < nums[j - 1] {
            nums[j] = nums[j - 1];
            j -= 1;
        }
        nums[j] = val_to_compare;
        i += 1;
    }
}

fn merge_and_insertion_sort(nums: &mut [i32]) {
    let len = nums.len();
    if len <= 1 {
        return;
    } else if len <= 16 {
        insertion_sort(nums);
        return;
    }

    // Can't do this because you can't have 2 mut references to nums
    // let left =  &mut nums[..len/2];
    // let right = &mut nums[len/2..];
    let (mut left, mut right) = nums.split_at_mut(len/2);
    let left_len = left.len();
    let right_len = right.len();
    merge_and_insertion_sort(&mut left);
    merge_and_insertion_sort(&mut right);

    let mut new_nums: Vec<i32> = Vec::with_capacity(len);
    let (mut left_index, mut right_index): (usize, usize) = (0, 0);
    while left_index < left_len || right_index < right_len {
        // I'm adding the leftover elements inside this loop, because doing .extend_from_slice() after the loop was slower
        if left_index == left_len {
            new_nums.push(right[right_index]);
            right_index += 1;
        } else if right_index == right_len {
            new_nums.push(left[left_index]);
            left_index += 1;
        } else {
            if left[left_index] < right[right_index] {
                new_nums.push(left[left_index]);
                left_index += 1;
            } else {
                new_nums.push(right[right_index]);
                right_index += 1;
            }
        }
    }

    // But copy_from_slice is faster than manually assigning the elements of nums
    nums.copy_from_slice(&new_nums);
}

fn mean(nums: &[i32]) -> Option<f64> {
    let len = nums.len();
    if len == 0 {
        return None;
    }

    let mut sum = 0;
    for &i in nums {
        sum += i;
    }

    Some(sum as f64 / len as f64)
}
