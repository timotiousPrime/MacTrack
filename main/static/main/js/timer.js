// // const timers = {}

// // function updateTimer(){
  
// //   let taskRows = $( ".task_row" )

// //   taskRows.each((index, element) => {
// //     // Instantiate task row variables
// //     let seconds = 0
// //     // Get active task Row Id
// //     let elementIdParts = $(element).attr("id").split("_")
// //     let taskId = elementIdParts[1]

// //     if ($(element).hasClass('active')){
// //       console.log("this element has ACTIVE class", $(element))
// //       let elementIdParts = $(element).attr("id").split("_")
// //       let taskId = elementIdParts[1]
// //       console.log("Task Row ID " + taskId + " is active")
  
// //       // Get Accumalated Time for task
// //       let elapsed_time_ele = $( "#elapsed_time_" + taskId)
// //       let elapsed_time_value = $( elapsed_time_ele ).text().trim()
// //       let timeParts = elapsed_time_value.split(":")
// //       seconds += ((+timeParts[0]*60*60)+(+timeParts[1]*60)+(+timeParts[2]))
  
// //       // Instantiate Timer
// //       timers[taskId] = setInterval(() =>{
// //         seconds++
// //         let date = new Date(null)
// //         date.setSeconds(seconds)
// //         let timeStr = date.toISOString().substring(11,11+8)
// //         $(elapsed_time_ele).text(timeStr)
// //         }, 1000)
// //     } else {
// //       // Pause timer
// //       clearInterval(timers[taskId])
// //     }
// //   })
// // }

// // $(document).ready(() => {
// //   updateTimer();

// //   // Clicking the start button should trigger the timer update
// //   $(".start_btn").on("click", () => {
// //     setTimeout(updateTimer, 100); // Delay to ensure the DOM updates
// //   });
// // });

// // $(window).ready(updateTimer)

// // let startBtns = $( ".start_btn" )
// // $(startBtns).on("click", updateTimer)


// // ###################### New code ###################### //

// const localStorageKey = 'taskTimers'
// // Create a list of all the task timers running
// let timers = {}

// // Example of a task timer
// // taskTimer: {taskId: taskId, elapsedTime: task.elapsedTime, startTime: date.time}

// function getTimerInfo(element){
//   // Task Id
//   let taskId = $(element).attr("id").split("_")[2]
//   // Task elapsedTime
//   let elapsedTime = $('#elapsed_time_'+taskId).text().trim()
//   // Time start btn was clicked
//   let startTime = new Date()

//   return {"taskId": taskId, "elapsedTime": elapsedTime, "startTime":startTime}
// }

// function getUpdatedTime(taskId){
//   // Get taskTimer with passed taskId from localStorage
//   const taskTimer = localStorage.getItem(localStorageKey)[taskId]
//   console.log("existing taskTimer: ")
//   console.log(taskTimer)
//   // Get time delta between when the task was added to LocalStorage and now
//   const now = new Date()
//   const deltaTime = now - new Date(taskTimer.startTime)
//   console.log("delta time: ", deltaTime)

//   return deltaTime
// }

// function getAccumalatedTime(elapsedTime){
//   const timeParts = elapsedTime.split(":")
//   const seconds = ((+timeParts[0]*60*60)+(+timeParts[1]*60)+(+timeParts[2]))
//   return seconds
// }

// function updateTime(element) {
//   const taskTimer = getTimerInfo(element)
//   timers[taskTimer.taskId] = taskTimer

//   // Store the updated task Timers object in localStorage
//   // localStorage.setItem(localStorageKey, timers)

//   const updatedTime = getUpdatedTime(taskTimer.taskId)
//   console.log(updatedTime)

//   let seconds = getAccumalatedTime(taskTimer.elapsedTime)

//   setInterval(() =>{
//     seconds++
//     let date = new Date(null)
//     date.setSeconds(seconds)
//     let timeStr = date.toISOString().substring(11,11+8)
//     $("#elapsed_time_"+taskTimer.taskId).text(timeStr)
//     }, 1000)
// }

// // // Initialize Local Storage
// // if (JSON.parse(localStorage.getItem(localStorageKey)) == {}) {
// //   localStorage.setItem(localStorageKey, JSON.stringify(timers))
// // } else {
// //   timers = JSON.parse(localStorage.getItem(localStorageKey))
// // }

// $(document).ready(() => {

//   // Check if there are any tasks in local storage
//   if (localStorage.getItem(localStorageKey)) {
//     console.log("Existing local storage on page ready: ")
//     console.log(localStorage.getItem(localStorageKey))

//   } else {
//     localStorage.setItem(localStorageKey, timers)
//     console.log("New local storage created:")
//     console.log(localStorage.getItem(localStorageKey))
//   }

//   // Clicking the start button should trigger the timer update
//   $(document).on("click", ".start_btn", (e) => {
//     setTimeout(() => {
//       updateTime(e.target)
//     }, 100); // Delay to ensure the DOM updates
//   });

//   $(document).on("click", ".pause_btn", (e) => {
//     const taskTimer = getTimerInfo(e.target)
//     const taskId = taskTimer.taskId

//     // clear the interval timer to stop the clock counting
//     clearInterval(timers[taskId])

//     // Remove timers for timers object
//     delete timers[taskId]

//     // Store the updated task Timers object in localStorage
//     // localStorage.setItem(localStorageKey, JSON.stringify(timers))
//   })
// });


// // Assuming you passed running_task to your JavaScript context
// var runningTask = {{ running_task|default:"null"|safe }};

// if (runningTask === null) {
//     // Handle the case where running_task is null (None in Django)
//     console.log("No running task.");
// } else {
//     // Handle the case where running_task has a value
//     console.log("Running task: " + runningTask);
// }

