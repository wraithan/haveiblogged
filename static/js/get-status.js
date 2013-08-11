var my_data = null

$(function() {
  $.getJSON('/status.json', function(data) {
    $.each(data, function(cat, blogged) {
      var block = $('<div>', {
        class: 'col-lg-4 btn'
      })
      block.append($('<h2>', {
        text: cat
      }))
      if (blogged) {
        block.addClass('btn-success')
      } else {
        block.addClass('btn-danger')
      }
      block.appendTo($('#status-display'))
    })
  })
})