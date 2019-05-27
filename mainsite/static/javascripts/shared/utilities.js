Attendee.utilities = {
  init: () => {
    console.log("attendee/mainsite/static/javascripts/shared/utilities.js");
  },

  convertUTC: (nodeClass, datasetName) => {
    const nodesWithUtcTime = document.querySelectorAll(nodeClass);

    nodesWithUtcTime.forEach((nodeWithUtcTime)=>{
      const utcDate = new Date(nodeWithUtcTime.dataset[datasetName]);
      nodeWithUtcTime.textContent = utcDate.toLocaleString();
    })
  }
}

$(document).ready(() => {
  Attendee.utilities.init();
});
