// src/module/mod.rs or src/module/submodule/mod.rs is the old style of module definition
// the modern style is src/module.rs or src/module/submodule.rs

// This makes the submodule available for import by modules that import this one
pub mod back_end_submod;

pub enum Appetizer {
    Soup{ name: String, cost: u32 },
    Salad{ name: String, cost: u32 },
    Salt,
    Pepper(String),
}

pub struct Breakfast {
    pub name: String,
    pub cost: u32,
    id: u32,
}

pub fn assign_order_id(order_name: &str) {

}

pub fn process_order(order_cost: u32, order_id: u32) {

}
