const wheel = document.getElementById('wheel');
const spinButton = document.getElementById('spin-button');
let spinning = false;


spinButton.addEventListener('click', () => {
    if (!spinning) {
      spinning = true;
      const degrees = 3600;
      const randomDegree = Math.floor(Math.random() * 360);
  
      const totalDegrees = degrees + randomDegree;
  
      wheel.style.transition = 'transform 4s cubic-bezier(0.1, 2.7, 0.58, 1)';
      wheel.style.transform = `rotate(${totalDegrees}deg)`;
  
      setTimeout(() => {
        spinning = false;
        const selectedItem = Math.floor((360 - (totalDegrees % 360)) / 60);
        const values = ['+100', '-100', '+500', '-500', '+1000', '-1000'];
        const result = values[selectedItem];

        console.log('Значение result:', result);

        document.getElementById('result-input').value = result;

        $.ajax({
          type: 'POST',
          url: '/random/',
          data: {
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            'result': result
          },
          success: function(response) {
            console.log('Результат успешно отправлен на сервер');
          },
          error: function(error) {
            console.error('Произошла ошибка при отправке результата на сервер');
          }
        });
  
      }, 4000);
    }
  });

  
  

