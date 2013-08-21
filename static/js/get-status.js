function make_element(type, opt) {
  var ele = document.createElement(type)
  for (var key in opt) {
    ele[key] = opt[key]
  }
  return ele
}

window.onload = function() {
  var xhr = new XMLHttpRequest()
  xhr.open('GET', '/status.json', true)
  xhr.responseType = 'json'
  xhr.onload = function(e) {
    if (this.status === 200) {
      var data = xhr.response
      var since = make_element('small', {
        textContent: ' (since ' + data.since + ')'
      })
      document.getElementById('header').appendChild(since)

      for (var cat in data.categories) {
        var block = make_element('div', {
          className: 'col-lg-4 col-md-4 col-sm-12 col-xs-12'
        })

        var link = make_element('a', {
          className: 'btn btn-block'
        , href: 'http://blog.wraithan.net/category/' + cat + '/'
        })

        link.appendChild(make_element('h2', {textContent: cat}))

        if (data.categories[cat]) {
          link.className += ' btn-success'
        } else {
          link.className += ' btn-failure'
        }

        block.appendChild(link)
        document.getElementById('status-display').appendChild(block)
      }
    }
  }
  xhr.send()
}
