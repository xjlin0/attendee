Attendee.utilities = {
  init: () => {
    console.log("attendee/mainsite/static/javascripts/shared/utilities.js");
  },

  convertUTC: (timeNodeSelector = "time", attributeName = "datetime") => {
      const nodesWithUtcTime = document.querySelectorAll(timeNodeSelector);

    nodesWithUtcTime.forEach((nodeWithUtcTime)=>{
      const utcDate = new Date(nodeWithUtcTime.getAttribute(attributeName)),
            timeZoneName = Intl.DateTimeFormat().resolvedOptions().timeZone.replace('/', '-');
      nodeWithUtcTime.textContent = utcDate.toLocaleString() + ' ' + timeZoneName;
    })
  }
}

$(document).ready(() => {
  Attendee.utilities.init();
});
