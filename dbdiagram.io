Enum RecordStatusEnum {
  ACTIVE
  DELETED
  ARCHIVED
 }

Enum AttendingDivisionEnum {
  CHINESE
  ENGLISH
  CHILDREN
  NURSERY
  STAFF
  OTHER
  NONE
 }

/// Dydamic tables for note & images for any tables ///

Table linknote {
  id int [pk]
  link_table varchar [note: "any table name will do"]
  link_id int [note: "any table primary id"]
  note_type varchar
  note_text varchar
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table linkimage {
  id int [pk]
  link_table varchar [note: "any table name will do"]
  link_id int [note: "any table primary id"]
  image_type varchar
  image_url varchar
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

/// core people tables ///

Table attendee {
  id int [pk]
  chinese_name varchar
  english_name varchar
  actual_birthday datetime
  estimated_birthday datetime
  medical_concern varchar [note: "food allergy: nuts"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // hope someday we can collect birth year / blood type

Table relative {
  id int [pk]
  primary_attendee_id int [ref: > attendee.id]
  relative_attendee_id int [ref: > attendee.id]
  relationship varchar // relative_attendee to primary_attendee
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // mother/father/parent/guardian/chaperon/register

Table address {
  id int [pk]
  email1 varchar
  email2 varchar
  phone1 varchar
  phone2 varchar
  address_type varchar [note: "example: normal, nursery, pick_up"]
  street1 varchar
  street2 varchar
  city varchar
  state varchar
  zip_code varchar [note: "Canada zip code have space"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table registration {
  id int [pk]
  apply_type varchar [note: "example: online / paper"]
  apply_key varchar [note: "example: E1T1F1 / paper form serial#"]
  donation decimal
  credit decimal [note: "some staff don't have to pay"]
  event_id int [ref: > event.id]
  main_attendee_id int [ref: > attendee.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table attending {
  id int [pk]
  price_value decimal [default: 999999]
  age int
  gender varchar
  attending_type varchar [note: "example: normal, not_going, staff"]
  attending_division AttendingDivisionEnum
  belief varchar
  bed_needs int
  mobility int [note: "mobility > room.accessibility to assign rooms, default 1000"]
  attendee_id int [ref: > attendee.id]
  registration_id int [ref: > registration.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table attending_address {
  id int [pk]
  attendee_id int [ref: > attendee.id]
  address_id int [ref: > address.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

/// for events ///

Table event {
  id int [pk]
  name varchar
  registration_start datetime
  registration_end datetime
  event_start datetime
  event_end datetime
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table event_address {
  id int [pk]
  event_id int [ref: > event.id]
  address_id int [ref: > address.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // different programs maybe at different bldg/address


/// for facilities ///

Table campus {
  id int [pk]
  name varchar
  address_id int [ref: > address.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}  // Main, Burbank, Sonoma, Cannery Park, etc

Table building {
  id int [pk]
  name varchar
  campus_id int [ref: > campus.id]
  address_id int [ref: > address.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}  // Fellowship hall, Library, Sirah/Grenach, Baseball field, etc

Table suite {
  id int [pk]
  name varchar [note: "example: 7214"]
  building_id int [ref: > building.id]
  location varchar [note: "2F floor"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}  // 2F, west wing, 7205

Table room {
  id int [pk]
  suite_id int [ref: > suite.id]
  name varchar
  label varchar [note: "A, B, C"]
  accessibility int [note: "attending.mobility > accessibility to assign rooms, default 0"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}  // pastor office, room 513, room 7205-A

Table bed {
  id int [pk]
  room_id int [ref: > room.id]
  name varchar [note: "can be *floor*"]
  size int [note: "for how many people, default 1"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

/// dynamic preference table ///

Table preference {
  id int [pk]
  attending_id_1 int [ref: > attending.id]
  attending_id_2 int [ref: > attending.id]
  preference_table varchar [note: "example: residence, ride"]
  preference_level int [note: "how like/hate"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // to define how two people like/hate to be in the same room/ride/discussion

/// room assignments ///

Table residence {
  id int [pk]
  event_id int [ref: > event.id]
  bed_id int [ref: > bed.id]
  attending_id int [ref: > attending.id]
  flexibility int [note: "to label if we can change or lock the assignment"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // to assign people to rooms, some kids sleep on the floor


/// ride & pick ups  ///

Table rider {
  id int [pk]
  attending_id int [ref: > attending.id]
  address_id int [ref: > address.id]
  can_drives int [note: "i.e. can give ride for x people"]
  need_rides int [note: "i.e. need to be picked up"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table ride {
  id int [pk]
  event_id int [ref: > event.id]
  driver_attending_id int [ref: > attending.id]
  passenger_attending_id int [ref: > attending.id]
  address_id int [ref: > address.id]
  flexibility int [note: "to label if we can change or lock it"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

/// discussion groups ///

Table character {
  id int [pk]
  name varchar [note: "example: (vice) leader / member"]
  type varchar [note: "children program, retreat discussion"]
  display_order int
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // some people don't attend discussions, such as kids.  Also, roles are for app users

Table discussion_session {
  id int [pk]
  name varchar [note: "Saturday session I / II"]
  event_id int [ref: > event.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table discussion_group {
  id int [pk]
  name varchar [note: "example: group I"]
  suite_id int [ref: > suite.id, note: "null able"]
  event_id int [ref: > event.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table discussion_participation {
  id int [pk]
  name varchar
  event_id int [ref: > event.id]
  discussion_group_id int [ref: > discussion_group.id]
  discussion_session_id int [ref: > discussion_session.id]
  attending_id int [ref: > attending.id]
  character_id int [ref: > character.id, note: "as group leader/member"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

// there's no attendance records needed yet 

// kid programs

Table kid_program_progression {
  id int [pk]
  name varchar [note: "2020q4, 2020 retreat"]
  display_order int
  event_id int [ref: > event.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table kid_program_group {
  id int [pk]
  name varchar [note: "Shining Stars, The Rock"]
  info varchar [note: "what to wear/bring, what to teach"]
  url varchar [note: "link for intro"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table kid_program_lesson {
  id int [pk]
  kid_program_progression_id int [ref: > kid_program_progression.id]
  kid_program_group_id int [ref: > kid_program_group.id]
  name varchar [note: "Lesson #3 resurrection"]
  start_time datetime
  end_time datetime
  location_type varchar [note: "any location table name will do"]
  location_id int [note: "any location table primary id"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum

  indexes {
    (kid_program_group_id, location_type, location_id, start_time) [unique]
  }
} // so we can have The Rock @ Main or Burbank campus

Table kid_program_team {
  id int [pk]
  kid_program_lesson_id int [ref: > kid_program_lesson.id]
  name varchar [note: "Small group 4th grade, (Main/Large group is null)"]
  display_order int
  start_time datetime
  end_time datetime
  location_type varchar [note: "any location table name will do"]
  location_id int [note: "any location table primary id"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // All Small groups are defined here, please don't define Main/Large group


Table kid_program_participation {
  id int [pk]
  kid_program_lesson_id int [ref: > kid_program_lesson.id]
  kid_program_team_id int [ref: > kid_program_team.id]
  attending_id int [ref: > attending.id]
  character_id int [ref: > character.id, note: "LG leader, student"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // denormalize and add kid_program_lesson_id here for easier query, kid_program_team_id is nullable

Table kid_program_group_schedule {
  id int [pk]
  kid_program_group_id int [ref: > kid_program_group.id]
  schedule_id int [ref: > schedule.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table schedule {
  id int [pk]
  name varchar [note: "Last Sunday of Feb 10AM"]
  frequency varchar [note: "WEEKLY"]
  byweekday int [note: "0 == Monday"]
  hour int [note: "0 is midnight, 12 is noon"]
  minute int [note: "0~59"]
  duration_in_minutes int
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // dateutil https://labix.org/python-dateutil

/// payments ///

Table price {
  id int [pk]
  price_label varchar
  price_type varchar  [note: "example: nobed_earlybird"]
  price_value decimal [default: 999999]
  start_date datetime [note: "When the price start to be effective"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // latest records meeting start_date and price_type will be effective

Table payment {
  id int [pk]
  payee_attending_id int [ref: > attending.id]
  amount decimal
  txn_type varchar [note: "example: paypal / check"]
  txn_id varchar [note: "example: paypal serial # / check #"]
  result varchar [note: "example: success / returned checks"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // how to support cancellation? manually negative amount?

Table registration_payment {
  id int [pk]
  registration_id int [ref: > registration.id]
  payment_id int [ref: > payment.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // how to support cancellation? manually negative payment?

// You can define relationship inline or separately
// Ref: order_items.product_id > products.id



