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
        converted = convert(unconverted, jp_Kata); 

    $this.val(converted);  

  })

})
