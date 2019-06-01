Attendee.utilities = {
  init: () => {
    console.log("attendee/mainsite/static/javascripts/shared/utilities.js");
  },

  convertUTC: (nodeClass, datasetName) => {
    const nodesWithUtcTime = document.querySelectorAll(nodeClass);

    nodesWithUtcTime.forEach((nodeWithUtcTime)=>{
      const utcDate = new Date(nodeWithUtcTime.dataset[datasetName]),
            timeZoneName = Intl.DateTimeFormat().resolvedOptions().timeZone;
      nodeWithUtcTime.textContent = utcDate.toLocaleString() + ' ' + timeZoneName + ' Time';
    })
  }
}

$(document).ready(() => {
  Attendee.utilities.init();
});
