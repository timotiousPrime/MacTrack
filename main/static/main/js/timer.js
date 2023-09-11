// For Active Tasks:
  // Hide edit btn for
  // Show pause btn for
  // Hide start btn for all

// For Inactive Tasks:
  // Show edit btns for inactive tasks
  // Hide pause btns for inactive tasks
  // Show start btns for inactive tasks

// $(window).on('resize', () =>{
//   let actionBtns = $( "btn-group" )
//   $(actionBtns).on("click", isTaskActive())

//   function isTaskActive(){
//     console.log("isTaskActive is working")
//   }
// })

let btnGroups = $( ".btn-group" )
let pauseBtns = $( ".pause_btn")
let startBtns = $( ".start_btn")
let editBtns = $( ".edit_btn")

$(window).ready(updateBtns)

function updateBtns(){
  console.log("updateBtns has been called")
  $(".btn-group").each((index, element)=> {
    let elementIdParts = $(element).attr("id").split("_")
    let elementId = elementIdParts[1]


    if ( $(element).hasClass("active") ){
      activateBtns(elementId)
    }
    else {
      deactivateBtns(elementId)
    }
  })
  
}

$(pauseBtns).on('click', (e) => {
  // Split Target ID to get Task ID 
  let taskIdParts = e.target.id.split("_")
  let taskId = taskIdParts[2]
  // Check if task is active
  let btnGroupId = '#task_' + taskId + '_btn_group'
  let isActive = $( btnGroupId ).hasClass('active')
  
  isActive ? activateBtns(taskId) : deactivateBtns(taskId)
  
  // remove active class from btnGroup
  let btnGroup = $( "task_" + taskId + "_btn_group" )
  $(btnGroup).removeClass("active")
}) 

$(startBtns).on('click', (e) => {
  // Split Target ID to get Task ID 
  let taskIdParts = e.target.id.split("_")
  let taskId = taskIdParts[2]
  // Check if task is active
  let btnGroupId = '#task_' + taskId + '_btn_group'
  let isActive = $( btnGroupId ).hasClass('active')
  
  isActive ? deactivateBtns(taskId) : activateBtns(taskId)

  // add active class to btnGroup
  let btnGroup = $( "task_" + taskId + "_btn_group" )
  $(btnGroup).addClass("active")
}) 

function activateBtns(id){
  console.log("task" + id + " being activated")
  // Instantiate relavent buttons
  let editBtn = $( "#edit_task_" + id )
  let startBtn = $( "#start_task_" + id )
  let pauseBtn = $( "#pause_task_" + id )

  $(editBtn).hide()
  $(startBtn).hide()
  $(pauseBtn).show()
}

function deactivateBtns(id){
  console.log("task" + id + " being deactivated")
  // Instantiate relavent buttons
  let editBtn = $( "#edit_task_" + id )
  let startBtn = $( "#start_task_" + id )
  let pauseBtn = $( "#pause_task_" + id )

  $(editBtn).show()
  $(startBtn).show()
  $(pauseBtn).hide()
}
