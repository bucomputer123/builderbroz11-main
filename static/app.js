

// Get Subscribers


$(window).load(function () {


    const youtubeKey ='AIzaSyBblR3HwHtr1WYUgAyFySn00gxPJ4wDXhw';
    const youtubeUser ='UCvSrWeilliH9cDUrn-CR3oQ';
    const delay = 1000; // 10 min
    const subCount = document.getElementById('subCount'); 
   
    
    
    
    let getSubscribers = () => {
    
        fetch(`https://www.googleapis.com/youtube/v3/channels?part=statistics&id=${youtubeUser}&key=${youtubeKey}`)
        .then(response => {
            return response.json()
        })
        .then(data => {
           
            //console.log(data);
            subCount.innerHTML = data["items"][0].statistics.subscriberCount;
            
        })
    
    }

        getSubscribers();

 

  
    
    
    
    var channelID = "UCvSrWeilliH9cDUrn-CR3oQ";
    var reqURL = "https://www.youtube.com/feeds/videos.xml?channel_id=";
    $.getJSON("https://api.rss2json.com/v1/api.json?rss_url=" + encodeURIComponent(reqURL)+channelID, function(data) {
       var link = data.items[0].link;
       var id = link.substr(link.indexOf("=")+1);
    $("#youtube_video").attr("src","https://youtube.com/embed/"+id + "?controls=0&showinfo=0&rel=0");
    });
    
 

  
    var d = Math.random()*360+1;
    
//     $('.rotate').each(function(){
          
//          $(this).css('transform',  'rotate('+d+'deg)');

//     // $(this).css("color" , "red");
// });
var a = (Math.random()*1)+d ;
var r = (Math.floor(Math.random()*-2+1));
    // Run code
    setInterval(() => {
 
        $('.rotate').each(function(){
          
            a+=0.01;
            if(r==0){
                 $(this).css('transform',  'rotate('+ -a + 'deg)');
            }
            else{
                $(this).css('transform',  'rotate('+ a + 'deg)');
            }
        });
    });
});

$('.rotate').hover(function(){
    $(this).addClass("pluse" , "animated");
    console.log((Math.floor(Math.random()*-2+1)));
  });