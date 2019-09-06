$("#condButton").click(function () {
    $.ajax("api/v1/conductivity/" + $("#tempInput").val())
        .done(function (response) {
            $("#AirCondTitle").attr("hidden", false);
            $("#AirCondValue").text(response);
        });
});

$("#tempInput").on('input', function () {
    $("#AirCondTitle").attr("hidden", false);
});