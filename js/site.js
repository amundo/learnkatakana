
function searchFlickr(query){
  var $thumbs = $('#thumbs');
  var url = "http://api.flickr.com/services/feeds/photos_public.gne?tags=" + query + "&tagmode=any&ss=1&format=json&l=commderiv&jsoncallback=?"
  var url = "http://api.flickr.com/services/feeds/photos_public.gne?tags=" + query + "&tagmode=any&ss=1&format=json&jsoncallback=?"
  $.getJSON(url,
    function(data){
      $thumbs.html("<h2>\u3010" + query + "\u3011</h2>");
      if(data.items.length == 0) { $thumbs.html('<h1>Sorry, no pics for <br>\u3010' + query + '\u3011. <br/>:(</h1>')} 
      $.each(data.items, function(i,item){
        var img = $('<img class="thumb" />').attr({"author": item.author, "src": item.media.m, "href": item.link}).appendTo($thumbs);
        //img.appendTo($thumbs);
        if ( i == 40 ) return false;
      });
   });

}




$(function(){

  function convert(text, rules){

    $.each(rules, function(i, rule){
     var before = rule[0],
         after =  rule[1];
     text = text.replace(before, after); 
    });

    return text;
  }

  $('input').keyup(function(e){

    $this = $(this);

    var unconverted = $this.val(),
        converted = convert(unconverted, ja_Kana); 

    $this.val(converted);  

  })

  $('ol#level').shuffle();
  $('<div/>', { 'id': 'thumbs', }).css({'float':'right','width' : '40%'}).appendTo('body');
  $('ol#level').delegate('li', 'click', function(ev){
   var query = $(this).text();
   searchFlickr(query); 
   ev.preventDefault();
   });

})
