let button1 = true;

$(function(){
    window.setInterval(function(){
        loadNewDecimal()
    }, 500) //2000 - время обновления
    //этот метод у тебя просто как обновление и он ничего не должен записывать, только читать
    function loadNewDecimal(){
        $.ajax({
            url:"/update_decimal",
            type: "POST",
            dataType: "json",
            success: function(data){
                
            }
        });
    }

    //чтобы не написывать большие строки кода на чистом js, можно использовать jquery инструменты, вот так можно реализовать событие на клик по кнопке
    //это событие запихнули во внутрь анонимной функции, так как если это не сделать, то это событие раньше инициализируется, чем прогрузится сама страница
    $('#click').click(() => {
        //твой код
        button1 =! button1;
        
        $('#click').text(`Лампа: ${button1}`);
    
        var params = {
                    list: [
                    {key: 'status', value: button1}
                    // {key: 'reg1', value: false}
                    // {key: 'reg2', value: true}
                    //         ...(n) сколько угодно
                    ]
                }
                
        setSwitch(params, (data, isErr) => {
            console.log(data, isErr)
        })
    });

});

function setSwitch(data, event) {
    $.ajax({
        url: '/switch',
        type:'POST',
        dataType:'json',
        headers: {
            'Content-Type': 'application/json'
        },
        data: JSON.stringify(data),
        success: (data) => {
            event(data, false);
        },
        error: () => {
            event(null, true);
        }
    })
}