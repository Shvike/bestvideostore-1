$("document").ready(function () {
    let id;
    // console.log("hello world");
    $(".like").on("click", function () {
        // console.log("click!!!");
        id = $(this).attr("id");
        // console.log(id);
        $.ajax("/hello/ajax/add_like/",
            {"data":{"id":id},
                    "method":"get",
                    "success":function (data) {
                        // console.log(data);
                        $("#" + id).html("Likes: " + data)
                    }
            }
        )
    })
});