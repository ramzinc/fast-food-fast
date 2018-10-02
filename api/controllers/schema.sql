
CREATE TABLE Users(
    user_id int primary key,
    full_name text ,
    admin boolean,
    email text,
    password text
);

CREATE TABLE Fast_Meals(
    meal_id int PRIMARY KEY NOT NULL ,
    meal_name text,
    price numeric
);

CREATE TABLE Fast_Order(
    order_id int PRIMARY KEY,
    user_id int  REFERENCES Users (user_id) ON UPDATE CASCADE ON DELETE RESTRICT,
    meal_id int  REFERENCES Fast_Meals (meal_id) ON UPDATE CASCADE ON DELETE RESTRICT
)
