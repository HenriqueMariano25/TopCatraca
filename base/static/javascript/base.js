// $("#formulario_excel").submit(function (event){
//
//     let data_inicial = $('#data_inicial').val()
//     let data_final = $('#data_final').val()
//     let hora_inicial = $('#hora_inicial').val()
//     let hora_final = $('#hora_final').val()
//     let csrf = $('[name=csrfmiddlewaretoken]').val()
//     if(1 === 1){
//         $.ajax({
//             url: 'relatorio/geral',
//             method: 'post',
//             dataType: 'json',
//             data: {
//                 'data_inicial':data_inicial,
//                 'data_final':data_final,
//                 'hora_inicial':hora_inicial,
//                 'hora_final':hora_final,
//                 'csrfmiddlewaretoken': csrf,
//             },
//             success: function (data){
//                 alert(data)
//             }
//         })
//     }else{
//       alert("Erro")
//     }
// })
$('#formulario_contagem').submit(function (event) {
    event.preventDefault()
    let data = $('#data').val()
    let hora_inicial = $('#hora_inicial_ref').val()
    let hora_final = $('#hora_final_ref').val()
    if (1 === 1) {
        $.ajax({
            url: 'contagem/refeitorio',
            method: 'get',
            dataType: 'json',
            data: {
                'data': data,
                'hora_inicial': hora_inicial,
                'hora_final': hora_final,
            },
            success: function (data) {
                $("#table_refeitorio tbody").children().remove();

                var tbody = document.querySelector('#table_refeitorio tbody');
                var trlinha = document.createElement("tr")
                var tddata = document.createElement("td")
                var tdhora = document.createElement("td")
                var tdrefeitorio1 = document.createElement("td")
                var tdrefeitorio2 = document.createElement("td")

                tddata.textContent = data['data']
                tdhora.textContent = data['horas']
                tdrefeitorio1.textContent = data['refeitorio_1']
                tdrefeitorio2.textContent = data['refeitorio_2']

                trlinha.appendChild(tddata);
                trlinha.appendChild(tdhora);
                trlinha.appendChild(tdrefeitorio1);
                trlinha.appendChild(tdrefeitorio2);

                tbody.appendChild(trlinha);
            }
        })
    } else {
        alert("Erro")
    }
})