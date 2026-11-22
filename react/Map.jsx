import React from 'react'

const Map = () => {
    const smartphone =[
        {
            id:1,
            model:"iphone 15 pro max",
            img:"https://m.media-amazon.com/images/I/71d7rfSl0wL._AC_UY327_FMwebp_QL65_.jpg"
        },
        {
            id:2,
            model:"iphone 16 pro max",
            img:"https://m.media-amazon.com/images/I/61135j8fPJL._AC_UY327_FMwebp_QL65_.jpg"
        },
        {
            id:3,
            model:"iphone 17 pro max",
            img:"https://m.media-amazon.com/images/I/71MXmswILHL._AC_UY327_FMwebp_QL65_.jpg"
        }
    ]

    const company=["Google","Apple","Microsoft","Nvidia","Spacex"]
  return (
        <>
         <div>
            {
                smartphone.map((data)=>(
                    <div key={data.id} style={{backgroundColor:"skyblue",height:"200px",width:"150px",padding:"10px",borderRadius:"10px",margin:"10px"}}>
                        <img src={data.img} alt="" style={{height:"150px",width:"130px"}} />
                        <p style={{fontSize:"small"}}>{data.model}</p>
                    </div>
                ))
            }
         </div>


         <div>
            {
                company.map((element,index)=>(
                    <div key={index}>
                        <h3>{element}</h3>
                    </div>
                ))
            }
         </div>
        </>
  )
}

export default Map
