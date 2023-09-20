// import {updateTimer} from "./timer.js"

//   let btnGroups = $( ".btn-group" )
//   let pauseBtns = $( ".pause_btn")
//   let startBtns = $( ".start_btn")
//   let editBtns = $( ".edit_btn")
  
//   $(window).ready(updateBtns)
  
//   function updateBtns(){
//       console.log("updateBtns has been called")
//       $(".task_row").each((index, element)=> {
//           let elementIdParts = $(element).attr("id").split("_")
//           let elementId = elementIdParts[1]
//           console.log("task row ID:", elementId)
          
//           let taskRow = "#task_" + elementId
          
//           console.log("task row is active? ", $(taskRow).hasClass("active"))
//           if ( $(taskRow).hasClass("active") ){
//               activateBtns(elementId)
//             }
//             else {
//                 deactivateBtns(elementId)
//             }
//             updateTimer()
//     })
    
//   }
  
//   $(pauseBtns).on('click', (e) => {
//       // Split Target ID to get Task ID 
//       let taskIdParts = e.target.id.split("_")
//       let taskId = taskIdParts[2]
//       // get task row
//       let taskRow = '#task_' + taskId
      
//       // remove active class from btnGroup
//       $(taskRow).removeClass("active")
//       updateTimer()
      
//       // Hide/Show relavent buttons
//       deactivateBtns(taskId)
//   }) 
  
//   $(startBtns).on('click', (e) => {
//       // Split Target ID to get Task ID 
//       let taskIdParts = e.target.id.split("_")
//       let taskId = taskIdParts[2]
//       // Get task row
//       let taskRow = '#task_' + taskId
      
//       // add active class to task row
//       $(taskRow).addClass("active")

//       // Start timer
//       updateTimer()
      
//       // Hide/Show relavent buttons
//       activateBtns(taskId)
//   }) 
  
//   function activateBtns(id){
//     console.log("task" + id + " being activated")
//     // Instantiate relavent buttons
//     let editBtn = $( "#edit_task_" + id )
//     let startBtn = $( "#start_task_" + id )
//     let pauseBtn = $( "#pause_task_" + id )
  
//     $(editBtn).hide()
//     $(startBtn).hide()
//     $(pauseBtn).show()
//   }
  
//   function deactivateBtns(id){
//     console.log("task" + id + " being deactivated")
//     // Instantiate relavent buttons
//     let editBtn = $( "#edit_task_" + id )
//     let startBtn = $( "#start_task_" + id )
//     let pauseBtn = $( "#pause_task_" + id )
  
//     $(editBtn).show()
//     $(startBtn).show()
//     $(pauseBtn).hide()
//   }
  