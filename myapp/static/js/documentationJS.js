$(document).ready(function() {
    var url = window.location.href;
    console.log(url)
     var activeTab = url.substring(url.indexOf("#") + 1);
     console.log(activeTab);
      $(".tab-pane").removeClass("active in");
    //   $("#" + activeTab).addClass("active in");
});