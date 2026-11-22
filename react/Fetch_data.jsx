import React, { useEffect, useState } from 'react'
import './Fetch_data.css'

const Fetch_data = () => {
    const [apidata, setapidata]=useState([])
    useEffect(()=>{
        const fetchdata= async()=>{
            const api=await fetch("https://fakestoreapi.com/products");
            const data=await api.json();
            console.log(data);
            setapidata(data);
        }
        fetchdata();
    },[])


  return (
    <div class="product-container">
         {
            apidata.map((items)=>(
                <div key={items.id}  style={{backgroundColor:"black",height:"280px",width:"200px",margin:"10px"}}>
                    <img src={items.image} alt=""   style={{height:"150px",width:"200px"}}/>
                    <h3 style={{fontSize:"15px",borderRadius:0,overflow:"hidden"}}>{items.title}</h3>
                    <h4 style={{color:"white",fontSize:"20px",textAlign:"center"}}>{items.price}</h4>
                </div>
            ))
         }
    </div>
  )
}

export default Fetch_data
