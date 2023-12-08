$('.clickableRow').on("click", (e) => {
    const tr = e.currentTarget
    // const trId = tr.id.split("-")[1]

    let isSelected = $(tr).hasClass( "selectedRow" )
    
    $(".selectedRow").removeClass("selectedRow bg-info")

    if (!isSelected) {
        $(tr).addClass( "selectedRow bg-info" )
    }
})