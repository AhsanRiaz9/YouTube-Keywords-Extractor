function isValidYoutubeURL(url) {
  let patterns = [
    "https://youtu.be/",
    "youtu.be/",
    "https://www.youtube.com/watch?v=",
    "youtube.com/watch?v=",
  ];
  for (let i = 0; i < patterns.length; i++) {
    if (url.indexOf(patterns[i]) == 0) {
      // alert("Correct URL");
      return true;
    }
  }
  // alert("Invalid URL");
  return false;
}
$(document).ready(function () {
  $("#copy-tags").click(function () {
    const area = $("#video-keywords");
    area.select();
    document.execCommand("copy");
    $(".copy-status").css("display", "block");
  });
  $("#searchTags").click(function () {
    let url = $("#video-url").val();
    let flag = isValidYoutubeURL(url);
    if (flag == false) {
      alert("Invalid YouTube URL");
      return;
    }
    // Using AJAX to get tags
    $.ajax({
      type: "POST",
      url: "/getYoutubeVideoTags",
      data: JSON.stringify({ url: url }),
      dataType: "json",
      async: true,
      beforeSend: function (xhr) {
        if (xhr && xhr.overrideMimeType) {
          xhr.overrideMimeType("application/json;charset=utf-8");
        }
      },
      dataType: "json",
      success: function (data) {
        //Do stuff with the JSON data
        if (data["tagList"].length == 0) {
          alert("No Result Found");
          return;
        }
        // console.log(data['tagList']);
        keyWords = "";
        tagList = data["tagList"];
        tags = "";
        for (let i = 0; i < tagList.length; i++) {
          keyWords =
            keyWords +
            `<a target="_blank" href="https://www.youtube.com/results?search_query=${tagList[i]}>" <button class="btn btn-danger mx-2 my-2">${tagList[i]}</button> </a> `;
          tags = tags + tagList[i];
          if (i != tagList.length - 1) {
            tags = tags + ",";
          }
        }
        // {#console.log(keyWords)#}
        document.getElementById("keywordsBtn").innerHTML = keyWords;
        // {#alert(tags);#}
        document.getElementById("keywordsBtn").innerHTML;
        $("#video-keywords").val(tags);
      },
    });
  });
});
