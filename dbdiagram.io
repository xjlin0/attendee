Enum RecordStatusEnum {
  ACTIVE
  DELETED
  ARCHIVED
 }

Table divisions {
  id int [pk]
  key varchar [note: "CHINESE ENGLISH CHILDREN OTHER NONE, etc"]
  name varchar
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
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
  main_attendee_id int [ref: > attendees.id]
  other_attendee_id int [ref: > attendees.id]
  relation_to_main varchar // relative_attendee to primary_attendee
  created_at datetime
  updated_at datetime
  status RecordStatusEnum

  indexes {
    (main_attendee_id, other_attendee_id) [unique]
  }
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
} // phone1 will be sms-messaged, email1 will be emailed.

Table registrations {
  id int [pk]
  apply_type varchar [note: "example: online / paper"]
  apply_key varchar [note: "example: E1T1F1 / paper form serial#"]
  donation decimal
  credit decimal [note: "some staff don't have to pay"]
  event_id int [ref: > events.id]
  main_attendee_id int [ref: > attendees.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table attendings {
  id int [pk]
  price_value decimal [default: 999999]
  age int
  attending_type varchar [note: "example: normal, not_going, staff"]
  belief varchar
  bed_needs int
  mobility int [note: "mobility > room.accessibility to assign rooms, default 1000"]
  attendee_id int [ref: > attendees.id]
  registration_id int [ref: > registrations.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table attending_divisions {
  id int [pk]
  attending_id int [ref: > attendings.id]
  division_id int [ref: > divisions.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum

  indexes {
    (attending_id, division_id) [unique]
  }
} // a person can join different divisions

Table attending_address {
  id int [pk]
  attendee_id int [ref: > attendees.id]
  address_id int [ref: > addresses.id]
  opt_in_sms_at datetime
  opt_out_sms_at datetime
  opt_in_email_at datetime
  opt_out_email_at datetime
  created_at datetime
  updated_at datetime
  status RecordStatusEnum

  indexes {
    (attendee_id, address_id) [unique]
  }
}

/// for events ///

Table events {
  id int [pk]
  name varchar
  registration_start datetime
  registration_end datetime
  division_id [ref: > divisions.id]
  event_start datetime
  event_end datetime
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table event_address {
  id int [pk]
  event_id int [ref: > events.id]
  address_id int [ref: > addresses.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum

  indexes {
    (event_id, address_id) [unique]
  }
} // different programs maybe at different bldg/address


/// for facilities ///

Table campus {
  id int [pk]
  name varchar
  address_id int [ref: > addresses.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}  // Main, Burbank, Sonoma, Cannery Park, etc

Table properties {
  id int [pk]
  name varchar
  campus_id int [ref: > campus.id]
  address_id int [ref: > addresses.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}  // Fellowship hall, Library, Sirah/Grenach, Baseball field, etc

Table suites {
  id int [pk]
  name varchar [note: "example: 7214"]
  property_id int [ref: > properties.id]
  location varchar [note: "2F floor"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}  // 2F, west wing, 7205

Table rooms {
  id int [pk]
  suite_id int [ref: > suites.id]
  name varchar
  label varchar [note: "A, B, C"]
  accessibility int [note: "attending.mobility > accessibility to assign rooms, default 0"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}  // pastor office, room 513, room 7205-A

Table beds {
  id int [pk]
  room_id int [ref: > rooms.id]
  name varchar [note: "can be *floor*"]
  size int [note: "for how many people, default 1"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

/// dynamic preference table ///

Table attending_preferences {
  id int [pk]
  main_attending_id int [ref: > attendings.id]
  other_attending_id int [ref: > attendings.id]
  preference_table varchar [note: "example: residences, rides, null means globally, such as elder care givers"]
  preference_level int [note: "how like/hate"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum

  indexes {
    (main_attending_id, other_attending_id, preference_table) [unique]
  }
} // [person to person] to define how two people like/unlike to be in the same room/ride/discussion,
  // i.e. Mother/baby want to be in the same ride, but not in the same discussion_groups

Table participation_preferences {
  id int [pk]
  attending_id int [ref: > attendings.id]
  preference_table varchar [note: "example: residences, rides, discussion_groups"]
  preference_id int [note: "how like/hate"]
  availability int [note: "positive is available, negative is unavailable, not null"]
  schedule_id int  [ref: > schedules.id] // nullable for single time
  start_at datetime  // can be generated from regular schedule
  end_at datetime    // can be generated from regular schedule
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // Optional: [person to participation] to define how a person's (in)availability, single time or from referencing regular schedule

Table character_preferences {
  id int [pk]
  main_character_id int [ref: > characters.id]
  other_character_id int [ref: > characters.id] // note: "1 means exclude everyone, 0 means compatible with everyone, not null"
  compatibility int [note: "positive: can be served simultaneously by the same person in the same participation, negative is not, not null"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // [participation to participation] In the same session, kid food preparers can be students too. Traffic controllers cannot be pianists.


/// room assignments ///

Table residences {
  id int [pk]
  event_id int [ref: > events.id]
  bed_id int [ref: > beds.id]
  attending_id int [ref: > attendings.id]
  flexibility int [note: "to label if we can change or lock the assignment"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // to assign people to rooms, some kids sleep on the floor


/// ride & pick ups  ///

Table riders {
  id int [pk]
  attending_id int [ref: > attendings.id]
  address_id int [ref: > addresses.id]
  can_drives int [note: "i.e. can give ride for x people"]
  need_rides int [note: "i.e. need to be picked up"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table rides {
  id int [pk]
  event_id int [ref: > events.id]
  driver_attending_id int [ref: > attendings.id]
  passenger_attending_id int [ref: > attendings.id]
  address_id int [ref: > addresses.id]
  flexibility int [note: "to label if we can change or lock it"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

/// discussion groups ///

Table characters {
  id int [pk] // [note: "id 1 is magic number, means all characters, 0 is no characters"]
  name varchar [note: "example: (vice) leader / member"]
  type varchar [note: "children program, retreat discussion"]
  display_order int
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // some people don't attend discussions, such as kids.  Also, roles are for app users

Table discussion_sessions {
  id int [pk]
  name varchar [note: "Saturday session I / II"]
  event_id int [ref: > events.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table discussion_groups {
  id int [pk]
  name varchar [note: "example: group I"]
  suite_id int [ref: > suites.id, note: "null able"]
  event_id int [ref: > events.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
}

Table discussion_participations {
  id int [pk]
  name varchar
  event_id int [ref: > events.id]
  discussion_group_id int [ref: > discussion_groups.id]
  discussion_session_id int [ref: > discussion_sessions.id]
  attending_id int [ref: > attendings.id]
  character_id int [ref: > characters.id] //, note: "as group leader/member"
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
  event_id int [ref: > events.id]
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
  program_progression_id int [ref: > program_progressions.id]
  program_group_id int [ref: > program_groups.id]
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
  program_session_id int [ref: > program_sessions.id]
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
  program_session_id int [ref: > program_sessions.id]
  program_team_id int [ref: > program_teams.id]
  attending_id int [ref: > attendings.id]
  character_id int [ref: > characters.id] // note: "LG leader, student"
  free int [note: "instance level: if negative, the person is unlikely to join other sessions at the same time, i.e. drivers"]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // denormalize and add program_session_id here for easier query, program_team_id is nullable

// Table 'event' provides division for creating program_progression
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
// Model 'Attending' provides divisions for participation assignment
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
  program_group_id int [ref: > program_groups.id]
  schedule_id int [ref: > schedules.id]
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
  payee_attending_id int [ref: > attendings.id]
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
  registration_id int [ref: > registrations.id]
  payment_id int [ref: > payments.id]
  created_at datetime
  updated_at datetime
  status RecordStatusEnum
} // how to support cancellation? manually negative payment?

// You can define relationship inline or separately
// Ref: order_items.product_id > products.id



