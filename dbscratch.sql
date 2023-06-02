SELECT
    id,
    first_name,
    last_name
FROM
    auth_user


DELETE FROM auth_user
WHERE id = 22

DELETE FROM bookclubapi_member
WHERE id = 6


DELETE FROM authtoken_token
WHERE user_id < 23


INSERT INTO bookclubapi_book (title, author, image)
    VALUES ('Lord of the Rings', 'J.R.R. Tolkien', 'https://media.istockphoto.com/id/172371649/photo/a-black-ornately-embossed-book-cover.jpg?s=612x612&w=0&k=20&c=S637eupjX2Y1a-nVnF0jl-IDLYJYMyg5vpwMXw2oqOU=')


INSERT INTO bookclubapi_book (title, author, image)
VALUES ('The Lion, the Witch, and the Wardobe', 'C.S. Lewis', 'https://media.istockphoto.com/id/172371649/photo/a-black-ornately-embossed-book-cover.jpg?s=612x612&w=0&k=20&c=S637eupjX2Y1a-nVnF0jl-IDLYJYMyg5vpwMXw2oqOU=')

UPDATE bookclubapi_book 
SET synopsis = 'A synopsis about Lord of the Rings'
WHERE id = 1

UPDATE bookclubapi_book 
SET synopsis = 'A synopsis about The Lion, the Witch, and the Wardrobe'
WHERE id = 2