$('.clickableRow').on("click", (e) => {
    const tr = e.currentTarget
    const trId = tr.id.split("-")[1]

    let isSelected = $(tr).hasClass( "selectedRow" )
    
    $(".selectedRow").removeClass("selectedRow")

    if (!isSelected) {
        console.log(tr.id + " is NOT selected!")
        $(tr).addClass( "selectedRow" )
    }



    console.log(trId)
})