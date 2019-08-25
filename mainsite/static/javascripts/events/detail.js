Attendee.eventsDetail = {
  init: () => {
    console.log("attendee/mainsite/static/javascripts/events/detail.js");
    Attendee.utilities.convertUTC();
  }
}

$(document).ready(() => {
  Attendee.eventsDetail.init();
});
