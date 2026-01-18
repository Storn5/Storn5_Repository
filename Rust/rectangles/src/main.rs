#[derive(Debug)]
struct Rect {
    width: u32,
    height: u32,
    x: u32,
    y: u32,
    name: String,
}
/*
fn borrow_string(s: String) {
    println!("{s}");
}
*/

/// Separate function that takes a &Rect reference as a parameter
fn get_area(rect: &Rect) -> u32 {
    // This is not allowed because we can't move stuff out of the reference we don't own
    // borrow_string(rect.name);

    rect.width * rect.height
}

impl Rect {
    /// Associated function that takes &self (&Rect) as a parameter
    // &self is short for self: &Self, which stands for self: &Rect
    fn get_area(&self) -> u32 {
        // This is not allowed because we can't move stuff out of the reference we don't own
        // borrow_string(self.name);

        self.width * self.height
    }

    fn can_contain(&self, rect2: &Rect) -> bool {
        if rect2.x >= self.x &&
           rect2.x + rect2.width <= self.x + self.width &&
           rect2.y >= self.y &&
           rect2.y + rect2.height <= self.y + self.height {
            true
        } else {
            false
        }
    }

    fn make_square(side_length: u32) -> Self {
        Self {
            width: side_length,
            height: side_length,
            x: 0,
            y: 0,
            name: String::new(),
        }
    }
}

fn main() {
    let mut rect1 = Rect {
        width: dbg!(20 + 3),
        height: 3,
        x: 0,
        y: 0,
        name: dbg!(String::from("My rectangle")),
    };
    let area = get_area(&rect1);
    let area2 = rect1.get_area(); // Automatic referencing: this is the same as (&rect1).get_area();
    println!("The area of rectangle {} ({rect1:#?}) at ({}, {}) is {} = {}", rect1.name, rect1.x, rect1.y, area, area2);
    dbg!(&rect1);

    let mut rect2 = Rect {
        width: 22,
        height: 1,
        x: 1,
        y: 1,
        name: String::from("My rectangle 2"),
    };
    let rect3 = Rect {
        width: 22,
        height: 1,
        x: 1,
        y: 3,
        name: String::from("My rectangle 3"),
    };
    let rect4 = Rect {
        width: 22,
        height: 1,
        x: 3,
        y: 1,
        name: String::from("My rectangle 4"),
    };
    let can_contain_rect2 = rect1.can_contain(&rect2);
    let mut_ref_to_rect1 = &mut rect1;
    mut_ref_to_rect1.height = 2;
    let square = Rect::make_square(35);

    println!("rect1 can contain rect2: {} {}", can_contain_rect2, mut_ref_to_rect1.height);
    println!("rect1 can contain rect3: {}", rect1.can_contain(&rect3));
    println!("rect1 can contain rect4: {}", rect1.can_contain(&rect4));
    println!("rect1 can contain square: {}", rect1.can_contain(&square));
}
