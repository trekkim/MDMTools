"use strict";

$(document).ready(function() {
        $("#restart_device").click(function(e){
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/vpp",
            async: true,
            data: {
                'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val()
       },
   });
   
});    

});
