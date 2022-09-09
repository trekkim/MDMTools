$(document).ready(function(){

load_json_data('country');

function load_json_data(id, parent_id)
{
 var html_code = '';
 $.getJSON('static/DEP/json/data.json', function(data){

  html_code += '<option value="">Select '+id+'</option>';
  $.each(data, function(key, value){
   if(id == 'country')
   {
    if(value.parent_id == '0')
    {
     html_code += '<option value="'+value.id+'">'+value.name+'</option>';
    }
   }
   else
   {
    if(value.parent_id == parent_id)
    {
     html_code += '<option value="'+value.id+'">'+value.name+'</option>';
    }
   }
  });
  $('#'+id).html(html_code);
 });

}

$(document).on('change', '#country', function(){
 var country_id = $(this).val();
 if(country_id != '')
 {
  load_json_data('state', country_id);
 }
 else
 {
  $('#state').html('<option value="">Select state</option>');
  $('#city').html('<option value="">Select city</option>');
 }
});
$(document).on('change', '#state', function(){
 var state_id = $(this).val();
 if(state_id != '')
 {
  load_json_data('city', state_id);
 }
 else
 {
  $('#city').html('<option value="">Select city</option>');
 }
});
});