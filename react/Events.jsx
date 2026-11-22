import React from "react"

const Events=()=>{

    const light=()=>{
        document.body.style.background="white";
        document.body.style.color="black"
    }

    const dark=()=>{
        document.body.style.background="black";
        document.body.style.color="white"
    }

    return(
        <>
            <button onClick={light}>light Theme</button>
            <button onClick={dark}>Dark Theme</button>
            <h2>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsam, ipsum. </h2>
        </>
    )
}

export default Events;