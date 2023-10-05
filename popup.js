document.addEventListener('DOMContentLoaded', function() {
  
    const sendDataBtn = document.getElementById('sendDataBtn');
    const outputDiv = document.getElementById('output');
    const inp = document.getElementById('myInput')
    const loader = document.getElementById('loader');
    const inpHide = document.getElementById('inp--hide');
    const ans = document.getElementById('h3')


    sendDataBtn.addEventListener('click', function() {
      // Send data to the local server
      const userInp = inp.value;
      const xhr = new XMLHttpRequest();
      xhr.open('POST', 'http://localhost:8000', true);
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
          const response = JSON.parse(xhr.responseText);
          ans.textContent = response.output;
          if(ans.textContent.trim() == 'Positive'){
            ans.classList.add('positive');
            ans.classList.remove('negative');
        }
        else{
            ans.classList.add('negative');
            ans.classList.remove('positive');
          }
        }
      };
      const data = {
        message: userInp
      };
      xhr.send(JSON.stringify(data));

      inpHide.classList.add('hidden');
      sendDataBtn.classList.add('hidden');
      loader.classList.remove('hidden');

      setTimeout(function() {
        loader.classList.add('hidden');
        outputDiv.classList.remove('hidden');
      }, 2000);

      setTimeout(function() {
        outputDiv.classList.add('hidden');
        inpHide.classList.remove('hidden');
        sendDataBtn.classList.remove('hidden');
      }, 7000);
    });
  });
  