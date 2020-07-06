
$(document).ready( function () {
    $('#myTable1').DataTable();
    
    });
    
// No conflict for WordPress
var $j = jQuery.noConflict();

$j( function() {
	$j( ".date-picker-min" ).datepicker({
	  dateFormat: "yy-mm-dd"
	});
	$j( ".date-picker-max" ).datepicker({
	  dateFormat: "yy-mm-dd"
	});
});

 