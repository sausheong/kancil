
$(document).ready(function(){  
    t = 0;
    $('#send').click(function(e){
        e.preventDefault();
        var prompt = $("#prompt").val().trimEnd();
        console.log(prompt);
        if(prompt == ""){
            $("#response").text("Please ask a question.");
        }
        else{            
            function myTimer() {
                $("#response").html("<p>Waiting for response ... " + t + "s</p>");
                t++;
            }
            const myInterval = setInterval(myTimer, 1000);          
            $.ajax({
                url: "/query",
                method:"POST",
                data: JSON.stringify({input: prompt}),
                contentType:"application/json; charset=utf-8",
                dataType:"json",
                success: function(data){
                    $("#response").html("<p>" + data.response + "</p>");                    
                    $("#response").append("<small class='text-secondary'>Responded in " + t + " seconds</small>");
                    $("#source").html("<small class='text-secondary'>" + data.source + "</small>");    
                    clearInterval(myInterval);
                    t = 0;
                }
              })   
              
        }
    });     
});  

