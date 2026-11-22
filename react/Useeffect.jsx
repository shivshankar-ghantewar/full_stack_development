import React, { useEffect, useState } from 'react'

const Useeffect = () => {
   const[counter,setcounter]=useState(0)
// useeffect works on page or reload of page
  useEffect(()=>{
    console.log("useeffect is runnuing....")
    document.title=counter;
  },[counter])  // useeffect reload when change happens in counter

  return (
    <div>
      <h1>counter={counter}</h1>
      <button onClick={()=>{setcounter(counter+1)}}>increase</button>
      <button onClick={()=>{setcounter(counter-1)}}>decraese</button>
     
    </div>
  )
}

export default Useeffect
