$("#SolveButton").click(function () {
    $.ajax("api/v1/solve1d/" + $("#Material1Input").val() + "_" + $("#Material1tkInput").val() + "_" + $("#hsTempInput").val() + "_" + $("#hsHInput").val() + "_" + $("#csTempInput").val() + "_" + $("#csHInput").val())
        .done(function (response) {
            $("SolveTitle").attr("hidden", false);
            $("#SolveValue").text(response);
        });
});

