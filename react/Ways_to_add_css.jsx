import React from 'react'
import './external.css'

const Ways_to_add_css = () => {
    // internal css
    const mystyle={
        backgroundColor:"green",
        padding:"5px",
        borderRadius:"10px"
    }
    return (
        <div>
            {/* inline css */}
            <h1 style={{backgroundColor:"red",margin:'10px'}}>Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis ducimus voluptatibus at rem ab ipsa esse, itaque atque voluptates nisi quaerat nemo, sint velit consectetur qui numquam recusandae nihil architecto.</h1>
            <h2 style={mystyle}>Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis ducimus voluptatibus at rem ab ipsa esse, itaque atque voluptates nisi quaerat nemo, sint velit consectetur qui numquam recusandae nihil architecto.</h2>
            <h3>Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis ducimus voluptatibus at rem ab ipsa esse, itaque atque voluptates nisi quaerat nemo, sint velit consectetur qui numquam recusandae nihil architecto.</h3>
        </div>
    )
}

export default Ways_to_add_css
