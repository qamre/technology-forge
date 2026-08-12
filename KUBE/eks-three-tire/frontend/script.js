async function backend(){

const response = await fetch("/api");

const data = await response.text();

document.getElementById("result").innerHTML=data;

}
