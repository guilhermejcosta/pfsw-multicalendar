Table calendar as c {
  id int [pk, increment]
  owner_id int [ref: > u.id]
  organization_id int [ref: - o.id]
  title varchar
  description varchar
  created_at timestamp
  deleted_at timestamp
  updated_at timestamp
  shared boolean
}

Table users as u {
  id int [pk, increment] // auto-increment
  full_name varchar
  display_name varchar
  email varchar
  contact_phone integer
  created_at timestamp
  deleted_at timestamp
  updated_at timestamp
}

Table organization as o {
  owner_id int [ref: - u.id]
  id int [pk]
  name varchar
  created_at timestamp
  updated_at timestamp
  deleted_at timestamp
}

Table organization_users as ou {
  organization_id int [pk]
  user_id varchar [ref: > u.id]
  type_user int [ref: > tuo.id]
}

Table type_user_organization as tuo {
  id int [pk]
  description varchar
}