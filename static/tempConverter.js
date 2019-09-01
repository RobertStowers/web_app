$("#convertButton").click(function () {
    $.ajax("api/v1/convert/" + $("#celsiusInput").val())
        .done(function (response) {
            $("#celsiusSolutionTitle").attr("hidden", false);
            $("#celsiusSolutionValue").text(response);
        });
});

$("#celsiusInput").on('input', function () {
    $("#celsiusSolutionTitle").attr("hidden", true);
});
