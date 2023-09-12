export const timers = {}

export function updateTimer(){
  console.log("startTimer function has been called")
  let taskRows = $( ".task_row" )

  taskRows.each((index, element) => {
    // Instantiate task row variables
    let seconds = 0

    if ($(element).hasClass('active')){
      console.log("this element has ACTIVE class", $(element))
      // Get active task Row Id
      let elementIdParts = $(element).attr("id").split("_")
      let taskId = elementIdParts[1]
      console.log("Task Row ID " + taskId + " is active")
  
      // Get Accumalated Time for task
      let elapsed_time_ele = $( "#elapsed_time_" + taskId)
      let elapsed_time_value = $( elapsed_time_ele ).text().trim()
      let timeParts = elapsed_time_value.split(":")
      seconds += ((+timeParts[0]*60*60)+(+timeParts[1]*60)+(+timeParts[2]))
  
      // Instantiate Timer
      timers[taskId] = setInterval(() =>{
        seconds++
        let date = new Date(null)
        date.setSeconds(seconds)
        let timeStr = date.toISOString().substring(11,11+8)
        $(elapsed_time_ele).text(timeStr)
        }, 1000)
    } else {
      console.log("this element has NO active class", $(element))
      // Get active task Row Id
      let elementIdParts = $(element).attr("id").split("_")
      let taskId = elementIdParts[1]
      console.log("Task Row ID " + taskId + " is NOT active")
      // Pause timer
      clearInterval(timers[taskId])
    }
  })
}
