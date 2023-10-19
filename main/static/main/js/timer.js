$(document).ready(() => {
  console.log("Page has loaded")

  // Check for running tasks
  let tasksData = JSON.parse(document.getElementById("running_task").textContent) 
  
  // Check for when start btn is clicked
  $(".start_btn").on("click", ()=> {
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
  $(".pause_btn").on("click", ()=> {
    clearInterval(timer)
  })
})
