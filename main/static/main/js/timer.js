$(window).on('resize', updateBtns)
    document.body.addEventListener('htmx:afterOnLoad', updateBtns)
    // Handle start/pause button changes
    let startBtns = $(".start_btn")
    let pauseBtns = $(".pause_btn")
    let btnGroups = $(".btn-group")
  
    function updateBtns(){
      console.log("this is working!pppppppp!!!!!!")
      console.log("Script running from static folder in main")
      $(btnGroups).each((index, ele) => {
      let taskId = ele.id.split("_")[1]
      let startBtn = $("#start_task_" + taskId)
      let pauseBtn = $("#pause_task_" + taskId)
      let editBtn = $("#edit_task_" + taskId)
  
      if ($(ele).hasClass("active")) {
        startBtn.hide()
        pauseBtn.show()
        editBtn.hide()
      } else {
        startBtn.show()
        pauseBtn.hide()
      }
    })
    }
    $(btnGroups).each((index, ele) => {
      let taskId = ele.id.split("_")[1]
      let startBtn = $("#start_task_" + taskId)
      let pauseBtn = $("#pause_task_" + taskId)
      let editBtn = $("#edit_task_" + taskId)
  
      if ($(ele).hasClass("active")) {
        startBtn.hide()
        pauseBtn.show()
        editBtn.hide()
      } else {
        startBtn.show()
        pauseBtn.hide()
      }
    })
  
    startBtns.each((index, ele) => {
      $(ele).click((e)=> {
        let taskId = e.target.id.split("_")[2]
        let editBtn = $("#edit_task_" + taskId)
        let startBtn = $("#start_task_" + taskId)
        let pauseBtn = $("#pause_task_" + taskId)
  
        $(startBtn).hide()
        $(editBtn).hide()
        $(pauseBtn).show()
      })
    })
    
    pauseBtns.each((index, ele)=> {
      $(ele).click((e) => {
        let taskId = e.target.id.split("_")[2]
        let editBtn = $("#edit_task_" + taskId)
        let startBtn = $("#start_task_" + taskId)
        let pauseBtn = $("#pause_task_" + taskId)
  
        $(startBtn).show()
        $(editBtn).show()
        $(pauseBtn).hide()
      })
    })