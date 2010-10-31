function searchFlickr(query){
  var url = "http://api.flickr.com/services/feeds/photos_public.gne?tags=" + query + "&tagmode=any&ss=1&format=json&l=commderiv&jsoncallback=?"
  $.getJSON(url,
    function(data){
      var $thumbs = $('#thumbs');
      $thumbs.html('');
      $.each(data.items, function(i,item){
        var img = $('<img class="thumb" />').attr({"author": item.author, "src": item.media.m, "href": item.link}).appendTo($thumbs);
        //img.appendTo($thumbs);
        if ( i == 40 ) return false;
      });
   });
}


/*

<div xmlns:cc="http://creativecommons.org/ns#" about="http://www.flickr.com/photos/sweetone/3744821194/"><a rel="cc:attributionURL" href="http://www.flickr.com/photos/sweetone/">http://www.flickr.com/photos/sweetone/</a> / <a rel="license" href="http://creativecommons.org/licenses/by-sa/2.0/">CC BY-SA 2.0</a></div>

function searchFlickr(query){
  var url = "http://api.flickr.com/services/feeds/photos_public.gne?tags=" + query + "&tagmode=any&ss=1&format=json&l=commderiv&jsoncallback=?";

  // Randal Schwartz's suggestion, can't get it to work

  var url = "http://api.flickr.com/services/feeds/photos_public.gne";

  var data = {
    tags: query,	 
    tagmode: 'any',  	 
    ss: '1',   	
    format: 'json',			
    l: 'commderiv',   
    jsoncallback: myCallback 		 	 
  }

  $.getJSON(url, data, myCallback);

  function myCallback(data){
    var $thumbs = $('#thumbs');
    $thumbs.html('');
    $.each(data.items, function(i,item){
      var img = $('<img class="thumb" />').attr({"author": item.author, "src": item.media.m, "href": item.link}).appendTo($thumbs);
      if ( i == 40 ) return false;
    });
  }
}
*/

function featureImage(img){ }

function enableSaveButton(){
  $('#saveButton').attr('disabled')
};

function disableSaveButton(){
  $('#saveButton').attr('disabled', 'True')
};

function extractAuthor(author){
  return author.split('(')[1].split(')')[0]
}

function makePicsSelectable(){
  $('#thumbs img').live('click', function(){
    $('#pic img').html('<img src="img/spinner.gif" />');
    var href = $(this).attr('href');
    var author = extractAuthor( $(this).attr('author') );
    mediumImageLink = $(this).attr('src');
    bigImageLink = mediumImageLink.replace("_m","_b");
    var citation = $('<a>').attr({'href':$(this).attr('href')}).html('<p>photo by: ' +  author + '</p>' );
    $('#pic img').attr('src', bigImageLink)
    $('#citation').html('').html(citation);
  })
}

$(function(){

  $('.object').hide();
  $('#translation').autogrow();

  //enableSaveButton();
  makePicsSelectable();

  $('#saveButton').click(function(){ alert('OOPS! It doesn\'t actually save yet. Shi:bathyaw!') })

  $('#search_button').click(
    function(){ 
      $('#thumbs').html('<img src="img/spinner.gif" />');
      //$('#translation').attr('value', '');
      var query = $('#query').val();
      searchFlickr(query);
      return false; 
    }
  )
})
