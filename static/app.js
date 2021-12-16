

$(window).load(function () {

  
    var d = Math.random()*360+1;
    
//     $('.rotate').each(function(){
          
//          $(this).css('transform',  'rotate('+d+'deg)');

//     // $(this).css("color" , "red");
// });
var a = (Math.random()*1)+d ;
var r = (Math.random()*-2+1);
    // Run code
    setInterval(() => {
 
        $('.rotate').each(function(){
          
            a+=0.01;
            if(r>0){
                 $(this).css('transform',  'rotate('+ -a + 'deg)');
            }
            else{
                $(this).css('transform',  'rotate('+ a + 'deg)');
            }
        });
    });
});
