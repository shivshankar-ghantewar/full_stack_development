import React from 'react'
import { useState } from 'react'

const Usestate_hook = () => {
    // 0 is initial value
    const [value, setvalue]=useState(0) 
   
    const increase=()=>{
        setvalue(value+1)
    }

    const Decrease=()=>{
        setvalue(value-1)
    }

  return (
    <div>
      <h1>counter ={value}</h1> <br />
      <button onClick={increase}>incerase value</button>
      <button onClick={Decrease }>Decrease value</button>
    </div>
  )
}

export default Usestate_hook
