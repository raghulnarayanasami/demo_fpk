$(document).ready(function() 
{ 
    $("#tcsCostArea").hide();
    $("#computeArea").hide();
    $('input[type="checkbox"]').click(function() { 
        var inputValue = $(this).attr("value"); 
        $("." + inputValue).toggle(); 
    }); 

    $('#checkid').click(function() {
    var checked = this.checked;
        $('input[type="checkbox"]').each(function() {
        this.checked = checked;
        });
    })

    
    $("#tcsCostDiv").click(function(){
    
        $("#tcsCostArea").show();
        $("#computeArea").hide();

    });

    $("#computeDiv").click(function(){
    
        $("#tcsCostArea").hide();
        $("#computeArea").show();
    });

    $(".rotate-icon").click(function(){
        $(this).toggleClass("ternright");
    })


}); 

