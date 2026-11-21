import React from 'react'

const Conditional_rendering = () => {
    const age=20;
  return (
    <div>
        {
            // ternary operator
          (age>=18) ?(<h1>you can drive</h1>) :(<h1>you can not drive</h1>)
        }
    </div>
  )
}

export default Conditional_rendering
