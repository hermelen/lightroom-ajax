$(document).ready(function(){
  $('form.light-form').submit(function(e){
    e.preventDefault();
    var url = $(this).attr('action');
    var data = $(this).serializeArray();
    var id = $(this).attr('id');
    var i = $('div#div-'+id+' i');
    var cursor = $('div#div-'+id+' input');
    $.ajax({
      url: url,
      data: data,
      type: "POST",
      success: function(response){
        if (response.status == "1") {
          i.attr('class', 'fas fa-lightbulb yellow');
          cursor.attr("checked","checked");
        } else {
          i.attr('class', 'far fa-lightbulb');
          cursor.removeAttr('checked');
        }
      },
      error: function(response){

      }
    })
  })
})
