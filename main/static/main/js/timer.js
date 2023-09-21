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

const timers = {}


$(document).ready(() => {
  let taskTimeData = JSON.parse(document.getElementById("running_task").textContent) 
  console.log(taskTimeData)

  if (taskTimeData) {
    let taskId = taskTimeData.id
    let time_started = taskTimeData.time_started 
    let elapsed_time = taskTimeData.elapsed_time
    
    let now = new Date()
    
    console.log("taskId", taskId);
    console.log("time_started", time_started);
    console.log("elapsed_time", elapsed_time);
    
    let ts = new Date(time_started)
    
    let seconds = (Math.floor((now - ts) / 1000)) + elapsed_time
    
    console.log("timedelta: ", seconds)
  
    timers[taskId] = setInterval(() =>{
    seconds++
    let date = new Date(null)
    date.setSeconds(seconds)
    let timeStr = date.toISOString().substring(11,11+8)
    $("#elapsed_time_"+taskId).text(timeStr)
    }, 1000)
    
  }

    $(document).on("click", ".pause_btn", () => {
      // clear the interval timer to stop the clock counting
      clearInterval(tictoc)
    })
})
