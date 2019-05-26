Attendee.utilities = {
  init: () => {
    console.log("attendee/mainsite/static/javascripts/shared/utilities.js");
  },

  test: () => {
    console.log("Attendee.utilities.test() ready");
  }
}

$(document).ready(() => {
  Attendee.utilities.init();
});
