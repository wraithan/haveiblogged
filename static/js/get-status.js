var my_data = null

$(function() {
  $.getJSON('/status.json', function(data) {
    $('#header').append($('<small>', {text: ' (since ' + data.since + ')'}))
    $.each(data.categories, function(cat, blogged) {
      var block = $('<div>', {
        class: 'col-lg-4 col-md-4 col-sm-12 col-xs-12'
      })
      var link = $('<a>', {
        href: 'http://blog.wraithan.net/category/' + cat + '/'
      , class: 'btn btn-block'
      }).append($('<h2>', {
        text: cat
      }))
      block.append(link)
      if (blogged) {
        link.addClass('btn-success')
      } else {
        link.addClass('btn-danger')
      }
      block.appendTo($('#status-display'))
    })
  })
})