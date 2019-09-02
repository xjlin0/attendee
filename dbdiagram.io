Enum RecordStatusEnum {
  ACTIVE
  DELETED
  ARCHIVED
 }

Enum AttendingDivisionEnum {
  CHINESE
  ENGLISH
  CHILDREN // NURSERY, STAFF combined
  OTHER
  NONE
 }

/// Dynamic tables for note & images for any tables ///

Table link_notes {
  id int [pk]
  link_table varchar [note: "any table name will do"]
  link_id int [note: "any table primary id"]
  note_type varchar
  note_text varchar
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table link_images {
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

Table attendees {
  id int [pk]
  first_name varchar
  last_name varchar
  first_name2 varchar
  last_name2 varchar
  other_name varchar
  gender varchar
  actual_birthday datetime
  estimated_birthday datetime
  medical_concern varchar [note: "food allergy: nuts"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // hope someday we can collect birth year / blood type

Table relationships {
  id int [pk]
  main_attendee_id int [ref: > attendee.id]
  other_attendee_id int [ref: > attendee.id]
  relation_to_main varchar // relative_attendee to primary_attendee
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // mother/father/parent/guardian/chaperon/register

Table addresses {
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

Table registrations {
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

Table attendings {
  id int [pk]
  price_value decimal [default: 999999]
  age int
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

Table attendings_address {
  id int [pk]
  attendee_id int [ref: > attendee.id]
  address_id int [ref: > address.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

/// for events ///

Table events {
  id int [pk]
  name varchar
  registration_start datetime
  registration_end datetime
  division AttendingDivisionEnum
  event_start datetime
  event_end datetime
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table events_address {
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

Table properties {
  id int [pk]
  name varchar
  campus_id int [ref: > campus.id]
  address_id int [ref: > address.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}  // Fellowship hall, Library, Sirah/Grenach, Baseball field, etc

Table suites {
  id int [pk]
  name varchar [note: "example: 7214"]
  property_id int [ref: > property.id]
  location varchar [note: "2F floor"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}  // 2F, west wing, 7205

Table rooms {
  id int [pk]
  suite_id int [ref: > suite.id]
  name varchar
  label varchar [note: "A, B, C"]
  accessibility int [note: "attending.mobility > accessibility to assign rooms, default 0"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}  // pastor office, room 513, room 7205-A

Table beds {
  id int [pk]
  room_id int [ref: > room.id]
  name varchar [note: "can be *floor*"]
  size int [note: "for how many people, default 1"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

/// dynamic preference table ///

Table attendings_preferences {
  id int [pk]
  attending_id_1 int [ref: > attending.id]
  attending_id_2 int [ref: > attending.id]
  preference_table varchar [note: "example: residence, ride"]
  preference_level int [note: "how like/hate"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // to define how two people like/hate to be in the same room/ride/discussion

Table participations_preferences {
  id int [pk]
  attending_id int [ref: > attending.id]
  participation_table varchar [note: "example: residence, ride"]
  participation_id int [note: "how like/hate"]
  available boolean [note: "true is available, false is unavailable, not null"]
  schedule_id int [ref: > schedules.id]   // nullable for single time
  start_at datetime  // can be generated from regular schedule
  end_at datetime    // can be generated from regular schedule
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // to define how a person's (in)availability, single time or from referencing regular schedule

/// room assignments ///

Table residences {
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

Table riders {
  id int [pk]
  attending_id int [ref: > attending.id]
  address_id int [ref: > address.id]
  can_drives int [note: "i.e. can give ride for x people"]
  need_rides int [note: "i.e. need to be picked up"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table rides {
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

Table characters {
  id int [pk] [note: "id 1 is magic number, means all characters, 0 is no characters"]
  name varchar [note: "example: (vice) leader / member"]
  type varchar [note: "children program, retreat discussion"]
  display_order int
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // some people don't attend discussions, such as kids.  Also, roles are for app users

Table characters_exclusions {
  id int [pk]
  main_character_id int [ref: > character.id]
  other_character_id int [ref: > character.id, note: "1 means exclude everyone, 0 means compatible with everyone, not null"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // don't consider rigidity here


Table discussion_sessions {
  id int [pk]
  name varchar [note: "Saturday session I / II"]
  event_id int [ref: > event.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table discussion_groups {
  id int [pk]
  name varchar [note: "example: group I"]
  suite_id int [ref: > suite.id, note: "null able"]
  event_id int [ref: > event.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table discussion_participations {
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

// kid or other programs

Table program_progressions {
  id int [pk]
  name varchar [note: "2020q4 kid programs, 2020 retreat"]
  display_order int
  event_id int [ref: > event.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table program_groups {
  id int [pk]
  name varchar [note: "Shining Stars, The Rock"]
  info varchar [note: "what to wear/bring, what to teach"]
  url varchar [note: "link for intro"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table program_sessions {
  id int [pk]
  program_progression_id int [ref: > program_progression.id]
  program_group_id int [ref: > program_group.id]
  name varchar [note: "Lesson #3 resurrection, retreat #2, etc"]
  start_time datetime
  end_time datetime
  location_type varchar [note: "any location table name will do"]
  location_id int [note: "any location table primary id"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum

  indexes {
    (program_group_id, location_type, location_id, start_time) [unique]
  }
} // so we can have The Rock @ Main or Burbank campus

Table program_teams {
  id int [pk]
  program_session_id int [ref: > program_session.id]
  name varchar [note: "Small group 4th grade, (Main/Large group is null)"]
  display_order int
  start_time datetime  [note: "team start/end time can be different from session"]
  end_time datetime
  location_type varchar [note: "any location table name, team location can be different from lesson"]
  location_id int [note: "any location table primary id"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // All Small groups are defined here, please don't define Main/Large group


Table program_participations {
  id int [pk]
  program_lesson_id int [ref: > program_session.id]
  program_team_id int [ref: > program_team.id]
  attending_id int [ref: > attending.id]
  character_id int [ref: > character.id, note: "LG leader, student"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // denormalize and add program_session_id here for easier query, program_team_id is nullable

// Table 'event' provides AttendingDivisionEnum for creating program_progression
//
// Table program_progressions example:
// +-------------------+----+-------------+
// |       event       |name|display_order|
// +-------------------+----+-------------+
// |2019-20 kid program| Q4 |     4       |
// +-------------------+----+-------------+

// Table program_sessions example:
// +-------------------+-------------+--------------------+
// |program_progression|program_group|        name        |
// +-------------------+-------------+--------------------+
// |          Q4       | The Rock    | Lesson #3 09/01/19 |
// +-------------------+-------------+--------------------+
//
//
// Table 'attendings' provides AttendingDivisionEnum for participation assignment
//
// Example of The Rock student participates large group AND 4th small group:
// +------------------+------------+---------+
// |  program_session |program_team|character|
// +------------------+------------+---------+
// |Lesson #3 09/01/19| 4th SG     | student |
// +------------------+------------+---------+
//
// Example of The Rock large group leader:
// +------------------+------------+---------+
// |  program_session |program_team|character|
// +------------------+------------+---------+
// |Lesson #3 09/01/19| NULL       |LG leader|
// +------------------+------------+---------+
//
// Example of The Rock large small group leader for 4th Grade:
// +------------------+------------+---------+
// |  program_session |program_team|character|
// +------------------+------------+---------+
// |Lesson #3 09/01/19| 4th SG     |SG leader|
// +------------------+------------+---------+


Table program_group_schedules {
  id int [pk]
  program_group_id int [ref: > program_group.id]
  schedule_id int [ref: > schedule.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table schedules {
  id int [pk]
  name varchar [note: "Last Sunday of Feb 10AM"]
  frequency varchar [note: "WEEKLY"]
  byweekday int [note: "0 == Monday"]
  hour int [note: "0 is midnight, 12 is noon"]
  minute int [note: "0~59"]
  start_at datetime  [note: "i.e.: every Tuesday from November'19"]
  end_at datetime [note: "null means endless"]
  duration_in_minutes int
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // dateutil https://labix.org/python-dateutil

/// payments ///

Table prices {
  id int [pk]
  price_label varchar
  price_type varchar  [note: "example: no bed_earlybird"]
  price_value decimal [default: 999999]
  start_date datetime [note: "When the price start to be effective"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // latest records meeting start_date and price_type will be effective

Table payments {
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

Table registrations_payment {
  id int [pk]
  registration_id int [ref: > registration.id]
  payment_id int [ref: > payment.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // how to support cancellation? manually negative payment?

// You can define relationship inline or separately
// Ref: order_items.product_id > products.id



