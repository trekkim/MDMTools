"use strict";

$(document).ready(function() {
    $(".modular_btn").click(function(event){

        $.ajax({
            type: "POST",
            url: "/modular",
            async: true,
            data: {
                'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
                'method': $(this).attr("id")
            },
            success: function(response) {
//                $("#modal_other").css( "maxWidth", ( $( window ).width() * 0.9 | 0 ) + "px" );
//                $('#modal_other').find('.modal_other_text').text(response['output']);
//                $("#modal_other").modal({
//                    closeExisting: false
//                });
            },
            error: function(response) {
//                $("#modal_other").css( "maxWidth", ( $( window ).width() * 0.9 | 0 ) + "px" );
//                $('#modal_other').find('.modal_other_text').text(response['output']);
//                $("#modal_other").modal({
//                    closeExisting: false
//                });
            }
        });
    });

       

   




$(".sso_tw_button").click(function(e){
        event.preventDefault();
       $.ajax({
           type: "POST",
           url: "/vpp",
           async: true,
           data: {
               'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
               'sso_tw_push': "tw_push",
              'device': $(this).attr("device")
           },
           success: function(response) {
               $('#VPPModal').find('.test_test2').html("<span class='fa fa-check fa-3x checkicon'></span>");

               if (response['result'] == 'Acknowledged') {
                   $('#VPPModal').find('.uuid_info').html("<span class='fas fa-check-circle fa-fw fa-3x checkicon'></span>");
                   $('#VPPModal').find('.status_info').text(response['details']);
               } else if(response['result'] == 'Error'){
                   $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
                   $('#VPPModal').find('.status_info').text("Sorry something went working");
               } else if(response['result'] == 'Idle') {
                   $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
                   $('#VPPModal').find('.status_info').text(response['details']);
               } else {
                   $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
               }
           },
           error: function(response) {
            $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
           }
    });
   
});

$(".sso_jp_button").click(function(e){
    event.preventDefault();
   $.ajax({
       type: "POST",
       url: "/vpp",
       async: true,
       data: {
           'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
           'sso_jp_push': "jp_push",
          'device': $(this).attr("device")
       },
       success: function(response) {
           $('#VPPModal').find('.test_test2').html("<span class='fa fa-check fa-3x checkicon'></span>");

           if (response['result'] == 'Acknowledged') {
               $('#VPPModal').find('.uuid_info').html("<span class='fas fa-check-circle fa-fw fa-3x checkicon'></span>");
               $('#VPPModal').find('.status_info').text(response['details']);
           } else if(response['result'] == 'Error'){
               $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
               $('#VPPModal').find('.status_info').text("Sorry something went working");
           } else if(response['result'] == 'Idle') {
               $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
               $('#VPPModal').find('.status_info').text(response['details']);
           } else {
               $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
           }
       },
       error: function(response) {
        $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
       }
});

});

$(".sso_ph_button").click(function(e){
    event.preventDefault();
   $.ajax({
       type: "POST",
       url: "/vpp",
       async: true,
       data: {
           'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
           'sso_ph_push': "ph_push",
          'device': $(this).attr("device")
       },
       success: function(response) {
           $('#VPPModal').find('.test_test2').html("<span class='fa fa-check fa-3x checkicon'></span>");

           if (response['result'] == 'Acknowledged') {
               $('#VPPModal').find('.uuid_info').html("<span class='fas fa-check-circle fa-fw fa-3x checkicon'></span>");
               $('#VPPModal').find('.status_info').text(response['details']);
           } else if(response['result'] == 'Error'){
               $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
               $('#VPPModal').find('.status_info').text("Sorry something went working");
           } else if(response['result'] == 'Idle') {
               $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
               $('#VPPModal').find('.status_info').text(response['details']);
           } else {
               $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
           }
       },
       error: function(response) {
        $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
       }
});

});
$(".sso_us_button").click(function(e){
    event.preventDefault();
   $.ajax({
       type: "POST",
       url: "/vpp",
       async: true,
       data: {
           'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
           'sso_us_push': "us_push",
          'device': $(this).attr("device")
       },
       success: function(response) {
           $('#VPPModal').find('.test_test2').html("<span class='fa fa-check fa-3x checkicon'></span>");

           if (response['result'] == 'Acknowledged') {
               $('#VPPModal').find('.uuid_info').html("<span class='fas fa-check-circle fa-fw fa-3x checkicon'></span>");
               $('#VPPModal').find('.status_info').text(response['details']);
           } else if(response['result'] == 'Error'){
               $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
               $('#VPPModal').find('.status_info').text("Sorry something went working");
           } else if(response['result'] == 'Idle') {
               $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
               $('#VPPModal').find('.status_info').text(response['details']);
           } else {
               $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
           }
       },
       error: function(response) {
        $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
       }
});

});
$(".sso_eu_button").click(function(e){
    event.preventDefault();
   $.ajax({
       type: "POST",
       url: "/vpp",
       async: true,
       data: {
           'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
           'sso_eu_push': "eu_push",
          'device': $(this).attr("device")
       },
       success: function(response) {
           $('#VPPModal').find('.test_test2').html("<span class='fa fa-check fa-3x checkicon'></span>");

           if (response['result'] == 'Acknowledged') {
               $('#VPPModal').find('.uuid_info').html("<span class='fas fa-check-circle fa-fw fa-3x checkicon'></span>");
               $('#VPPModal').find('.status_info').text(response['details']);
           } else if(response['result'] == 'Error'){
               $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
               $('#VPPModal').find('.status_info').text("Sorry something went working");
           } else if(response['result'] == 'Idle') {
               $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
               $('#VPPModal').find('.status_info').text(response['details']);
           } else {
               $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
           }
       },
       error: function(response) {
        $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
       }
});

});

$(".push_default").click(function(e){
    event.preventDefault();
   $.ajax({
       type: "POST",
       url: "/vpp",
       async: true,
       data: {
           'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
           'default': "default2",
          'device': $(this).attr("device")
       },
       success: function(response) {
           $('#VPPModal').find('.test_test2').html("<span class='fa fa-check fa-3x checkicon'></span>");

           if (response['result'] == 'Acknowledged') {
               $('#VPPModal').find('.uuid_info').html("<span class='fas fa-check-circle fa-fw fa-3x checkicon'></span>");
               $('#VPPModal').find('.status_info').text(response['details']);
           } else if(response['result'] == 'Error'){
               $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
               $('#VPPModal').find('.status_info').text("Sorry something went working");
           } else if(response['result'] == 'Idle') {
               $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
               $('#VPPModal').find('.status_info').text(response['details']);
           } else {
               $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
           }
       },
       error: function(response) {
        $('#VPPModal').find('.uuid_info').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
       }
});

});


});
