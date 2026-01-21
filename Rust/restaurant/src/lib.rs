use back_end::Appetizer;

mod front_end;
mod back_end;

mod restaurant_module {
    pub mod hosting {
        use crate::front_end;

        pub fn add_to_waitlist() {

        }

        fn seat_at_table() {
            front_end::find_a_seat();
            front_end::reserve_seat();
        }
    }

    mod serving {
        // Structs/Enums are named directly in the use statement, functions are referenced by their crate
        // This is the same as use crate::{back_end, back_end::back_end_submod, back_end::Breakfast};
        use crate::back_end::{self, back_end_submod, Breakfast};

        fn take_order(order: Breakfast) {
            back_end::assign_order_id(&order.name);
            back_end::process_order(order.cost, 0 /* order.id is private */);
            if true {
                super::fix_incorrect_order();
            }
            back_end_submod::do_something();
        }

        fn serve_order() {

        }

        fn take_payment() {

        }
    }

    fn fix_incorrect_order() {

    }
}

pub fn eat_at_restaurant() {
    crate::restaurant_module::hosting::add_to_waitlist();
    restaurant_module::hosting::add_to_waitlist();
    let appetizer = Appetizer::Salt;
    let appetizer2 = Appetizer::Salad {
        name: String::from("Caesar"),
        cost: 42,
    };
}
