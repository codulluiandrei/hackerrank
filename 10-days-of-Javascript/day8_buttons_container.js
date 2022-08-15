window.onload = () => {
    const button5 = document.getElementById('btn5');
    button5.addEventListener('click', () => {
         let array = [
              document.getElementById('btn1').innerText,
              document.getElementById('btn2').innerText,
              document.getElementById('btn3').innerText,
              document.getElementById('btn6').innerText,
              document.getElementById('btn9').innerText,
              document.getElementById('btn8').innerText,
              document.getElementById('btn7').innerText,
              document.getElementById('btn4').innerText       
         ];
         array = [
              ...array.slice(array.length - 1), ...array.slice(0, array.length - 1)
         ];
         document.getElementById('btn1').innerText = array[0];
         document.getElementById('btn2').innerText = array[1];
         document.getElementById('btn3').innerText = array[2];
         document.getElementById('btn6').innerText = array[3];
         document.getElementById('btn9').innerText = array[4];
         document.getElementById('btn8').innerText = array[5];
         document.getElementById('btn7').innerText = array[6];
         document.getElementById('btn4').innerText = array[7];       
    });  
}