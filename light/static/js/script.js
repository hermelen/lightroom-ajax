$(document).ready(function(){
  $('div.toggle-group').click(function(){
    parentDiv = $(this).parents('div.single-light-div');
    closeParentDiv = parentDiv.find('div.toggle');
    optionOn  = parentDiv.find('select option:nth-child(1)');
    optionOff = parentDiv.find('select option:nth-child(2)');
    if (closeParentDiv.hasClass('off')) {
      console.log('off->on');
      optionOff.attr("selected","selected");
      optionOn.removeAttr('selected');
    } else {
      console.log('on->off');
      optionOff.removeAttr('selected');
      optionOn.attr("selected","selected");
    }
  })
})
