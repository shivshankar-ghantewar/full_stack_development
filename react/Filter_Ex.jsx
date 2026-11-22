import React from 'react'

const Filter_Ex = () => {

    const person=[
        {id:1,name:"ironman",active:true},
        {id:2,name:"spiderman",active:true},
        {id:3,name:"batman",active:false},
        {id:3,name:"Thor",active:false},
    ]

   const active_users=person.filter((data)=>data.active);
    console.log(active_users)
  return (
    <div>
        {
           active_users.map((item)=><div key={item.id}>
                 <h2>{item.name }</h2>
            </div>)
        }
    </div>
  )
}

export default Filter_Ex
