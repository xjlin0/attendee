Attendee.addressesDetail = {
  init: () => {
    console.log("attendee/mainsite/static/javascripts/addresses/detail.js");
    Attendee.utilities.convertUTC();
  }
}

$(document).ready(() => {
  Attendee.addressesDetail.init();
});
