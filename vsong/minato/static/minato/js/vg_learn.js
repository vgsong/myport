
$(document).ready(function() {

    $("#refreshTable").on("click", function() {

        const selectedText = $("#progDropdown").val();
        const data = JSON.parse($("#data-id").text());

        let result = ""  ;
        let wo_count = data["PRO J"].length;

        for (let i = 0; i <= wo_count; i+= 1){
            if (selectedText == data["PROG"][i]) {
                console.log(i);
                result += `<tr>
                            <td>${data["PROG"][i]}</td>
                            <td>${data["PROJ"][i]}</td>
                            <td>${data["DESC"][i]}</td>
                        </tr>`
            }
        } 

        $("#projtableResults").html(result);

    });
});
