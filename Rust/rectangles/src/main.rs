#[derive(Debug)]
struct Rect {
    width: u32,
    height: u32,
    x: u32,
    y: u32,
    name: String,
}

fn borrow_string(s: String) {
    println!("{s}");
}

fn get_area(rect: &Rect) -> u32 {
    // This is not allowed because we can't move stuff out of the reference we don't own
    // borrow_string(rect.name);

    rect.width * rect.height
}

fn main() {
    let rect1 = Rect {
        width: dbg!(20 + 3),
        height: 3,
        x: 0,
        y: 0,
        name: dbg!(String::from("My rectangle")),
    };
    let area = get_area(&rect1);
    println!("The area of rectangle {} ({rect1:#?}) at ({}, {}) is {}", rect1.name, rect1.x, rect1.y, area);
    dbg!(&rect1);
}
