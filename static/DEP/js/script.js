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

    $("#apply_button").click(function(e){
        $.ajax({
            type: "POST",
            url: "/apply",
            async: true,
            data: {
                'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val()
            },
            success: function(response) {
               

                if (response['result'] == 'Success') {
                    $('#exampleModalApply').find('.text_apply').html("<span class='fa fa-check fa-3x checkicon'></span>");
                    $('#exampleModalApply').find('.text_apply2').text(response['details']);
                } else if(response['result'] == 'Error'){
                    $('#exampleModalApply').find('.text_apply').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
                    $('#exampleModalApply').find('.text_apply2').text(response['details']);
                } else if(response['result'] == 'Questionable') {
                    $('#exampleModalApply').find('.text_apply').html("<span class='fa fa-question fa-3x questionicon'></span>");
                    $('#exampleModalApply').find('.text_apply2').text(response['details']);
                } else {
                    $('#exampleModalApply').find('.text_apply').html("<span class='fa fa-question fa-3x questionicon'></span>");
                    $('#exampleModalApply').find('.text_apply2').text(response['details']);
                }

                
            },
            error: function(response) {
                $('#exampleModalApply').find('.modal_status_text').text('Error');
                $('#exampleModalApply').find('.modal_output_text').text('Likely connection issues or bad server response');
                $('#exampleModalApply').find('.modal_additional_text').text('');
                $('#exampleModalApply').find('.graphic_result').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
                $("#exampleModalApply").modal({
                    closeExisting: false
                });

            }
        });
    });

   
    $("#add_button").click(function(e){
        $.ajax({
            type: "POST",
            url: "/add",
            async: true,
            data: {
                'id': $('#serial_number')[0].value,
                'tlacitkoregionu': $('#tlacitko').serialize(),
                'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val()

            },
            success: function(response) {
                $('#exampleModal2').find('.test_test2').html("<span class='fa fa-check fa-3x checkicon'></span>");

                if (response['result'] == 'Success') {
                    $('#exampleModal2').find('.text_add').html("<span class='fa fa-check fa-3x checkicon'></span>");
                    $('#exampleModal2').find('.text_add2').text("Success");
                } else if(response['result'] == 'Error'){
                    $('#exampleModal2').find('.text_add').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
                    $('#exampleModal2').find('.text_add2').text(response['details']);
                } else if(response['result'] == 'Questionable') {
                    $('#exampleModal2').find('.text_add').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
                    $('#exampleModal2').find('.text_add2').text(response['details']);
                } else {
                    $('#exampleModal2').find('.text_add').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
                }
            },
            error: function(response) {
             $('#exampleModal2').find('.text_add').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
            }
        });
    });
    
    // $("#testuji").on('change', function (e) {

    //     $.ajax({
    //         type: "POST",
    //         url: "/add",
    //         async: true,
    //         data: { 
    //             'tlacitkoregionu': $('#tlacitko').serialize(), 
    //             'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
    //         },
    //         success: function (response) { }
    //     });

    // });

    $("#remove_button").click(function(e){
        $.ajax({
            type: "POST",
            url: "/remove",
            async: true,
            data: {
                'id': $('#serial_number')[0].value,
                'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val()
            },
            success: function(response) {
                
                    $('#exampleModal').find('.test_test').html("<span class='fa fa-check fa-3x checkicon'></span>");

                if (response['result'] == 'Success') {
                    $('#exampleModal').find('.text_remove').html("<span class='fa fa-check fa-3x checkicon'></span>");
                    $('#exampleModal').find('.text_remove2').text("Device removed");
                } else if(response['result'] == 'Error'){
                    $('#exampleModal').find('.text_remove').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
                    $('#exampleModal').find('.text_remove2').text("Device not found");
                } else if(response['result'] == 'Empty') {
                    $('#exampleModal').find('.text_remove').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
                    $('#exampleModal').find('.text_remove2').text("Device not found");
                } else {
                    $('#exampleModal').find('.text_remove').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
                    $('#exampleModal').find('.text_remove2').text("Device not found");
                }

            },
            error: function(response) {
                    $('#exampleModal').find('.text_remove').html("<span class='fa fa-exclamation fa-3x exclamationicon'></span>");
            }
        });
    });


    $("#get_json_form").submit(function(event) {
        event.preventDefault();
        $.ajax({
            type: "GET",
            url: "/get_json",
            async: true,
            success: function(response) {
                $('#modal_json').find('.modal_json_text').text(JSON.stringify(response, undefined, 2));
                $("#modal_json").modal({
                    closeExisting: false
                });
            },
            error: function(response) {
                $('#modal_json').find('.modal_json_text').text('Error');
                $("#modal_json").modal({
                    closeExisting: false
                });
            }
        });
    });

$(".sync_button").click(function(e){
         event.preventDefault();
        $.ajax({
            type: "POST",
            url: "/api_command",
            async: true,
            data: {
                'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
                'action_sync': 'sync_dev'
            }
        });
    });

$(".restart_button").click(function(e){
         event.preventDefault();
        $.ajax({
            type: "POST",
            url: "/vpp",
            async: true,
            data: {
               'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
               'action_re': "restart", 
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


$(".push_update").click(function(e){
        event.preventDefault();
       $.ajax({
           type: "POST",
           url: "/vpp",
           async: true,
           data: {
               'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
               'action_up': "update",
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

$(".install_profile").click(function(e){
    event.preventDefault();
   $.ajax({
       type: "POST",
       url: "/vpp",
       async: true,
       data: {
           'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
           'action_pro': "profile",
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

$(".remove_profile").click(function(e){
    event.preventDefault();
   $.ajax({
       type: "POST",
       url: "/vpp",
       async: true,
       data: {
           'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
           'action_rempro': "remove-profile",
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

$(".update_enroll_profile").click(function(e){
    event.preventDefault();
   $.ajax({
       type: "POST",
       url: "/vpp",
       async: true,
       data: {
           'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
           'action_en_pro': "enroll_profile",
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

$(".erase_device").click(function(e){
    event.preventDefault();
   $.ajax({
       type: "POST",
       url: "/vpp",
       async: true,
       data: {
           'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
           'action_del': "erase",
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

$(".remove_app").click(function(e){
    event.preventDefault();
   $.ajax({
       type: "POST",
       url: "/vpp",
       async: true,
       data: {
           'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
           'remove_app': "remove_application",
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
        } else if(response['result'] == 'Remove') {
            $('#VPPModal').find('.uuid_info').html("<span class='fas fa-check-circle fa-3x exclamationicon'></span>");
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



$(".push_app").click(function(e){
        //$(this).toggleClass("active"); //if you wanna have info about pressed button
        e.preventDefault();
       $.ajax({
           type: "POST",
           url: "/vpp",
           async: true,
           data: {
           'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
           'action': "push",
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
 

$(".lock_button").click(function(e){
    event.preventDefault();
   $.ajax({
       type: "POST",
       url: "/vpp",
       async: true,
       data: {
           'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
           'action_lck': "lock",
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




$(".push_notification").click(function(e){
    event.preventDefault();
   $.ajax({
       type: "POST",
       url: "/vpp",
       async: true,
       data: {
           'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
           'action_not': "notify",
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