// if (!timers){
//   const timers = {}
// } else {
//   console.log(timers)
// }



// $(document).ready(() => {
//   let taskTimeData = JSON.parse(document.getElementById("running_task").textContent) 
//   console.log(taskTimeData)

//   if (taskTimeData) {
//     let taskId = taskTimeData.id
//     let time_started = taskTimeData.time_started 
//     let elapsed_time = taskTimeData.elapsed_time
    
//     let now = new Date()
    
//     console.log("taskId", taskId);
//     console.log("time_started", time_started);
//     console.log("elapsed_time", elapsed_time);
    
//     let ts = new Date(time_started)
    
//     let seconds = (Math.floor((now - ts) / 1000)) + elapsed_time
    
//     console.log("timedelta: ", seconds)
  
//     timers[taskId] = setInterval(() =>{
//     seconds++
//     let date = new Date(null)
//     date.setSeconds(seconds)
//     let timeStr = date.toISOString().substring(11,11+8)
//     $("#elapsed_time_"+taskId).text(timeStr)
//     }, 1000)
    
//   }
  
// ***************** FIX THIS!!! *****************
//     $(document).on("click", ".pause_btn", () => {
  //       // clear the interval timer to stop the clock counting
  //       console.log($(".pause_btn"))
  //       // clearInterval(tictoc)
  //     })
  // })
  
  // WIP

  // $(document).ready(() => {
  //   if (!timers) {
  //     const timers = null
    

  //   // Clear / Set timers
  //   if (timers){
  //     clearInterval(timers["timer"])
  //   } else {
  //     timers["timer"] = null
  //   }
  //   console.log("Task Timer page is ready")
    
  //   let tasksData = JSON.parse(document.getElementById("running_task").textContent) 
 
  // for (task in tasksData) {
  //   console.log("Task: ", task, tasksData[task]['elapsed_time'])
  //   if (tasksData[task]["is_running"]){

  //     // Get existing elapsed Time
  //     // Recieve elapsed time in seconds
  //     let elapsed_seconds = tasksData[task]['elapsed_time']

  //     // Get time started
  //     let startDate = new Date(tasksData[task]["time_started"])
  //     let now = new Date()
  //     let seconds = (Math.floor((now - startDate) / 1000))
  //     console.log("Seconds since started: ", seconds)

  //     // Add Existing elapsed time to time from time started for TotalTime
  //     total_seconds = elapsed_seconds + seconds
  //     // Get hours, minutes and seconds
  //     hours = Math.floor(total_seconds / 3600)
  //     minutes = Math.floor((total_seconds / 60) % 60)
  //     seconds = Math.floor(total_seconds % 60)
  //     console.log(hours, minutes, seconds)
  //     // Display total time
  //     display_time = hours + ":" + minutes + ":" + seconds 

  //     if (timers["timer"] !== null){
  //       clearInterval(timers["timer"])
  //     }

  //     timers["timer"] = setInterval(() => {
  //       seconds++
  //       if (seconds == 60){
  //         seconds = 0
  //         minutes++
  //         if (minutes == 60) {
  //           minutes = 0
  //           hours++
  //         }  
  //       }
  //       console.log(hours, minutes, seconds)
  //     }, 1000)            
  //   }
  //   }
  // }

  // Get local Storage


  // Get tasks 

  // let taskRows = $(".task_row")

  // $(".pause_btn").click(() => {
  //   let btnId = $(".pause_btn").prop("id")
  //   let taskId = btnId.split("_")[2] 

  //   console.log("Pause Button Clicked: ", btnId)

  //   console.log(taskId)

  //   clearInterval(timers["timer"])

  // })
// })

$(document).ready(() => {
  console.log("Page has loaded")

  // Check for running tasks
  let tasksData = JSON.parse(document.getElementById("running_task").textContent) 
  
  // Check for when start btn is clicked
  $(".start_btn").on("click", (e)=> {
    // I dont know why this only works when I dont declare "timer", but it works 
    clearInterval(timer)
  })


  for (task in tasksData){

    if (tasksData[task]["is_running"]){
      let taskId = task

      // Get existing elapsed Time
      // Recieve elapsed time in seconds
      let elapsed_seconds = tasksData[task]['elapsed_time']

      // Get time started
      let startDate = new Date(tasksData[task]["time_started"])
      let now = new Date()
      let seconds = (Math.floor((now - startDate) / 1000))

      // Add Existing elapsed time to time from time started for TotalTime
      let total_seconds = elapsed_seconds + seconds
      // Get hours, minutes and seconds
      let hours = Math.floor(total_seconds / 3600)
      let minutes = Math.floor((total_seconds / 60) % 60)
      seconds = Math.floor(total_seconds % 60)
      
      // I dont know why this only works when I dont declare "timer", but it works 
      timer = setInterval(() => {
        seconds++
        if (seconds == 60){
          seconds = 0
          minutes++
          if (minutes == 60) {
            minutes = 0
            hours++
          }  
        }

        let displayMin = ""
        let displaySec = ""

        if (minutes < 10){
          displayMin = `${0}${minutes}`
        }
        else {
          displayMin = minutes
        }

        if (seconds < 10){
          displaySec = `${0}${seconds}`
        }
        else {
          displaySec = seconds
        }

        let elapsedTimeId = "#elapsed_time_" + taskId
        $(elapsedTimeId).text(hours + ":" + displayMin + ":" + displaySec)
        // $("#elapsed_time_" + tasksData[task]["id"]).text(hours + ":" + minutes + ":" + seconds)
        }, 1000) 
        localStorage.setItem("timer", timer)
    }
 }


// Check for when pause btn is clicked
  $(".pause_btn").on("click", (e)=> {
    clearInterval(timer)
  })
})
