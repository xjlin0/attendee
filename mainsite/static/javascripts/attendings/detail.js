Attendee.attendingsDetail = {
  init: () => {
    console.log("attendee/mainsite/static/javascripts/attendings/detail.js");
    Attendee.utilities.convertUTC();
  }
}

$(document).ready(() => {
  Attendee.attendingsDetail.init();
});
