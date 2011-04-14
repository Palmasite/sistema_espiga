/**
 * @author palmasite
 */

/**
 * @post login
 */
function logar(){
	var	user = $('#login_user').val();
	var pass = $('#login_pass').val();
	$.post('/logar', {username:user,password:pass} ,function(data) {
  		alert(data);
	});

}

