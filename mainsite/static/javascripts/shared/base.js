(($, Attendee) => {
  if (typeof Attendee === 'undefined') window.Attendee = {};
  console.log("attendee/mainsite/static/javascripts/base.js");
  document.cookie = 'timezone=' + encodeURIComponent(jstz.determine().name()) + '; path=/';
})(window.jQuery, window.Attendee); // https://stackoverflow.com/a/18315393
