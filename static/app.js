const cors = require("cors")
app.use(cors({
    origin:'http://127.0.0.1:8000', 
     methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type'],
  credentials: true
}))


// var settings = {
//     "url": "https://api.twitter.com/2/users/1471330955637837826/tweets",
//     "method": "GET",
//     "timeout": 0,
//     "headers": {
//       "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAF%2BpXAEAAAAA%2F%2BdZ5p4EyPY5vUBRNYNwcfP7WcA%3DmGYtD5dumYaoOD4K1eM7San4B3GCJ5gg6CANz6YflrQAN1k4tZ",
//       "Cookie": "guest_id=v1%3A163982968721781484; guest_id_ads=v1%3A163982968721781484; guest_id_marketing=v1%3A163982968721781484; personalization_id=\"v1_BYscqoAV+ygfTMR4hLC+Cw==\""
//     },
//   };
  
//   $.ajax(settings).done(function (response) {
//     console.log(response);
//   });




$(window).load(function () {








    const youtubeKey ='AIzaSyBblR3HwHtr1WYUgAyFySn00gxPJ4wDXhw';
    const youtubeUser ='UCvSrWeilliH9cDUrn-CR3oQ';
    const delay = 100000; // 10 min
    const subCount = document.getElementById('subCount'); 
   
    
    $('.rotate').hover(function () 
    {
        console.log("in");
    } , function () {
        console.log("out");
    })

    
    
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
    setInterval(() => {
        // getSubscribers();
    }, delay);
        

 

  
    
    
    
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