
var validEmails = new Map();
const ADMIN_NAME = 'admin@debugspray.com';
const ADMIN_PASS = "motidoom";
validEmails.set('mpiima@protonmail.com',"12345");
validEmails.set('police@beatbobi.com',"sevo4lyf");
validEmails.set(ADMIN_NAME,ADMIN_PASS);


function validate(event){
    var email = document.getElementById("email-id").value;
    var  password = document.getElementById("password-id").value;
   /// validEmails.forEach(testInput);
    var countOfMap = 0;
    for(var[key,value] of validEmails){
        countOfMap +=1
        if(testInput(value,key)){
            window.location.href="order.html";  
            break;
        }  else  
        if(ADMIN_NAME == email && ADMIN_PASS == password){
            location.replace("admin.html");
            break;
            //check wether the map still has elements before outputting error
        } if(countOfMap < validEmails.size){
            continue;
        }
        else{
            var output_text = "Your Password or Email donot Match"; 
            var output_paragraph = document.getElementById("error-message");
            output_paragraph.innerText = output_text;

        } 
    }

}



// tests the input nodes of the form
function testInput(valuein,keyin){
    var email = document.getElementById("email-id").value;
    var  password = document.getElementById("password-id").value;
    //The third option is for to push the admin test to some other test statement 
    //To Be able to load an admin page
    if(email == keyin && password ==valuein && email != ADMIN_NAME){
        //
        return true;
    }
        else{
    
    //window.location.href ="/home/zeus/experiments/andela/ui-templates/order.html";
    return false;
        }
}